# 5 槽位通用模板（核心骨架）

来自 fal.ai 官方推荐结构，适用于所有 gpt-image-2 任务（UI / 海报 / 照片 / 产品图）。

---

## 📐 模板

```
Scene: [where this happens, time of day, background, environment]
Subject: [who or what is the main focus]
Important details: [materials, layout, typography, exact copy, state, spacing]
Use case: [editorial photo / product mockup / poster / UI screen / infographic / concept frame]
Constraints: [no watermark / no logos / no extra text / preserve X]
```

**五个槽位对应五个常见坑**：
1. 图在哪里发生
2. 图的主角是什么
3. 哪些细节必须可见
4. 最终成品是什么类型
5. **什么绝对不能漂移** ← 最容易被忽略，大部分平庸 prompt 都死在这里

---

## 🎯 UI 场景的 5 槽位化（填空版）

### 通用 UI 模板

```
Scene: [viewport type: mobile phone screen / desktop browser / tablet / smart TV].
       [device frame: iPhone 15 Pro / MacBook Pro 14 browser / no frame, just the screen].
       [background outside the screen: clean studio / on a wooden desk / floating on gradient].

Subject: [product type: SaaS analytics dashboard / mobile to-do app / e-commerce product page / landing page for X].
         [app name in ALL CAPS or "quotes": "NESTING" / "DAYBREAK" / "LUMEN"].

Important details:
- Header: [logo position, navigation items, user avatar area]
- Main content: [specific sections with exact copy]
- Typography: [font style, hierarchy, line height]
- Colors: [primary color HEX, background, accent, text colors]
- Spacing: [8px grid / generous negative space / tight packed]
- State: [what's selected, active, loading, error state if any]
- Data: [if charts/numbers, specify the exact numbers]

Use case: Realistic UI mockup screenshot of a shipped product.

Constraints:
- No watermark. No real app branding.
- No extra words. No duplicate text.
- Perfect text legibility. Pixel-perfect alignment.
- Do not add imaginary features not described above.
```

---

## 🌟 填空示例（一步步教你用）

### 示例 1: 简单 · 移动 To-do App

```
Scene: iPhone 15 Pro screen, portrait orientation, showing a todo app.
       White status bar at top reads "9:41 AM".

Subject: A minimalist to-do app called "DAYBREAK".

Important details:
- Header: Large display title "DAYBREAK" in bold. 
          Subtitle underneath: "Tuesday, 23 April".
- Task list (4 items, one is checked):
  [✓] Review quarterly notes
  [ ] Call mom
  [ ] Ship the image update
  [ ] Pick up bread
- Typography: Rounded sans serif font, 28pt title, 17pt body.
- Colors: Muted cream background (#FAF6EE), deep navy accent (#1E2A44), 
          task text in charcoal (#2C2C2E).
- Spacing: Generous vertical rhythm, 16px between tasks, card-style rows 
           with soft shadows.
- Bottom: A floating round "+" button in deep navy.

Use case: Clean mobile app screenshot for portfolio.

Constraints:
- No watermark. No real app branding (no Apple logo, no Todoist/Things).
- Text must be 100% readable.
- No extra words. No duplicate text.
```

### 示例 2: 中等 · SaaS Dashboard

```
Scene: MacBook Pro 14" browser window, Chrome-like top bar with 3 tabs 
       and URL bar reading "app.lumen.io/dashboard". Clean gradient 
       background behind the laptop (soft pink to blue).

Subject: A SaaS analytics dashboard for a product called "LUMEN".

Important details:
- Top nav: LUMEN logo on far left. Nav items (left to right): 
  "Overview", "Analytics", "Reports", "Settings". 
  User avatar circle on far right.
- Sidebar (280px wide): Light gray (#F5F5F7). Menu items with icons:
  [⊙] Dashboard (selected, highlighted blue)
  [📊] Analytics
  [👥] Customers  
  [💰] Revenue
  [⚙] Settings

- Main content area:
  - Top row: 4 KPI cards (MRR / Active Users / Churn / NPS)
    Each card: big number (e.g., "$48,291"), label below, small delta 
    arrow with % change.
  - Middle: Large line chart titled "Daily Active Users (Last 30 Days)". 
    Y-axis goes 0-5000. Line color: #3B82F6 (blue).
  - Bottom: 2 columns — left is "Top Products" table (4 rows), 
    right is donut chart "Traffic Sources".

- Typography: Inter or SF Pro, 14px body, 24px H2, 32px KPI numbers.
- Colors: Primary #3B82F6, success #10B981, danger #EF4444,
          background #FFFFFF, border #E5E7EB, text #111827.
- Spacing: 24px padding inside cards, 16px gap between cards.

Use case: Realistic product screenshot for marketing website.

Constraints:
- No watermark. No real company logos (no Notion, Linear, Stripe logos).
- All chart data must look plausible, not lorem ipsum.
- Perfect legibility on 2x retina display.
```

### 示例 3: 复杂 · 产品 Landing Page Hero

```
Scene: Full-width desktop viewport (1440px wide), scrolled to top.
       Above-the-fold hero section visible.

Subject: Landing page hero for a developer productivity tool called "FORGE".

Important details:
- Top navigation (sticky): FORGE wordmark on left (heavy sans serif, 
  all lowercase "forge"). Right side: nav items "Product / Docs / 
  Pricing / Blog" then a primary pill button "Get Started".

- Hero headline (EXACT TEXT, one line): 
  "Ship your next project in half the time."
  Typography: 64px serif display font, tight line-height, center-aligned.

- Sub-headline (EXACT TEXT, one line):
  "A minimal Git workflow for teams who value focus."
  Typography: 20px regular, medium gray (#6B7280), center-aligned.

- CTA row (centered, below sub-headline):
  Primary button: "Start free trial" (black background, white text, 
  rounded 8px, 48px tall).
  Secondary link: "Watch demo →" (no background, text only, same gray).

- Hero visual (below CTAs): A tilted mockup of a dark-theme code editor 
  showing a git log terminal output with colorful commit graph on the left.
  Visual floats with soft shadow, slight 3d perspective, 
  ~60% viewport width.

- Trust bar (below hero visual): Grayed out 6 company logos in a row 
  with text "Trusted by teams at:" above. Use generic placeholder logos 
  (no real brands).

Background: Pure white with very subtle grid dots (1px dots at 32px 
            intervals, 5% opacity).

Use case: Marketing landing page hero screenshot.

Constraints:
- No watermark. No real company logos (GitHub, GitLab, Vercel, etc.).
- All text must be crisp and readable.
- Consistent 8px grid alignment throughout.
- No duplicate headlines.
```

---

## 🔑 使用技巧

### 技巧 1: **先低质打样，再高质出片**
```powershell
# 草稿（快 + 便宜）
.\gen-image.ps1 -PromptFile prompt.txt -Size "1024x1024" -Quality low

# 满意后再高质
.\gen-image.ps1 -PromptFile prompt.txt -Size "1536x1024" -Quality high
```

### 技巧 2: **迭代而非堆积**
如果第一张图 80% 对但有 3 个问题，**不要重写 prompt**。
用 image edit 一次改一个问题（目前的脚本暂未支持 edit，需要时调用 `/v1/images/edits`）。

### 技巧 3: **Use case 槽是模型切换器**
- `Use case: UI mockup` → 模型切到界面设计模式
- `Use case: editorial photo` → 切到杂志摄影模式
- `Use case: poster` → 切到海报排版模式

**漏掉 use case 是最常见的翻车原因**。

### 技巧 4: **Constraints 越明确越好**
除了通用的 `no watermark / no logos`，针对 UI 特别有效的：
- `No lorem ipsum. All text must be real content.`
- `Pixel-perfect alignment on 8px grid.`
- `No AI-style generic stock photos.`
- `Realistic data, not exaggerated or unrealistic numbers.`
