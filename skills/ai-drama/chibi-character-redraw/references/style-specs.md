# Q 版轻写实风格规范（style-specs）

本文件定义 Q 版比例、轻写实风格、动作、光影色彩、画面基础、渲染质量与 Negative Prompt。一致性规则见 [identity-lock.md](identity-lock.md)。

## Q 版比例规范

标准 **3 头身比例**（super deformed chibi）：

- 头部约占整体高度 1/2
- 身体小巧精致
- 四肢略短
- 结构合理
- 保留真实骨架逻辑
- 保留角色体态特征

**禁止**：极端低幼化、过胖 Q 版、超夸张搞笑比例。

**整体接近**：高端收藏级 Q 版手办。

## 风格要求

**Q 版 + 轻写实融合**（non-flat chibi）。

视觉方向：

- 半写实 CG
- 高质量角色手办
- Stylized realism
- Anime realism hybrid

**必须保留**：体积感、材质感、柔和真实光影、高级角色渲染质感。

**禁止**：扁平卡通、廉价手游 Q 版、低幼儿童画风、泡泡头风格。

## 动作规则

自然站姿或轻微动态。

**要求**：动作符合角色气质。

**禁止**：搞怪动作、夸张卖萌、表情包式动作、低幼 Pose。

## 光影规则

**柔和光照**（soft lighting）：

- 柔和体积阴影
- 轻微环境光
- 无硬阴影
- 无高反差电影光

整体干净通透。

## 色彩规则

**必须保留原角色配色体系**：

- 色彩干净
- 明亮通透
- 不脏色
- 不过饱和

**禁止**：改变整体色彩风格。

## 画面基础

- **9:16 竖版**
- 单人
- 全身清晰展示
- 人物居中
- **纯白背景（#FFFFFF）**
- 无渐变
- 无场景
- 无背景元素
- 无地面阴影
- 无文字
- 无 UI
- 无水印

## 渲染质量关键词

```
semi-realistic chibi,
high-end collectible figurine,
premium CG character,
stylized realism,
3D anime realism,
ultra detailed,
soft shading,
subsurface scattering,
physically based rendering,
octane render quality,
UE5 cinematic character quality,
clean rendering,
high detail fabric,
high detail hair,
high detail face,
premium lighting,
delicate materials.
```

## Negative Prompt

```
low quality,
flat cartoon,
cheap chibi,
overcute,
baby face,
round face redesign,
big mouth,
super deformed comedy style,
pixelated,
blurry,
bad anatomy,
extra fingers,
bad hands,
plastic hair,
oversaturated,
text,
watermark,
logo,
UI,
background scene,
gradient background,
cropped body,
low detail,
2D doodle,
western cartoon,
funny expression,
exaggerated expression,
childish style
```

## 最终目标

在严格保留原角色**脸型 / 嘴型 / 五官结构 / 气质 / 发型 / 服装 / 花纹 / 纹理 / 角色识别度**的前提下，生成：

> **白底纯净 + 3 头身 Q 版 + 半写实 CG + 收藏级手办质感** 的高质量角色形象。
