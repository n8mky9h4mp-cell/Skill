---
name: character-design-board
description: 生成横版角色设定板完整中文提示词：黑金版式 + 主肖像 + 三视图 + 面部/发饰/服装/材质/鞋子/配件/纹样多栏目，16:9 高信息密度，收藏级设定稿质感。当用户提到角色设定板、角色设定集、角色概念设计、character design board、character sheet、角色设定表、多视图设定、角色展示板时使用。只输出可复制中文提示词，不直接生成图片。
---

# 角色设定板生成（character-design-board）

输出一张专业、完整、信息密度高的横版**角色设定板**提示词：黑金版式 + 主肖像 + 三视图 + 多个细节栏目，16:9，收藏级设定稿质感。

> **核心原则**：「版式信息密度高 + 角色跨视图完全一致 + 黑金克制典雅」。结构清晰优先于装饰效果。

完整 16 节提示词模板见 [references/prompt-template.md](references/prompt-template.md)；变量表、内部生成规则与负面提示词见 [references/variables-and-rules.md](references/variables-and-rules.md)。

## 何时使用

- 为任意世界观角色（古风 / 国漫 / 现代 / 科幻 / 仙侠 / 偶像 / 游戏角色）生成专业设定集页面
- 需要主肖像 + 正/侧/背三视图 + 面部/发饰/服装/材质/鞋子/配件/纹样等多栏目的一站式展示
- 输出用于游戏角色概念设计、国漫角色原画设定稿、影视角色设定集、IP 衍生视觉基础

## 何时不使用

- 古风美女/男主四视图 → 用 `guofeng-beauty-turnaround` / `guofeng-handsome-male-turnaround`
- 3D 国漫 CG 角色四视图 → 用 `guofeng-character-3d-sheet`
- Q 版轻写实角色重绘 → 用 `chibi-character-redraw`
- 单张角色立绘（无多视图、无版式栏目）→ 用对应 `guofeng-beauty-portrait` / `guofeng-beauty-halfbody`

## 工作流程

1. **收集变量**：按 [variables-and-rules.md](references/variables-and-rules.md) 的变量表收集角色资料；未提供项按世界观与气质合理补充，但**不得改变用户明确指定**的设定。
2. **套用模板**：把变量填入 [prompt-template.md](references/prompt-template.md) 的 16 节结构。
3. **按角色类型调整栏目**：依据角色类型（战斗 / 现代 / 仙侠 / 科幻 / 偶像）增减细节栏目，规则见内部生成规则第 8 条。
4. **加负面提示词**：附上 [variables-and-rules.md](references/variables-and-rules.md) 末尾的负面提示词。
5. **输出**：合成可直接喂图像模型的完整中文提示词。

## 变量速查（核心字段）

完整字段与内部生成规则见 [references/variables-and-rules.md](references/variables-and-rules.md)。

| 分组 | 变量 |
| --- | --- |
| 身份 | `character_name_cn` · `character_name_en` · `gender` · `age` · `height` · `identity` · `organization` |
| 设定 | `worldview` · `character_type` · `personality` · `keywords` · `character_bio` |
| 视觉 | `element` · `element_symbol` · `face` · `eyes` · `hair_style` · `hair_color` · `makeup` · `body_proportion` |
| 配色 | `color_scheme` · `bg_tone` · `main_color` · `secondary_color` · `accent_color` · `support_colors` |
| 服饰 | `costume` · `costume_structure` · `hair_accessories` · `jewelry` · `shoes` · `materials` · `patterns` |
| 道具 | `props` · `mascot` · `pose_expression` |
| 输出 | `render_style` |

## 输出规范要点

| 维度 | 规格 |
| --- | --- |
| 比例 | 16:9 横向超宽，建议 2048×1152 或更高 |
| 版式 | 左信息区(36%) + 中三视图 + 右细节区 + 底部配件/纹样区，暗金细线分隔 |
| 配色 | 深黑/炭黑/黑褐底 + 香槟金/古铜金标题 + 角色主色/辅助色/点缀色 |
| 一致性 | 主肖像、三视图、所有细节特写必须是**同一角色的同一套设定** |
| 文字 | 中文栏目标题端正可读；模型不稳定时保留暗金标题框，禁止乱码 |
| 风格 | 高端游戏角色设定集 / 影视级概念设计 / 国漫原画设定稿 |

## 参考文件

- **[references/prompt-template.md](references/prompt-template.md)** — 完整 16 节中文提示词模板（画面规格 / 版式 / 左信息区 / 主肖像 / 三视图 / 面部 / 发饰 / 服装 / 材质 / 鞋子 / 配件 / 纹样 / 设定文字 / 光影 / 质量 / 文字要求）
- **[references/color-palettes.md](references/color-palettes.md)** — 10 套预设配色方案，每套含角色配色 + 协调版式配色（黑金古典 / 仙侠霜白 / 赛博青红 / 蒸汽黄铜 / 暗黑哥特 / 敦煌矿物 / 少年热血 / 偶像应援 / 水墨淡彩 / 机械兽金）
- **[references/variables-and-rules.md](references/variables-and-rules.md)** — 完整变量表 + 12 条内部生成规则 + 负面提示词
