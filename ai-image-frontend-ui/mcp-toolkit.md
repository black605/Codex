---
title: MCP Toolkit · UI 场景的 MCP 工具箱
role: 工具参考手册
parent: intp-triforce.md
---

# MCP Toolkit · UI 场景的 MCP 工具箱

> **为什么这个文件关键**：
> ConardLi 做不了 MCP，所以他只能生成"看起来合理"的 placeholder。
> 我们有 MCP，**所有 placeholder 都可以被真实素材替代**。
>
> 这就是为什么我们的 UI 生成**在"真实性"这一维上碾压 ConardLi**。

---

## 🧭 快速查询表：我想要…

| 我想要 | 用哪个 MCP tool | 产出 |
|---|---|---|
| **真品牌 logo** (GitHub/Discord/etc) | `mcp4_logo_search` | JSX/TSX/SVG |
| **真 UI 组件** (Button/Card/etc) | `mcp10_get_item_examples_from_registries` | shadcn 组件代码 |
| **添加组件到项目** | `mcp10_get_add_command_for_items` | `npx shadcn add button` |
| **查最新 React/Tailwind 用法** | `mcp3_query-docs` | 最新官方文档 |
| **页面渲染截图** | `mcp0_take_screenshot` + `mcp0_navigate_page` | PNG |
| **多设备测试截图** | `mcp6_browser_resize` + `mcp6_browser_take_screenshot` | 多尺寸 PNG |
| **a11y + 性能 audit** | `mcp0_lighthouse_audit` | JSON 报告 |
| **真实用户数据** (给 dashboard demo) | `mcp7_pg_execute_query` | 查询结果 |
| **新 UI 组件灵感** | `mcp4_21st_magic_component_inspiration` | 21st.dev 组件 |
| **基于需求生成组件** | `mcp4_21st_magic_component_builder` | React 组件代码 |
| **改进现有组件** | `mcp4_21st_magic_component_refiner` | 优化后代码 |

---

## 🏛 1. `mcp4_logo_search` · 真品牌 Logo 搜索

**最直接解决"trust bar 假 logo"痛点的工具**。

### 基本用法
```typescript
mcp4_logo_search({
  queries: ["github", "vercel", "stripe", "notion", "linear"],
  format: "TSX"  // 或 "JSX" / "SVG"
})
```

### 返回内容
每个 logo 给你：
- Component name（如 `GitHubIcon`）
- 完整组件代码（SVG 嵌入）
- Import 方式

### 在 UI 场景的用法

**场景 A：Trust bar（客户 logo 墙）**
```typescript
// 步骤 1: 拿真 logo
const logos = mcp4_logo_search({
  queries: ["github", "vercel", "stripe", "figma", "notion", "linear"],
  format: "SVG"
})

// 步骤 2: 在 React 里拼成 trust bar
<div className="trust-bar">
  <p className="text-xs uppercase tracking-wider text-gray-500">
    Trusted by teams at
  </p>
  <div className="flex gap-16 items-center grayscale opacity-60">
    {logos.map(logo => <logo.Component key={logo.name} className="h-8" />)}
  </div>
</div>
```

**场景 B：集成页（"Works with…"）**
展示"我们支持哪些集成"的区域，直接用真 logo 比 "Connect to Slack / GitHub / Jira" 文字更有说服力。

### 🚫 ConardLi 做不到这个
他只能说"use placeholder geometric shapes"。我们可以**直接放真 logo**，但明确规定"这是 AI 抓来的公开 SVG，商用前请确认品牌授权"。

---

## 🎨 2. `mcp10_*` (shadcn) · 真 UI 组件库

**所有 UI 的"真实代码"来源**。不要让 AI 手写 Button 了，直接用 shadcn。

### 四个关键工具

| Tool | 用途 |
|---|---|
| `mcp10_list_items_in_registries` | 列出所有可用组件 |
| `mcp10_search_items_in_registries` | 模糊搜组件（"表单"、"dialog"、"表格"） |
| `mcp10_view_items_in_registries` | 看具体组件的完整代码 |
| `mcp10_get_item_examples_from_registries` | 看组件的用法示例 |
| `mcp10_get_add_command_for_items` | 生成 `npx shadcn add xxx` 命令 |

### 典型工作流

```
用户需求：做一个带排序的用户管理表格

Step 1: 搜有什么表格组件
mcp10_search_items_in_registries({
  registries: ["@shadcn"],
  query: "data table"
})
→ 返回 [@shadcn/table, @shadcn/data-table, @shadcn/data-table-demo]

Step 2: 看具体代码和用法
mcp10_view_items_in_registries({
  items: ["@shadcn/data-table"]
})
mcp10_get_item_examples_from_registries({
  registries: ["@shadcn"],
  query: "data-table-demo"
})
→ 返回完整的 TanStack Table 集成示例

Step 3: 生成安装命令
mcp10_get_add_command_for_items({
  items: ["@shadcn/data-table", "@shadcn/table", "@shadcn/button"]
})
→ 返回 "npx shadcn@latest add data-table table button"

Step 4: 用户跑这个命令 → 真组件进项目
```

### INTP 升级：用 shadcn 做 image-2 的"字体参考"

image-2 不知道你项目里用了什么字体。但你可以在 prompt 里描述：
```
Typography: uses the font stack configured in this project's 
shadcn/ui setup — specifically Geist Sans (variable font) for 
display and body, JetBrains Mono for code.
```

这样生成的 image-2 mockup 会和真实渲染更接近。

---

## 🌐 3. `mcp3_*` (context7) · 最新文档查询

**AI 训练数据 cutoff 问题的解药**。

### 用法
```typescript
// Step 1: 解析库 ID
mcp3_resolve-library-id({
  libraryName: "Tailwind CSS",
  query: "最新的 4.0 语法有什么变化"
})
→ "/tailwindlabs/tailwindcss/v4.0.0"

// Step 2: 查文档
mcp3_query-docs({
  libraryId: "/tailwindlabs/tailwindcss/v4.0.0",
  query: "oklch color syntax in arbitrary values"
})
→ 最新官方文档片段
```

### 在 UI 场景的用法

**场景 A：用最新 Tailwind**
问：`"Tailwind CSS v4 里 oklch() 怎么在 arbitrary values 里写"`
→ 拿到最新写法，不会写出过时的 `bg-[oklch(...)]` 不兼容版本

**场景 B：shadcn/ui 最新组件 API**
问：`"shadcn DataTable 2026 最新版的 sorting API"`
→ 直接拿最新 filter/sort 写法

**场景 C：React 19 hooks**
问：`"React 19 useActionState 新用法"`
→ 不会给你 deprecated useFormState

### INTP 原则
> **每次写新代码前，对核心 API 先 `context7 query-docs` 一下**。
> 50% 的 AI 生成 bug 来自训练数据 cutoff。

---

## 🖥 4. `mcp0_*` (chrome-devtools) · 真实渲染 + Lighthouse

**把"生成的 HTML"变成"真的可验证"的关键工具**。

### 核心工具

| Tool | 用途 |
|---|---|
| `mcp0_navigate_page` | 加载 HTML 文件或 URL |
| `mcp0_take_screenshot` | 截图（支持 fullPage） |
| `mcp0_take_snapshot` | 拿 a11y tree（比截图更准） |
| `mcp0_lighthouse_audit` | 性能 + a11y + SEO + best practices |
| `mcp0_performance_start_trace` | 性能 trace（LCP, CLS, INP） |
| `mcp0_emulate` | 模拟设备（viewport / CPU throttle / network） |

### INTP 工作流：代码 → 渲染 → 对比 image-2 意图

```
Step 1: 你写了一个 Landing.html
Step 2: mcp0_navigate_page({ type: "url", url: "file:///.../Landing.html" })
Step 3: mcp0_take_screenshot({ 
          filePath: "actual-render.png", 
          fullPage: true 
        })
Step 4: 对比之前 image-2 出的 mockup-intent.png
Step 5: 差异大的地方 → 改代码 → 回到 Step 2
```

### Lighthouse 在 UI 场景的用法

```
mcp0_lighthouse_audit({
  device: "desktop",
  mode: "navigation"
})
```

返回 a11y / SEO / best practices 评分。**任何 UI 交付前必跑一遍**，确保：
- 对比度达到 AAA
- 没有缺失的 alt 属性
- 没有 console error

### INTP 原则：代码 → 渲染 → 截图 进 `NOTES.md`

每次交付都带上 chrome-devtools 的实际渲染截图，这样用户看到的是**真实渲染**，不是"AI 以为的渲染"。

---

## 🧪 5. `mcp6_*` (playwright) · 自动化交互测试

**测试交互、多设备响应、复杂流程的首选**。

### 核心工具

| Tool | 用途 |
|---|---|
| `mcp6_browser_navigate` | 加载页面 |
| `mcp6_browser_resize` | 改 viewport 尺寸 |
| `mcp6_browser_snapshot` | 拿 a11y tree |
| `mcp6_browser_take_screenshot` | 截图 |
| `mcp6_browser_click` + `mcp6_browser_fill_form` | 模拟用户操作 |

### 典型 UI 验证流程

```
# 验证响应式
for viewport in [[375, 667], [768, 1024], [1440, 900], [2560, 1440]]:
    mcp6_browser_resize(*viewport)
    mcp6_browser_take_screenshot(f"landing-{viewport[0]}x{viewport[1]}.png")

# 验证暗色模式
mcp6_browser_navigate("...")
mcp6_browser_evaluate("() => document.documentElement.classList.add('dark')")
mcp6_browser_take_screenshot("landing-dark.png")

# 验证交互流
mcp6_browser_click({ ref: "[login-button-ref]" })
mcp6_browser_snapshot()  # 看登录表单是否出现
```

### INTP 升级：3 套截图都要交付

**每个 UI 交付打包里必须有**：
- `mockup-intent.png` — image-2 生的设计意图图（2K）
- `render-desktop-2560.png` — chrome-devtools 桌面渲染
- `render-mobile-375.png` — playwright 移动渲染
- `render-dark-mode.png` — playwright 暗色模式渲染
- `lighthouse-report.json` — 性能 + a11y 数据

**只有这些都齐了才算交付完成**。

---

## 🎨 6. `mcp4_21st_magic_*` · UI 组件灵感 + 生成

shadcn 覆盖不到的组件，用 21st.dev 找灵感。

### 三个工具

| Tool | 用途 |
|---|---|
| `mcp4_21st_magic_component_inspiration` | 搜 21st.dev 上的组件设计灵感 |
| `mcp4_21st_magic_component_builder` | 基于需求直接生成 React 组件 |
| `mcp4_21st_magic_component_refiner` | 改进现有组件的 UI |

### 典型用法

```typescript
// 需要一个特别的 pricing card 设计
mcp4_21st_magic_component_inspiration({
  searchQuery: "pricing card animated",
  message: "需要一个有动画效果的定价卡片"
})
→ 返回 21st.dev 上的几个参考组件

// 或直接生成
mcp4_21st_magic_component_builder({
  searchQuery: "hero section brutalist",
  message: "做一个 brutalist 风格的 hero 区",
  ...
})
→ 返回完整组件代码
```

### INTP 用法：image-2 → 21st.dev → 具体实现

```
Step 1: image-2 出一个 pricing 区的 mockup
Step 2: 用 mockup 描述去 21st_magic_component_inspiration 搜类似组件
Step 3: 用 21st_magic_component_builder 基于需求生成接近 mockup 的代码
Step 4: chrome-devtools 渲染对比
Step 5: 用 21st_magic_component_refiner 迭代改进
```

---

## 💾 7. `mcp7_*` / `mcp9_*` (数据库) · 真数据驱动 demo

做 dashboard / 数据可视化 demo 时，**别编假数据**——直接查真的。

### 适用场景
- 给 nous 项目做管理后台 demo → 直接查 `postgres-nous`
- 做缓存监控 UI → 直接查 `redis-nous`
- 展示 "live demo with real data" 时的最佳证据

### 示例

```typescript
// dashboard KPI 卡要"本月活跃用户数"
mcp7_pg_execute_query({
  operation: "count",
  query: "SELECT COUNT(DISTINCT user_id) FROM sessions WHERE created_at > NOW() - INTERVAL '30 days'"
})
→ 拿到真数字，比 "12,483" 有说服力

// 折线图要"过去 30 天每日活跃"
mcp7_pg_execute_query({
  operation: "select",
  query: `SELECT DATE(created_at) as day, COUNT(DISTINCT user_id) as dau
          FROM sessions 
          WHERE created_at > NOW() - INTERVAL '30 days'
          GROUP BY day ORDER BY day`
})
→ 真正的增长曲线
```

---

## 🧬 8. MCP 组合拳：完整 UI Task Playbook

### Playbook: "做个 SaaS Landing Page"

```
⬇️ 阶段 1：探索（能力 1 + 3）
1. [Prompt] 读 aesthetic-families.md，选 2 个候选家族
2. [image-2] 批量出 4 张 v0（2 家族 × 2 布局方案）
3. [人] 选方向

⬇️ 阶段 2：采集真素材（能力 2）
4. [MCP logo_search] 抓 trust bar 需要的 6 个真 logo
5. [MCP shadcn search] 查 Hero/Card/Button 可用组件
6. [MCP context7] 查最新 Tailwind v4 + Geist 字体用法

⬇️ 阶段 3：终稿 mockup（能力 1）
7. [image-2] 出 v1 高质 2K，trust bar 位置用真 logo 的几何占位

⬇️ 阶段 4：代码生成（能力 2 + 3）
8. [Prompt + shadcn 代码] LLM 写 React 代码
9. [MCP 用刚拿的 logo SVG] 替换 trust bar

⬇️ 阶段 5：跨模态验证（能力 2）
10. [MCP chrome-devtools] 渲染截图
11. [MCP playwright] 多 viewport 截图 + 暗色模式
12. [MCP lighthouse] a11y + 性能 audit
13. [人] 对比 v1 mockup 和实际渲染，差异大处回到 step 8

⬇️ 阶段 6：交付
14. 代码 + mockup.png + render-desktop.png + render-mobile.png 
    + lighthouse.json + NOTES.md（决策日志）
```

**ConardLi 能做**：3 (的 prompt 部分)、8
**我们能做**：1-14 全部

---

## 🎯 快速引用片段

### 片段 1：在 prompt 里声明 MCP 能力

放到 `claude-design-workflow.md` 里的 Step 3（Declare Design System）：

```markdown
Design Decisions:
- Aesthetic family: Warm Editorial
- Colors: oklch-based, derived from brand terracotta
- Typography: Tiempos Headline + Geist Body (via shadcn)
- Real assets sources:
  - Trust bar logos → mcp4_logo_search
  - Hero components → @shadcn/card, @shadcn/button
  - Latest Tailwind syntax → context7 /tailwindlabs/tailwindcss/v4
- Placeholder policy:
  - Logos: USE real (logo_search), NOT fabricated
  - Data: USE real (postgres-nous if available), NOT hardcoded
  - Copy: placeholder ONLY if user hasn't provided
- Validation:
  - chrome-devtools screenshot vs image-2 mockup diff
  - lighthouse score > 95 for a11y
  - playwright multi-viewport check
```

### 片段 2：NOTES.md 模板升级版

```markdown
# UI Generation Notes — {Project}

## 决策表（含 MCP 使用）
| 决策 | 选择 | 依据 | MCP 工具 |
|---|---|---|---|
| 真 logo | GitHub / Vercel / Stripe | brand_list.md | mcp4_logo_search ✅ |
| Hero 组件 | shadcn/hero-section | 现代 landing 标配 | mcp10_view_items ✅ |
| 数据 | 真实 DAU 曲线 | 客户要"live demo" | mcp7_pg_query ✅ |
| 字体 | Geist Sans | Anthropic 刚开源 | context7 /vercel/geist ✅ |

## 交付清单
- [ ] mockup-intent.png（image-2 设计意图）
- [ ] render-desktop-2560.png（chrome-devtools）
- [ ] render-mobile-375.png（playwright）
- [ ] render-dark.png（playwright dark mode）
- [ ] lighthouse-report.json（MCP audit）
- [ ] code.tsx（React 源码）
- [ ] NOTES.md（本文件）
```

---

## 🏆 MCP 使用哲学

> **Placeholder 是 MCP 填真的"接口"。**
>
> 每次写 placeholder 时问自己：**"这个能用 MCP 拿真的吗？"**
>
> - `[Logo]` → `mcp4_logo_search` 可以拿真的 ✅ 必须
> - `[Component]` → `mcp10_view_items` 可以拿真的 ✅ 必须
> - `[Data]` → `mcp7_pg_query` 可以拿真的（本项目数据库） ✅ 必须
> - `[Latest API]` → `mcp3_query-docs` 可以拿真的 ✅ 必须
> - `[User photo]` → 真人脸有隐私风险 ❌ 继续用字母首字母占位
> - `[Company testimonial]` → 涉及商誉虚构 ❌ 继续用 placeholder
>
> **能拿真的就拿真的，不能拿的才用 placeholder 标记。**
