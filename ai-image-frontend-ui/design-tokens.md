# 设计 Token 参考库

给 prompt 用的"客观视觉事实"素材库。直接拷片段到 prompt 的 Details / Constraints 里。

---

## 🎨 配色方案（可拷贝 HEX）

### 中性灰阶（通用骨架）
```
#F9FAFB  (50)   - Lightest, page backgrounds
#F3F4F6  (100)  - Subtle backgrounds, hover states
#E5E7EB  (200)  - Borders, dividers
#D1D5DB  (300)  - Disabled text, placeholders
#9CA3AF  (400)  - Muted text, icons
#6B7280  (500)  - Secondary text
#4B5563  (600)  - Body text
#374151  (700)  - Headings secondary
#1F2937  (800)  - Headings primary
#111827  (900)  - Near-black, darkest
#0A0A0A  (1000) - True near-black for high contrast
```

### 主色调色板（按风格）

#### SaaS Blue（Linear / Vercel / Stripe 风）
```
Primary:   #3B82F6  (brand blue)
Hover:     #2563EB  
Light:     #EFF6FF  (tint for selected bg)
Dark:      #1E3A8A  (pressed state)
```

#### Emerald Green（Notion-like / finance-friendly）
```
Primary:   #10B981
Hover:     #059669
Light:     #ECFDF5
Dark:      #064E3B
```

#### Purple（Coin / crypto / creative）
```
Primary:   #8B5CF6
Hover:     #7C3AED
Light:     #F5F3FF
Dark:      #5B21B6
```

#### Warm Terracotta（editorial / premium）
```
Primary:   #D97757
Hover:     #BC5A3E
Light:     #FEF3EE
Dark:      #8A3D27
```

#### Pure Monochrome（Apple-like / luxury）
```
Primary:   #0A0A0A
Background: #FFFFFF
Subtle BG: #FAFAFA
Accent:    #3B82F6 或 transparent
```

### 语义色（Semantic）
```
Success:  #10B981  (green)
Warning:  #F59E0B  (amber)
Danger:   #EF4444  (red)
Info:     #3B82F6  (blue)
```

### 暗色主题调色板
```
Background:   #0D1117 (GitHub dark)  或  #1E1E2E (Dracula)  或  #282C34 (OneDark)
Surface:      #161B22
Border:       #30363D
Text primary: #C9D1D9
Text muted:   #8B949E
Accent blue:  #58A6FF
Accent green: #3FB950
Accent red:   #F85149
```

---

## 🔤 字体选择指南

> ⚠️ **重要更新**：Anthropic 官方明确指出 `Inter` / `Roboto` / `Arial` / `Space Grotesk` 是 **"AI slop"字体**，是模型默认会选但效果千人一面的陷阱。本节已重排，**distinctive 字体在前，fallback 字体在后**。详见 `anti-slop-rules.md`。

### 🚫 AI Slop 陷阱清单（避免作为首选）
| 字体 | 为什么要避免 | 来源 |
|---|---|---|
| **Inter** | Anthropic 官方点名，模型过度偏好 | Anthropic |
| **Roboto** | Material 默认，无品牌识别度 | Anthropic |
| **Arial** | 通用无特征 | Anthropic |
| **Space Grotesk** | Anthropic 原话"You still tend to converge on Space Grotesk" | Anthropic |
| **Fraunces** | AI 生成内容过度使用，**与紫粉渐变组合 = peak AI aesthetic** | ConardLi 实测 |
| **system-ui** | 默认系统字体调用，完全无识别度 | ConardLi 实测 |
| Helvetica / Helvetica Neue | 万金油，无个性 | 通用经验 |
| SF Pro（过度泛用时）| Apple 生态可以，其他场景会显得"默认" | 通用经验 |

**何时仍可用**：
- 快速 MVP 原型（功能优先，美学不是重点）
- 确实需要"系统默认"的场景（操作系统设置页、无品牌工具）
- 作为 fallback 字体栈的后备

---

### ✅ Display / Headlines（推荐 distinctive 选择）

**衬线方向**（Warm / Editorial / Premium）
```
Tiempos Headline       - 编辑杂志，humanist，略高对比 (Anthropic 风)
GT Sectra              - 杂志感，现代衬线
Canela                 - 时尚品牌衬线，高端感
PP Editorial New       - 当代编辑设计
Recoleta               - 圆润友好衬线
Miller                 - 传统报纸衬线，权威感
Caslon / Garamond      - 经典古典，A24/Criterion 风
```

**Grotesque 方向**（Modern / Tech / Confident）
```
GT America             - 美式现代 grotesque（Linear 风味）
Söhne                  - 瑞士精致 neo-grotesque（Stripe 风）
Söhne Breit            - Söhne 的宽版
PP Mori                - 当代简洁 geometric
Monument Grotesk       - display 版本，戏剧感
Druk                   - 超粗 condensed，brutalist 专用
PP Neue Machina        - 角分明 techno-brutalist
```

**Display / 特殊用途**
```
Eiko                   - cinematic display
Clash Display          - 超宽 geometric，声明感
Gambarino              - 活泼 display serif
Author                 - 文学 humanist
Roobert                - 工程技术气质（PostHog 风）
```

### ✅ Body（推荐 distinctive 选择）
```
Söhne Buch             - 高级中性
GT Planar              - 精准工程感
PP Neue Montreal       - 当代专业
Tiempos Text           - 衬线正文，阅读友好
PP Editorial Old       - 传统编辑
Reader                 - 学术阅读
Aktiv Grotesk          - 瑞士精确
Untitled Sans          - 实验性中性
```

### ✅ Mono（代码 / IDE / 终端）
```
Berkeley Mono          - 当代首选，character 强
JetBrains Mono         - 开源，ligatures，humanist warmth
IBM Plex Mono          - 工程专业
Commit Mono            - 新锐，圆角温和
MD IO                  - 实验性 mono
Monaspace              - GitHub 新作，5 个协作字族
```
避免：Courier New / Consolas / Menlo（全是默认）

### ✅ Rounded（friendly / consumer app）
```
Recoleta Rounded       - 衬线圆润
PP Mori Rounded        - geometric 圆润
Gambarino              - 活泼圆润衬线
```
避免：Nunito / Quicksand（Duolingo/Figma 之外易显套路）

---

### 🎯 描述字体的 image-2 话术

image-2 没法真的 import 字体，但**可以描述字形特征让模型画出接近的字形**：

| 想要的感觉 | image-2 prompt 描述法 |
|---|---|
| Tiempos Headline | `elegant humanist serif with sharp terminals and slight stress contrast, editorial newspaper feel` |
| Canela | `flared-stem serif with condensed proportions, high-end fashion magazine quality` |
| GT America | `wide American grotesque with mechanical precision and slight warmth` |
| Söhne | `refined Swiss neo-grotesque, neutral but sophisticated, tight tracking` |
| PP Neue Machina | `condensed geometric sans with angular terminals, techno-brutalist character` |
| Druk | `super-heavy condensed display sans, newspaper-headline authority` |
| Berkeley Mono | `contemporary monospace with rounded terminals and coding ligatures` |
| Recoleta | `rounded display serif with friendly contemporary humanism, high x-height` |
| Caslon | `classical oldstyle serif, book-typography tradition, deep warmth` |
| Monument Grotesk | `cinematic display grotesque, dramatic weights, heavy presence` |

---

### ⚡ Prompt 用法示例

**Editorial Minimalism 场景**（Linear 风）：
```
Typography: a refined American grotesque with subtle warmth (GT America 
or Söhne character — NOT Inter, NOT Space Grotesk). Display 64px with 
tight tracking, body at 17px with 1.65 line-height.
```

**Warm Editorial 场景**（Anthropic 风）：
```
Typography: a characterful serif body (Tiempos Text feel — humanist, 
slight contrast, warm terminals). Display in a softened sans (Söhne 
Breit character). Generous line-height 1.7.
```

**Brutalist 场景**：
```
Typography: deliberate clash of a heavy condensed display (Druk or 
PP Neue Machina character) at 200px+ with a classical oldstyle serif 
(Caslon feel) for body. Mix justifications for deliberate tension.
```

**Mono 场景**（Terminal / IDE）：
```
Typography: 100% monospace throughout (Berkeley Mono / JetBrains Mono 
character — angular but readable, coding ligatures visible in the 
code blocks).
```

---

## 📐 间距 & 网格系统

### 通用 8px 网格
```
4px   (0.5) - 微间距（icon 内部）
8px   (1)   - 基础单位
12px  (1.5) - 小组件间距
16px  (2)   - 默认内边距
24px  (3)   - 卡片内边距
32px  (4)   - 主内容内边距
48px  (6)   - 区块间距
64px  (8)   - 大区块间距
96px  (12)  - 顶部 hero 间距
128px (16)  - 超大空白
```

### 4px 密集网格（仪表盘类）
```
2px, 4px, 8px, 12px, 16px, 20px, 24px
```

**Prompt 用法**：
```
Spacing: Strict 8px grid. 24px padding inside cards. 
         16px gap between cards. 48px between major sections.
```

---

## 💎 圆角 / 阴影 / 边框

### Border Radius（圆角）
```
0px    - Sharp / brutalist
4px    - Subtle / form inputs
8px    - Default buttons, cards
12px   - Larger cards, modals
16px   - Hero sections
24px   - Pills / mobile-first
999px  - Full pill shape
```

### Box Shadow（阴影层次）
```
None                                              - flat design
0 1px 2px rgba(0,0,0,0.05)                       - very subtle
0 1px 3px rgba(0,0,0,0.1)                        - card default
0 4px 6px -1px rgba(0,0,0,0.1)                   - card elevated
0 10px 15px -3px rgba(0,0,0,0.1)                 - modal
0 20px 50px rgba(0,0,0,0.3)                      - hero visual float
```

**Prompt 用法**：
```
Cards: 12px rounded corners, subtle shadow (0 1px 3px with 10% opacity),
       1px border #E5E7EB.
Hero visual: floats with soft drop shadow (0 20px 50px at 30% opacity).
```

---

## 🎯 UI 风格定义词典

复制到 prompt 的 `Important details` 里：

### Flat Design
```
Flat design style: solid colors, no gradients, no shadows, 
2D icons, clear typography, high contrast.
```

### Neumorphism（拟物 2.0）
```
Neumorphism style: soft inner+outer shadows on monochromatic background, 
extruded-from-surface look, rounded corners, pastel colors.
```

### Glassmorphism（玻璃拟态）
```
Glassmorphism style: translucent frosted glass panels with backdrop blur,
subtle white/gray tints over colorful background, visible edge borders,
light shadow.
```

### Brutalism
```
Brutalism: harsh high-contrast colors (black/white/yellow/red), 
heavy typography in all caps, no rounded corners, visible grid lines, 
raw/unfinished feel, asymmetric layouts.
```

### Swiss / International Typographic
```
Swiss design: strict grid system, heavy sans serif (Helvetica-like), 
asymmetric but balanced layout, generous white space, minimal color 
(often just black + one accent).
```

### Bento Box（Apple 近期风格）
```
Bento grid layout: rounded cards of varying sizes tiled like bento box,
each card a different but harmonious color/content, 
subtle gradients within each card, 16-24px gaps.
```

### Editorial / Magazine
```
Editorial design: serif display headlines, asymmetric type hierarchy, 
mix of image and large text blocks, generous whitespace, 
newspaper-grid feel but modern.
```

---

## 🖼 常见 device frame

```
iPhone 15 Pro frame (6.1" or 6.7") with Dynamic Island notch, 
  titanium bezel, portrait orientation.

iPhone mini frame, classic notch.

MacBook Pro 14" frame, Space Black, 3:2 aspect screen, Notch visible.

iPad Pro 12.9" frame, landscape, slim bezels.

Desktop browser chrome: Chrome-like top bar with 3 tabs, 
  back/forward arrows, URL bar reading "https://{{URL}}".

Safari-style browser chrome with distinct rounded tab shape.

No frame: just the UI filling the full canvas, clean bleed.
```

---

## 🎨 Backgrounds / Environments

```
Pure white #FFFFFF - default
Subtle cream #FAF6EE - warmer editorial
Gradient dawn pink-orange - landing page
Gradient cool blue-purple - tech / SaaS
Deep forest green #1F2E27 - editorial luxury  
Soft gray #F5F5F7 - Apple-like neutral
Dot grid pattern 1px at 32px spacing, 5% opacity - tech brand
Light noise/grain overlay - editorial texture
Studio seamless backdrop (pale gray roll) - product photography
```

---

## ⚡ 快速 prompt 片段（直接粘贴）

### "像 Linear 的感觉"
```
Linear-like aesthetic: pure black-on-white, generous whitespace, 
single accent color (violet oklch(0.55 0.20 285)), rounded 8px corners, 
thin hairline borders, a narrow humanist grotesque with slight warmth 
(GT Planar / Söhne character — NOT Inter, NOT Space Grotesk), 
keyboard shortcut hints visible, dense but calm.
```

### "像 Stripe 的感觉"
```
Stripe-like aesthetic: rich gradient top (purple to pink to orange), 
clean white card overlay, Söhne typography, precise currency 
formatting in mono font, subtle hover states, generous padding.
```

### "像 Notion 的感觉"
```
Notion-like aesthetic: pure white background, 
a warm humanist serif body text (Tiempos Text / PP Editorial Old character), 
emoji-rich headers (Notion is one of the FEW brands where emoji is on-brand), 
minimalist blocks, subtle gray separators, generous line-height 1.7, 
no heavy colors — mostly warm ink #37352F on white with accent on links.
```

### "像 Apple 的感觉"
```
Apple-like aesthetic: SF Pro Display for headlines (thin weight, 
tracking tight), SF Pro Text for body, pure white or pale gray 
background, subtle shadows, mathematically precise spacing, 
generous negative space, one accent color used sparingly.
```

### "像 Vercel 的感觉"
```
Vercel-like aesthetic: black and white monochrome, 
Geist Sans typography, triangle logo motif, 
pure black #000 CTA buttons with white text, 
code blocks in dark mode, subtle gridlines at 10% opacity.
```

---

## 🎨 oklch 色彩系统（感知均匀）

> **为什么用 oklch 不用 HSL？**
>
> HSL 中 "50% lightness" 的黄色 ≈ 90% 亮度视觉，"50% lightness" 的蓝色 ≈ 40% 亮度视觉 — **同 lightness 但视觉差异巨大**。
>
> `oklch()` 基于感知均匀色彩空间，同 lightness 值**视觉亮度真的一致**。做设计系统色板时是压倒性性能优势。

### 📦 oklch 基础概念

```
oklch(L C H)
└─ L = lightness  (0.0 = 纯黑 / 1.0 = 纯白)
└─ C = chroma     (0.0 = 灰色 / 0.4 = 极饱和)
└─ H = hue        (0° = 红 / 90° = 黄 / 180° = 青 / 270° = 蓝紫)
```

**预设色盘**（直接用）：

```css
/* oklch-based 主色系统（来自 ConardLi） */
:root {
  --primary-h: 250;  /* hue: 250° = blue-violet */
  --primary:       oklch(0.55 0.25 var(--primary-h));  /* 主色 */
  --primary-light: oklch(0.75 0.15 var(--primary-h));  /* 浅版 */
  --primary-dark:  oklch(0.35 0.20 var(--primary-h));  /* 深版 */
  
  /* 灰阶 9 级（chroma 趋近 0，略带色彩倾向保证和主色和谐） */
  --gray-50:  oklch(0.98 0.002 250);
  --gray-100: oklch(0.96 0.004 250);
  --gray-200: oklch(0.92 0.006 250);
  --gray-300: oklch(0.87 0.008 250);
  --gray-400: oklch(0.71 0.010 250);
  --gray-500: oklch(0.55 0.014 250);
  --gray-600: oklch(0.45 0.014 250);
  --gray-700: oklch(0.37 0.014 250);
  --gray-800: oklch(0.27 0.014 250);
  --gray-900: oklch(0.21 0.014 250);
}
```

### 📝 image-2 prompt 里怎么表达 oklch？

image-2 不能真的解析 `oklch()`函数，但可以通过**描述 hue + lightness + chroma**让模型生成和谐色彩：

```
Color system: derive harmonious palette from oklch space —
- Primary hue is violet (oklch hue ~285°), used at medium lightness 0.55 
  with moderate chroma 0.25 for the main brand color.
- Neutrals are derived from the same hue family (violet-tinted grays), 
  ensuring tonal harmony — NOT random desaturated grays.
- Same lightness values across colors appear VISUALLY equally bright 
  (unlike HSL where yellow-at-50% outshines blue-at-50%).
- Use a dominant primary + ONE sharp accent, not timid evenly-distributed palettes.
```

**实用描述模板**：
```
Color: primary oklch(0.55 0.25 285) — a deep violet at medium lightness.
Background: oklch(0.98 0.002 285) — near-white with faint violet tint.
Text primary: oklch(0.21 0.014 285) — near-black with matching hue family.
Accent: oklch(0.70 0.20 30) — a sharp coral to break the monotony.
```

---

## 🎨×🔤 4 个 Pre-validated 色×字配对（无设计上下文时的开局）

> 当你**完全没有设计上下文**时，以下 4 个是经过验证的开局组合。一旦用户给了 brand 或 design system 就**立即抩弃**，按他的材料走。

来源 ConardLi，我们**移除了含禁用字体的组合**（ConardLi 原表中 Space Grotesk 组与 Anthropic 规则矛盾）。

### 配对 1：Elegant Editorial（编辑优雅）
```
Primary: oklch(0.35 0.10 30)   — warm brown
Fonts:   Newsreader (display) + Outfit (body)
Best for: Content platforms, blogs, editorial sites, writing tools

image-2 prompt: "Warm brown primary color in oklch space at medium-low 
lightness, paired with a humanist serif display font (Newsreader character) 
and a clean geometric body sans (Outfit character). Editorial magazine feel."
```

### 配对 2：Premium Brand（高端品牌）
```
Primary: oklch(0.20 0.02 250)  — near-black with subtle blue undertone
Fonts:   Sora (display) + Plus Jakarta Sans (body)
Best for: Luxury, consulting, finance, premium SaaS

image-2 prompt: "Near-black primary color with subtle blue undertone 
(derived in oklch space), paired with a contemporary geometric display 
(Sora character) and a modern humanist body sans (Plus Jakarta Sans 
character). Precise, confident, premium."
```

### 配对 3：Lively Consumer（活泼消费型）
```
Primary: oklch(0.70 0.20 30)   — warm coral
Fonts:   Plus Jakarta Sans (display) + Outfit (body)
Best for: E-commerce, lifestyle, social, consumer apps

image-2 prompt: "Warm coral primary color at high lightness and saturation 
(derived in oklch space), paired with a rounded geometric display 
(Plus Jakarta Sans character) and a clean body sans (Outfit character). 
Friendly, optimistic, approachable."
```

### 配对 4：Artisan Warmth（手工人文感）
```
Primary: oklch(0.55 0.15 80)   — caramel / warm mustard
Fonts:   Caveat (decorative accent) + Newsreader (body)
Best for: Food & beverage, education, creative, handmade products

image-2 prompt: "Caramel warm-mustard primary color at medium lightness 
(oklch hue ~80°), with a handwritten decorative font (Caveat character) 
used sparingly for accents, and a warm humanist serif body (Newsreader 
character). Feels human, not mechanical."
```

### ❗ 要避开的组合（ConardLi 点名）
- ❌ **Inter + Roboto + 蓝按钮** — "peak AI aesthetic"，一眼假
- ❌ **Fraunces + 紫粉渐变** — 另一个伪高级垃圾组合
- ❌ **3+ 字体家族** — 视觉混乱
- ❌ Space Grotesk + Inter — 两个一起是双重 slop

---

## 📉 字号对比比例（ConardLi 实证）

视觉震慑的秘诀—— **h1 与 body 字号比 4-6×**是正常的。

| 场景 | 建议 body 字号 | 建议 h1 字号 | 比例 |
|---|---|---|---|
| 1920×1080 presentation | 24px+ | 96-144px | 4-6× |
| Web landing page | 16-18px | 64-96px | 4-5.5× |
| Mobile app | 16px | 28-36px | 1.8-2.3× (屏幕小) |
| Print | 12pt+ | 48-60pt | 4-5× |

触摸目标最小尺寸（ConardLi）：**44×44px**（iOS HIG 标准）。
