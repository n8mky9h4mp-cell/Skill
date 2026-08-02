# 小游戏项目目录规范

本规范是新游戏仓库目录的默认来源。先按 PRD 裁剪实际结构，再创建文件；不要为了补齐目录树生成空目录。

## 默认仓库结构

```text
<repo>/
├── client/                         # 完整 Cocos Creator 3.8+ 项目
│   ├── assets/
│   │   ├── scenes/                 # 启动、菜单、战斗、结算等场景
│   │   ├── scripts/
│   │   │   ├── core/               # 生命周期、事件、状态机、对象池
│   │   │   ├── game/               # 玩家、敌人、武器、关卡、掉落
│   │   │   ├── ui/                 # 界面组件与表现逻辑
│   │   │   ├── platform/           # 微信、抖音、编辑器模拟适配
│   │   │   ├── services/           # 存档、广告、音频、网络等服务
│   │   │   └── config/             # 游戏平衡和静态配置
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
│   │   └── bundles/                # 确认分包或独立加载边界后创建
│   ├── extensions/                 # 使用项目扩展时创建
│   ├── settings/                   # Cocos 项目设置，纳入版本控制
│   ├── package.json
│   └── tsconfig.json               # 项目实际生成或使用时保留
├── docs/
│   └── game/
│       ├── PRD.md
│       ├── progress.md
│       ├── tasks.md
│       └── audio-prompts.md         # 需要音频生成提示词时创建
├── server/                          # 后端决策门槛通过后创建
├── shared/                          # 确有跨端协议或类型时创建
├── tools/                           # 确有可重复项目脚本时创建
├── .gitignore
└── README.md
```

目录树展示允许的职责边界，不表示所有目录都必须存在。`client/` 与 `docs/game/` 是新项目的固定边界；其内部也只创建当前 PRD 和任务实际需要的子目录。

## 仓库级职责

- `client/` 必须是可由 Cocos Creator 3.8+ 独立打开的完整项目，至少以真实的 `assets/` 和 `package.json` 为准，不手工伪造引擎文件。
- `docs/game/` 只放游戏产品与交付文档，不混放引擎缓存、构建结果或临时调研文件。
- `server/` 仅在 [backend-and-data.md](backend-and-data.md) 的后端启用门槛通过后创建。
- `shared/` 仅用于真实存在的跨端协议、Schema 或生成类型，不作为通用工具或复制代码的容器。
- `tools/` 仅用于需要重复、确定性执行的项目脚本；一次性命令留在任务记录中。

## Cocos 资源职责

- `scenes/` 放 `.scene` 等场景资源；场景数量按 PRD 决定，不要求每个流程节点都拆成独立场景。
- `scripts/core/` 放与具体题材无关的基础能力，不依赖 `game/`、`ui/` 或具体平台实现。
- `scripts/game/` 放局内规则和实体行为；公共玩法代码不得直接调用 `wx` 或 `tt`。
- `scripts/ui/` 放界面组件与表现协调，不复制核心数值规则。
- `scripts/platform/` 放平台接口、环境选择、编辑器模拟和微信/抖音实现。
- `scripts/services/` 放跨场景服务；服务保持少量、职责单一，避免为每个对象创建全局单例。
- `scripts/config/` 放类型化静态配置和常量，不放运行时状态或密钥。
- `prefabs/`、`textures/`、`audio/` 的子目录随实际资源创建，避免同一资源在多个职责目录重复。
- `bundles/` 仅在 PRD 明确首包、分包、远程资源或独立加载策略后创建。

## 必备与条件创建

| 路径 | 新项目规则 | 启用条件 |
| --- | --- | --- |
| `client/` | 必备 | 创建或接管 Cocos 项目 |
| `docs/game/` | 必备 | 玩法方向获批后创建三份主文档 |
| `client/assets/scripts/platform/` | 双端项目必备 | 微信、抖音或编辑器模拟至少一种适配开始实施 |
| `client/assets/bundles/` | 条件创建 | PRD 明确分包、远程资源或独立加载边界 |
| `client/extensions/` | 条件创建 | 项目实际使用 Cocos 扩展 |
| `docs/game/audio-prompts.md` | 条件创建 | 需要交付音效或 BGM 生成提示词 |
| `server/` | 条件创建 | 后端决策门槛通过并获用户确认 |
| `shared/` | 条件创建 | 已有跨端协议、Schema 或生成类型 |
| `tools/` | 条件创建 | 已有需要维护的确定性项目脚本 |

## 命名规则

- 文件夹使用小写英文或小写连字符，不使用空格和中文路径。
- Cocos `Component`、TypeScript 类及其文件使用 `PascalCase`，例如 `PlayerController.ts`。
- 普通模块、配置和工具文件使用 `camelCase`，例如 `weaponConfig.ts`。
- 资源名称使用稳定、可检索的英文小写连字符；替换图片或音频时保持引用路径稳定。
- 同一概念只归属一个职责目录；无法判断时先依据使用方和生命周期确定归属，不新建含义模糊的 `common/`、`misc/` 或 `utils/`。

## 版本控制边界

- 提交 `assets/`、`settings/`、实际使用的 `extensions/`、`package.json` 和其他手工维护的项目文件。
- `assets/` 中资源对应的 `.meta` 文件随资源提交；不要手工修改 UUID，也不要只移动资源而丢失 `.meta`。
- 由 Cocos Creator 创建项目时保留其 `.gitignore` 规则，并在仓库根目录覆盖 `client/` 下的生成目录。
- 忽略 `client/build/`、`client/library/`、`client/local/`、`client/profiles/`、`client/temp/` 等构建、缓存或本机目录。
- 不提交 App Secret、令牌、签名、私密平台配置、本机绝对路径或带真实用户数据的调试文件。

## 新项目执行顺序

1. 在 PRD 中写出按本规范裁剪后的实际目录树和主要职责。
2. 在 `tasks.md` 中为首个任务列出将创建或修改的精确路径。
3. 使用 Cocos Creator 3.8+ 在 `client/` 创建项目，保留编辑器实际生成的项目标识和配置。
4. 只创建当前任务需要的资源子目录；通过 Cocos 资源管理器移动已导入资源，保持 `.meta` 关系。
5. 完成任务后对照 PRD、任务路径和实际文件；存在偏差时先记录原因并同步文档。

## 已有项目兼容

先读取真实项目结构、Cocos 版本、场景、脚本和版本控制状态。现有结构职责清楚时沿用，不为匹配本规范重排无关文件。只有现有边界会阻碍新增功能、双端适配或维护时才提出迁移，并先说明影响、更新 PRD 和拆分迁移任务。
