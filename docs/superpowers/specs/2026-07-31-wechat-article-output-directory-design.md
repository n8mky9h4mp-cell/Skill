# 微信公众号文章默认输出目录设计

## 目标

将 `write-wechat-articles` 生成文章时的默认根目录从 `articles/` 改为 `微信公众号文章/`。

Skill 名称和安装目录保持不变：

```text
skills/write-wechat-articles/
```

## 输出结构

修改后的默认结构：

```text
微信公众号文章/
└── YYYY-MM-DD-短标题/
    ├── article.md
    ├── wechat.md
    ├── wechat.html
    └── assets.md
```

日期、短标题清理、同名目录追加数字后缀和不可写时的回退规则均保持不变。

## 修改范围

同步修改：

- `skills/write-wechat-articles/SKILL.md`
- `skills/write-wechat-articles/references/wechat-formatting.md`
- `skills/write-wechat-articles/references/quality-checklist.md`
- 记录旧路径的相关设计文档
- 全局安装目录中的 `write-wechat-articles` 副本

根目录 `README.md` 当前未声明文章保存路径，不需要修改。

## 兼容与迁移

当前仓库没有实际的 `articles/` 文章目录，因此不迁移文件。

本次只改变后续文章的默认保存位置，不自动移动或删除其他工作区中已有的 `articles/`。用户明确指定保存路径时，继续以用户要求为准。

## 验收

- Skill 和排版规范不再把 `articles/` 作为默认输出目录。
- 检查清单使用 `微信公众号文章/`。
- 四个文章文件及其职责保持不变。
- 源 Skill 与全局安装副本一致。
- Skill 元数据、链接和 Markdown 格式检查通过。
