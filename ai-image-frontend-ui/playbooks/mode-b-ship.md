---
title: Playbook · Mode B 落地模式
mode: Ship
when_to_use: 用户有明确的视觉稿，要做成真代码
capability_ratio:
  mcp:     50%
  prompt:  30%
  image-2: 20%
---

# Playbook: Mode B · 落地模式

> **假设用户需求**：
> "这个 mockup（`mockup-v1-high.png`）帮我做成 React + shadcn/ui 的代码，
> 要能跑、要响应式、要有暗色模式。"

---

## 🎯 这个场景的关键特征

- ✅ 用户有**明确的视觉稿**
- ✅ 用户知道**技术栈**（React + shadcn）
- ❌ 用户**不想亲自写代码**
- ❌ 用户**不想一遍遍改 bug**

→ **MCP 主导**：拿真组件、真渲染、真验证

---

## 🚀 完整工作流

### Step 1: Prompt 工程 · 从 mockup 提取 design tokens

让 AI 看着 `mockup-v1-high.png` 提取结构化 tokens：

```
请分析 @design/mockup-v1-high.png 并提取完整 design tokens：

1. Color palette (估算 HEX 和 oklch)
2. Typography hierarchy (字体性格 + 字号 + 字重)
3. Spacing rhythm (px 单位)
4. Border-radius strategy
5. Shadow hierarchy
6. Layout structure (grid / flex)

写到 design/extracted-tokens.md
```

得到类似：

```markdown
# Extracted Tokens from mockup-v1-high.png

## Color
- Background: oklch(0.97 0.005 40) ≈ #FAF8F2
- Primary ink: oklch(0.20 0.02 30) ≈ #1E1815
- Secondary text: oklch(0.50 0.01 30) ≈ #736963
- Accent terracotta: oklch(0.60 0.20 30) ≈ #D97757
- Hairline: oklch(0.92 0.005 40) ≈ #E8E3D7

## Typography
- Display: humanist serif (Tiempos Headline character), 72px, weight 500, tracking -1%
- H2: serif, 36px, weight 500
- Body: editorial serif (PP Editorial Old character), 18px, weight 400, line-height 1.7
- Small: 14px, weight 500, uppercase, letter-spacing 1.5px

## Spacing
- Base unit: 8px
- Hero padding: 120px top, 80px bottom
- Section gaps: 96px
- Card internal padding: 32px

## Radius
- Cards: 12px
- Buttons: 999px (pill)

## Shadow
- Card: 0 1px 2px rgba(0,0,0,0.04)
- Hero visual: 0 20px 60px rgba(0,0,0,0.15)
```

### Step 2: MCP 拿真 shadcn 组件

```typescript
// 先看 mockup 需要哪些组件
// 观察到：Button (pill primary + text link), Hero section, Trust bar, Feature section

mcp10_search_items_in_registries({
  registries: ["@shadcn"],
  query: "button"
})

mcp10_view_items_in_registries({
  items: ["@shadcn/button"]
})
// → 完整 Button 代码 + CVA variants 定义

mcp10_get_add_command_for_items({
  items: ["@shadcn/button", "@shadcn/card"]
})
// → "npx shadcn@latest add button card"
```

**用户跑这个命令** → 真组件进项目。

### Step 3: MCP 查最新的 Tailwind v4 oklch 写法

```typescript
mcp3_query-docs({
  libraryId: "/tailwindlabs/tailwindcss",
  query: "v4 oklch in @theme config and arbitrary values syntax"
})
```

拿到最新写法后写 `app/globals.css`：

```css
@import "tailwindcss";

@theme {
  --color-bg: oklch(0.97 0.005 40);
  --color-ink: oklch(0.20 0.02 30);
  --color-text-muted: oklch(0.50 0.01 30);
  --color-accent: oklch(0.60 0.20 30);
  --color-hairline: oklch(0.92 0.005 40);
  
  --font-display: 'Tiempos Headline', Georgia, serif;
  --font-body: 'PP Editorial Old', 'Times New Roman', serif;
  
  /* NOT using Inter, Roboto, system-ui */
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  @theme {
    --color-bg: oklch(0.15 0.01 30);
    --color-ink: oklch(0.92 0.005 40);
    /* ... */
  }
}
```

### Step 4: MCP 抓真 trust bar logo

```typescript
mcp4_logo_search({
  queries: ["figma", "notion", "linear", "vercel", "supabase", "resend"],
  format: "TSX"
})
// 返回 6 个 TSX 组件代码，保存到 src/components/brand-icons.tsx
```

### Step 5: 代码生成（LLM + 所有真素材）

Windsurf 里的 prompt：

```
根据以下素材生成 Landing.tsx：

1. 设计意图锚点: @design/mockup-v1-high.png
2. Design tokens: @design/extracted-tokens.md  
3. 已安装 shadcn 组件: @/components/ui/button.tsx, @/components/ui/card.tsx
4. Trust bar 真 logo: @/components/brand-icons.tsx
5. Global CSS: @app/globals.css

要求：
- 严格遵循 mockup 的布局（左对齐 hero，不是居中）
- 字体用 extracted-tokens.md 里的（NO Inter/Roboto/Space Grotesk/Fraunces/system-ui）
- 所有颜色用 CSS variables（见 globals.css）
- Trust bar 6 个 logo 位置用 brand-icons.tsx
- 支持暗色模式（不用 JS toggle，走 prefers-color-scheme）
- Responsive: 375px / 768px / 1440px
- a11y: 所有交互元素 focus-visible，headings 有正确语义

输出: src/app/landing/page.tsx
```

Windsurf 会读图、读所有 @文件、调用 MCP 确认后生成 React 代码。

### Step 6: chrome-devtools MCP 渲染验证

```typescript
// 起项目本地服务
// (在终端) pnpm dev → localhost:3000/landing

mcp0_navigate_page({
  type: "url",
  url: "http://localhost:3000/landing"
})

mcp0_take_screenshot({
  filePath: "renders/render-desktop-2560.png",
  fullPage: true
})
```

### Step 7: Visual-to-Code Loop（迭代）

按 `visual-to-code-loop.md` 做 diff：

**第一轮 diff 结果可能是**：
- ✅ 整体调子对（warm editorial vibe）
- ⚠️ Hero 字号偏小（mockup 72px, render 64px — CSS 没覆盖 shadcn 默认）
- ⚠️ Trust bar 间距太密（mockup 80px gap, render 40px）
- ⚠️ Terracotta accent 偏橙（色值需微调）

**LLM 改代码**：
```
修改 src/app/landing/page.tsx:
- Hero headline: text-5xl → text-7xl (72px)
- Trust bar: gap-10 → gap-20
- --color-accent: oklch(0.60 0.20 30) → oklch(0.58 0.19 28)
其他保持不变
```

**重新 chrome-devtools 截图 → 再 diff**。

收敛后进入 Step 8。

### Step 8: Playwright 多 viewport 验证

```typescript
mcp6_browser_navigate({ url: "http://localhost:3000/landing" })

// 桌面
mcp6_browser_resize({ width: 1440, height: 900 })
mcp6_browser_take_screenshot({ filename: "renders/render-desktop-1440.png" })

// 平板
mcp6_browser_resize({ width: 768, height: 1024 })
mcp6_browser_take_screenshot({ filename: "renders/render-tablet.png" })

// 手机
mcp6_browser_resize({ width: 375, height: 812 })
mcp6_browser_take_screenshot({ filename: "renders/render-mobile.png" })

// 暗色模式
mcp6_browser_evaluate({
  function: "() => document.documentElement.classList.add('dark')"
})
mcp6_browser_take_screenshot({ filename: "renders/render-dark.png" })
```

### Step 9: Lighthouse audit

```typescript
mcp0_lighthouse_audit({
  device: "desktop",
  mode: "navigation",
  outputDirPath: "reports/"
})
```

目标分数：
- Performance: ≥ 90
- Accessibility: ≥ 95 (必须)
- Best Practices: ≥ 95
- SEO: ≥ 90

**a11y 不达标必须修**（对比度、语义 HTML、alt 属性等）。

### Step 10: 交付 6 件套

```
my-landing/
├── design/
│   ├── mockup-v1-high.png         # 设计意图锚点
│   ├── extracted-tokens.md        # 从 mockup 提取的 tokens
│   └── design-decisions.md        # 决策日志
├── src/
│   ├── app/
│   │   ├── globals.css            # oklch + CSS variables
│   │   └── landing/page.tsx       # 终版代码
│   └── components/
│       ├── ui/ (shadcn)           # 真组件
│       └── brand-icons.tsx        # 真 logo SVG
├── renders/
│   ├── render-desktop-2560.png
│   ├── render-desktop-1440.png
│   ├── render-tablet.png
│   ├── render-mobile.png
│   └── render-dark.png
├── reports/
│   └── lighthouse-report.json     # 性能 + a11y 报告
└── NOTES.md                       # 完整决策日志
```

---

## 💰 成本和时间总计

| 项 | 花费 |
|---|---|
| image-2 用量（已有 mockup） | $0 |
| MCP 工具调用 | $0 |
| LLM 生成/迭代代码 | 约 4 轮 iteration |
| 人工时间 | 约 45 分钟 |
| **总 API 成本** | **~$0**（图已在 Mode A 生了） |

---

## 🆚 对比 ConardLi

| 环节 | ConardLi | Mode B |
|---|---|---|
| 提取 tokens | 靠 AI 看代码/截图猜 | 看 **image-2 mockup** 精确提取 |
| 组件来源 | AI 手写 | **shadcn MCP 真组件** |
| API 最新写法 | 训练数据 | **context7 MCP 最新文档** |
| Logo | placeholder 或 AI 编 | **logo_search MCP 真 SVG** |
| 渲染验证 | 人开浏览器看 | **chrome-devtools 自动截图** |
| 多设备 | CSS 信仰 | **playwright 真实截图** |
| a11y | 忽略或粗验 | **lighthouse MCP 强制 audit** |
| diff 迭代 | 靠语言描述 | **mockup vs render 视觉 diff** |

**核心差异**：Mode B 的代码是**"可证伪"的**—— 有 6 件套证据。
ConardLi 的代码是**"看起来 OK"的**—— 只能主观判断。

---

## 🚨 Mode B 容易踩的坑

### 坑 1：看图生代码时，AI 自动 "improve" 设计

LLM 可能说"我改进了一下布局，加了..."。**必须明确禁止**：

```
严格遵循 mockup，不要"改进"或"补全"任何元素。
mockup 里没有的就是没有。不确定时 ASK USER。
```

### 坑 2：shadcn 组件默认样式覆盖你的 tokens

shadcn 的 Button 默认用 `bg-primary`，你必须在 globals.css 里把 `--primary` 设成你的 oklch 色。

### 坑 3：image-2 画的效果代码实现不了

image-2 可以画出 blur + blend-mode 堆叠的复杂效果，但代码 1:1 还原很难。

**防御**：diff 时，**优先还原大骨架（70% 权重），细节效果降级可接受**。把"实现不了的 design intent"记录在 NOTES.md。

### 坑 4：Logo 商用风险

`logo_search` 抓的是 AI 整理的公开 SVG 数据库，**商用前必须确认品牌授权**。mockup 演示 OK，正式上线前替换成真正授权的。
