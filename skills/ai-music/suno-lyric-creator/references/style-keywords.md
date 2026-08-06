# 全曲风写词、人声与风格关键词库

本文件用于选择歌词语体、押韵方式、情绪强度、人声真实性词和曲风专项写法。先确定语言与主曲风，再选规则；不要把国风十三辙、流行 Hook 或气声女声套给所有作品。

## 目录

1. 通用情绪与能量
2. 多语言写词
3. 曲风专项写词
4. 人声与真实性
5. Hook、riff、flow 与 motif
6. 质量检查

## 1. 通用情绪与能量

### 1.1 情绪词

| 中文 | 英文 | 强度 | 常见用途 |
|------|------|------|----------|
| 平静 | peaceful / calm | 1 | Ambient、Folk、Jazz Ballad |
| 温柔 | tender / gentle | 2 | Pop、Folk、Soul |
| 怀旧 | nostalgic | 2 | City Pop、Country、Guofeng |
| 苦乐参半 | bittersweet | 2 | 关系、成长、回忆 |
| 怅惘 | wistful | 2 | Folk、Jazz、Guofeng |
| 忧郁 | melancholic | 2 | R&B、Dream Pop、Blues |
| 希望 | hopeful | 2 | Pop、Cinematic、Folk |
| 喜悦 | joyful | 3 | Dance Pop、Latin、Ska |
| 自信 | confident | 3 | Hip-Hop、Funk、Pop |
| 反叛 | defiant / rebellious | 4 | Punk、Rock、Rap |
| 热烈 | passionate | 4 | Latin、Soul、Rock |
| 强烈 | intense | 4 | EDM、Metal、Trailer |
| 史诗 | epic / majestic | 5 | Cinematic、Orchestral、Metal |
| 绝望 | desperate | 5 | Dark Ambient、Doom、悲剧 |

每个 Prompt 通常选择 2–3 个相互兼容的情绪词。需要情绪弧线时，使用“起点 + 转化 + 终点”，例如 `melancholic, gradually hopeful`。

### 1.2 能量与动态

| 目标 | Prompt 词 |
|------|-----------|
| 极简 | sparse, minimal, restrained |
| 松弛 | laid-back, pocketed, unhurried |
| 流动 | flowing, swaying, gently pulsing |
| 推进 | driving, propulsive, building |
| 爆发 | explosive, hard-hitting, massive |
| 渐强 | slow-burn crescendo, layered build |
| 戏剧对比 | sudden drop, dynamic contrast, dramatic pause |
| 消散 | decaying, dissolving, fading into silence |

## 2. 多语言写词

### 2.1 中文普通话

- 先考虑自然语序和可唱性，再考虑押韵。
- 可使用十三辙，也可使用现代口语近韵。
- 避免整首都用“的、了、着、过”做韵脚。
- Pop / R&B 可使用长短句与断句；Rap 增加内韵；Guofeng 才优先四、五、七字句。

常用韵部：

| 韵部 | 情绪 | 示例韵脚 |
|------|------|----------|
| ang / iang | 开阔、明亮 | 光、方向、远方 |
| an / ian | 温暖、叙事 | 年、从前、人间 |
| ou / iu | 含蓄、回望 | 秋、回眸、温柔 |
| i / ü | 细腻、现代 | 记忆、呼吸、距离 |
| ao / iao | 洒脱、动作 | 跑、燃烧、浪潮 |
| en / in | 深沉、克制 | 人、痕、安静 |

### 2.2 粤语

- 以自然粤语表达为前提，不把普通话逐字改写。
- 留意粤语声调、入声和口语词。
- 用户未提供粤语能力要求时，避免生僻俚语和强地域笑点。
- 输出可注明建议由粤语母语者复核咬字与声调。

### 2.3 英语

- 旋律重音落在实词重音，不把弱读词放在长强拍。
- 使用 end rhyme、internal rhyme、slant rhyme 和 multisyllabic rhyme。
- 避免为了押韵反复使用 `love / above / forever` 等陈词。
- Rap 优先 cadence、stress pattern 和 bar length；Pop 优先标题 Hook。

### 2.4 日语

- 以 mora（拍）和自然助词位置组织句子。
- 避免把中文语序逐字翻译成日语。
- J-Pop 可使用较密音节；Ballad 保留长元音和停顿空间。
- 无法确认表达自然度时，使用较简洁的标准语，并建议母语复核。

### 2.5 双语

- 为每种语言分配功能，而不是逐句对译。
- 常见方案：Verse 主语言、Pre 过渡、Chorus 以短外语 Hook 强化记忆。
- 两种语言的人称、时间线和语气必须一致。
- 控制切换频率，避免每行切换造成表演困难。

## 3. 曲风专项写词

### 3.1 Pop

- 一首歌只服务一个核心概念。
- Verse 提供证据，Pre 提出压力，Chorus 给出一句可概括的情感真相。
- Hook 通常 2–8 个中文字符或 2–7 个英文词。
- 最终 Chorus 可改写一到两行，让重复产生新意义。

关键词：`catchy hook, conversational lyrics, universal theme, singable phrasing`

### 3.2 Folk / Singer-Songwriter

- 每段至少新增一个事件、时间、地点或因果。
- 使用生活物件和动作，不用空泛“青春、远方、梦想”代替故事。
- Refrain 简短，像故事中的固定标记。

关键词：`storytelling, intimate, plainspoken, vivid details, reflective`

### 3.3 Country / Americana

- 第一段交代 who / where，第二段交代 consequence，Bridge 揭示代价或反转。
- 标题最好能在 Chorus 中变成 punchline。
- 口语真实优先于文学修辞。

关键词：`narrative payoff, specific places, conversational, title hook`

### 3.4 R&B / Soul

- 允许半句、停顿、重复和拖尾，给 groove 留空间。
- 使用身体感、触觉、时间、室内细节和关系边界。
- 副歌可克制，不强求高音大爆发。
- ad-lib 不写成主叙事，可在段落说明中标注。

关键词：`intimate, sensual, syncopated phrasing, negative space, ad-libs`

### 3.5 Hip-Hop / Rap

先确定 BPM、半拍感和 bar 数，再写词。

- 每个 bar 有可识别的重音落点。
- 使用内韵、跨行韵、多音节韵和押头韵。
- punchline 服务观点，不连续堆双关。
- Verse 之间必须推进立场、证据或故事。
- Hook 可旋律化，但不能只是普通 Pop 副歌移植。

检查：

- 16 bars 是否真的可数
- flow 是否有变化
- 韵脚是否只押最后一个字
- beat switch 后语义是否变化

关键词：`dense internal rhymes, multisyllabic rhyme, pocketed flow, punchlines`

### 3.6 Rock

- 句子以强动词、冲突和立场为主。
- 重要词对齐 snare、riff 切口或小节强拍。
- 允许不整齐句长，避免朗诵腔。
- Bridge 可由声音动态承担，不一定写哲理总结。

关键词：`urgent, anthemic, raw, riff-aligned phrasing, live energy`

### 3.7 Punk

- 短句、直接、快速、可齐唱。
- 使用反问、命令、口号和自嘲。
- 不堆辞藻，不做冗长铺陈。

关键词：`shout-along, blunt, rebellious, concise, sarcastic`

### 3.8 Metal

- 主题可处理神话、权力、心理冲突、末世或存在问题。
- 使用高对比、具象动作和强音节。
- clean 与 harsh vocal 段落需要不同音节密度。
- 不默认写暴力细节，也不默认使用极端嗓。

关键词：`dark imagery, dramatic tension, forceful stresses, mythic scale`

### 3.9 EDM / Electronic

- topline 句子短、元音清楚，适合重复与 vocal chop。
- build 减少文字密度，Drop 可用无词动机。
- Techno / House 可完全依靠 groove，不强制歌词叙事。

关键词：`minimal topline, repetitive hook, open vowels, drop-ready`

### 3.10 Jazz

- 语言像自然对话，可略微落后于拍点。
- 使用机智、含蓄、暧昧和双层含义。
- AABA 的 B 段需要新视角或新和声语感。
- 不强制整齐韵脚，重视 phrasing 和留白。

关键词：`conversational phrasing, understated, witty, behind-the-beat`

### 3.11 Blues

- 常用 AAB：第一句陈述，第二句重复或微改，第三句回应。
- 写具体困境、欲望、工作、道路、金钱或关系。
- 可以苦中带笑，不只写悲惨。

关键词：`AAB lyric form, plainspoken, weary humor, call and response`

### 3.12 Reggae / Ska

- 句子服从反拍和松弛 pocket。
- 可写团结、日常、社会观察、自由与希望。
- chant / response 适合作为 Hook。

关键词：`laid-back phrasing, chant hook, social observation, uplifting`

### 3.13 Latin

- 先确认子风格，再匹配歌词密度与重音。
- Reggaeton 适合短 Hook；Salsa 适合 call and response；Bolero 适合长抒情句；Tango 适合戏剧停顿。
- 不把“热情、舞蹈、夜晚”当作全部拉丁表达。

关键词：`rhythmic phrasing, call and response, passionate, danceable`

### 3.14 Classical / Cinematic

- 纯音乐不写歌词。
- 艺术歌曲、合唱或主题曲要让文字重音服从乐句和呼吸。
- 影视主题曲先服务剧情角色，再考虑通用金句。

关键词：`through-composed text, motif-driven, narrative function, choral diction`

### 3.15 Ambient / Experimental

- 允许词语碎片、重复、耳语、语音采样和非线性文本。
- 每次重复应改变音色、空间或语义。
- 不要求传统押韵或完整副歌。

关键词：`fragmented text, mantra, whispered phrases, semantic ambiguity`

### 3.16 Guofeng

根据子风格选择语体：

- 古风 / 江南 / 仙侠：四、五、七字句，十三辙，比兴与留白。
- 新中式：现代语序 + 克制传统意象。
- 国潮 / 国风电子：可使用现代口语、Rap 或短 Hook。
- 戏腔：字头清楚、拖腔空间、强情绪转折。
- 家国 / 武侠：开阔韵脚、动作和宏观画面。

国风意象采用“三意象法则”：同一段只选 2–3 个有时空或动作关系的意象。

关键词：`classical Chinese diction, restrained imagery, tonal phrasing, poetic but singable`

## 4. 人声与真实性

### 4.1 通用真人感

| 目标 | Prompt 词 |
|------|-----------|
| 自然呼吸 | natural breathing |
| 近麦私密 | intimate close-mic vocals |
| 不过度修音 | raw vocals, imperfect takes |
| 动态真实 | dynamic vocal delivery, emotional dynamics |
| 轻微沙哑 | subtle rasp |
| 轻微破音 | slight vocal crack |
| 微颤音 | slight vibrato |
| 现场质感 | live performance feel |

通常选择 2–4 个，不要全部堆入。

### 4.2 按曲风

| 曲风 | 推荐组合 |
|------|----------|
| Pop | mid-range, breathy or dynamic, slight vibrato |
| Folk / Country | raw, natural breathing, intimate |
| R&B / Soul | intimate close-mic, breathy, vocal fry, ad-libs |
| Hip-Hop | confident, conversational, pocketed flow |
| Rock | raw, gritty, dynamic |
| Punk | urgent, imperfect, gang vocals |
| Metal | powerful clean; harsh vocals only if requested |
| Jazz | conversational, behind-the-beat, subtle vibrato |
| Blues | soulful, gritty, expressive bends |
| Reggae | laid-back, warm, chant-ready |
| Latin | rhythmic, passionate, call and response |
| Guofeng | breathy / mid-range / raw / opera-style by subgenre |
| Ambient | whispered, vocal texture, spoken fragments |

### 4.3 音域与唱法

- 用户要求舒适区时，写明大致音域、`comfortable range`、`no belting`、`no key change`。
- 不把高音等同于高潮；可用和声、配器和歌词变化。
- 男声、女声、对唱或合唱由叙事与音色决定，不以主题刻板匹配。
- 特殊唱法必须与用户要求相符。

## 5. Hook、riff、flow 与 motif

不同曲风的记忆点形式不同：

| 曲风 | 主要记忆点 |
|------|------------|
| Pop | 歌词 Hook + 主旋律 |
| Folk / Country | 标题 Refrain + 故事反转 |
| R&B | groove + vocal phrase |
| Hip-Hop | flow pattern + punchline + Hook |
| Rock / Metal | riff + dynamic hit |
| Punk | shout-along line |
| EDM | drop motif + sound design |
| Jazz | melodic head + harmonic turn |
| Blues | AAB line + guitar response |
| Classical / Cinematic | leitmotif |
| Ambient | timbral event / mantra |
| Guofeng | 核心意象句 + 民族音色动机 |

不要因为没有歌词副歌就判定作品“没有 Hook”。

## 6. 质量检查

### 通用

- [ ] 语言自然，重音符合目标语言
- [ ] 写词方式与曲风一致
- [ ] 每段新增信息、视角或动态
- [ ] 记忆点形式符合曲风
- [ ] 没有为了押韵牺牲语意
- [ ] 没有文化或性别刻板拼贴

### 人声

- [ ] 人声类型符合用户要求
- [ ] 真人感关键词 2–4 个且不矛盾
- [ ] 音域、唱法和高潮方式一致
- [ ] 纯音乐没有人声描述

### 反模式

- 所有中文歌词都写成古风七字句
- 所有女声都使用气声
- 所有 Rock / Metal 都写成喊叫
- Rap 只有句尾单押，没有 bars 和 flow
- Jazz 只加入 saxophone，没有和声与留白
- Latin、Reggae、Country 只使用表面场景词
- 双语歌词逐句机械翻译
