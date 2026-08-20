# reference.md（风格与评测资产）

本文件用于"水豚噜噜"风格的一致性控制、负面约束、镜头模板与模型选优评分。它应尽量稳定；只在你确认风格资产变更时更新。

## 1) 角色锚点（Character Anchors）
用于锁定"水豚噜噜"的形象一致性。下列段落建议 **每次 T2I 都强制包含**（中英二选一或同时）。

### 1.1 角色锚点（中文）
- 水豚噜噜（capybara mascot），单角色为主，Q 版卡通比例，圆润体型、短四肢、表情夸张但可爱。
- 眼睛为简化黑点/小椭圆，鼻口极简，不出现写实牙齿细节。
- **【面部干净度-关键约束】面部必须绝对干净光滑**：不允许任何凸起的圆点、斑点、痘痘、雀斑、疣、黑头、胡须点、脸部装饰物、皮肤纹理。面部只保留眼睛、鼻子、嘴巴三个五官元素，其余区域必须是纯净光滑的色块。
- 质感为"卡通表情包形象"，可按风格选择 **插画贴纸** 或 **3D 公仔**；边缘干净，面部与身体结构稳定，不要多余肢体。
- **皮肤质感统一**：整体为光滑的软胶/公仔质感，不允许任何凹凸纹理、颗粒、毛孔、毛发细节、表面凸起物。

### 1.2 Character anchor (English)
- Lulu the capybara mascot, single character, chibi cartoon proportions, round body, short limbs, cute exaggerated meme facial expressions.
- Simple dot/oval eyes, minimal nose and mouth, no realistic teeth details.
- **[FACIAL CLEANLINESS - CRITICAL] Face must be absolutely clean and smooth**: NO raised dots, NO spots, NO freckles, NO warts, NO blackheads, NO whisker dots, NO facial decorations, NO skin texture bumps. Face contains ONLY eyes, nose, and mouth - all other areas must be pure smooth color blocks.
- Meme mascot look; can be sticker illustration or 3D toy depending on style anchors; clean edges, stable anatomy, no extra limbs.
- **Uniform skin texture**: Entire body should have smooth soft-vinyl/toy-like texture; NO bumpy textures, NO grains, NO pores, NO fur details, NO surface protrusions.

### 1.3 样例风格 v1 角色锚点（3D 公仔渲染专用）
当你想强制贴近你提供的那张图时，把这一段强制加进 prompt（中英均可）：
- 3D 软萌公仔风，圆润大头与身体，短粗手臂，皮肤像软胶/公仔材质，**无描边**，表面细节极少
- 暖黄色主体，口鼻/脸颊区域有橙色渐变；五官极简（弯弯眼/点状眼、简化嘴形），笑容夸张可爱
- **面部无任何多余元素**：不允许脸上有任何凸起圆点、斑点、胡须点或装饰物
- （可选）头顶一个小橘子/小果实帽作为标志性元素

## 2) 风格锚点（Style Anchors）
目标：尽可能接近"网上流行的水豚噜噜表情包"观感（干净、卡通、可读、适合动起来）。

### 2.1 推荐风格锚点（通用）
（优先从中选 3-6 个放入 `t2i.style_anchors`）
- 干净背景，主体突出（clean background, subject centered）
- 贴纸感、表情包插画（sticker-like, meme illustration）
- 柔和色块与轻阴影（soft color blocks, gentle shading）
- 线条简洁、轮廓清晰（simple lines, crisp outline）
- 低细节但高可读（low detail, high readability）
- 轻微颗粒/纸感（subtle grain / paper texture, optional）

### 2.2 场景风格调味（按场景选）
- 打工/办公室：冷白光、简洁工位、键盘/工牌/咖啡杯点缀
- 雨天：窗外雨滴、伞、路灯反光（但背景保持简化）
- 过年：红色点缀、灯笼/春联（避免出现大段可读文字）

### 2.3 样例风格 v1（来自你提供的图：暖黄 3D 软萌玩具渲染）
这一版更偏"3D 玩具/公仔渲染"的噜噜观感：**无描边、柔和渐变阴影、微微发光的暖黄皮肤、干净背景**。

**视觉关键词（建议加入 prompt）**
- 3D cute mascot / toy-like character, soft studio lighting
- smooth gradient shading, rounded shapes, clean edges, no lineart / no outline
- subtle bloom / glow, gentle rim light
- low texture detail (almost plastic / soft vinyl), no pores, no fur detail
- **clean smooth face with no spots or raised dots**

**样例背景元素（仅当场景允许时使用）**
- deep blue dreamy night sky, bokeh stars
- hanging star-shaped lights, occasional shooting stars

**样例子风格：高亮白天泳池（来自你提供的泳池图）**
- high-key daylight, clear blue sky, clean summer vibe
- stylized 3D environment, but character remains toy-like and smooth
- pool water + small splashes (keep clean, avoid overly realistic gritty water)
- props: orange-and-white lifebuoy swim ring, beach umbrella, pool tiles

**样例子风格：室内暖光躺平（来自你提供的粉色软垫图）**
- warm cozy indoor lighting, soft ambient bounce light, golden room tone
- minimal clean interior, soft box / strip light feel (warm ceiling light band)
- character remains toy-like and smooth; keep fabric details simple and clean
- props: big pink cushion / pillow, simple floor, clean corner background

**样例子风格：图书馆/书架挑书（来自你提供的书架图）**
- warm afternoon sunlight through windows, cozy library ambience
- wooden bookshelves, shallow depth of field (background softly blurred)
- keep book spines stylized/simplified (avoid readable text); warm wood floor
- optional soft "micro-fuzz / velvet-like" surface on character (VERY subtle; not realistic fur strands)

**样例子风格：派对庆祝/彩纸雨（来自你提供的彩灯派对图）**
- colorful party stage bokeh lights, festive ambience, shallow depth of field
- confetti falling, clean celebratory vibe (avoid dirty/gritty paper dust)
- props: rainbow party hat with pom-pom, curly ribbon streamers around the head
- character front-facing hero pose, hands on hips, proud smile
- allow simple whisker lines (few thin curved lines), but keep face minimal and clean

**样例配色（近似，可用作调色约束）**
- 夜空深蓝：#0B1733 ~ #132B5A
- 白天天空蓝：#8CC9FF ~ #BFE3FF
- 泳池水蓝：#2FA3E6 ~ #77D6F5
- 主体暖黄：#F6E0A2 ~ #F3D487
- 面部橙色渐变：#F3A14B ~ #E98B2A
- 短裤偏橘红：#D86F3F
- 五官黑：#141414；牙齿白：#FFFFFF
- 室内暖墙/环境光：#F2C06B ~ #F6D38A
- 软垫粉：#E8A2B4 ~ #F1B6C6
- 木质书架棕：#8A5A3B ~ #B07A4E
- 书本点缀色（可选）：#2D4C7A / #7A2D2D / #D7C3A2
- 派对霓虹散景（可选点缀）：#7B61FF / #2FD7FF / #FF4D8D / #FFD166 / #7CFF6B

**样例"标志性小道具"（可选）**
- 头顶小橘子/小果实帽（orange fruit hat）

## 3) 负面提示词（Negative Prompt）
建议始终包含（可按平台语言偏好中英混用）：
- 多余肢体、断肢、融合、扭曲、畸形、手脚异常、脸崩
- 写实人类、真实照片感、皮肤毛孔、真实牙齿、恐怖血腥
- 文字水印、logo、签名、二维码、乱码字
- 低清、噪点、马赛克、过度锐化、过曝、强压缩

### 3.1 面部干净度负面词（必须包含-防止脸上出现异常元素）
- **facial spots, raised dots on face, freckles, moles, warts, blackheads, acne, pimples**
- **whisker dots, beard stubble, facial hair dots, skin bumps, texture bumps**
- **facial decorations, face stickers, face paint dots, beauty marks**
- 脸上斑点、面部凸起圆点、雀斑、痣、疣、黑头、痘痘、胡须点、皮肤纹理凸起

### 3.2 样例风格 v1 额外负面词（用于避免跑到 2D/动漫/写实）
- 2d, anime, manga, cel shading, lineart, sketch, watercolor
- realistic fur, detailed hair strands, skin pores, photorealistic
- harsh shadows, dramatic noir lighting, heavy grain, dirty textures
- dirty pool, algae, murky water, gritty realism, harsh specular highlights
- highly detailed fabric weave, dirty bedding, messy wrinkles, realistic textile fibers
- readable text, sharp typography, book titles, watermark-like text
- realistic fur strands, detailed hair strands (allow only very subtle velvet-like fuzz if needed)
- messy confetti dust, dirty floor, gritty film dirt, heavy motion blur

## 4) I2V 稳定性提示（Motion Prompts）
### 4.1 正向（推荐）
- 形象稳定、角色不变（consistent character, identity locked）
- 动作幅度小、自然连贯（small natural motion, smooth movement）
- 镜头稳定（stable camera, minimal shake）
- 背景稳定、无大幅形变（stable background, no warping）

### 4.2 负向（抑制）
- 角色漂移、换脸、闪烁（identity drift, face swap, flicker）
- 抖动、果冻、扭曲（jitter, wobble, warping）
- 快速镜头运动、强摇镜（fast camera move, heavy shake）

## 5) 镜头模板（Shot Templates）
优先"可读 + 稳定 + 适合表情包"。

### 5.1 单镜头（默认）
- 固定机位或轻微推近
- 2-4 个微动作循环：眨眼 → 轻点头 → 叹气/笑 → 回到初始

### 5.2 双镜头（可选）
- 镜头1：铺垫（2s）主体反应
- 镜头2：包袱（2s）夸张表情/小动作（幅度仍要小）

## 6) 评分量表（Rubric）与阈值（Thresholds）
用于模型选优与自动回退。每项 0-5 分。

### 6.1 T2I 评分维度（建议权重）
- 风格一致性（0.25）
- **形象一致性/可控性（0.30）** ← 权重提升，确保角色形象正确
- 提示词贴合度（0.20）
- **面部干净度（0.15）** ← 新增：检查面部是否有异常元素
- 可动性（姿态不过度极端）（0.10）

**T2I 通过阈值**：加权总分 ≥ 4.0 且 "形象一致性" ≥ 4.0 且 **"面部干净度" ≥ 4.5**

### 6.2 I2V 评分维度（建议权重）
- 形象稳定（0.35）
- 动作自然（0.25）
- 抖动/扭曲控制（0.20）
- 语义贴合（0.10）
- 画质与压缩观感（0.10）

**I2V 通过阈值**：加权总分 ≥ 4.0 且 "形象稳定" ≥ 4.0

## 7) 模型注册表（Model Registry，供应商无关写法）
这里不写死"唯一最好模型"，而是写"候选池 + 适用场景 + 试跑策略"，由 `model_routing` 输出中做选择。

### 7.1 文本推理模型（Reasoning）
偏好：结构化 JSON 稳、提示词工程强、能做多轮自检。
- 候选：高推理能力通用大模型（例如：具备强规划/结构化输出能力的模型）

### 7.2 文生图（T2I）
偏好：卡通/插画风格稳定、对参考图一致性强、细节不过度写实。
- 候选：高质量通用 T2I / 插画风强 T2I / 支持参考图一致性控制的模型

### 7.3 图生视频（I2V）
偏好：身份不漂移、少闪烁、少扭曲；对"轻动作"更稳。
- 候选：稳定性优先的 I2V / 动作自然优先的 I2V（先短预览再全量）

## 8) 没有参考图时的"伪参考"策略（重要）
当用户仅给场景词，为了让形象稳定：
- 强制使用 `character_anchors` + `style_anchors`
- 背景保持极简（单色或轻场景元素）
- 动作更小，镜头更稳

## 9) 有参考图时的策略（重要）
当用户给 1 张主参考图：
- 锁定：角色外观与配色、表情范围
- 不锁定：背景（除非用户明确要"同款背景"）
- 若出现跑偏：降低背景复杂度 + 强化角色锚点 + 改用更强一致性控制的 T2I 候选

### 9.1 样例图"风格拆解清单"（用于生成 t2i.style_profile）
当存在参考图/样例图时，先用视觉分析提取下列要素，再回写到提示词里：
- 调色板：主色 3-6 个（用颜色名 + 近似 hex，如果可得）
- 线条：是否有描边、粗细、边缘是否圆润
- 阴影：是否有投影/描边阴影/色块阴影
- 质感：是否有颗粒/纸感/胶片感（尽量轻）
- 背景：是否纯色、是否常用简单道具（桌子/窗户/路灯等）
- 表情：常见表情范围（摆烂/震惊/偷笑/委屈等）
- 角色一致性锚点：眼鼻口的简化方式、体型比例、常用姿态
- **面部干净度检查**：确认参考图中角色面部是否干净光滑，无异常元素

### 9.2 针对"样例风格 v1"的 style_profile 建议填法
当你想强制贴近这张样例图时，`t2i.style_profile` 推荐：
- palette: ["#0B1733", "#132B5A", "#F6E0A2", "#F3A14B", "#D86F3F", "#141414", "#FFFFFF"]
- line_style: "no outline, clean edges, rounded silhouette"
- shading: "smooth gradient shading, soft light; either gentle studio bloom (night) or high-key daylight (pool); subtle subsurface feel; gentle rim light"
- background_style: "simple clean background; optional dreamy deep-blue starry sky with hanging star lights; or bright summer pool with clean water and minimal props; or warm cozy indoor corner with soft ceiling strip light and a big pink cushion"
- background_style: "simple clean background; optional dreamy deep-blue starry sky with hanging star lights; or bright summer pool with clean water and minimal props; or warm cozy indoor corner with soft ceiling strip light and a big pink cushion; or cozy library with wooden bookshelves and soft warm sunlight"
- expression_range: ["big smile", "crescent eyes", "open-mouth happy", "cute excited", "gentle happy", "mild surprise", "half-lidded sleepy", "smug grin", "curious focused", "proud grin"]
- **facial_cleanliness: "absolutely clean and smooth face, no spots, no raised dots, no freckles, no facial decorations"**

## 10) 图片质量检查清单（生图后必检）
生成图片后，在进行图生视频前，必须进行以下检查：

### 10.1 面部干净度检查（最高优先级）
- [ ] 面部是否只有眼睛、鼻子、嘴巴三个五官元素？
- [ ] 面部是否有任何凸起的圆点或斑点？
- [ ] 面部是否有雀斑、痣、疣、黑头、痘痘？
- [ ] 面部是否有胡须点或胡须纹理？
- [ ] 面部皮肤是否干净光滑，无凹凸纹理？

**如果任一项检查不通过，必须重新生成图片或使用更强的负面提示词。**

### 10.2 整体形象检查
- [ ] 角色比例是否正确（Q版圆润体型）？
- [ ] 肢体数量是否正确（无多余肢体）？
- [ ] 皮肤质感是否统一（软胶/公仔质感）？
- [ ] 整体风格是否与参考图一致？

## 11) 道具与场景元素库（v1 常用）
用于让"只有场景词"也更像同一套 IP 素材。

### 11.1 夏日/泳池
- 救生圈：橙白条纹 lifebuoy / swim ring（优先）
- 遮阳伞：白橙条纹 beach umbrella（背景虚化/简化）
- 泳池砖：蓝色瓷砖边缘（几何清晰，干净）
- 水花：少量飞溅（保持干净、少噪点、不过度写实）

### 11.2 室内/躺平
- 大粉色软垫/抱枕：big pink cushion / pillow（主道具）
- 顶部暖色灯带：warm ceiling strip light band（背景氛围）
- 干净角落墙面：minimal clean corner wall（避免杂物）

### 11.3 图书馆/学习
- 木质书架：wooden bookshelf（主背景）
- 书本：books (stylized spines, no readable titles)
- 木地板：warm wooden floor（干净）
- 绿植点缀：potted plant / greenery（背景虚化）
- 光线：warm afternoon sunlight / soft window light

### 11.4 派对/庆祝
- 彩纸：confetti（适量、干净）
- 彩灯散景：party bokeh lights / stage bokeh（背景）
- 派对帽：rainbow party hat with pom-pom（主道具）
- 彩带：curly ribbon streamers（头部周围点缀）

## 12) 眼睛与表情细节允许项（v1 统一性）
为了兼容你给的多张样例（闭眼弯弯 / 大眼有眼白 / 半眯眼摆烂），建议把"眼睛风格"写成允许集，而不是固定一种：
- 眼睛允许：crescent closed eyes（开心闭眼）、round eyes with sclera + pupil（大眼）、half-lidded sleepy eyes（半眯眼摆烂）
- 约束：不要写实虹膜纹理；眼白保持干净；瞳孔简单黑圆/椭圆即可


## 13) 你提供"水豚噜噜风格样例"后我会做什么（可选增强）
当你给我 3-5 张同风格样例图（或一套素材包），我会把本文件升级为"强风格版"：
- 从样例里提炼专属：配色、线条、阴影、表情范围、常用道具
- 生成更精准的 `style_anchors` 与 `character_anchors`（中英）
- 给出 6-10 条可复用场景模板（打工/恋爱/雨天/过年/社恐/摆烂等）
