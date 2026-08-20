# 水豚噜噜表情包视频生成技能

一个 Cursor Agent Skill，用于生成风格一致的"水豚噜噜"表情包短视频方案。

## 功能

- 场景解析 → 文生图提示词 → 图生视频镜头与参数
- 候选模型自动评估选优
- 输出可供网页端调用的结构化 JSON

## 安装

将整个 `lulu-meme-video` 文件夹复制到：

```
macOS/Linux: ~/.cursor/skills/
Windows: %USERPROFILE%\.cursor\skills\
```

目录结构：
```
~/.cursor/skills/
└── lulu-meme-video/
    ├── SKILL.md        # 主技能定义
    ├── reference.md    # 风格锚点、角色锚点、评分量表
    ├── examples.md     # 示例输入输出、Web API 契约
    └── README.md       # 本文件
```

## 使用

在 Cursor 中输入相关关键词即可自动触发：

- "水豚噜噜"
- "表情包"
- "capybara lulu"
- "meme"
- "文生图"
- "图生视频"
- "短视频"

### 示例输入

```
做一个水豚噜噜表情包视频：打工摸鱼，被老板突然路过吓一跳
```

### 输出

结构化 JSON，包含：
- `input_summary` - 归一化输入
- `scene_analysis` - 场景分析
- `t2i` - 文生图提示词（中英文 + 负面提示词）
- `i2v` - 图生视频方案（镜头、动作、参数）
- `model_routing` - 模型选优路由
- `quality_gates` - 质量闸门与阈值
- `fallback_plans` - 回退方案

## 依赖

- 无外部依赖（纯提示词工程）
- 输出 JSON 供 Web 端/后端调用任意 AI 平台

## 特性

- **风格一致性**：内置角色锚点和风格锚点，确保"水豚噜噜"形象稳定
- **面部干净度控制**：强制约束面部干净光滑，无异常元素
- **模型无关**：输出标准化 JSON，可映射到任意 T2I/I2V 平台
- **质量闸门**：内置评分量表和自动回退策略

## License

MIT
