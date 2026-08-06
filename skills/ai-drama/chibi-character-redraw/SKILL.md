---
name: chibi-character-redraw
description: 将任意参考角色重绘为「Q版轻写实（semi-realistic chibi）」形象的提示词生成器，9:16 竖版、3 头身、白底纯净、收藏级手办质感。严格保留原角色脸型/五官/发型/服装/纹理/气质，仅做比例 Q 版化。当用户提到 Q版化、Q版角色、chibi、二头身/三头身、角色手办、Q版重绘、萌化角色、semi-realistic chibi、收藏级 Q 版时使用。只输出可复制中文提示词，不直接生成图片。
---

# Q 版轻写实角色重绘（chibi-character-redraw）

把任意参考角色重绘为 **3 头身 Q 版 + 轻写实 CG + 收藏级手办质感** 的形象，**严格锁定原角色识别度**。

> **唯一核心原则**：「只允许比例 Q 版化，不允许角色设计变化」。Q 版后必须一眼认出是同一个角色。

详细锁定规则见 [references/identity-lock.md](references/identity-lock.md)；Q 版比例、风格、光影、画面、渲染与 Negative Prompt 见 [references/style-specs.md](references/style-specs.md)。

## 何时使用

- 把已有角色（国漫 / 游戏 / 影视 / 小说插画 / OC）重绘为 Q 版手办风
- 制作收藏级 Q 版角色立绘、IP 衍生形象
- 任意角色类型的 Q 版化：男 / 女 / 宠物 / 怪兽 / 幻想生物 / 机械 / 龙 / 兽人 / 精灵 / 机甲

## 何时不使用

- 古风美女四视图设定 → 用 `guofeng-beauty-turnaround`
- 古风男主四视图设定 → 用 `guofeng-handsome-male-turnaround`
- 国漫 CG 角色四视图设定板 → 用 `guofeng-character-3d-sheet`
- 需要正常比例的角色立绘 → 用 `guofeng-beauty-portrait` / `guofeng-beauty-halfbody`

## 工作流程

1. **读取参考**：确认用户提供参考图的全部识别特征（脸型、五官、发型、服装、纹理、气质、配色）。
2. **锁定清单**：按 [identity-lock.md](references/identity-lock.md) 逐项列出"必须保留"的特征，标注原角色气质关键词。
3. **Q 版化映射**：对每项特征给出 Q 版缩放/圆润化说明，**不得**改设计（见各规则的"禁止"项）。
4. **套风格规范**：按 [style-specs.md](references/style-specs.md) 写入 3 头身比例、轻写实 CG、柔和光影、白底纯净、渲染质量、Negative Prompt。
5. **输出提示词**：合成完整中文提示词，结构 = `角色一致性锁定 + Q 版比例 + 轻写实风格 + 画面基础 + 渲染质量 + Negative Prompt`。

## 输出规范要点

| 维度 | 规格 |
| --- | --- |
| 比例 | 标准 3 头身（头部约占整体 1/2），高端收藏级手办 |
| 风格 | semi-realistic chibi + 轻写实 CG（non-flat chibi） |
| 构图 | 9:16 竖版，单人全身，人物居中 |
| 背景 | 纯白 #FFFFFF，无渐变、无场景、无地面阴影、无文字/UI/水印 |
| 光影 | 柔和光照，柔和体积阴影，无硬阴影/高反差 |
| 一致性 | 脸型/五官/眉/嘴/妆/气质/发/纹理/服装 100% 锁定原角色 |

## 参考文件

- **[references/identity-lock.md](references/identity-lock.md)** — 脸部 / 眼眉嘴 / 妆容 / 气质 / 发型 / 纹理印记 / 角色类型的一致性锁定规则
- **[references/style-specs.md](references/style-specs.md)** — Q 版比例、轻写实风格、服装道具、动作、光影色彩、画面基础、渲染质量、Negative Prompt
