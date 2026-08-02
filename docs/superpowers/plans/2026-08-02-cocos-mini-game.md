# Cocos Creator 双端小游戏 Skill 实施计划

## 目标

根据已批准的设计新增 `skills/cocos-mini-game/`，使智能体能从一个主题开始，完成趋势调研、玩法提案、PRD 与计划文档、Cocos Creator 3.8+ 2D 实施、微信/抖音双端适配和静态验收。

用户已明确跳过 Skill eval、基准测试与描述优化。

## 步骤 1：创建主入口

文件：`skills/cocos-mini-game/SKILL.md`

- 编写强触发描述，覆盖主题策划、Cocos Creator、微信小游戏、抖音小游戏和双端适配。
- 固化两次用户确认门槛。
- 定义按阶段读取 references 的路由。
- 定义状态回写、阻塞报告和停止条件。

验证：frontmatter 名称等于目录名；主入口少于 500 行；所有引用文件存在。

## 步骤 2：创建策划与文档模块

文件：

- `references/trend-research.md`
- `references/game-concept.md`
- `references/project-readiness-and-compliance.md`
- `references/prd-template.md`
- `references/project-planning.md`

内容：近期趋势检索、方案评分、PRD 必填结构、技术栈、目录树、进度与任务格式、合规时效性和素材授权。

验证：PRD、进度和任务字段可以互相追溯；不固化易变化的政策或包体数字。

## 步骤 3：创建工程与平台模块

文件：

- `references/cocos-architecture.md`
- `references/backend-and-data.md`
- `references/platform-adapter.md`
- `references/wechat-mini-game.md`
- `references/douyin-mini-game.md`
- `references/iaa-ads.md`

内容：最小 2D 架构、后端启用门槛、平台统一接口、编辑器模拟、两端构建与 SDK 差异、广告奖励状态机和失败降级。

验证：玩法代码不得直接散落 `wx`/`tt`；支付、排行榜、3D 不进入首版实现。

## 步骤 4：创建素材、构建与运营模块

文件：

- `references/assets-and-audio.md`
- `references/build-and-validation.md`
- `references/release-and-operations.md`

内容：图片生成规范、音频提示词、Web Mobile 与双端构建、设备/弱网/性能检查、发布准备和首版指标。

验证：没有声称未执行的构建或真机结果；缺少工具或账号时能给出明确阻塞项。

## 步骤 5：更新仓库索引

文件：`README.md`、`llms.txt`

- Skill 数量从 6 更新为 7。
- 加入 `cocos-mini-game` 入口、用途和关键参考文件。

验证：新增本地链接全部存在。

## 步骤 6：静态验收

- 检查所有 Markdown 链接。
- 检查 frontmatter、目录名和 `name` 一致。
- 检查新增文件是否有未完成标记或临时说明。
- 运行 `git diff --check`。
- 审阅最终差异，只暂存本任务文件。
