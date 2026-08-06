# Suno 全曲风 Prompt 公式

Prompt 必须让曲风、节奏、配器、人声/无人声、结构和制作质感互相一致。不要用标签数量掩盖不明确的音乐设计。

## 目录

1. 通用公式
2. 人声与纯音乐分支
3. 18 类曲风模板
4. 融合与未知曲风
5. 长度与质量控制
6. 故障排查

## 1. 通用公式

按以下顺序：

```text
<主曲风 + 子风格>,
<情绪 + 能量>,
<BPM + 拍号 + groove>,
<3–5 个核心乐器/音色>,
<具体场景 + 制作质感>,
<人声或 instrumental>,
<结构/高潮约束>,
<质量词>,
(((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 字段要求

| 字段 | 目标 |
|------|------|
| 主曲风 | 写清子风格或年代，不只写 Pop / Rock / Electronic |
| 情绪 | 2–3 个相容词，必要时写转化路径 |
| 节奏 | 具体 BPM、拍号和 groove / swing / half-time / free-time |
| 配器 | 3–5 个核心音色；管弦可按乐器组 |
| 场景 | 时间、地点、空间或剧情功能中的至少两项 |
| 制作 | acoustic、live-room、analog、polished、lo-fi、hybrid 等 |
| 人声 | 类型 + 2–4 个真实性/唱法词；纯音乐写 no vocals |
| 结构 | catchy chorus、AABA、build and drop、motif development 等 |
| 质量 | 选择一档，避免重复同义词 |

## 2. 人声与纯音乐分支

### 2.1 有人声

```text
<language> <vocal type>, <range/timbre>, <2–4 realism or delivery terms>
```

示例：

- `Mandarin female vocals, warm mid-range, intimate close-mic, natural breathing`
- `English male rock vocals, gritty and raw, dynamic live delivery`
- `bilingual duet, contrasting soft and powerful voices, natural phrasing`
- `confident rap vocals, pocketed flow, clear consonants, restrained ad-libs`

音域约束：

- `comfortable vocal range`
- `no belting`
- `no key change`
- `low-register delivery`
- `brief high notes only`

### 2.2 纯音乐

必须写：

`instrumental, no vocals`

不得同时出现 `female vocals`、`choir vocals`、`vocal chops` 等人声要求。若使用无词人声纹理，则作品不再属于严格 no-vocals，应写成 `wordless vocal textures` 并在输出中说明。

纯音乐还应描述：

- motif
- development
- dynamic arc
- ending / loop behavior

## 3. 18 类曲风模板

模板用于结构参考，不要原样套用与主题无关的场景。

### 3.1 Pop

```text
Modern Mandopop, polished indie pop, bittersweet and hopeful, 96 BPM, 4/4 time, piano, clean electric guitar, warm synth pads, tight drums, bass guitar, late-night city walk turning into sunrise, Mandarin female vocals, clear mid-range, natural breathing, dynamic delivery, concise verses, memorable singable chorus, Hi-Res audio, 24-bit master, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.2 Rock

```text
Alternative rock, guitar-driven and emotionally restrained, tense then cathartic, 118 BPM, 4/4 time, overdriven electric guitars, bass guitar, acoustic drum kit, subtle organ, live rehearsal room energy, Mandarin male vocals, raw and dynamic, slight rasp, recurring riff, full-band chorus, bridge breakdown and guitar solo, reference quality, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.3 Metal

```text
Progressive metal, dark and defiant, 132 BPM with changing meters, down-tuned guitars, tight bass, double-kick acoustic drums, restrained orchestral layer, vast ruined industrial landscape, powerful clean vocals with brief harsh accents only, complex recurring riffs, controlled breakdown, melodic solo, massive but clear mix, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

如果用户未允许极端嗓，删除 `harsh accents`。

### 3.4 Punk

```text
Pop punk, fast, youthful and rebellious, 178 BPM, 4/4 time, distorted rhythm guitars, pick bass, punchy acoustic drums, small sweaty club performance, urgent imperfect lead vocals, gang-vocal hook, short verses, half-time bridge, hard-stop ending, raw live production, streaming master, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.5 Folk

```text
Intimate indie folk, warm, reflective and quietly healing, 78 BPM, 4/4 time, fingerpicked acoustic guitar, upright piano, cello, brushed percussion, rain fading outside a small wooden room, Mandarin female vocals, raw, breathy, close-mic, natural breathing, detailed storytelling verses, short recurring refrain, organic live-room sound, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.6 R&B / Soul

```text
Alternative R&B, neo-soul, cold and intimate, 76 BPM, 4/4 time, restrained syncopated groove, Rhodes electric piano, warm sub-bass, tight drums, muted guitar, rain-lit apartment after midnight, Mandarin female vocals, breathy low alto, intimate close-mic, subtle vocal fry, spacious verses, restrained chorus, ad-lib outro, 24-bit master, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.7 Hip-Hop / Rap

```text
Modern boom bap with subtle jazz influence, focused and self-assured, 88 BPM, 4/4 time, dusty sampled drums, upright bass loop, chopped piano, muted horn texture, late-night train platform atmosphere, Mandarin rap vocals, clear consonants, pocketed flow, dense internal rhymes, two 16-bar verses, 8-bar hook, purposeful beat switch, warm analog mix, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

Trap / Drill 需替换鼓组、BPM pocket 和 808 描述，不要只改名称。

### 3.8 Electronic / EDM

```text
Melodic house, euphoric and wistful, 124 BPM, 4/4 four-on-the-floor groove, warm synth plucks, wide pads, deep rounded bass, crisp electronic drums, coastal highway at blue hour, instrumental, no vocals, motif-led intro, controlled build, melodic first drop, stripped breakdown, evolved second drop, clean club-ready master, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.9 Jazz

```text
Cool vocal jazz, intimate and understated, 72 BPM, 4/4 with a relaxed swing feel, upright piano, upright bass, brushed drums, muted trumpet, dim hotel lounge before closing, English female vocals, conversational phrasing, behind-the-beat delivery, subtle vibrato, AABA form, spacious trumpet solo, natural room ambience, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.10 Blues

```text
Electric Chicago blues, weary but wry, 92 BPM, 4/4 shuffle, expressive electric guitar, harmonica, Hammond organ, bass, live drums, nearly empty roadside bar at midnight, English male vocals, gritty and soulful, AAB lyric form, 12-bar progression, guitar-vocal call and response, raw live mix, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.11 Country / Americana

```text
Americana country ballad, honest, nostalgic and resilient, 84 BPM, 4/4 time, acoustic guitar, telecaster, pedal steel, upright bass, brushed drums, dawn over a quiet highway and an old gas station, English female vocals, natural storytelling, warm mid-range, specific narrative verses, title-payoff chorus, fiddle-free organic production, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.12 Reggae / Ska

```text
Roots reggae, warm, reflective and quietly defiant, 78 BPM, 4/4 one-drop groove, melodic deep bass, offbeat guitar skank, organ bubble, restrained drums, sunlit neighborhood after rain, relaxed lead vocals, natural phrasing, chant-ready refrain, spacious dub break, tape delay accents, warm analog mix, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.13 Latin

```text
Romantic bachata, tender and rhythmically intimate, 126 BPM, 4/4 time, requinto guitar, rhythm guitar, bongo, güira, bass, warm courtyard dance at night, Spanish duet vocals, natural rhythmic phrasing, call and response, concise verses, memorable chorus, acoustic-forward polished production, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

使用 Salsa、Bolero、Tango、Bossa Nova 或 Reggaeton 时，必须替换具体节奏和核心配器。

### 3.14 Classical / Orchestral

```text
Neo-classical chamber orchestral, contemplative and gradually hopeful, free-flowing 68 BPM, 3/4 time, solo piano, chamber strings, clarinet, soft timpani, first light entering an abandoned hall, instrumental, no vocals, fragile four-note motif, contrapuntal development, restrained climax, intimate coda, natural hall acoustics, realistic orchestration, 24-bit master, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.15 Cinematic / Soundtrack

```text
Cinematic fantasy game score, mysterious, adventurous and luminous, 90 BPM, shifting 6/8 and 4/4, strings, woodwinds, French horns, hybrid percussion, one wooden flute soloist, hidden valley revealed at sunrise, instrumental, no vocals, clear leitmotif, three-stage narrative build, heroic climax, unresolved magical tail for scene transition, wide dynamic range, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.16 Ambient / Experimental

```text
Minimal dark ambient, suspended, desolate and slowly transforming, free time, low analog drone, granular field recordings, bowed metal, distant prepared piano, empty underground station after the last train, instrumental, no vocals, gradual spectral movement, sparse events, one density peak, long subtractive decay, deep spatial mix, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

### 3.17 World / Regional

```text
Contemporary Celtic folk, windswept and hopeful, 104 BPM, 6/8 time, fiddle, uilleann pipes, acoustic guitar, bodhrán, upright bass, cliff path above the sea at dawn, English female vocals, raw and clear, natural ornamentation, dance-like refrain, organic ensemble recording, respectful regional instrumentation, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

将 `Celtic` 替换为其他地域时，必须同步更换乐器、节奏与唱法，禁止笼统 `tribal/ethnic`。

### 3.18 Guofeng

```text
Jiangnan guofeng ballad, graceful, wistful and gently healing, 76 BPM, 4/4 time, guzheng, xiao flute, sparse pipa, soft string ensemble, old stone alley after rain at dawn, Mandarin female vocals, breathy soft mid-range, intimate close-mic, natural breathing, restrained verse-chorus form, no belting, traditional Chinese instruments, authentic timbre, pentatonic scale, 24-bit master, (((Quality: MAX, MAX, MAX, Realism: MAX)))
```

`pentatonic scale` 仅在子风格需要时使用。戏腔、国风电子、家国、敦煌等应加载各自唱法、节奏和配器。

## 4. 融合与未知曲风

### 4.1 融合公式

```text
<主曲风>, blended with <次曲风> through <明确的一到两项元素>, ...
```

示例：

```text
Alternative R&B blended with restrained guofeng instrumentation through guzheng harmonics and xiao responses, ...
```

规则：

- 主曲风决定结构和 groove。
- 次曲风只贡献明确元素。
- 第三风格最多一个点缀。
- 检查 BPM、拍号、人声和低频逻辑是否冲突。

### 4.2 未知曲风

如果无法直接确认：

1. 保留用户给出的曲风名称。
2. 写出可确认的速度、节奏、配器、地域、年代与人声特征。
3. 选择最近的主曲风作为结构骨架。
4. 不写未经确认的文化或音乐学术语。

格式：

```text
<user genre label>, interpreted as <nearest genre family> with <confirmed traits>, ...
```

## 5. 长度与质量控制

### 5.1 Prompt 长度

| 类型 | 目标词数 |
|------|----------|
| Demo / 短歌 | 40–65 |
| 标准歌曲 | 50–100 |
| 融合 / 管弦 / 复杂纯音乐 | 70–120 |

超长时按顺序精简：

1. 删除重复质量词
2. 合并场景描述
3. 减少非核心乐器
4. 删除同义情绪词

不要删除：

- 主曲风和子风格
- BPM / 拍号或 free-time
- 核心配器
- 人声或 no-vocals 约束
- 结构特征
- `(((Quality: MAX, MAX, MAX, Realism: MAX)))`

### 5.2 质量词

基础：

`studio quality, professional mix, mastered, high fidelity`

标准：

`Hi-Res audio, 24-bit master, reference quality, mastered for streaming`

按曲风增加一到两项：

- Acoustic：`natural resonance, live-room sound`
- Rock：`live band energy, realistic room mics`
- Electronic：`controlled sub-bass, precise transients`
- Vintage：`tape warmth, analog saturation`
- Orchestral：`natural hall acoustics, realistic orchestration`
- Guofeng：`traditional Chinese instruments, authentic timbre`

## 6. 故障排查

### 6.1 曲风只像普通流行

- 检查是否写了曲风专属结构。
- 检查节奏词是否具体。
- 检查核心配器是否真的具有辨识度。
- 删除泛化 `catchy pop` 标签。

### 6.2 人声像 AI

- 选择 2–4 个真实唱法词：`natural breathing`、`raw`、`intimate close-mic`、`slight rasp`。
- 减少 `perfect, angelic, crystalline, soaring`。
- 写明音区和动态，不只写性别。

### 6.3 配器混浊

- 减到 3–5 个核心音色。
- 明确主旋律、和声、节奏和低频职责。
- 管弦按乐器组描述。

### 6.4 结构不对

- Rap 检查 bars。
- EDM 检查 build/drop。
- Jazz 检查 AABA 或 head–solo–head。
- Blues 检查 AAB / 12-bar。
- Classical / Cinematic 检查 motif development。
- Ambient 检查音色随时间变化。

### 6.5 纯音乐出现人声

- 确认存在 `instrumental, no vocals`。
- 删除所有 vocal、choir、vocal chop、chant 等词。
- 如果需要无词人声纹理，改为非严格纯音乐并明确说明。

### 6.6 国风关键词污染非国风

非国风 Prompt 删除：

- `traditional Chinese instruments`
- `authentic timbre`（除非确实指某传统乐器真实性）
- `pentatonic scale`
- 无关古筝、二胡、箫等配器

### 6.7 用户约束冲突

用户硬约束优先。在输出中用一句话说明取舍，不隐藏冲突，也不擅自忽略。
