---
title: Playbook · Mode A 探索模式
mode: Explore
when_to_use: 用户只有模糊想法，需要探索设计方向
capability_ratio:
  image-2: 50%
  prompt:  30%
  mcp:     20%
---

# Playbook: Mode A · 探索模式

> **假设用户需求**：
> "给 Nous 项目做个 SaaS 产品 landing page，
> 面向 B 端知识管理工具用户，
> 想要有点高级感但不要太冷。
> 你先帮我想想走哪个方向。"

---

## 🎯 这个场景的关键特征

- ✅ 用户知道**大致目的**（SaaS landing）
- ✅ 用户知道**目标用户**（B 端知识管理）
- ✅ 用户知道**基本调性期待**（高级感 + 不太冷）
- ❌ 用户**不知道**具体视觉方向
- ❌ 用户**不知道**该用什么色、什么字

→ **image-2 主导**：快速出多个方向让用户选

---

## 🚀 完整工作流

### Step 1: Prompt 工程 · 圈定 2-3 个候选家族（5 分钟）

读 `aesthetic-families.md` 的 Picker 三问：

```
Q1: read-heavy or scan-heavy?
    → knowledge management 产品大多 read + scan 并重
    → 家族 1 Editorial Minimalism 或 家族 3 Warm Editorial

Q2: 用户是谁？
    → B 端 prosumer / knowledge worker
    → 家族 3 Warm Editorial（prosumer 最佳）

Q3: 要勇气感吗？
    → "高级感但不太冷" = 温暖精致，不要激进
    → 不选家族 8 Brutalist

最终候选: 家族 3 Warm Editorial (主推) + 家族 1 Editorial Minimalism (备选)
```

### Step 2: 写候选 design system 决策表

创建 `design/design-decisions.md`：

```markdown
# Design Decisions — Nous Landing Page

## 候选方向 A: Warm Editorial（推荐）
- Inspired by: Anthropic × Notion × Substack
- Primary: oklch(0.35 0.10 30) warm brown
- Accent: oklch(0.60 0.20 30) terracotta
- Background: oklch(0.97 0.005 40) warm cream
- Display: Tiempos Headline character
- Body: PP Editorial Old character
- Vibe: 温暖、人文、精致、有厚度

## 候选方向 B: Editorial Minimalism（备选）
- Inspired by: Linear × Mintlify
- Primary: oklch(0.20 0.02 250) near-black
- Accent: oklch(0.55 0.20 285) violet
- Background: pure white
- Display: GT America character
- Body: Söhne Buch character
- Vibe: 冷静、精确、现代

## Avoid（两个方向都避免）
- NO Inter, Roboto, Arial, Space Grotesk, Fraunces, system-ui
- NO purple-pink gradients
- NO 3-column symmetric feature grid
- NO fabricated testimonials / logos
```

### Step 3: image-2 批量出 v0（3 分钟 + $0.04）

创建两个 prompt 文件：

**`design/prompt-v0-warm.txt`**：
```
Create a realistic full-width desktop landing page hero section for a 
knowledge management SaaS called "NOUS" (targeting B2B prosumers).

Visual style: Warm editorial in the spirit of Anthropic × Notion.

Color: warm cream background oklch(0.97 0.005 40) with subtle paper grain, 
deep ink text oklch(0.20 0.02 30), one terracotta accent oklch(0.60 0.20 30) 
on the primary CTA only.

Typography: a characterful humanist serif display (Tiempos Headline 
character — elegant terminals, slight stress contrast, editorial) at 
72px tight line-height. Body in a warm editorial body serif 
(PP Editorial Old character) at 18px generous line-height 1.7.

Layout (asymmetric, editorial):
- Top nav: "NOUS" wordmark left, nav items "Product / Pricing / Docs / Blog" 
  center, "Start writing" terracotta pill button right.
- Hero headline (EXACT TEXT, 2 lines, LEFT-aligned not centered):
  "Think better.
  Write slower."
- Subheadline (EXACT TEXT, 1 line):
  "A knowledge management tool for people who value the act of thinking."
- CTA row (left-aligned): Primary terracotta "Start your first note" + 
  secondary text link "Read the manifesto →"
- Hero visual (right side, tilted 3D mockup): an editorial-looking note 
  editor screenshot with serif body text

Background: warm cream with very subtle paper grain texture (3% opacity).

Use case: Realistic landing page hero screenshot for a B2B knowledge tool.

Constraints:
- NO Inter, Roboto, Arial, Space Grotesk, Fraunces, system-ui fonts.
- NO purple-pink gradients.
- NO symmetric 3-column feature grid below hero.
- Trust bar: 6 monochrome abstract geometric marks (circle/hexagon/
  square/triangle/plus/chevron) as logo placeholders, NOT fabricated 
  company logos.
- All copy must be EXACTLY as specified above.
- Pixel-perfect editorial layout, 8px grid.
```

**`design/prompt-v0-minimalism.txt`**：
```
Create a realistic full-width desktop landing page for "NOUS".

Visual style: Editorial minimalism in the spirit of Linear × Mintlify.

Color: pure white background, near-black text oklch(0.20 0.02 250), 
one violet accent oklch(0.55 0.20 285) used sparingly on interactive 
elements only. NO gradient, NO purple-pink.

Typography: a refined American grotesque (GT America character) for 
display at 64px with tight tracking, a Swiss neo-grotesque body 
(Söhne Buch character) at 17px line-height 1.6.

Layout (symmetric, centered):
- Top nav: "NOUS" wordmark + centered nav + violet CTA pill
- Hero (CENTER-aligned):
  Headline (EXACT TEXT): "Think better. Write slower."
  Subheadline (EXACT TEXT): "A knowledge management tool for 
  people who value the act of thinking."
  Primary CTA: "Start your first note" (violet pill)
  Secondary: "Read the manifesto →"
- Hero visual (below, centered): tilted 3D product mockup

Background: pure white with ONE hairline rule separating hero from 
trust bar.

Constraints: [same anti-slop + placeholder rules as above]
```

**跑脚本（2 张图并行）**：
```powershell
.\gen-image.ps1 -PromptFile design\prompt-v0-warm.txt `
                -Size "1024x1024" -Quality low `
                -OutPath design\v0-warm-low.png

.\gen-image.ps1 -PromptFile design\prompt-v0-minimalism.txt `
                -Size "1024x1024" -Quality low `
                -OutPath design\v0-minimalism-low.png
```

**成本**：~$0.02 × 2 = $0.04

### Step 4: 用户决策（关键人机交互点）

把两张图给用户看：

> "这是两个方向的粗稿。左边是 Warm Editorial（Anthropic/Notion 风），右边是 Editorial Minimalism（Linear 风）。你倾向哪个？
> 
> **方向 A 温暖感更强**，适合突出产品的人文属性；
> **方向 B 更精确冷静**，适合突出专业度。
> 
> 选一个我再做高质版本。如果你觉得要混一下，也可以说具体想要哪些元素混搭。"

---

假设用户选 A（Warm Editorial）。

### Step 5: MCP 采集真素材（10 分钟）

#### 5.1 抓真 logo（trust bar 用）

Nous 是知识管理 SaaS，trust bar 可以放"被这些团队使用"的真 logo：

```typescript
mcp4_logo_search({
  queries: [
    "figma",      // 协作产品
    "notion",     // 竞品/工具
    "linear",     // B2B
    "vercel",     // 开发者
    "supabase",   // 开发者  
    "resend"      // B2B
  ],
  format: "TSX"
})
```

保存到 `src/components/TrustBarLogos.tsx`。

⚠️ **注意**：这只是 mockup 演示，真上线前需要确认这些品牌是否真的用 Nous 或授权展示。

#### 5.2 查最新 Tailwind v4 oklch 用法

```typescript
mcp3_resolve-library-id({
  libraryName: "Tailwind CSS",
  query: "oklch color with arbitrary values v4"
})
// → "/tailwindlabs/tailwindcss"

mcp3_query-docs({
  libraryId: "/tailwindlabs/tailwindcss",
  query: "How to use oklch colors in Tailwind 4 with CSS variables"
})
// → 拿到最新官方写法
```

#### 5.3 查 shadcn 对应组件

```typescript
mcp10_search_items_in_registries({
  registries: ["@shadcn"],
  query: "hero section landing"
})
// → 返回候选组件

mcp10_view_items_in_registries({
  items: ["@shadcn/button", "@shadcn/card"]
})
// → 拿完整代码
```

### Step 6: image-2 出 v1 高质版（$0.16）

更新 prompt（加入从 MCP 拿到的真 logo 名称，明确告诉 image-2 这几个位置是真 logo），然后：

```powershell
.\gen-image.ps1 -PromptFile design\prompt-v1-warm-final.txt `
                -Size "1536x1024" -Quality high `
                -OutPath design\mockup-v1-high.png
```

这张 mockup 就是**设计意图的物理锚点**，后续代码全以它为准。

### Step 7: 交付 Mode A 产物

给用户：

```
design/
├── design-decisions.md          # 决策日志
├── prompt-v0-warm.txt           # 草稿 prompt
├── prompt-v1-warm-final.txt     # 终稿 prompt
├── v0-warm-low.png              # A 方向草稿 ($0.02)
├── v0-minimalism-low.png        # B 方向草稿 ($0.02)
└── mockup-v1-high.png           # 选中的终稿 ($0.16)

src/
└── components/
    └── TrustBarLogos.tsx        # 真 logo SVG
    
NOTES.md                         # 本 playbook 全记录
```

---

## 💰 成本和时间总计

| 项 | 花费 |
|---|---|
| image-2 2 张草稿 | $0.04 |
| image-2 1 张终稿 | $0.16 |
| MCP 工具调用 | $0 |
| 时间（人+AI） | 约 30 分钟 |
| **总 API 成本** | **$0.20** |

**对比 ConardLi 方式**：
- ConardLi 没法可视化探索
- 全靠语言描述，用户得脑补两个方向
- 选错方向后代码已经写好，返工成本高

**Mode A 的价值**：**$0.20 买 10 分钟内锁定对的方向**。

---

## 📦 Mode A 之后往哪走？

选完方向有了 `mockup-v1-high.png` 之后：
- 继续 **Mode B（落地）**，把 mockup 变成真代码
- 见 `playbooks/mode-b-ship.md`
