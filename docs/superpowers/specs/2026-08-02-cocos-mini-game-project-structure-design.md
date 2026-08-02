# Cocos 小游戏目录规范设计

## 背景

`cocos-mini-game` 已规定 Cocos Creator 3.8+、TypeScript、微信与抖音双端适配，并要求 PRD 包含技术栈和目录结构。现有规范主要描述 `assets/` 内部结构，尚未统一游戏仓库根目录、Cocos 客户端目录、可选后端目录和版本控制边界。

本设计将目录规范提升为独立参考文档，供新项目创建、已有项目接管、PRD 编写和任务拆解共同引用。

## 目标

- 默认采用单仓库，固定以 `client/` 承载完整 Cocos Creator 项目。
- 固定以 `docs/game/` 承载 PRD、进度清单和任务拆解。
- `server/`、`shared/`、`tools/` 等扩展目录只在满足启用条件后创建。
- 统一 `assets/` 内的代码、预制体、图片、音频和分包资源边界。
- 明确应提交与应忽略的 Cocos Creator 文件。
- 让 PRD 中的目录、任务中的文件路径和实际工程保持一致。

## 非目标

- 不规定具体游戏的场景、角色、敌人或武器数量。
- 不强制重排已有项目的合理目录。
- 不提前创建后端、共享协议、工具脚本或资源分包。
- 不替代微信、抖音平台构建和发布规范。

## 方案选择

采用“受控单仓库 + 按需目录”方案：

1. `client/` 和 `docs/game/` 是新项目必备边界。
2. `server/` 仅在后端决策门槛通过后创建。
3. `shared/` 仅在存在实际跨端协议或共享类型后创建。
4. `tools/` 仅在存在需要重复、确定性执行的项目脚本后创建。
5. 其他资源子目录也按实际内容创建，不保留空目录。

该方案兼顾首版纯客户端的简洁性和以后增加后端的扩展空间，优于提前生成完整空骨架，也比将 Cocos 项目直接放在仓库根目录更容易维持职责边界。

## 标准目录

```text
<repo>/
├── client/
│   ├── assets/
│   │   ├── scenes/
│   │   ├── scripts/
│   │   │   ├── core/
│   │   │   ├── game/
│   │   │   ├── ui/
│   │   │   ├── platform/
│   │   │   ├── services/
│   │   │   └── config/
│   │   ├── prefabs/
│   │   │   ├── characters/
│   │   │   ├── enemies/
│   │   │   ├── weapons/
│   │   │   ├── effects/
│   │   │   └── ui/
│   │   ├── textures/
│   │   │   ├── characters/
│   │   │   ├── enemies/
│   │   │   ├── environment/
│   │   │   ├── effects/
│   │   │   └── ui/
│   │   ├── audio/
│   │   │   ├── bgm/
│   │   │   └── sfx/
│   │   └── bundles/
│   ├── extensions/
│   ├── settings/
│   ├── package.json
│   └── tsconfig.json
├── docs/
│   └── game/
│       ├── PRD.md
│       ├── progress.md
│       ├── tasks.md
│       └── audio-prompts.md
├── server/
├── shared/
├── tools/
├── .gitignore
└── README.md
```

目录树展示全部允许边界，不表示必须一次性创建。新项目只创建当前 PRD 和任务实际需要的目录。

## 职责边界

### 仓库级目录

- `client/`：完整且可由 Cocos Creator 3.8+ 独立打开的客户端项目。
- `docs/game/`：游戏产品和交付文档，不混放引擎生成文件。
- `server/`：账号、云存档、排行榜、活动配置等服务端实现；启用条件由后端决策规范控制。
- `shared/`：跨客户端和服务端共享的协议、Schema 或生成类型；不得成为通用杂物目录。
- `tools/`：项目级确定性脚本；一次性命令和临时文件不得纳入。

### Cocos 资源目录

- `scenes/`：启动、菜单、战斗、结算等场景资源。
- `scripts/core/`：生命周期、事件、状态机、对象池等基础能力，不依赖具体题材。
- `scripts/game/`：玩家、敌人、武器、关卡、掉落和局内规则。
- `scripts/ui/`：界面组件与表现逻辑。
- `scripts/platform/`：微信、抖音和编辑器模拟适配；业务代码不得直接调用 `wx` 或 `tt`。
- `scripts/services/`：存档、广告、音频、网络等跨场景服务。
- `scripts/config/`：游戏平衡和静态配置，不放运行时状态。
- `prefabs/`、`textures/`、`audio/`：按资源职责分类，只有存在对应资源时才创建子目录。
- `bundles/`：确认需要分包、远程资源或独立加载边界后才创建。

## 命名与版本控制

- 文件夹使用小写或小写连字符命名，不使用空格和中文路径。
- TypeScript 组件和类文件使用 `PascalCase`；普通模块与配置使用 `camelCase`。
- `assets` 中资源对应的 `.meta` 文件随资源提交，禁止手工改写 UUID。
- `settings/`、`assets/`、实际使用的 `extensions/`、`package.json` 和手工维护的项目文件纳入版本控制。
- `build/`、`library/`、`local/`、`profiles/`、`temp/` 等生成或本地目录由 `.gitignore` 排除。
- 密钥、令牌、平台私密配置和本机绝对路径不得提交。

## 已有项目兼容策略

接管已有项目时，先读取真实目录、Cocos 版本和版本控制状态。若现有结构职责清楚，不为匹配标准而搬迁无关文件。只有目录冲突会阻碍新增功能、双端适配或维护时才提出迁移，并先同步更新 PRD 和任务文档。

## Skill 集成

- 新增 `references/project-structure.md`，作为完整目录规范的唯一详细来源。
- `SKILL.md` 在文档阶段和实施阶段要求读取该规范。
- `references/prd-template.md` 的目录章节引用标准结构，并要求记录实际裁剪和偏差。
- `references/cocos-architecture.md` 聚焦运行架构与依赖方向，不再重复完整仓库树。
- `references/project-planning.md` 要求任务路径与批准后的实际目录一致。
- `llms.txt` 增加新参考文档索引。

## 验证标准

- 新增参考文档的链接均能解析到实际文件。
- `SKILL.md` frontmatter、名称和目录保持一致。
- 新增内容不含 `TODO`、`TBD` 或占位说明。
- Markdown 代码围栏闭合，`git diff --check` 无空白错误。
- 不修改或提交与本任务无关的 `AGENTS.md` 用户改动。
