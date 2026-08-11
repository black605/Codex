---
name: Placeholder Philosophy（占位符哲学）
source:
  - Claude Design 泄露 system prompt
  - ConardLi/web-design-skill （Anti-slop 实战库）
---

# Placeholder Philosophy · 占位符哲学

> **核心论断**（ConardLi 原话）：
> **A placeholder signals "real material needed here."**
> **A fake signals "I cut corners."**
>
> **占位符 = 诚实标记需要真东西**
> **编造 = 糊弄了事**

---

## 🎯 为什么这对 image-2 生图特别重要

image-2 被训练在巨量"伪造"数据上（假 logo、假数字、假证言），默认会**自动补全**所有缺失元素：
- 你没说 "trust bar"，它给你画 6 个虚假科技公司 logo
- 你没给具体数字，它给你填 "10,000+ users" / "4.9 stars"
- 你没说 testimonial，它给你编 "This product changed my life! — Sarah K."

**这些虚假内容 = 生成即污染**，投产时 100% 要被替换，还会让生成图**一眼假**。

**解决方案**：在 prompt 里**显式规定 placeholder 语法**，告诉模型"这里画占位符，别自由发挥"。

---

## 📐 6 种场景的 placeholder 规范

### 场景 1：缺图标

| 场景 | prompt 写法 | 视觉效果 |
|---|---|---|
| 菜单项图标 | `icon: small square outline with letter label inside (e.g., "[D]" for dashboard)` | 方框+字母，一眼看出是占位 |
| 装饰性图标 | `icon placeholder: 24×24 rounded square in neutral gray, center-aligned` | 灰色小方块 |
| 小图标 (功能) | `icon: ▢ symbol or simple geometric placeholder (circle/triangle)` | 几何符号 |

**❌ 反模式**：让 image-2 画具体图标（"draw a settings gear icon"）— 出来的图标永远歪七扭八。
**✅ 正模式**：画占位符，告诉真实开发阶段替换成 Lucide / Heroicons。

### 场景 2：缺头像

| 场景 | prompt 写法 |
|---|---|
| 用户列表头像 | `avatars: letter-initial circles with color fill (e.g., "JD" on teal circle, "MK" on coral circle, "RL" on slate circle). NOT fake faces, NOT stock photos.` |
| 团队展示 | `team photos: circular placeholder frames with uppercase initials on solid brand-color backgrounds` |

**💡 提示**：不要让 image-2 生成"AI 生成的人脸"放头像里—— 永远有深度恐怖谷。

### 场景 3：缺图片

| 场景 | prompt 写法 |
|---|---|
| Hero 大图 | `hero visual: placeholder rectangle labeled "[16:9 hero image]" with subtle dashed border, NOT a fake product photo` |
| 产品图 | `product shot: neutral gray card with "[Product Image · 4:3]" label in center` |
| 博客缩略图 | `post thumbnail: [thumbnail · 3:2] placeholder with aspect ratio noted` |

### 场景 4：缺数据（最难，但最重要）

**⚠️ 最大陷阱**：让 image-2 编图表数据，它会编得"像真的"但完全不合理（曲线波动完美、增长率恰好一致）。

| 场景 | prompt 写法 |
|---|---|
| KPI 数字 | `KPI values: use clearly illustrative numbers like "XX,XXX" or "[metric value]", NOT fabricated realistic-looking stats` |
| 图表 | `line chart: show a plausible monotonic upward curve with NO specific Y-axis values labeled, OR use illustrative labels like "$—,—" instead of real dollar amounts` |
| 表格 | `data table: rows labeled "Item 1 / Item 2 / Item 3", NO fabricated company names or metrics` |
| 百分比 | `avoid specific percentages unless provided by the user` |

**真正该做的**：prompt 里明确说 `"All numbers are illustrative only"` 或 `"Watermark 'Demo data' at 10% opacity in corner"`。

### 场景 5：缺 logo / 客户墙（"trust bar"）

**这是最严重的 AI slop 陷阱之一**。模型默认会编"trusted by" 6 个公司 logo—— 全是 fake brand。

| 场景 | prompt 写法 |
|---|---|
| Trust bar | `trust bar: 5-6 monochrome abstract geometric marks (circle / square / triangle / hexagon / cross), NOT fabricated company logos. Small caption "Trusted by [placeholder clients]".` |
| 品牌露出 | `brand mark: use the text "[BRAND NAME]" in block letters, paired with a simple geometric abstract shape` |
| Partner 墙 | `partner row: 6 identical grey squares with "[Logo]" text inside, spaced evenly. Do NOT invent company names.` |

### 场景 6：缺用户证言

| 场景 | prompt 写法 |
|---|---|
| Testimonial 卡 | `testimonial cards: each card has "[testimonial quote needed]" in italic, attribution as "[Name, Role, Company]" placeholder format` |
| Review 星级 | `ratings: show "[★★★★★]" as placeholder, do NOT fabricate specific review numbers` |

---

## 🏛 Placeholder 的 6 个语法公约（在 prompt 里声明）

把这段直接粘到你的 UI prompt 的 Constraints 段：

```
Placeholder conventions (CRITICAL):
1. Missing icons → render as [icon] labeled rectangles or simple 
   geometric marks (circle/square), NEVER attempt to draw detailed icons.
2. Missing avatars → use letter-initial circles on solid color 
   backgrounds, NEVER generate AI faces or use stock photos.
3. Missing images → render placeholder rectangles with aspect-ratio 
   labels (e.g., "[16:9 image]"), NEVER fabricate product photos.
4. Missing data → use illustrative values like "XX,XXX" or "[metric]", 
   NEVER fabricate realistic-looking numbers.
5. Missing logos → use monochrome geometric shapes (abstract marks), 
   NEVER invent or copy real company logos.
6. Missing testimonials → use "[quote needed]" placeholders in italic, 
   NEVER generate fake user reviews with fake names.
```

---

## ⚖️ 占位符的"礼貌"程度梯度

越**明显**的占位符越专业——让观众一眼看出"这里需要真素材"。

### 优秀占位符特征
- **视觉上明显**：不会被误认为是最终内容
- **带标签**：文字说明"这里缺什么"（`[16:9 image]`、`[testimonial needed]`）
- **中性色**：灰阶/低饱和，不抢主体视觉
- **尺寸正确**：占据未来真素材该有的位置

### 糟糕占位符特征（= fake）
- 看起来像真东西（AI 生成的假图标、假 logo）
- 没标签（无法区分是最终素材还是占位）
- 用鲜艳颜色（"看起来完整"但全是假的）
- 尺寸随意（占位不准，后期替换时布局崩）

---

## 📝 Placeholder vs Fake 对照表（image-2 场景）

| 需求 | ❌ Fake（生图错误做法） | ✅ Placeholder（正确做法） |
|---|---|---|
| 客户 logo 墙 | 生成 6 个虚假科技公司 logo | 6 个灰色几何形状 + 标注"[Logo placeholders]" |
| 用户头像 | AI 生成的"真实人脸" | 带字母首字母的彩色圆圈 |
| 博客缩略图 | AI 生成的"相关图片" | 灰色矩形 + "[3:2 thumbnail]" 标签 |
| 仪表盘数字 | 编造的 "$48,291 MRR" | `"[$XX,XXX MRR]"` 或明确标注"illustrative" |
| 证言卡 | 编造的 "Sarah K., CMO at Acme" | `"[Testimonial]"` + `"[Name, Role]"` |
| 工程图表数据 | 完美渐上涨曲线 + 具体数字 | 一般形状曲线 + Y轴无具体数字标签 |

---

## 💡 为什么这条哲学对**生图**比对**代码**更关键

代码场景里，placeholder 是"我没写完"的信号，用户可以后续补完。

**生图场景里，placeholder 是防止模型"自作主张编内容"的唯一手段**。一旦图里有编造的数据/logo/证言，整张图基本废了——后期 Photoshop 覆盖的成本比重画还高。

**策略**：
1. 知道哪些东西你**确定会给真材料** → 在 prompt 里写具体内容
2. 知道哪些东西你**确定不会给** → 明确说 "render as placeholder"
3. 每次生图前，把 `placeholder-philosophy.md` 的 6 条公约粘到 prompt 末尾

---

## 🎁 可拷贝的 Pre-prompt 声明（放在 Important details 开头）

```
Content policy for this UI mockup:
- Real content provided: [headline / product name / specific copy you'll give]
- Everything else must use PLACEHOLDERS following these rules:
  · Icons → [icon] labeled rectangles or simple geometric marks
  · Avatars → letter-initial circles, no AI-generated faces
  · Images → placeholder rectangles with aspect-ratio labels
  · Data/Numbers → illustrative values like "XX,XXX"
  · Logos → monochrome geometric abstracts, no fabricated brands
  · Testimonials → "[quote needed]" in italic
- This is a DESIGN MOCKUP, not a finished product — placeholders are 
  EXPECTED and SIGNAL professionalism.
```
