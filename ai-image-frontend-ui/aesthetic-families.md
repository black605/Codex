# 9 大美学家族（Aesthetic Families）

> 来自 `awesome-claude-design` 社区收敛的 9 大 UI 美学家族。每个家族都有**代表品牌 + HEX 色板 + image-2 prompt 片段**，可以直接拷贝到 `Important details` 里。

**使用方法**：
1. 先用下面 **Picker 三问** 选家族
2. 复制对应家族的 **image-2 片段** 到你的 prompt
3. 替换具体 copy / 数据

---

## 🎯 Picker：我该用哪个家族？

回答三个问题：

### 问题 1：产品是 read-heavy 还是 scan-heavy？
- **Read-heavy**（文档 / 博客 / 长文） → 家族 1 Editorial Minimalism 或 家族 3 Warm Editorial
- **Scan-heavy**（Dashboard / 数据 / 监控） → 家族 4 Data-Dense Pro 或 家族 2 Terminal-Core

### 问题 2：用户是谁？
- **Developer** → 家族 2 Terminal-Core 或 家族 4 Data-Dense Pro
- **Designer / Creator** → 家族 5 Cinematic Dark 或 家族 6 Playful Color
- **Consumer** → 家族 7 Glass / Soft-Futurism 或 家族 6 Playful Color
- **Prosumer**（专业消费者） → 家族 3 Warm Editorial

### 问题 3：品牌要显"勇气"吗？
- **要** → 家族 8 Neon Brutalist 或 家族 9 Cult / Indie Picks
- **不要** → 留在家族 1-7

---

## 家族 1️⃣ Editorial Minimalism

**代表品牌**：Linear / Stripe / Vercel / Mintlify

**核心特征**：
- 干净中性色（白 / 近黑）+ **单一锐利强调色**
- 衬线或窄 grotesque 标题，宽松行高
- 为阅读而生

**色板**：
```
Linear:    #FFFFFF / #0F0F14 / accent #5E6AD2 (violet)
Stripe:    #FFFFFF / #0A2540 / accent #635BFF
Vercel:    #FFFFFF / #000000 / single grayscale ramp
Mintlify:  #FFFFFF / #0C0C0E / green accent
```

**适用场景**：文档站、定价页、博客、SaaS landing

### 📋 image-2 prompt 片段（直接拷贝）
```
Visual style: Editorial minimalism in the spirit of Linear + Stripe.
Color: pure white #FFFFFF background, near-black #0F0F14 for headlines, 
       medium gray #687076 for body, a single sharp violet accent 
       #5E6AD2 used sparingly on interactive elements (links, primary 
       button) — NOT a gradient.
Typography: a narrow humanist grotesque with slight warmth (think GT 
       Planar or Söhne feel, not Inter, not Space Grotesk). Display at 
       ~56-72px with tight tracking. Body at 16-18px with generous 
       line-height (1.6-1.7).
Background: pure solid white, no gradient. ONE hairline rule (1px 
       #E3E4E6) to separate major sections.
Motion hint: suggest staggered reveal by having one headline fully 
       settled and a sub-element slightly below baseline.
```

**避坑**：
- ❌ 不要放"3-column feature grid + icon above title + short copy"（套路）
- ❌ 不要多个 accent 色（破坏 single-accent 原则）

---

## 家族 2️⃣ Terminal-Core

**代表品牌**：Ollama / Warp / Raycast / OpenCode / Hacker News

**核心特征**：
- 全等宽字体
- 近黑背景 + phosphor 绿 / 琥珀色 / 白
- 硬边，CLI 隐喻（`$`、`>`、`~/`）
- Zero 装饰，zero 渐变

**色板**：
```
Ollama:    #000000 / #FFFFFF / (no accent)
Warp:      #0B0D14 / #16D5E6 (cyan) / #FF7A59 (coral)
Raycast:   #1D1D1F / #FF6363 / #FFFFFF
OpenCode:  #080808 / #D2D2D2 / phosphor green
```

**适用场景**：开发者工具、CLI 产品、DevOps dashboard

### 📋 image-2 prompt 片段
```
Visual style: Terminal-core aesthetic in the spirit of Warp + Raycast.
Color: near-black background #0B0D14, soft white primary text #E5E7EB, 
       one cyan accent #16D5E6 for prompts and selection, 
       one coral #FF7A59 for destructive/error states. 
       NO other colors. NO gradients.
Typography: 100% monospace throughout — variable-width characters are 
       BANNED. Use a programming font with ligatures (think JetBrains 
       Mono / Berkeley Mono / IBM Plex Mono character — angular, 
       readable, slight humanist warmth).
Background: flat near-black, no gradient, no texture — optional subtle 
       CRT scanline at 2% opacity.
Layout: hard 90° corners throughout (no rounded). Box-drawing characters 
       (┌ ─ │ └ ┘) for borders. Dollar-prompt ($) markers. ASCII-art 
       headers if appropriate.
```

**避坑**：
- ❌ 任何 sans serif 字体混入
- ❌ 圆角（> 2px）
- ❌ 软阴影 / 柔和过渡

---

## 家族 3️⃣ Warm Editorial ⭐（Claude 自家风格）

**代表品牌**：Anthropic / Notion / Resend / Substack

**核心特征**：
- 赤陶土 / 奶白 / 泥土色
- 衬线正文或温暖 humanist
- 亲和但精致，"人"的味道

**色板**：
```
Anthropic:  #F4F3EE (cream) / #C96442 (terracotta) / #191817 (ink)
Notion:     #FFFFFF / #37352F (warm near-black) / warm grays
Resend:     #0A0A0A / #FFFFFF / mono accents
Substack:   #FFFFFF / #1A1A1A / #FF6719 (orange)
```

**适用场景**：写作工具、编辑器、媒体网站、Anthropic 风

### 📋 image-2 prompt 片段
```
Visual style: Warm editorial in the spirit of Anthropic + Notion.
Color: cream background #F4F3EE (warmer than pure white, paper-like), 
       deep ink #191817 for primary text, warm mid-gray #716B66 for 
       secondary, one terracotta accent #C96442 on links and primary 
       CTAs.
Typography: a characterful serif for body text (think Tiempos Text / 
       PP Editorial New feel — humanist, slight contrast, warm 
       terminals). Display in a softened geometric sans (think Söhne 
       Breit feel — precise but not cold). Line-height 1.55-1.7 for 
       reading comfort.
Background: cream with very subtle paper grain texture at 3% opacity. 
       OPTIONAL: a single off-center terracotta diagonal band cutting 
       across a corner.
Composition: generous negative space (at least 40% whitespace), 
       asymmetric but balanced, magazine-like.
```

**避坑**：
- ❌ 纯白背景（丢掉"warm"味道）
- ❌ 冷色 accent（蓝色 / 紫色会打破和谐）
- ❌ 数字感过强（gradient mesh / neon）

---

## 家族 4️⃣ Data-Dense Pro

**代表品牌**：ClickHouse / PostHog / Grafana / Sentry / Supabase

**核心特征**：
- 图表是主角
- 紧凑间距，饱和的分类调色板
- 固定宽度数字
- **通常 dark-first**

**色板**：
```
ClickHouse:  #181818 / #FAFF69 (signal yellow) / magenta
PostHog:     #1D4AFF / #F9BD2B (yellow) / #000
Grafana:     #111217 / #F47C1B (orange) / multi-series
Sentry:      #362D59 / #F6827D (salmon) / #584774
Supabase:    #171717 / #3ECF8E (green)
```

**适用场景**：监控、分析、BI、Dashboard

### 📋 image-2 prompt 片段
```
Visual style: Data-dense professional dashboard in the spirit of 
Grafana + ClickHouse.
Color: dark chrome background #111217, near-white chart lines and 
       text #E8E8E8, a categorical palette for chart series — 
       signal yellow #FAFF69, hot magenta #FF4FCE, cyan #16D5E6, 
       orange #F47C1B, violet #8B5CF6. Each series gets ONE saturated 
       hue, no gradient fills on bars.
Typography: a characterful technical sans for UI labels (think Roobert 
       / GT Planar feel — precise, engineered). Numbers MUST be in a 
       tabular-figure monospace (so they align column-wise in tables). 
       Keep labels at 11-13px to maximize data density.
Background: dark chrome #111217, absolute black for chart areas #000, 
       1px hairlines #2A2D35 for grid.
Composition: dense information panels, multiple side-by-side charts, 
       tight 8-12px gutters, NO wasted whitespace. Each chart is a 
       self-contained card with a tiny title-bar (timeseries / bar / 
       heatmap / big-number).
```

**避坑**：
- ❌ 浅色主题（scan-heavy 场景深色更好）
- ❌ 图表用 gradient fill（看着花哨，实际信息量下降）
- ❌ 大标题 / 大空白（浪费数据展示空间）

---

## 家族 5️⃣ Cinematic Dark

**代表品牌**：Runway / ElevenLabs / Midjourney / Minimax

**核心特征**：
- 电影级渐变
- 超大字号
- 运动感极强
- 媒体主导的 hero

**色板**：
```
Runway:      #000 / saturated magenta + cyan
ElevenLabs:  #0A0A0A / electric blue / wave motifs
Midjourney:  #000 / earth tones + lilac
Minimax:     #000 / neon lime on charcoal
```

**适用场景**：AI 产品、创作工具、媒体平台

### 📋 image-2 prompt 片段
```
Visual style: Cinematic dark in the spirit of Runway + Midjourney.
Color: absolute black #000000 base, with a saturated gradient mesh 
       background — magenta #FF006E blending into electric cyan #00E0FF 
       at the corners, most concentrated behind the hero element. 
       Foreground text in pure white, used sparingly.
Typography: a cinematic display face — think Eiko / Monument Grotesk 
       Heavy feel — at massive sizes (96-160px) with dramatic line 
       breaks. Body in a precise neo-grotesque at 16-18px.
Background: dark gradient mesh with visible film grain noise overlay 
       at 8% opacity (adds that "cinema" crush to the shadows). 
       Optional: a single out-of-focus lens-flare bokeh in the corner.
Composition: media-heavy — a large video still or AI-generated hero 
       image occupies 50%+ of the canvas. Text is deliberately small 
       relative to imagery (reverse of most SaaS sites).
```

**避坑**：
- ❌ 纯色黑背景（失去"cinematic"深度）
- ❌ 多个均匀色点缀（破坏 mood）

---

## 家族 6️⃣ Playful Color

**代表品牌**：Figma / Clay / Duolingo / Mailchimp / Cal

**核心特征**：
- 高饱和度
- 插画 accents
- 圆角
- 装饰形状
- 消费者友好

**色板**：
```
Figma:     #0ACF83 / #F24E1E / #A259FF / #FF7262 / #1ABCFE  (全 5 色)
Clay:      #F6E9C9 / organic shapes / soft gradients
Duolingo:  #58CC02 (green) / #FFFFFF / #FF4B4B (heart red)
Mailchimp: #FFE01B (yellow) / #000
Cal:       #292929 / #FFFFFF / single accent
```

**适用场景**：C 端产品、教育、工具、创意平台

### 📋 image-2 prompt 片段
```
Visual style: Playful color in the spirit of Figma + Duolingo.
Color: a 3-color saturated palette — primary electric green #58CC02, 
       secondary hot coral #FF4B6E, tertiary sunshine yellow #FFE01B. 
       Plus white #FFFFFF and one near-black #1B1B1B for contrast. 
       Colors used confidently in large flat blocks, NOT in timid 
       small accents.
Typography: a rounded geometric sans with personality (think Recoleta / 
       PP Mori Rounded / Nunito Heavy feel — friendly, hand-drawn hint 
       but still precise). Display chunky and bold, body at 17px 
       rounded regular.
Background: a playful composition — either ONE large soft gradient 
       (yellow-to-orange) with cut-out organic blob shapes, OR a 
       checkered/striped pattern in muted colors behind a white 
       content card.
Decorative: include 2-3 abstract geometric shapes (circles, squiggles, 
       stars) positioned asymmetrically in the background, in the 
       accent colors.
```

**避坑**：
- ❌ 颜色过多（5+ 色会乱，最多 3-4 色）
- ❌ 严肃字体（GT America / Söhne 会失去 playful 感）

---

## 家族 7️⃣ Glass / Soft-Futurism

**代表品牌**：Apple / Arc / Airbnb / Granola / Spotify

**核心特征**：
- 磨砂玻璃模糊
- 层叠半透明
- 柔和渐变
- Apple 毗邻的高端质感

**色板**：
```
Apple:    #FFFFFF / #1D1D1F / system colors (SF symbols)
Arc:      #FFFFFF / radial pastel gradients
Airbnb:   #FFFFFF / #FF385C (rausch red) / #222
Granola:  #FAF8F2 / warm glass
Spotify:  #000000 / #1DB954 (signature green)
```

**适用场景**：消费级高端、macOS 生态、premium brands

### 📋 image-2 prompt 片段
```
Visual style: Glass / soft-futurism in the spirit of Apple + Arc Browser.
Color: warm off-white base #FAF8F2, with multiple translucent 
       "glass panel" overlays (30-40% opacity, heavy backdrop blur). 
       Pastel gradient spheres behind — peach #FFB4A2, periwinkle 
       #B8C0FF, mint #A7E8BD — blurred to 60px radius. 
       One system red #FF385C for primary action.
Typography: a precise humanist sans (think SF Pro Display / Inter 
       Display feel, but NOT generic Inter — use weighted contrast 
       with Thin display at 72px and Regular body). Tracking slightly 
       tight on display.
Background: gradient mesh of soft pastels, OVER that a large frosted-
       glass card overlay containing the content. The glass card has 
       1px subtle white border and a soft drop shadow.
Composition: layers upon layers — 3+ translucent surfaces at different 
       depths, each with slight shadow, creating apparent z-depth.
```

**避坑**：
- ❌ 太 saturated（破坏 soft 感）
- ❌ 硬边（矛盾于 glass aesthetic）

---

## 家族 8️⃣ Neon Brutalist

**代表品牌**：Bugatti / PlayStation / The Verge / Pitchfork

**核心特征**：
- 硬边
- 故意丑的字体混搭
- 超大数字
- 饱和单色
- 声明式作品

**色板**：
```
Bugatti:     #0D1321 (deep navy) / electric blue / chrome
PlayStation: #000 / full-spectrum prism (PS5 brand colors)
The Verge:   #FF6600 (orange) / #000 / #FFF
Pitchfork:   #FFFFFF / #000 / #FF5D1F (signature orange)
```

**适用场景**：媒体、创意作品集、音乐/游戏、态度明确的品牌

### 📋 image-2 prompt 片段
```
Visual style: Neon brutalism in the spirit of The Verge + Pitchfork.
Color: pure white #FFFFFF base, aggressive near-black #000 for 
       typography (super heavy weights), ONE signature orange 
       #FF5D1F used as a weapon — in full-bleed color blocks, 
       oversized numerals, and deliberate dissonance.
Typography: deliberate font mixing — a display serif (Didone / 
       Miller feel) at oversized 120-200px for one word, a brutalist 
       grotesque (PP Neue Machina / Druk feel) for headers, and a 
       humanist serif for body. Mix justifications (some left, some 
       centered, some right) to create rhythm through imbalance.
Background: pure white or deep black, with ONE massive oversized 
       numeral or punctuation mark rendered at 400px+ in the accent 
       color, positioned off-canvas-edge for drama.
Composition: asymmetric grid, deliberate whitespace imbalance, 
       full-bleed edges that cut content, stacked headlines with 
       varying weights creating visual tension.
```

**避坑**：
- ❌ "干净" / "对称" / "舒适"（全都反 brutalism）
- ❌ 柔和色板（必须至少一个 saturated accent）

---

## 家族 9️⃣ Cult / Indie Picks

**代表品牌**：Superhuman / Obsidian / Paradigm / A24 / Letterboxd / Criterion / ProPublica / Dimension / thesephist.com

**核心特征**：
- 不是 Fortune 500 的套路
- **值得克隆的冷门品牌**（社区标注）
- 往往 hybrid 多个家族

**灵感方向**：
- `A24` — 电影公司，极简衬线 + 大幅照片 + 黄色 accent
- `Criterion` — 电影收藏，经典衬线 + 红色 + 文学质感
- `Letterboxd` — 影评社区，深绿深橘 + 手绘气息
- `Paradigm` — 加密投资，暗黑 editorial + 单一冷色
- `Superhuman` — 邮件，极简 + 极限键盘快捷键密度
- `Obsidian` — 笔记，紫色 + 节点图美学
- `Granola` — AI 笔记，warm glass + 笔迹风
- `thesephist.com` — 个人网站，brutalist + 功能至上

### 📋 通用 "indie / cult" image-2 片段
```
Visual style: cult-indie aesthetic, inspired by [A24 + Criterion] OR
[Letterboxd + Paradigm] OR [Superhuman + Obsidian] — pick one pair.

[A24 + Criterion 版]:
Color: rich parchment cream #F4EED6, deep ink #181312, one signal 
       red #CE3B34 used on one single element (title or ornament).
Typography: a classic oldstyle serif (Caslon / Garamond character), 
       title set large with generous tracking, body in smaller roman. 
       ALL CAPS small labels for metadata.
Background: aged paper with subtle yellowing at edges, very faint 
       horizontal rule lines like an old book page.
Composition: book-jacket framing — single dominant image, title 
       anchored below, small credits like a movie poster.

[Letterboxd + Paradigm 版]:
Color: deep forest #0F1B10 base, burnt orange #F48B2C accents, 
       off-white #EFEBDC text. Feels like a hand-bound ledger.
...
```

---

## 🎨 Remix Recipes（混搭配方）

单一家族容易做"干净的克隆"，但混搭家族能做出**新东西**：

### 推荐混搭
| 配方 | 家族组合 | 适用场景 |
|---|---|---|
| **Warm Brutalist** | 3 Warm Editorial × 8 Neon Brutalist | 有态度的编辑产品 |
| **Data Dark Editorial** | 4 Data-Dense × 5 Cinematic | AI 产品 landing page |
| **Terminal Playful** | 2 Terminal-Core × 6 Playful Color | 面向开发者的 C 端产品 |
| **Glass Minimal** | 1 Editorial × 7 Glass | 高端 B2B SaaS |
| **Cinematic Indie** | 5 Cinematic × 9 Cult/Indie | 创作者工具、作品集 |
| **Warm Terminal** | 2 Terminal × 3 Warm | Anthropic / 复古 CLI 产品 |

### 混搭 prompt 模板
```
Visual style: a remix of [家族 A 的核心特征] and [家族 B 的核心特征].
Take the [typography / color / layout] of A, combined with the 
[texture / motion / density] of B.
The result should feel [新品牌气质 — e.g., "confident but warm", 
"technical but playful"].

Specifically:
- Typography: [从 A 或 B 挑一个]
- Color: [把 A 的主色 + B 的 accent]
- Background: [从 B 借气质]
- Layout: [从 A 借骨架]
```

---

## ⚡ 最终决策表

```
┌─────────────────┬──────────┬─────────┬──────────┬─────────────┐
│ 家族            │ 字体倾向 │ 色彩能量 │ 装饰量    │ Read/Scan   │
├─────────────────┼──────────┼─────────┼──────────┼─────────────┤
│ 1 Editorial Min │ 衬线优雅 │ 低       │ 极少      │ Read        │
│ 2 Terminal-Core │ 等宽     │ 低-中    │ 无        │ Scan        │
│ 3 Warm Editorial│ 衬线温暖 │ 中        │ 少        │ Read        │
│ 4 Data-Dense    │ 工程 sans│ 中(多系列)│ 密集       │ Scan        │
│ 5 Cinematic Dark│ display  │ 高        │ 中（光影） │ 两者都行     │
│ 6 Playful Color │ 圆润     │ 极高      │ 多（形状） │ 两者都行     │
│ 7 Glass/Futurism│ humanist │ 中        │ 多（层叠） │ Consumer    │
│ 8 Neon Brutalist│ 混搭     │ 高        │ 极致       │ 都可，但激烈 │
│ 9 Cult/Indie    │ 各种     │ 各种      │ 各种       │ 各种        │
└─────────────────┴──────────┴─────────┴──────────┴─────────────┘
```
