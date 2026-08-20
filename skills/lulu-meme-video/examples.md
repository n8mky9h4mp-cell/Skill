# examples.md（示例输入/输出与网页端契约）

下面示例用于帮助技能稳定产出结构化 JSON。你可以把这些示例当作“回归测试用例”。

## 示例 1：仅场景词（默认单镜头）
用户输入：
> 做一个水豚噜噜表情包视频：打工摸鱼，被老板突然路过吓一跳

期望输出要点：
- 场景：办公室工位、键盘/咖啡杯点缀、背景简化
- 动作：敲键盘 → 听到脚步 → 眼睛一缩/僵住 → 假装认真
- 镜头：固定机位，轻微推近（可选）
- T2I：强角色锚点 + 办公室调味风格
- I2V：小动作、强稳定提示

## 示例 2：参考图 + 场景词（锁角色不锁背景）
用户输入：
> 用这张水豚噜噜参考图，生成“雨天等车，叹气然后挤出微笑”的短视频，4 秒，9:16

期望输出要点：
- `t2i.reference_strategy.enabled = true`
- `t2i.reference_strategy.lock_character = true`
- `t2i.reference_strategy.copy_background = false`
- I2V：雨天元素简化；镜头稳定；动作幅度小

## 示例 3：强贴合你这张样例图的风格（无参考图也能跑）
用户输入：
> 做一个水豚噜噜表情包视频：开心庆祝，背景可以是星空挂小星星灯

建议在输出 JSON 的 `t2i` 中使用（片段示例，便于直接拼接）：

**prompt_zh 片段：**
- 3D 软萌公仔风的水豚噜噜，圆润体型，短四肢，无描边，边缘干净
- 柔和渐变阴影，棚拍柔光，轻微泛光，温暖暖黄色主体，橙色脸颊/口鼻区域渐变
- 表情包夸张可爱的大笑表情，弯弯眼
- （可选背景）深蓝梦幻星空，散景小星星，挂着星星小灯，偶尔流星

**prompt_en 片段：**
- Lulu the capybara mascot, 3D cute toy-like character, rounded shapes, short limbs, clean edges, no outline, no lineart
- smooth gradient shading, soft studio lighting, subtle bloom, gentle rim light
- warm pale-yellow body, orange gradient muzzle/cheeks, big happy smile, crescent eyes
- (optional background) dreamy deep-blue starry sky, bokeh stars, hanging star-shaped lights, occasional shooting stars

**negative_prompt 片段：**
- 2d, anime, manga, cel shading, lineart, sketch, watercolor
- photorealistic, skin pores, realistic fur, detailed hair strands
- extra limbs, deformed, warped, jitter, text, watermark, logo, qr code

## 示例 4：白天泳池/夏日子风格（来自你提供的泳池图）
用户输入：
> 做一个水豚噜噜表情包视频：夏天在泳池边跑起来，开心到张嘴笑，4 秒，16:9

建议在输出 JSON 的 `t2i` 中使用（片段示例，便于直接拼接）：

**prompt_zh 片段：**
- 3D 软萌公仔风的水豚噜噜，圆润体型，短四肢，无描边，边缘干净，暖黄色主体，橙色脸颊/口鼻区域渐变
- 高亮白天阳光，蓝天，夏日清爽氛围，棚拍级干净画面
- 泳池场景：蓝色泳池水、蓝色瓷砖池沿，少量干净水花飞溅
- 道具：橙白条纹救生圈（套在身上），背景可有简化的遮阳伞

**prompt_en 片段：**
- Lulu the capybara mascot, 3D cute toy-like character, rounded shapes, short limbs, clean edges, no outline
- high-key daylight, clear blue sky, clean summer vibe, smooth gradient shading, subtle subsurface feel
- poolside scene: clean blue pool water, blue tile edge, small clean water splashes
- prop: orange-and-white lifebuoy swim ring around the body, optional simplified beach umbrella in background

**negative_prompt 片段：**
- 2d, anime, manga, cel shading, lineart, sketch, watercolor
- photorealistic skin pores, realistic fur, gritty realism, algae, murky water, dirty textures
- extra limbs, deformed, warped, jitter, text, watermark, logo, qr code

## 示例 5：室内暖光“躺平摆烂”子风格（来自你提供的粉色软垫图）
用户输入：
> 做一个水豚噜噜表情包视频：下班回家直接躺平，半眯眼坏笑，3 秒，9:16

建议在输出 JSON 的 `t2i` 中使用（片段示例，便于直接拼接）：

**prompt_zh 片段：**
- 3D 软萌公仔风的水豚噜噜，圆润体型，短四肢，无描边，边缘干净，暖黄色主体，橙色脸颊/口鼻区域渐变
- 室内暖光氛围，柔和环境光反弹，顶部暖色灯带光，干净简约的室内角落
- 动作姿态：侧躺/趴在一个大粉色软垫上，一只手撑头，另一只手搭在软垫上
- 表情：半眯眼摆烂，坏笑/得意笑，露出一颗小白牙（可选）

**prompt_en 片段：**
- Lulu the capybara mascot, 3D cute toy-like character, rounded shapes, short limbs, clean edges, no outline
- warm cozy indoor lighting, soft ambient bounce light, warm ceiling strip light band, minimal clean interior corner
- pose: lounging on a big pink cushion/pillow, head resting on one hand, relaxed lazy posture
- expression: half-lidded sleepy eyes, smug grin, optional single small tooth showing

**negative_prompt 片段：**
- 2d, anime, manga, cel shading, lineart, sketch, watercolor
- photorealistic, skin pores, realistic fur, detailed iris texture
- highly detailed fabric weave, messy wrinkles, dirty bedding
- extra limbs, deformed, warped, jitter, text, watermark, logo, qr code

## 示例 6：图书馆/认真挑书子风格（来自你提供的书架图）
用户输入：
> 做一个水豚噜噜表情包视频：在图书馆认真挑书，找到一本书眼睛一亮，4 秒，16:9

建议在输出 JSON 的 `t2i` 中使用（片段示例，便于直接拼接）：

**prompt_zh 片段：**
- 3D 软萌公仔风的水豚噜噜，圆润体型，短四肢，无描边，边缘干净，暖黄色主体，橙色脸颊/口鼻区域渐变
- 图书馆场景：木质书架、书本陈列、木地板，背景轻微虚化，干净温暖
- 光线：午后暖阳从窗边打进来，柔和环境光反弹
- 动作：伸手从书架抽出一本书，表情从专注到眼睛一亮（大眼带眼白版本也可）
- 书脊保持简化，不要可读书名文字

**prompt_en 片段：**
- Lulu the capybara mascot, 3D cute toy-like character, rounded shapes, short limbs, clean edges, no outline
- cozy library scene: wooden bookshelves, warm wooden floor, books on shelves, shallow depth of field, clean warm ambience
- warm afternoon sunlight / soft window light, gentle ambient bounce
- action: reaching and pulling a book from the shelf, expression turns curious and delighted (round eyes with sclera allowed)
- keep book spines stylized, no readable titles or typography

**negative_prompt 片段：**
- 2d, anime, manga, cel shading, lineart, sketch, watercolor
- readable text, sharp typography, book titles, watermark, logo
- photorealistic, skin pores, realistic fur strands, detailed iris texture
- extra limbs, deformed, warped, jitter

## 示例 7：派对庆祝/彩纸雨子风格（来自你提供的彩灯派对图）
用户输入：
> 做一个水豚噜噜表情包视频：生日派对上臭屁庆祝，双手叉腰得意笑，4 秒，9:16

建议在输出 JSON 的 `t2i` 中使用（片段示例，便于直接拼接）：

**prompt_zh 片段：**
- 3D 软萌公仔风的水豚噜噜，圆润体型，短四肢，无描边，边缘干净，暖黄色主体，橙色脸颊/口鼻区域渐变
- 正面站姿，英雄式构图，双手叉腰，得意/臭屁的骄傲笑容，张嘴笑露一颗小白牙（可选）
- 头戴彩虹派对帽（顶部毛球），头部周围有彩带卷卷装饰；允许几根很细的胡须线条（简洁、不要写实毛）
- 背景：派对彩灯散景（五彩 bokeh），少量彩纸雨飘落，地面少量彩纸（保持干净）

**prompt_en 片段：**
- Lulu the capybara mascot, 3D cute toy-like character, rounded shapes, short limbs, clean edges, no outline
- front-facing hero pose, hands on hips, proud smug grin, open-mouth smile, optional single small tooth
- rainbow party hat with pom-pom, curly ribbon streamers around the head; allow a few simple whisker lines (thin, minimal)
- background: colorful party stage bokeh lights, shallow depth of field, confetti falling (clean, not gritty)

**negative_prompt 片段：**
- 2d, anime, manga, cel shading, lineart, sketch, watercolor
- gritty realism, dirty confetti dust, heavy motion blur, film dirt
- photorealistic, skin pores, realistic fur strands, detailed iris texture
- readable text, watermark, logo, qr code
- extra limbs, deformed, warped, jitter

## 网页端最小契约（建议）
你可以按这个契约实现一个网页：输入场景关键词/上传参考图 → 调用后端生成任务 → 轮询任务 → 返回视频 URL。

### 1) POST `/api/lulu/generate`
Request JSON（示例）：

```json
{
  "scene_text": "雨天等车，叹气然后挤出微笑",
  "reference_images": [
    {
      "name": "ref.png",
      "content_type": "image/png",
      "base64": "..."
    }
  ],
  "constraints": {
    "duration_sec": 4,
    "aspect_ratio": "9:16",
    "resolution": "720x1280",
    "fps": 24,
    "looping": false,
    "subtitles": { "enabled": false, "text": "" }
  },
  "model_pool": {
    "reasoning": ["reasoning_candidate_A", "reasoning_candidate_B"],
    "t2i": ["t2i_candidate_A", "t2i_candidate_B"],
    "i2v": ["i2v_candidate_A", "i2v_candidate_B"]
  },
  "tryrun": {
    "t2i_preview": true,
    "i2v_preview_seconds": 2
  }
}
```

Response JSON（示例）：

```json
{
  "job_id": "job_123",
  "status": "queued",
  "plan": {
    "request_version": "2026-02-02",
    "t2i": { "prompt_zh": "", "prompt_en": "", "negative_prompt": "" },
    "i2v": { "shotlist": [], "generation_params": {} },
    "model_routing": { "t2i_model": { "selected": "" }, "i2v_model": { "selected": "" } }
  }
}
```

### 2) GET `/api/lulu/jobs/{job_id}`
Response JSON（示例）：

```json
{
  "job_id": "job_123",
  "status": "succeeded",
  "artifacts": {
    "keyframe_image_url": "https://cdn.example.com/keyframe.png",
    "video_url": "https://cdn.example.com/video.mp4"
  },
  "scores": {
    "t2i": { "style": 4.5, "identity": 4.2, "clean": 4.6, "total": 4.4 },
    "i2v": { "stability": 4.3, "motion": 4.1, "warp": 4.2, "total": 4.2 }
  }
}
```

