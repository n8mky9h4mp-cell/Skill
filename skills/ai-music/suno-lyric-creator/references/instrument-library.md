# 全曲风配器与音色库

配器用于建立曲风身份、段落功能和能量曲线。先确定主曲风与节奏骨架，再选择 3–5 个核心乐器或音色组；不要把乐器名称当作装饰目录。

## 目录

1. 三层配器法
2. 全曲风配器矩阵
3. 乐器与音色词库
4. 环境声与声音设计
5. 混音与避坑

## 1. 三层配器法

| 层次 | 职责 | 典型元素 |
|------|------|----------|
| 主体层 | 主旋律、riff、Hook、leitmotif | 人声、吉他、钢琴、sax、民族乐器、synth lead |
| 和声/空间层 | 和弦、持续音、氛围、对位 | keys、strings、pads、guitar layers、choir |
| 节奏/低频层 | groove、pulse、低音与重击 | drums、percussion、bass、sub-bass、ostinato |

原则：

- 普通歌曲选 3–5 个核心音色。
- 管弦作品可按 `strings / woodwinds / brass / percussion` 四个乐器组计数。
- 同音区避免超过三个主导音色。
- 每件乐器写明段落职责，例如“Verse 稀疏、Chorus 扩宽、Bridge 退出”。
- 用户禁用鼓、BGM、高音或特定乐器时，模板不得覆盖。

## 2. 全曲风配器矩阵

### 2.1 Pop

```text
主体：lead vocal / piano / synth lead
和声：pads / guitar / string ensemble
节奏：drum kit / electronic drums / bass guitar / synth bass
亮点：intro motif、post-chorus synth hook
```

子风格：

- Synth-pop：analog synth、arpeggiator、electronic drums
- Indie Pop：clean guitar、warm keys、organic drums
- City Pop：electric piano、funky bass、clean guitar、brass/sax
- Dream Pop：reverb guitar、pads、soft drum machine

### 2.2 Rock

```text
主体：electric guitar riff + lead vocal
和声：rhythm guitars / optional organ or keys
节奏：bass guitar + acoustic drum kit
亮点：guitar solo、feedback tail、dynamic stop
```

- Indie / Alternative：clean-to-overdrive guitar、roomy drums
- Hard Rock：crunch guitar、power chords、large acoustic drums
- Post-Rock：delay guitar、layered tremolo、crescendo drums
- Psychedelic：modulated guitar、organ、tape echo

### 2.3 Metal

```text
主体：down-tuned distorted guitars
和声：double-tracked guitars / optional orchestra or synth
节奏：tight bass + double-kick acoustic drums
亮点：breakdown、guitar solo、drum accents
```

- Doom：slow heavy riffs、low organ、long decay
- Metalcore：syncopated chugs、breakdown、clean chorus
- Symphonic：orchestra/choir as a group, not ten separate instruments
- Progressive：changing meters、extended-range guitar、motif callbacks

### 2.4 Punk

```text
主体：distorted rhythm guitar
和声：second guitar or gang vocals
节奏：pick bass + fast acoustic drums
亮点：count-in、half-time bridge、hard stop
```

保持简单、快速、现场感；不要添加不必要的弦乐和氛围 pad。

### 2.5 Folk / Singer-Songwriter

```text
主体：acoustic guitar / piano / vocal
和声：harmonica / fiddle / cello / light strings
节奏：cajon / brushed percussion / upright bass
亮点：fingerpicked intro、short instrumental turnaround
```

优先真实木质共鸣、指尖噪声和自然房间感。

### 2.6 Country / Americana

```text
主体：acoustic guitar / telecaster / lead vocal
和声：pedal steel / fiddle / mandolin / banjo
节奏：upright or electric bass + acoustic drums
亮点：instrumental turnaround、fiddle/steel answer
```

- Bluegrass：banjo、mandolin、fiddle、upright bass，少用鼓
- Modern Country：telecaster、pedal steel、full drums、bass

### 2.7 R&B / Soul / Funk

```text
主体：lead vocal / Rhodes / clean guitar
和声：warm keys / pads / backing vocals / horns
节奏：groovy bass / sub-bass / tight drums
亮点：vamp、ad-lib outro、syncopated guitar
```

- Neo-Soul：Rhodes、warm bass、pocket drums、jazz guitar
- Alternative R&B：minimal synth、sub-bass、sparse electronic drums
- Classic Soul：organ/piano、horn section、live drums、bass
- Funk：slap/finger bass、clavinet、tight guitar、horn stabs

### 2.8 Hip-Hop / Rap

```text
主体：sample / keys / synth motif
和声：texture / pad / chopped sample
节奏：kick, snare, hats, 808 or sampled bass
亮点：beat switch、sample drop、ad-lib space
```

- Boom Bap：sample chops、dusty drums、warm bass
- Trap：808 bass、rolling hi-hats、sparse keys
- Drill：sliding 808、syncopated hats、dark bells
- Lo-Fi：soft drums、vinyl texture、jazzy keys
- Conscious：organic sample、clear midrange for dense lyrics

### 2.9 Electronic / EDM

```text
主体：synth lead / pluck / bass motif
和声：pads / arpeggiator / atmospheric FX
节奏：electronic drums / sub-bass / percussion loop
亮点：riser、impact、drop sound design
```

- House：four-on-the-floor kick、offbeat hats、bass groove
- Techno：repetitive synth sequence、industrial percussion
- Trance：supersaw、arpeggio、long build、wide pads
- Future Bass：chord chops、sidechain、vocal chops
- Dubstep：wobble/growl bass、half-time drums
- Drum and Bass：breakbeats、reese bass、fast hats
- Synthwave：analog synth、gated snare、retro bass
- Downtempo：soft beat、subtle textures、slow pulse

### 2.10 Jazz

```text
主体：piano / saxophone / trumpet / guitar / vocal
和声：piano or guitar comping
节奏：upright bass + brushed or ride-led drums
亮点：solo space、trading fours、tag ending
```

- Swing：walking bass、ride cymbal、horns
- Cool Jazz：muted trumpet、soft sax、restrained rhythm section
- Jazz Ballad：piano、upright bass、brushes
- Fusion：electric piano、electric bass、drums、guitar/synth
- Bossa Jazz：nylon guitar、soft percussion、upright bass

### 2.11 Blues

```text
主体：electric/acoustic guitar + vocal
和声：Hammond organ / piano / harmonica
节奏：bass + shuffle drums
亮点：call-and-response fills、turnaround
```

明确 acoustic Delta、electric Chicago、soul blues 或 blues rock，避免混用。

### 2.12 Reggae / Ska

```text
主体：lead vocal / melodic bass
和声：offbeat guitar or organ skank / horns
节奏：one-drop or steppers drums / percussion
亮点：dub delay、toast section、horn response
```

Reggae 低频为主角；Ska 加快速度并突出 upstroke guitar 与 horns。

### 2.13 Latin

先选子风格：

| 子风格 | 核心节奏/配器 |
|--------|---------------|
| Reggaeton | dembow、sub-bass、electronic percussion、synth |
| Salsa | clave、congas、timbales、piano montuno、brass、bass |
| Bachata | requinto guitar、rhythm guitar、bongo、güira、bass |
| Bolero | nylon guitar、piano、soft percussion、strings |
| Tango | bandoneon、piano、violin、double bass |
| Bossa Nova | nylon guitar、soft shaker、upright bass、piano |
| Latin Pop | modern drums、bass、nylon guitar、percussion |

不要只写 `Latin percussion`；至少指明具体节奏或两件打击乐。

### 2.14 Classical / Orchestral

```text
主体：solo instrument or thematic section
和声：strings / woodwinds / brass
节奏：orchestral percussion / ostinato / no pulse
亮点：motif handoff、counterpoint、orchestral swell
```

乐器组：

- Strings：violin、viola、cello、double bass
- Woodwinds：flute、oboe、clarinet、bassoon
- Brass：horn、trumpet、trombone、tuba
- Percussion：timpani、snare、bass drum、cymbals、mallets
- Color：harp、piano、celesta、choir

小编制使用 chamber ensemble；不要为“宏大”自动全开所有组。

### 2.15 Cinematic / Game / Trailer

```text
主体：leitmotif on piano, strings, brass or ethnic soloist
和声：orchestra / choir / hybrid synth
节奏：timpani / hybrid percussion / pulse
亮点：riser、impact、climax silence、motif reprise
```

- 亲密剧情：piano、solo strings、soft texture
- 悬疑：low strings、prepared piano、subtle pulse
- 动作：brass ostinato、strings、hybrid percussion
- 奇幻：orchestra、choir、harp、one regional soloist
- 游戏循环：结尾需可无缝回到开头

### 2.16 Ambient / Experimental

```text
主体：drone / motif fragment / found sound
和声：pads / granular clouds / spectral texture
节奏：free-time events / soft pulse / glitch
亮点：spatial movement、filter evolution、texture mutation
```

可用：

- field recordings
- granular synthesis
- tape loops
- prepared piano
- bowed metal
- modular synth
- electroacoustic textures

重点是随时间演变，不是静态铺底。

### 2.17 World / Regional

选择具体地域，不使用笼统 `tribal`：

| 地域 | 可选代表音色 |
|------|--------------|
| West African | kora、balafon、djembe、talking drum |
| Middle Eastern | oud、qanun、ney、darbuka |
| Indian | sitar、sarod、bansuri、tabla、tanpura |
| Celtic | fiddle、uilleann pipes、harp、bodhrán |
| Nordic | hardanger fiddle、tagelharpa、frame drum |
| Japanese traditional | koto、shakuhachi、shamisen、taiko |
| Korean traditional | gayageum、daegeum、janggu |
| Southeast Asian | gamelan、kulintang、khim、regional flutes |

不确定文化细节时，减少数量并说明按给定特征推导。

### 2.18 Guofeng

| 子风格 | 核心配器 |
|--------|----------|
| 古风流行 | dizi/erhu、guzheng、piano、strings、light rhythm section |
| 江南 | dizi、guzheng、erhu/yangqin、light percussion、rain/water |
| 仙侠 | xiao、guzheng、harp/strings、soft percussion |
| 敦煌 | pipa、dombra/rawap、hand drums、strings |
| 戏腔 | jinghu、yueqin、bangu、strings |
| 侠客 | dizi、pipa、guqin、drums、bass |
| 家国 | bianzhong、suona/dizi、orchestra、large drums |
| 禅意 | guqin、xiao、muyu/bells、flowing water |
| 国风电子 | pipa/dizi motif、synth、electronic drums、808 |
| 国潮 | sampled Chinese instrument、drum machine、bass、modern synth |

仅在国风分支使用 `traditional Chinese instruments, authentic timbre`；五声音阶按子风格需要启用，不是所有中国音乐的唯一音阶。

## 3. 乐器与音色词库

### 吉他

- acoustic guitar、fingerpicked acoustic guitar
- clean electric guitar、jangly guitar
- overdriven guitar、distorted rhythm guitar
- down-tuned guitar、extended-range guitar
- pedal steel、lap steel
- nylon-string guitar

### 键盘与合成器

- acoustic piano、felt piano、upright piano
- Rhodes electric piano、Wurlitzer、Hammond organ、clavinet
- analog synth、FM synth、modular synth
- synth pad、pluck、supersaw、arpeggiator

### 低频

- electric bass、upright bass、fretless bass
- synth bass、sub-bass、808 bass、reese bass

### 鼓与打击

- acoustic drum kit、roomy drums、tight drums、brushed drums
- electronic drums、drum machine、breakbeats
- double kick、half-time drums、four-on-the-floor
- congas、bongos、timbales、clave、shaker、tambourine
- cajon、frame drum、taiko、timpani

### 人声组

- backing vocals、layered harmonies、gang vocals
- gospel choir、chamber choir、wordless choir
- vocal chops、vocal texture、spoken samples

## 4. 环境声与声音设计

### 自然

- rain、wind、flowing water、ocean waves、thunder、birdsong、forest ambience

### 城市与人文

- city ambience、train station、cafe room tone、crowd murmur、vinyl crackle、tape hiss

### 影视/实验

- field recording、foley texture、reverse swell、impact、riser、sub drop、granular wash

使用原则：

- Intro、Bridge、Breakdown、Outro 最适合环境声。
- 环境声服务具体场景，不全程铺满。
- 用户要求“仅环境音及音效”时，不得加入 BGM 或隐性音乐铺底。

## 5. 混音与避坑

### 频段分工

- 高：cymbals、flute、bright synth、upper strings
- 中：vocal、guitar、piano、sax、民族弹拨
- 低：bass、cello、kick、sub、low brass

### 真实性词

- acoustic：natural resonance、live-room sound、finger noise
- electronic：precise transients、controlled sub-bass、wide stereo image
- vintage：tape warmth、analog saturation、limited bandwidth
- rock：live band energy、room mics、amp character
- orchestral：natural hall、dynamic range、realistic orchestration

### 反模式

- 同音区堆叠过多
- 只列乐器，不写段落职责
- 所有风格都加入 piano + strings
- 所有电子音乐都使用 808
- Reggae 忽略 bass，Jazz 忽略 comping，Metal 忽略 riff
- 管弦作品把每件乐器逐一塞进 Prompt
- 地域乐器跨文化无逻辑混搭
