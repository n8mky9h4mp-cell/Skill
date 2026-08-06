# 全曲风路由矩阵

本文件负责把用户需求映射为可执行的曲风规则。先确定主曲风，再加载对应的结构、配器、写词与 Prompt 规范。不要把曲风名称当作装饰标签；结构、节奏、人声、歌词语体和配器必须共同体现该曲风。

## 目录

1. 自动选择流程
2. 18 个主曲风家族
3. 融合曲风
4. 未知曲风兜底
5. 冲突处理

## 1. 自动选择流程

### 1.1 决策优先级

`用户明确指定 > 用户提供的参考歌曲或艺术家特征 > 主题与使用场景推导 > 默认推荐`

- 用户指定曲风时直接采用，不因主题刻板印象擅自替换。
- 用户只给主题时，从下列五个维度自动选择一个主曲风，并用一句话说明理由。
- 用户要求融合时，最多使用两个主曲风作为骨架；第三种风格只能贡献一种点缀元素。

### 1.2 五维匹配

| 维度 | 低值示例 | 高值示例 | 影响 |
|------|----------|----------|------|
| 情绪能量 | 平静、私密、冥想 | 热烈、愤怒、史诗 | BPM、动态、鼓组、人声强度 |
| 叙事密度 | 氛围、重复、动机 | 故事、观点、事件推进 | Verse 数量、歌词密度、结构 |
| 使用场景 | 放松、学习、背景 | 舞台、舞池、短视频、影视 | Hook 时机、结构规模、混音 |
| 声音偏好 | 原声、复古、自然 | 电子、重型、实验、管弦 | 配器与制作质感 |
| 人声需求 | 无人声、轻声 | 说唱、强唱、合唱、特殊唱法 | 音域、flow、和声、段落标签 |

### 1.3 快速路由

- 强叙事 + 原声质感 → Folk / Country / Singer-Songwriter
- 强 Hook + 普适旋律 → Pop
- 私密夜晚 + 律动 → R&B / Soul
- bars、flow、态度表达 → Hip-Hop / Rap
- riff、现场乐队、动态递进 → Rock
- 重型失真、极端动态、breakdown → Metal
- 舞池、build、drop → Electronic / EDM
- 和声色彩、swing、即兴 → Jazz
- 12-bar、蓝调音阶、生活苦乐 → Blues
- offbeat、松弛律动 → Reggae / Ska
- clave、syncopation、拉丁打击乐 → Latin
- 主题动机、管弦叙事 → Classical / Orchestral / Cinematic
- 音色演变、空间感、弱叙事 → Ambient / Experimental
- 明确地域乐器与语言传统 → World / Regional
- 中国传统语体、五声音阶、民族乐器 → Guofeng

## 2. 18 个主曲风家族

### 2.1 Pop / 流行

- **子风格**：Mandopop、C-Pop、synth-pop、indie pop、dream pop、city pop、dance-pop、power ballad、bedroom pop
- **BPM / 拍号**：70–130；通常 4/4
- **结构**：Verse–Pre–Chorus、Hook 前置或精简流行结构
- **写词**：清晰口语、单一核心概念、短 Hook；主歌用具体细节，副歌扩大共鸣
- **人声**：mid-range、breathy、dynamic、layered vocals；按情绪选择轻声或强唱
- **配器**：piano、synth、guitar、bass、drums、strings
- **Prompt 核心**：catchy melody、polished production、memorable chorus
- **反模式**：只有泛化“好听、感人”，没有清晰 Hook 或段落对比

### 2.2 Rock / 摇滚

- **子风格**：indie rock、alternative rock、folk rock、pop rock、post-rock、garage rock、psychedelic rock、hard rock
- **BPM / 拍号**：80–170；常用 4/4，后摇可变拍
- **结构**：riff intro、Verse–Chorus、动态递进、solo、crescendo
- **写词**：直接、有动作和立场；句长服从鼓点与 riff，允许不规则重音
- **人声**：raw、gritty、dynamic、powerful 或 restrained indie vocals
- **配器**：electric guitar、bass guitar、acoustic drums、optional keys
- **Prompt 核心**：guitar-driven、live band energy、dynamic crescendo
- **反模式**：把摇滚等同于“大声”，却没有 riff、鼓贝斯互动和动态曲线

### 2.3 Metal / 金属

- **子风格**：heavy metal、metalcore、progressive metal、symphonic metal、nu metal、doom metal、power metal
- **BPM / 拍号**：60–220；4/4、6/8 或复合/变拍
- **结构**：riff、double-kick section、breakdown、solo、dramatic bridge
- **写词**：高强度意象、冲突、神话、心理或社会主题；句子与切分 riff 对齐
- **人声**：powerful clean、grit、scream/growl 仅在用户允许时使用
- **配器**：down-tuned guitars、bass、acoustic drums、double kick、optional orchestra
- **Prompt 核心**：heavy riffs、tight rhythm section、breakdown、massive drums
- **反模式**：未经用户允许加入极端嗓；只有失真吉他，没有重型结构

### 2.4 Punk / 朋克

- **子风格**：pop punk、punk rock、post-punk、emo、hardcore punk
- **BPM / 拍号**：120–220；通常 4/4
- **结构**：短 Intro、快速 Verse–Chorus、短 bridge；少铺垫
- **写词**：直白、反叛、青春、讽刺或自嘲；句子短，强重音
- **人声**：raw、urgent、imperfect、gang vocals
- **配器**：distorted guitars、pick bass、fast acoustic drums
- **Prompt 核心**：fast tempo、raw live energy、shout-along hook
- **反模式**：制作过度精致、歌词过分文雅、结构拖沓

### 2.5 Folk / 民谣

- **子风格**：acoustic folk、indie folk、urban folk、traditional folk、singer-songwriter、folk pop
- **BPM / 拍号**：60–110；4/4、3/4 或 6/8
- **结构**：叙事 Verse、简短 Chorus、strophic 或 Verse–Chorus
- **写词**：人物、时间、地点和动作具体；优先故事推进与自然口语
- **人声**：raw、breathy、intimate close-mic、natural breathing
- **配器**：acoustic guitar、piano、harmonica、cajon、upright bass、strings
- **Prompt 核心**：storytelling、organic、intimate live-room sound
- **反模式**：空泛抒情、每段只换意象不推进故事

### 2.6 R&B / Soul

- **子风格**：contemporary R&B、alternative R&B、neo-soul、bedroom R&B、classic soul、funk soul
- **BPM / 拍号**：60–105；通常 4/4
- **结构**：groove-first Verse、Pre、restrained Chorus、vamp、ad-lib outro
- **写词**：私密、感官、都市、关系边界；允许口语断句与重复
- **人声**：breathy、intimate、melismatic、vocal fry、emotional ad-libs
- **配器**：Rhodes、groovy bass、tight drums、sub-bass、guitar、pads
- **Prompt 核心**：syncopated groove、late-night intimacy、warm low end
- **反模式**：所有句子整齐七字；旋律和鼓点没有切分

### 2.7 Hip-Hop / Rap

- **子风格**：boom bap、trap、lo-fi hip-hop、conscious rap、drill、melodic rap、old school
- **BPM / 拍号**：65–160；通常 4/4，可用半拍感
- **结构**：8/16/24-bar Verse、Hook、beat switch、intro/outro
- **写词**：flow 优先；使用内韵、多音节韵、重音回环、punchline 与观点推进
- **人声**：spoken-rhythmic、confident、conversational、melodic hook
- **配器**：sample、drum machine、808/sub-bass、keys、texture
- **Prompt 核心**：specific drum era/region、flow、bass character、sample texture
- **反模式**：只在普通流行歌词上加“rap”；不标 bars、不考虑重音与内韵

### 2.8 Electronic / EDM

- **子风格**：house、techno、trance、future bass、dubstep、drum and bass、synthwave、downtempo、chillwave
- **BPM / 拍号**：70–180；通常 4/4，D&B 常 160–180
- **结构**：intro、build、drop、breakdown、second drop、outro
- **写词**：短句、重复 Hook、vocal chop 友好；纯音乐可完全无歌词
- **人声**：processed lead、airy topline、chopped vocals 或 instrumental
- **配器**：synth lead、pads、arpeggiator、electronic drums、sub-bass、FX
- **Prompt 核心**：明确子风格、BPM、drop 类型和低频质感
- **反模式**：只写 electronic；没有 build/drop 能量曲线

### 2.9 Jazz

- **子风格**：vocal jazz、swing、bebop、cool jazz、jazz ballad、bossa jazz、jazz fusion
- **BPM / 拍号**：50–240；4/4 swing、3/4、5/4 等
- **结构**：AABA、ABAC、head–solo–head、vamp
- **写词**：重视自然重音、留白、机智和对话感；不强制密集押韵
- **人声**：conversational phrasing、behind-the-beat、subtle vibrato、scat 可选
- **配器**：piano、upright bass、brushed drums、saxophone、trumpet、guitar
- **Prompt 核心**：swing feel、extended harmony、improvisational space
- **反模式**：套流行大副歌；乐器很多却没有和声与即兴空间

### 2.10 Blues

- **子风格**：Delta blues、Chicago blues、electric blues、soul blues、blues rock
- **BPM / 拍号**：55–150；4/4 shuffle 或 12/8
- **结构**：12-bar blues、AAB lyric form、call and response
- **写词**：具体困境、苦中带笑、重复首句后给出转折；口语自然
- **人声**：raw、gritty、soulful、expressive bends
- **配器**：electric/acoustic guitar、harmonica、organ、bass、drums
- **Prompt 核心**：12-bar form、shuffle、blue notes、call and response
- **反模式**：只有悲伤情绪，没有 AAB、shuffle 或蓝调音阶特征

### 2.11 Country / Americana

- **子风格**：modern country、classic country、Americana、bluegrass、country pop、outlaw country
- **BPM / 拍号**：65–150；4/4、2/4 或 3/4
- **结构**：故事 Verse、清晰 Chorus、turnaround、bridge 或 instrumental break
- **写词**：人物与地名具体，因果清楚，口语化，标题常是核心反转
- **人声**：natural storytelling、warm twang 可选
- **配器**：acoustic guitar、telecaster、pedal steel、banjo、fiddle、mandolin、upright bass
- **Prompt 核心**：storytelling、rootsy、specific acoustic instruments
- **反模式**：用公路、酒馆等表面词替代真实故事

### 2.12 Reggae / Ska

- **子风格**：roots reggae、dub、dancehall、ska、reggae pop
- **BPM / 拍号**：70–150；通常 4/4
- **结构**：groove intro、Verse–Chorus、dub break、toast/rap 可选
- **写词**：松弛、团结、社会观察、阳光或抗争；句子服从反拍
- **人声**：laid-back、warm、chant、toast
- **配器**：offbeat guitar/keys、deep bass、one-drop drums、horns
- **Prompt 核心**：one-drop、skank rhythm、deep rounded bass、dub space
- **反模式**：只有热带意象，没有反拍和低频结构

### 2.13 Latin

- **子风格**：reggaeton、salsa、bachata、bolero、Latin pop、tango、bossa nova
- **BPM / 拍号**：70–180；4/4 为主，部分 3/4
- **结构**：循环律动、Verse–Chorus、montuno、dance break
- **写词**：身体感、情感张力、呼应重复；根据语言保持自然重音
- **人声**：rhythmic phrasing、passionate、call and response
- **配器**：congas、bongos、timbales、clave、nylon guitar、piano、brass
- **Prompt 核心**：明确 clave/dembow/bolero 等节奏，不只写 Latin
- **反模式**：把所有拉丁风格都写成 reggaeton

### 2.14 Classical / Orchestral

- **子风格**：chamber、romantic orchestral、minimalism、neo-classical、choral、contemporary classical
- **BPM / 拍号**：按段落变化；支持变速与变拍
- **结构**：主题、发展、对比主题、再现、coda；可使用 through-composed
- **写词**：器乐默认无歌词；艺术歌曲或合唱按文本重音与乐句组织
- **人声**：classical solo、choir、operatic，仅在用户要求时使用
- **配器**：strings、woodwinds、brass、percussion、piano、harp
- **Prompt 核心**：motif development、orchestral dynamics、movement/form
- **反模式**：把管弦乐仅当“宏大铺底”，没有主题发展

### 2.15 Cinematic / Soundtrack

- **子风格**：film score、trailer music、game soundtrack、anime score、documentary score、hybrid orchestral
- **BPM / 拍号**：按画面和情绪变化
- **结构**：cue-based、act arc、motif development、climax、resolution
- **写词**：通常纯音乐；主题曲可采用 Pop 或 Orchestral 人声结构
- **人声**：instrumental、wordless choir、solo vocalise 或明确歌词
- **配器**：orchestra、piano、hybrid percussion、synth textures、ethnic soloist
- **Prompt 核心**：叙事场景、时间长度、动态节点、主题动机
- **反模式**：只写 epic cinematic，缺少剧情功能和动态路径

### 2.16 Ambient / Experimental

- **子风格**：ambient、dark ambient、drone、soundscape、minimal electronic、glitch、electroacoustic
- **BPM / 拍号**：无固定拍、40–100 或自由速度
- **结构**：音色渐变、层次累积、事件式结构、缓慢再现
- **写词**：可无歌词；有人声时使用碎片、重复、耳语或语音采样
- **人声**：whisper、vocal texture、spoken fragments 或 no vocals
- **配器**：pads、field recordings、drone、granular texture、prepared instruments
- **Prompt 核心**：空间、材质、演变速度、声像与动态
- **反模式**：强行加入副歌；只有“空灵”而没有音色演变

### 2.17 World / Regional

- **子风格**：African、Middle Eastern、Indian、Celtic、Nordic、Japanese traditional、Korean traditional、Southeast Asian 等
- **BPM / 拍号**：依据具体地域传统
- **结构**：优先遵循具体传统或与一个现代主曲风融合
- **写词**：尊重语言重音、文化语境和主题，避免拼贴式异域想象
- **人声**：依据传统唱法；不确定时使用自然现代唱法并说明推导
- **配器**：选择 2–3 个确切地域乐器，加必要现代节奏/和声层
- **Prompt 核心**：具体地域、乐器、节奏循环与演唱方式
- **反模式**：使用 vague “tribal/ethnic” 标签；混搭无关文化元素

### 2.18 Guofeng / 国风

- **子风格**：古风流行、江南、仙侠、敦煌、戏腔、国风电子、国潮、侠客、禅意、家国、暗黑国风
- **BPM / 拍号**：50–130；4/4、3/4、6/8 或戏曲板式
- **结构**：标准古风、Drop、戏腔爆点、电影叙事、氛围渐进
- **写词**：中文十三辙、古典或新中式语体、比兴与具体意象；现代国潮可使用口语
- **人声**：breathy、mid-range、raw、opera-style、powerful，按子风格选择
- **配器**：guzheng、pipa、dizi、xiao、erhu、guqin、percussion、orchestra、modern rhythm section
- **Prompt 核心**：traditional Chinese instruments、authentic timbre；需要时使用 pentatonic scale
- **反模式**：无逻辑堆砌民族乐器；所有国风都使用同一种气声女声

## 3. 融合曲风

### 3.1 组合规则

1. 选择一个**主骨架**：决定结构、主要节奏与段落能量。
2. 选择一个**次风格**：贡献和声、配器、人声或制作质感中的一到两项。
3. 第三个风格若存在，只允许作为单一亮点，例如一件乐器或一个桥段。
4. 在 Prompt 中明确主次，例如 `Alternative R&B with restrained guofeng instrumentation`，不要并列堆标签。

### 3.2 冲突检查

- BPM、拍号或 groove 冲突：以主骨架为准。
- 人声冲突：用户指定优先，否则选择更符合叙事视角的方式。
- 配器过多：保留每个风格最具辨识度的一到两个音色。
- 结构冲突：只使用一种主结构；次风格通过段落质感体现。

## 4. 未知曲风兜底

遇到矩阵外名称时：

1. 提取节奏、速度和拍号。
2. 提取标志性乐器与音色。
3. 提取年代、地域和制作质感。
4. 提取人声方式。
5. 提取结构惯例。
6. 映射到最近的主曲风家族，保留原名称作为子风格标签。

如果无法可靠确认其传统，明确写出“按所给特征推导”，不要编造文化或音乐学细节。缺少可用特征时，回退到 Pop 或 Singer-Songwriter 结构，并保留用户明确约束。

## 5. 冲突处理

- 用户硬约束始终优先。
- “不要鼓”“不要高音”“纯音乐”“仅环境音”等约束不得被曲风模板覆盖。
- 如果硬约束削弱典型曲风特征，用一句话说明取舍，再给出最接近的实现。
- 不因题材自动套用性别、语言或文化刻板印象。
- 不自动增加用户未要求的融合风格。
