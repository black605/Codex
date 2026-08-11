# Anti-Slop Rules（反 AI 平庸规则）

> **权威来源**：Anthropic 官方《[Prompting for Frontend Aesthetics](https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics)》Cookbook，配合泄露的 Claude Design system prompt（`CL4R1T4S/ANTHROPIC/Claude-Design-Sys-Prompt.txt`）。

---

## 🚫 什么是 "AI slop"

用户给"让人一眼看出是 AI 生成的平庸设计"起的名字。

**Anthropic 官方诊断**：模型会默认收敛到"on distribution"的选择——这些选择不是错的，但**千人一面**，导致所有 AI 生成的 UI 长得像同一个人设计的。

---

## 🔴 禁用清单（NEVER use）

> **来源合并**：Anthropic 官方 `DISTILLED_AESTHETICS_PROMPT` + ConardLi `web-design-skill` 基于实测 AI 输出总结的扩展清单。

### 1. 被用烂的字体（硬规则）
- **Inter** ⚠️（Anthropic 官方点名批评）
- **Roboto**
- **Arial**
- **Space Grotesk** — Anthropic 原话"You still tend to converge on Space Grotesk"
- **Fraunces** — ConardLi 实测：AI 生成内容过度使用
- **system-ui** — 默认系统字体调用，完全无品牌识别度

这 6 个是**业界双重认证**的 AI slop 字体触发器，出现在任何 prompt 里都要立即警觉。

### 2. 陈词滥调的色彩方案
- **紫-粉渐变 + 白色/暗色背景**（最典型的 AI slop）
- **紫-粉-蓝三色渐变**（ConardLi 补充，"obviously AI" 指标）
- `#3B82F6` 无脑主色
- "Tech blue" `#3B82F6` 到 `#6366F1` 的无脑渐变
- 均匀分布的 timid palette（四五个同饱和度柔和色）
- **Fraunces + 紫粉渐变** 组合（ConardLi 点名"peak AI aesthetic"）

### 3. 可预测的布局
- 三列 feature grid + 对称 CTA
- Hero → Features → Testimonials → CTA 的套路
- 卡片 4-up grid with identical sizes
- "上导航 + 左侧栏 + 主内容"的 SaaS 模板味

### 4. 套路化组件（ConardLi 补充）
- **Rounded cards with colored left-border accent**（⭐ 最典型的"我是 AI"标志）
- Rounded-12px cards with subtle shadow 泛滥
- **Cookie-cutter gradient buttons + large-radius card combos**
- Linear 抄袭版（不是真的 Linear aesthetic，是 AI 以为的 Linear）
- Stripe 抄袭版（purple-pink 渐变自嗨）

### 5. Emoji 滥用（ConardLi 独立章节）

**默认规则：NO emoji by default**。只有当品牌本身用 emoji（Notion / 早期 Linear / 某些 C 端品牌）才可以用，且必须匹配品牌的**密度和场景**。

| 用法 | 判定 |
|---|---|
| 用 emoji 代替图标：`🚀 ⚡ ✨` 填充 | ❌ 典型 AI slop |
| 用 emoji 当"活泼装饰"：`"标题前加个 emoji 让它活泼点"` | ❌ 典型 AI slop |
| 缺图标时用 placeholder 标记"需要真图标" | ✅ 专业做法 |
| 品牌本身用 emoji，复现品牌风格 | ✅ 忠于品牌 |

### 6. 假内容（ConardLi 独立章节）
- **Fake stats / 编造的数字**（"10x growth" / "98% satisfaction"）
- **Fake logo walls**（trust bar 里编造的客户 logo）
- **Fake testimonials**（编造的用户证言 + 假头像 + 假职位）
- **Meaningless icon spam** — "data slop"，一堆图标没有信息量
- **SVG 自绘复杂图形**（模型画不好的东西硬画，出来像手抖简笔画）

**替代方案**：用 placeholder 明确标记"这里需要真数据/logo/证言"，见 `placeholder-philosophy.md`。

---

## ✅ 推荐清单（DO use）

### 1. Typography：有识别度的字体
**image-2 prompt 片段**：
```
Typography: distinctive serif display font with editorial character 
(think Tiempos Headline / Canela / GT Sectra feel, not Playfair).
Body: a characterful grotesque (think Söhne / GT America, not Helvetica).
Code: JetBrains Mono with ligatures.
```

或者：
```
Typography: a wide brutalist sans (like PP Mori / PP Neue Machina feel), 
all-caps headlines, heavy weight, tight tracking.
```

### 2. Color：主色 + 锐利口音
**原则**（官方原话）：
> "Dominant colors with sharp accents outperform timid, evenly-distributed palettes."

**image-2 prompt 片段**：
```
Color: dominant warm terracotta #C96442 as the hero color, 
paired with deep cream #F4F3EE background and one sharp electric 
accent #5E6AD2 used sparingly on interactive elements only.
```

**灵感来源**（官方建议）：
- IDE themes（Dracula, Nord, One Dark, Tokyo Night, GitHub Dark）
- Cultural aesthetics（Swiss, Japanese, Memphis, Brutalism）
- Film color grading（Wong Kar-wai, Spielberg, Coen Brothers）
- **不要**从 Tailwind 默认色板自嗨

### 3. Motion：单一高影响时刻
**原则**：
> "One well-orchestrated page load with staggered reveals creates more delight than scattered micro-interactions."

image-2 本身不能生成动图，但**描述静态时可以暗示动态感**：
```
The hero copy appears as if mid-stagger-in animation: 
the headline is fully settled, the sub-headline halfway faded in, 
suggesting a sophisticated sequence reveal.
```

### 4. Backgrounds：大气层 + 深度
**原则**：
> "Create atmosphere and depth rather than defaulting to solid colors."

**image-2 prompt 片段**（按家族选一个）：
```
Background: a CSS radial gradient mesh (deep navy #0A0E27 to 
midnight purple #1A1030 to abyss black #000), suggesting 
cosmic atmosphere.
```

或：
```
Background: off-white #FAF8F2 with faint Risograph-style grain 
and a single diagonal terracotta accent bar cutting across 30% 
of the canvas.
```

或：
```
Background: tight 16px dot grid in 4% opacity on pure black, 
with one blurred orange orb (#D97757, 40% opacity, 400px radius) 
floating top-right.
```

---

## 🧠 三大策略（Anthropic 官方蓝图）

### 策略 1：分维度 · 独立驱动
**不要**写一句 `"make it beautiful"`。
**要**分别驱动 4 个维度：

```
Typography: {{具体字体 + 调性}}
Color: {{一个主色 + 一个 sharp accent + background}}
Motion: {{暗示动态 / 或直接说 static editorial}}
Background: {{纹理 / 渐变 / 几何 / 氛围}}
```

### 策略 2：引用设计灵感（不要太直接）
❌ `"copy Linear's design"`（容易做成粗糙抄袭）
✅ `"editorial minimalism in the spirit of Linear + Mintlify: calm neutrals, one strong accent, generous line-height"`

### 策略 3：显式叫板默认（Call out common defaults）
直接告诉模型"不要默认往那里走"：
```
Avoid AI-slop defaults: 
- No Inter, no Roboto, no generic system fonts.
- No purple-to-pink gradients.
- No 3-column feature grid hero.
- No rounded-12px card sameness.
```

---

## 🎯 image-2 专用：把美学规则翻译成视觉描述

image-2 不像 Claude Code 可以选字体 import。但**可以通过"描述字形特征"暗示模型往哪种字体方向画**：

### 字体暗示法（告诉模型"像什么字体"）

| 想要 | image-2 prompt 写法 |
|---|---|
| Tiempos Headline 感 | `elegant humanist serif with sharp terminals and slight contrast, editorial feel` |
| Canela 感 | `flared-stem serif with condensed proportions, high-end fashion magazine feel` |
| GT America 感 | `clean grotesque with wide proportions and mechanical quality` |
| Söhne 感 | `refined neo-grotesque, neutral but sophisticated, tight tracking` |
| PP Neue Machina | `condensed geometric sans with angular terminals, techno-brutalist feel` |
| Recoleta 感 | `rounded display serif, friendly and contemporary, high x-height` |
| JetBrains Mono | `monospace font with rounded corners and coding ligatures` |
| Clash Display 感 | `wide geometric sans with exaggerated proportions, display-heavy` |

### 色彩暗示法

不要直接说 "purple gradient"。说：
```
Color palette: deep oxblood #5A1A1A, aged cream #EFE9DB, 
and a single sharp chartreuse accent #D4FF00 — reads like 
a vintage typography journal.
```

或：
```
Color palette: photographic dawn colors — soft rose #F4C3B5, 
steel blue #4C6A8C, warm bone #F5EBD8. 
NO generic tech blue, NO purple gradients.
```

---

## 📋 Slop 自检 checklist（每次生图前过一遍）

跑图前，把 prompt 对着这个 checklist 过一遍：

- [ ] 字体有**具体性格描述**，不只是 "clean sans serif"？
- [ ] 字体**不是** Inter / Roboto / Arial / Space Grotesk？
- [ ] 色彩有**主色 + sharp accent**，不是 timid 均分？
- [ ] 色彩**不是**紫-粉渐变？
- [ ] 背景有**纹理或层次**，不只是 pure white？
- [ ] 布局**不是**陈词滥调的 hero-features-testimonials-CTA？
- [ ] Prompt 里有明确的 **"Avoid"** 列表？
- [ ] 有引用具体的设计语言家族（见 `aesthetic-families.md`）？
- [ ] 标题 copy 是**具体的句子**，不是 "Your Product Tagline"？

**如果有任何一项打钩失败，重写 prompt**。

---

## 🔥 终极 anti-slop 魔咒（可拷贝到任何 UI prompt 末尾）

**v2 升级版**（合并 Anthropic + ConardLi 双重军规）：

```
Anti-slop constraints (CRITICAL — follow strictly):

Typography:
- NO Inter, Roboto, Arial, Space Grotesk, Fraunces, or system-ui.
- Use a distinctive typographic character with visible personality.
- Maximum 2 font families.

Color:
- NO purple-to-pink gradients. NO purple-pink-blue three-color gradients.
- NO generic #3B82F6 tech blue dominance.
- Use dominant color + sharp accent (NOT timid evenly-distributed palettes).
- If possible, derive colors in oklch space for perceptual uniformity.

Layout:
- NO symmetric 3-column feature grids.
- NO rounded cards with colored left-border accent (the #1 AI tell).
- NO cookie-cutter gradient buttons + large-radius card combos.

Icons & Graphics:
- NO emoji as icon substitutes.
- NO self-drawn complex SVG attempts (use honest [icon] placeholders).
- NO meaningless icon spam / "data slop".

Content:
- NO Lorem ipsum. NO "Your Tagline Here" placeholders.
- NO fabricated customer logos, fake testimonials, or made-up stats.
- Use placeholder markers like [16:9 image] or [testimonial needed] 
  to signal real assets are required.

Background:
- Background must have atmosphere (texture / gradient mesh / pattern / 
  geometric layering), NOT solid color.

Overall:
- Every component should feel chosen for this specific product's story,
  not reusable AI template output.
- Aim for Dribbble / Behance showcase quality, not "functional mockup".
```

---

## 📖 延伸：Anthropic 官方原 prompt 全文（可直接使用）

来自 `DISTILLED_AESTHETICS_PROMPT`，可以放到任何 Claude 对话或生图 prompt 里：

```xml
<frontend_aesthetics>
You tend to converge toward generic, "on distribution" outputs. 
In frontend design, this creates what users call the "AI slop" 
aesthetic. Avoid this: make creative, distinctive frontends that 
surprise and delight.

Focus on:

Typography: Choose fonts that are beautiful, unique, and interesting. 
Avoid generic fonts like Arial and Inter; opt instead for distinctive 
choices that elevate the frontend's aesthetics.

Color & Theme: Commit to a cohesive aesthetic. Use CSS variables for 
consistency. Dominant colors with sharp accents outperform timid, 
evenly-distributed palettes. Draw from IDE themes and cultural 
aesthetics for inspiration.

Motion: Use animations for effects and micro-interactions. Prioritize 
CSS-only solutions for HTML. Use Motion library for React when 
available. Focus on high-impact moments: one well-orchestrated page 
load with staggered reveals (animation-delay) creates more delight 
than scattered micro-interactions.

Backgrounds: Create atmosphere and depth rather than defaulting to 
solid colors. Layer CSS gradients, use geometric patterns, or add 
contextual effects that match the overall aesthetic.

Avoid generic AI-generated aesthetics:
- Overused font families (Inter, Roboto, Arial, system fonts)
- Clichéd color schemes (particularly purple gradients on white backgrounds)
- Predictable layouts and component patterns
- Cookie-cutter design that lacks context-specific character

Interpret creatively and make unexpected choices that feel genuinely 
designed for the context. Vary between light and dark themes, different 
fonts, different aesthetics. You still tend to converge on common 
choices (Space Grotesk, for example) across generations. Avoid this: 
it is critical that you think outside the box!
</frontend_aesthetics>
```
