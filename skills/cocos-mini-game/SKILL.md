---
name: cocos-mini-game
description: 使用 Cocos Creator 3.8+ 从主题策划、PRD 和任务规划开始，直接开发可发布到微信小游戏与抖音小游戏的 2D IAA 游戏。用户提到 Cocos 小游戏、微信小游戏、抖音小游戏、双端小游戏、小游戏主题策划、小游戏 PRD、小游戏广告变现或希望从一个主题生成并实施完整游戏时必须使用；即使用户只说“做一个小游戏”或“微信小程序游戏”，也先用本 Skill 判断目标并推进完整流程。
compatibility: 需要可读写的项目工作区；趋势、平台规则和合规检查需要联网；实际构建需要 Cocos Creator 3.8+ 及对应平台开发者工具。
---

# Cocos Creator 双端小游戏开发

从一个主题开始，先完成有来源的玩法决策和项目文档，再实施微信、抖音双端 2D 小游戏。首版以 IAA 广告变现为目标，不实现支付、排行榜或 3D 专项能力。

## 核心原则

- 先验证玩法方向，再写 PRD；先批准 PRD，再修改项目。
- 公共玩法代码不直接调用 `wx` 或 `tt`，所有平台能力经过统一适配层。
- 只实现 PRD 已批准的最小闭环，不预建商城、复杂社交、实时对战或大型后端。
- 平台政策、API、包体限制和审核规则具有时效性，执行时查询当前官方资料并记录日期。
- 缺少工具、账号、App ID 或真机条件时如实记录阻塞，不声称已经验证。
- 图片可调用当前环境可用的生成工具；音效和 BGM 只交付专业平台生成提示词。

## 工作流

### 阶段 0：识别输入与项目

1. 提取用户给出的主题、目标平台、引擎版本和已有项目路径。
2. 用户说“微信小程序游戏”时，按 [references/project-readiness-and-compliance.md](references/project-readiness-and-compliance.md) 判断其目标是否实际为微信小游戏。
3. 只读检查现有项目结构、Cocos 版本、未提交修改和可用工具。保留用户已有改动。
4. 新项目默认以 Cocos Creator 3.8+、TypeScript、2D、微信与抖音双端为基线。

### 阶段 1：联网调研与玩法提案

1. 完整阅读：
   - [references/trend-research.md](references/trend-research.md)
   - [references/game-concept.md](references/game-concept.md)
2. 联网查询最近 6–12 个月的榜单、行业报告、代表产品和平台动向。
3. 区分来源事实与推断，不能把旧数据包装成当前趋势。
4. 根据主题给出 2–3 个玩法方向，包含核心循环、用户、IAA 广告点、成本、风险和推荐理由。
5. 明确推荐一个方向，同时保留其他方案的适用条件。

**门槛 1：等待用户选择玩法方向。未选择前，不生成正式 PRD，不创建游戏代码或素材。**

### 阶段 2：项目准备与文档

用户选定玩法后，完整阅读：

- [references/project-readiness-and-compliance.md](references/project-readiness-and-compliance.md)
- [references/prd-template.md](references/prd-template.md)
- [references/project-planning.md](references/project-planning.md)
- 需要后端判断时读取 [references/backend-and-data.md](references/backend-and-data.md)

在目标游戏项目创建或更新：

```text
docs/game/
├── PRD.md
├── progress.md
└── tasks.md
```

PRD 必须包含技术栈和目标项目目录树。三份文档使用一致的功能名称、路径、范围与完成条件。

**门槛 2：等待用户批准三份文档。未批准前，不创建或修改游戏代码和资源。**

### 阶段 3：实施核心游戏

文档获批后：

1. 完整阅读 [references/cocos-architecture.md](references/cocos-architecture.md)。
2. 从 `tasks.md` 选择一个最小、无阻塞任务，标记为进行中。
3. 实现可重复游玩的闭环：启动、进入、核心操作、成功或失败、结算、再次开始。
4. 每完成一个任务就验证产物，并同步更新 `progress.md` 与 `tasks.md`。
5. 实施确需偏离 PRD 的技术栈或目录结构时，先更新 PRD 并说明原因。

### 阶段 4：素材与平台能力

按实际任务完整阅读：

- [references/assets-and-audio.md](references/assets-and-audio.md)
- [references/platform-adapter.md](references/platform-adapter.md)
- [references/wechat-mini-game.md](references/wechat-mini-game.md)
- [references/douyin-mini-game.md](references/douyin-mini-game.md)
- [references/iaa-ads.md](references/iaa-ads.md)

先建立编辑器模拟实现，再分别实现微信与抖音适配。模拟结果必须可识别，不能伪装成真实登录、分享或广告成功。

### 阶段 5：构建、验收与交付

1. 完整阅读：
   - [references/build-and-validation.md](references/build-and-validation.md)
   - [references/release-and-operations.md](references/release-and-operations.md)
2. 先验证 Web Mobile 核心玩法，再验证微信和抖音构建。
3. 平台 SDK 能力必须在对应开发者工具或真机验收。
4. 记录已通过、未通过、未执行和受阻项，不混用状态。
5. 最终确保 PRD、进度、任务和实际项目一致。

## 任务循环

每次只推进一个可验证任务：

```text
领取任务 → 标记进行中 → 实施 → 验证 → 回写结果 → 领取下一项
```

验证失败时保留具体错误并修复；同一外部阻塞重复出现时停止重试，记录恢复条件并继续处理不依赖该条件的任务。

## 范围变更

以下需求会显著扩大首版范围，先说明影响并取得用户确认：

- 支付、内购或混合变现。
- 好友排行榜、开放数据域或复杂社交。
- 实时联网、跨设备云存档、服务端权威奖励或运营后台。
- 3D 玩法或重度物理。
- 自动发布、提审或操作线上账号。

## 交付摘要

最终报告应包含：

- 选定玩法与核心闭环。
- PRD、进度和任务文档路径。
- 主要代码与素材路径。
- Web Mobile、微信、抖音各自的验证状态。
- 外部阻塞与最短人工操作步骤。
- 音效和 BGM 提示词清单路径。
- 发布前仍需用户完成的账号、合规和真机事项。
