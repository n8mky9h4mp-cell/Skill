# Cocos 小游戏目录规范实施计划

## 目标

根据已批准的目录规范设计，更新现有 `cocos-mini-game` Skill，使新游戏默认使用 `client/` 承载完整 Cocos Creator 项目、`docs/game/` 承载项目文档，并按启用条件创建 `server/`、`shared/`、`tools/` 等可选目录。

用户已明确不需要 Skill eval 或基准测试，本次只执行静态验证。

## 步骤 1：新增目录规范参考

文件：`skills/cocos-mini-game/references/project-structure.md`

- 定义仓库级和 `client/assets/` 级标准目录。
- 定义必备、条件创建和生成目录。
- 定义命名、版本控制、已有项目兼容和变更流程。

## 步骤 2：接入主工作流

文件：`skills/cocos-mini-game/SKILL.md`

- 在项目识别、文档准备和核心实施阶段路由目录规范。
- 明确新项目以受控单仓库为默认结构。
- 要求任务路径、PRD 目录和实际工程保持一致。

## 步骤 3：消除重复规范

文件：

- `skills/cocos-mini-game/references/prd-template.md`
- `skills/cocos-mini-game/references/cocos-architecture.md`
- `skills/cocos-mini-game/references/project-planning.md`

- PRD 模板要求基于标准目录裁剪实际树，并记录可选目录启用理由。
- 架构文档引用完整目录规范，只保留运行架构和职责补充。
- 任务规划要求路径符合已批准的实际目录，不提前创建可选目录。

## 步骤 4：更新索引

文件：`llms.txt`

- 增加小游戏项目目录规范入口。
- 保留现有 Skill 数量与主索引，不修改无关条目。

## 步骤 5：静态验证

- 检查 `SKILL.md` frontmatter、名称和目录一致。
- 检查新增与修改后的本地 Markdown 链接存在。
- 检查未完成标记和占位说明。
- 检查 Markdown 代码围栏。
- 运行 `git diff --check`。
- 只提交本任务文件，不包含用户修改的 `AGENTS.md`。
