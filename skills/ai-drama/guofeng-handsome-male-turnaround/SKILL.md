---
name: guofeng-handsome-male-turnaround
description: 古风帅气男主四视图角色设定提示词生成器，16:9 横版，GPT Image 2 专用。生成成年古风男性的超写实 3D 国漫 CG 角色设定板提示词，包含上半身特写、全身正视图、侧视图和背视图，并强调跨视图一致性。用户提到古风帅哥、古装男主、仙侠男主、男性角色设定、男角色四视图、国漫男主、游戏男角色或男性 AI 绘画 prompt 时，都应使用此技能。只输出可复制提示词，不直接生成图片。
---

# 古风帅气男主四视图生成器

## 角色职责

以顶级 3D 国漫角色美术总监和提示词工程师的视角设计成年古风男性。将东方男性审美、身份叙事与电影级 CG 材质结合，优先保证角色辨识度和四视图一致性。

## 工作流程

### 1. 提取参数

从用户输入中提取以下信息；未指定项标记为“随机”：

- 风格：仙侠、玄幻、江湖侠客、宫廷权贵、儒雅书生、敦煌异域、妖族、暗黑魔尊
- 身份：宗门首席、剑客、将军、王侯、谋士、书生、祭司、妖族领主、魔尊等
- 面部：脸型、眉眼、鼻唇、肤色、年龄感、胡须
- 体型：身高比例、肩背轮廓、肌肉程度
- 发型：发色、长度、束发方式、发冠或发带
- 服装：轮廓、主色、材质、纹样、护甲
- 挂饰：冠饰、腰封、玉佩、腰牌、香囊、流苏或身份信物
- 特殊要求：用户明确指定的其他细节

角色必须是成年男性。除非用户明确要求，否则设定为 20—35 岁，体态挺拔匀称，避免幼态、女性化、油腻感和夸张健美肌肉。

### 2. 读取参考库

按需读取以下文件，选择同一风格下彼此协调的元素：

- 风格、身份与配色：`references/style-library.md`
- 男性面部与体型：`references/facial-features.md`
- 发型、发色与冠饰：`references/hairstyles.md`
- 服装轮廓与材质：`references/costumes.md`
- 挂饰与身份信物：`references/accessories.md`

用户指定内容优先。随机生成时，先确定风格与身份，再选择兼容特征；主色不超过三种。四视图不得出现任何道具或武器，包括手持、背负、腰佩、悬挂或放置在画面中的物件。仅允许固定在服装或身体上的装饰性挂饰，如玉佩、腰牌、香囊、流苏和小型身份信物。

### 3. 生成角色名

生成 2—4 字古风男性姓名。名字应符合风格与身份，避免直接使用知名作品角色名。

### 4. 组装提示词

正面提示词使用六段结构：

1. 角色描述
2. 服装设计
3. 版式
4. 镜头设计
5. 材质表现
6. 画质要求

主体描述使用简体中文；PBR、UE5、SSS、HDR 等必要渲染术语保留英文。

## 输出格式

严格按以下顺序输出，不调用任何生图工具。

### 一、角色设定卡

用 Markdown 表格展示：

| 类别 | 内容 |
|---|---|
| 基本信息 | 角色名、成年年龄段、风格、身份 |
| 气质与配色 | 气质、主色、辅色 |
| 面部与体型 | 脸型、眉眼、鼻唇、肤色、体型 |
| 发型设计 | 发色、发型、冠饰、发质 |
| 服装设计 | 款式、层次、材质、纹样 |
| 挂饰 | 玉佩、腰牌、香囊、流苏、身份信物 |

### 二、GPT Image 2 正面提示词（可直接拷贝）

将完成的提示词放入一个代码块，并替换所有变量：

```text
超写实 3D 国漫 CG 角色设定板，成年古风男性角色四视图与特写展示。
一位{{风格}}男主，名为{{角色名}}，身份为{{身份}}，年龄约{{年龄段}}。
{{肤色}}，{{脸型}}，骨相立体利落，{{眉型}}，{{眼型}}，目光{{眼神}}，高挺鼻梁，{{唇型}}，下颌线清晰。
{{体型}}，肩背挺拔，腰身利落，身体比例自然；俊朗阳刚而不粗犷，不幼态，不女性化，不过度肌肉化。
{{发色}}{{发型}}，{{发型细节}}，发丝具有真实重量、毛流和高光；{{冠饰描述}}。
整体气质{{气质描述}}，高辨识度国漫男主面容，不对应任何现有影视、动漫或游戏角色。
---
服装设计：
{{服装款式}}，以{{主色}}为主色、{{辅色}}为辅色，整体颜色不超过三种。
{{服装层次}}，{{服装纹样}}，{{服装材质}}，剪裁符合成年男性肩背与腰线。
{{挂饰描述}}。
服装结构清晰，兼顾身份叙事与活动合理性，影视级细节，四视图中的纹样、扣件、腰封和配饰位置完全一致。
---
版式：
16:9 横版构图，纯白无缝背景，无地平线，无场景元素，无道具，无武器，无文字，无水印。
Character Turnaround Sheet，从左到右依次排列：上半身特写、全身正视图、全身侧视图、全身背视图。
四视图水平基线一致、人物比例一致、面容一致、体型一致、发型一致、服装结构一致、挂饰位置一致。
画面中不出现任何道具或武器，不手持、不背负、不腰佩武器，不放置扇、剑、刀、枪、法器、权杖或其他独立物件；仅保留固定于服装的装饰性挂饰。
100% character continuity，100% cross-view consistency，同一成年男性角色。
---
镜头设计：
左侧上半身特写：头部轻微侧转，85mm 人像镜头，焦点锁定双眼，五官完整清晰。
全身正视图：自然站姿，双臂自然下垂，与身体适度分离，完整展示服装正面和鞋履。
全身侧视图：标准 90 度侧面，保持头身比例和服装轮廓准确。
全身背视图：标准 180 度背面，完整展示发型、冠饰、披风及服装后背结构。
所有视图均完整显示，不裁切头顶、手、衣摆或双足。
---
材质表现：
PBR Physically Based Rendering，UE5 Render，Metahuman Quality，Subsurface Scattering，SSS 皮肤。
真实男性皮肤毛孔与微表面，适度皮肤纹理，真实眉毛、睫毛和头发着色器。
真实丝绸、棉麻、皮革、金属、玉石和护甲材质，准确反射与折射，真实布料垂坠和褶皱。
电影级三点布光，柔和主光、自然补光、清晰轮廓光，HDR Lighting，纯白背景保持干净。
---
画质要求：
8K Ultra HD，Ultra Detailed，Masterpiece，Best Quality，Hyper Realistic，Photorealistic，Cinematic。
Ultra Sharp Focus，High Clarity，Refined Edges，Controlled Details，Smooth Shading，Clean Rendering。
Luxury Character Design，AAA Game Character，Perfect Character Sheet，{{风格英文标签}}。
```

若无挂饰，删除对应句子，不保留空变量或生硬标点。

### 三、负面提示词（可直接拷贝）

```text
worst quality, low quality, normal quality, lowres, blurry, out of focus, noise, film grain, artifacts, jpeg artifacts, oversharpen, oversaturated, dirty texture, rough texture, plastic skin, waxy skin, excessive skin smoothing, bad anatomy, bad hands, extra fingers, missing fingers, fused fingers, duplicate limbs, extra arms, extra legs, mutated body, wrong proportions, asymmetrical face, cross eye, lazy eye, feminine face, female body, child, teenager, baby face, overly delicate feminine features, heavy makeup, exaggerated bodybuilder muscles, greasy face, old-looking face, multiple characters, cropped body, cut head, cut feet, cut hands, watermark, text, logo, signature, background objects, environment, props, handheld object, weapon, sword, blade, spear, fan, staff, magic artifact, floating accessories, inconsistent face, inconsistent body, inconsistent outfit, inconsistent hairstyle, inconsistent hanging ornaments, different character between views, different colors between views
```

## 质量检查

输出前逐项确认：

- 角色是成年男性，俊朗阳刚且符合用户指定气质。
- 风格、身份、面部、发型、服装和配饰相互协调。
- 主色不超过三种，画面中不存在任何道具或武器。
- 四个视图顺序正确，均未被裁切。
- 面容、体型、发型、服装、纹样和挂饰跨视图一致。
- 正面提示词包含完整六段，且不存在任何双花括号占位符残留。
- 输出只有角色设定卡、正面提示词和负面提示词，不直接生图。
