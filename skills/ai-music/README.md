# AI 音乐技能（ai-music）

存放 AI 音乐创作与音乐视频化的 Agent Skills，覆盖从作词、配器规划到 MV 分镜的完整链路。

## 工作流概览

```
主题/灵感 → 歌词与 Suno Prompt → 生成音频 → MV 分镜与视频提示词
```

## 目录约定

每个技能仍遵循仓库根 [AGENTS.md](../../AGENTS.md) 的 Skill 约定：

```
skills/ai-music/<技能名>/SKILL.md
skills/ai-music/<技能名>/references/...
skills/ai-music/<技能名>/scripts/...
```

`npx skills` 支持 catalog 布局（`skills/<category>/<name>/SKILL.md`），安装命令不变：

```bash
npx skills add xiongxianzhu/xskills --list
npx skills add xiongxianzhu/xskills --skill <技能名> -g -y
```

## 技能索引

| 技能 | 说明 |
| --- | --- |
| [`suno-lyric-creator`](./suno-lyric-creator/SKILL.md) | 面向 Suno AI 的全曲风歌曲与纯音乐创作：歌词、英文 Prompt、配器、结构、BPM、查重报告 |
| [`music-mv-storyboard`](./music-mv-storyboard/SKILL.md) | 根据歌曲名称、歌词、风格、时长生成覆盖整首歌的 MV 分镜与 Seedance / 即梦视频提示词 |
