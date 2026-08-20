---
name: lulu-meme-video
description: Generate “水豚噜噜”风格一致的表情包短视频方案（场景解析→文生图提示词→图生视频镜头与参数→候选模型自动评估选优→输出可供网页端调用的结构化 JSON）。Use when the user mentions 水豚噜噜/表情包/capybara lulu/meme/文生图/图生视频/短视频.
---

# 水豚噜噜表情包视频生成

## 核心原则（必须遵守）
- 产出必须是“可执行方案”，而不是泛泛建议：给出 **T2I 提示词**、**I2V 镜头与参数**、**模型路由与评分**、**fallback**。
- 不绑定具体供应商/SDK：输出“模型无关”的请求体与决策理由，便于网页端/后端映射到任意平台。
- 全程保持“水豚噜噜”风格一致：优先 **角色一致性** 与 **风格一致性**，其次再追求复杂场景。
- 不向用户追问：缺失信息使用保守默认值，并在 `input_summary.assumptions` 里写清楚。

## 适用输入
- 场景关键词：例如“打工摸鱼 / 雨天等车 / 过年拜年 / 被老板盯上”
- 可选参考图：1-5 张（推荐 1 张主参考）
- 可选约束：时长、比例（9:16/16:9/1:1）、是否循环、字幕/贴纸、情绪、动作、道具

## 必须输出（只输出一个 JSON 对象）
严格只输出一个 JSON，不要输出 markdown、解释、前后缀文本。

JSON 顶层字段必须包含：
- `request_version`
- `input_summary`
- `scene_analysis`
- `t2i`
- `i2v`
- `model_routing`
- `quality_gates`
- `web_api_contract`
- `fallback_plans`

## 工作流（按顺序执行）

### 1) 归一化输入（input_summary）
- 提取：场景、地点/时间、情绪、关键动作、道具、镜头偏好、比例/时长、是否循环、是否有参考图。
- 默认值（可在 `reference.md` 调整）：
  - 时长：3-5 秒
  - 镜头：1 个主镜头（必要时 2-3 镜头）
  - 镜头运动：固定机位或极轻微推拉
  - 动作幅度：小幅、可读、稳定

### 2) 场景分析（scene_analysis）
- 输出角色设定（保持单角色为主）、情绪弧线、动作分解（2-4 个微动作）、背景简洁度建议。
- 避免：写实人类主角、多角色拥挤、复杂文字海报、强恐怖/血腥元素。

### 3) 生成文生图提示词（t2i）
- 必须同时给出：
  - `prompt_zh`
  - `prompt_en`
  - `negative_prompt`（**必须包含面部干净度负面词**）
  - `composition`（构图与镜头）
  - `style_anchors`（从 `reference.md` 选取）
  - `character_anchors`（从 `reference.md` 选取，**必须包含面部干净度约束**）
- **面部干净度强制约束**（每次生成必须包含）：
  - 正向提示词中加入：`clean smooth face with no spots or raised dots`
  - 负面提示词中加入：`facial spots, raised dots on face, freckles, moles, warts, blackheads, acne, pimples, whisker dots, beard stubble, facial hair dots, skin bumps, texture bumps`
- 若有参考图，先产出一个 `style_profile`（写进 `t2i.style_profile`），再生成提示词：
  - 调色板与主色比例、线条粗细与边缘处理、阴影方式、背景简化习惯、表情范围（可爱/摆烂/震惊等）
  - **面部干净度检查**：确认参考图中角色面部干净光滑
- 若有参考图：
  - 指定 `reference_strategy`：锁定角色外观/配色/表情范围；不强拷贝背景（除非用户明确要求）。

### 3.5) 图片质量检查（生图后、视频前必检）
**在生成图片后、进行图生视频前，必须执行以下检查：**

**面部干净度检查（最高优先级）**：
- 面部是否只有眼睛、鼻子、嘴巴三个五官元素？
- 面部是否有任何凸起的圆点或斑点？
- 面部是否有雀斑、痣、疣、黑头、痘痘？
- 面部是否有胡须点或胡须纹理？
- 面部皮肤是否干净光滑，无凹凸纹理？

**如果任一项检查不通过**：
1. 强化负面提示词，重新生成图片
2. 或降低背景复杂度，让模型更专注于角色
3. 或更换 T2I 候选模型

### 4) 生成图生视频方案（i2v）
- 目标：形象稳定、动作自然、抖动/扭曲尽量少。
- **前提**：图片必须通过 3.5 步的质量检查
- 必须输出：
  - `shotlist`（每个镜头的动作、镜头运动、节奏）
  - `motion_prompts`（稳定/一致性提示词）
  - `duration_sec`, `fps`, `resolution`, `aspect_ratio`
  - `looping`（若循环：首尾动作与构图约束）

### 5) 模型选优与路由（model_routing）
将任务拆为三段并分别路由：
- 文本推理（场景理解/提示词/镜头脚本/参数）：选择“推理强、结构化输出稳”的模型。
- 文生图（关键帧）：选择“风格/形象一致性强”的模型。
- 图生视频：选择“稳定、少漂移、动作自然”的模型。

必须执行“低成本试跑选优”：
- T2I：2 个候选模型 → 低分辨率/少步数预览 → 评分 → 选最佳关键帧
- I2V：1-2 个候选模型 → 2 秒预览 → 评分 → 选最佳生成全量

评分维度与阈值：使用 `reference.md` 的量表（必须写入输出的 `quality_gates`）。

### 6) 质量闸门与回退（quality_gates / fallback_plans）
若不达标，按优先级回退：
1. 强化角色锚点、降低背景复杂度
2. 减小动作幅度、减少镜头运动
3. 更换候选模型（按模型注册表）
4. 缩短时长/减少镜头数量

## 输出 JSON 模板（字段可扩展但不可缺省）
按此结构输出（示例字段名固定；内容根据输入填充）：

```json
{
  "request_version": "2026-02-02",
  "input_summary": {
    "user_scene_text": "",
    "has_reference_images": false,
    "constraints": {
      "duration_sec": 4,
      "aspect_ratio": "9:16",
      "resolution": "720x1280",
      "fps": 24,
      "looping": false,
      "subtitles": { "enabled": false, "text": "" }
    },
    "assumptions": []
  },
  "scene_analysis": {
    "core_gag": "",
    "emotion": "",
    "actions": [],
    "environment": "",
    "camera": { "shot_count": 1, "movement": "static_or_subtle_push" }
  },
  "t2i": {
    "prompt_zh": "",
    "prompt_en": "",
    "negative_prompt": "",
    "facial_cleanliness_prompt": {
      "positive": "clean smooth face with no spots or raised dots, pure smooth skin texture",
      "negative": "facial spots, raised dots on face, freckles, moles, warts, blackheads, acne, pimples, whisker dots, beard stubble, facial hair dots, skin bumps, texture bumps, facial decorations"
    },
    "style_anchors": [],
    "character_anchors": [],
    "style_profile": {
      "palette": [],
      "line_style": "",
      "shading": "",
      "background_style": "",
      "expression_range": [],
      "facial_cleanliness": "absolutely clean and smooth face, no spots, no raised dots"
    },
    "composition": "",
    "reference_strategy": {
      "enabled": false,
      "lock_character": true,
      "lock_palette": true,
      "copy_background": false
    },
    "generation_params": { "steps": 28, "cfg": 4.5, "seed": null }
  },
  "i2v": {
    "shotlist": [
      {
        "shot_id": "S1",
        "visual": "",
        "action": "",
        "camera_motion": "static",
        "notes": ""
      }
    ],
    "motion_prompts": {
      "positive": [],
      "negative": []
    },
    "generation_params": {
      "duration_sec": 4,
      "fps": 24,
      "stability": "high",
      "motion_strength": "low_to_medium"
    }
  },
  "model_routing": {
    "reasoning_model": { "candidates": [], "selected": "", "why": "" },
    "t2i_model": { "candidates": [], "selected": "", "why": "" },
    "i2v_model": { "candidates": [], "selected": "", "why": "" },
    "tryrun_plan": []
  },
  "quality_gates": {
    "rubric": [
      { "dimension": "style_consistency", "weight": 0.25 },
      { "dimension": "character_consistency", "weight": 0.30 },
      { "dimension": "prompt_adherence", "weight": 0.20 },
      { "dimension": "facial_cleanliness", "weight": 0.15, "critical": true },
      { "dimension": "animation_readiness", "weight": 0.10 }
    ],
    "thresholds": {
      "overall_min": 4.0,
      "character_consistency_min": 4.0,
      "facial_cleanliness_min": 4.5
    },
    "auto_fix_actions": [
      "strengthen_facial_negative_prompt",
      "reduce_background_complexity",
      "switch_t2i_candidate"
    ]
  },
  "web_api_contract": {
    "endpoint_suggestion": "/api/lulu/generate",
    "request_json": {},
    "response_json": {}
  },
  "fallback_plans": []
}
```

## 参考资料
- 风格锚点、角色锚点、禁用项、评分量表、镜头模板：见 [reference.md](reference.md)
- 示例输入/输出与网页端请求示例：见 [examples.md](examples.md)

