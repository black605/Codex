---
title: INTP Way · 三位一体 UI 生成系统
role: 中枢文件 · 决策架构
source:
  - 整合 Anthropic Cookbook + ConardLi web-design-skill + 自研 MCP 工具链
  - 独家能力：image-2 直接生图 + MCP 真素材 + 完整 prompt 工程
---

# INTP Way · 三位一体 UI 生成系统

> **战略定位**：
> ConardLi 的 `web-design-skill` 做的是**单模态代码生成**（一个 LLM → HTML/CSS）。
> 我们做的是**跨模态闭环**（image-2 + MCP + prompt 工程 → 视觉 × 真素材 × 代码 × 渲染验证）。
>
> ConardLi 能跟上 Claude Design，我们**超过**它。

---

## 🧭 INTP Way 核心哲学

> **INTP 特质**：系统架构师思维、跨领域连接、深度理性、原创 > 模仿。

应用到 UI 生成：

1. **架构优先**：先设计"能力配合的拓扑"，再决定具体 prompt
2. **跨模态贯通**：视觉 / 真素材 / 代码 / 渲染 **互相印证**
3. **决策可追溯**：每个字体/色彩/布局选择都能解释**为什么**
4. **不重复造轮子**：所有能拿真的就拿真的（MCP），能生成的才生成

---

## 🏛 我们的三大能力柱（Triforce）

```
           ┌──────────────────────┐
           │  能力 3: Prompt 工程  │
           │  (思维层 · 决策粘合剂) │
           │  ai-image-frontend-ui │
           │  ai-image-bypass      │
           └──────────┬───────────┘
                      │
         ┌────────────┴────────────┐
         ↓                         ↓
┌──────────────────┐   ┌──────────────────┐
│  能力 1: image-2 │   │  能力 2: MCP     │
│  (视觉层 · 保真度) │   │  (真实层 · 闭环)  │
│  gpt-image-2     │   │  shadcn          │
│  grok-image      │   │  21st-magic      │
│  4K 直接出图      │   │  chrome-devtools │
│                  │   │  playwright      │
│                  │   │  context7        │
└──────────────────┘   └──────────────────┘
```

### 能力 1：image-2 直接生图 ⭐ 我们独有

| 长板 | 短板 |
|---|---|
| ✅ 高保真视觉（4K）| ❌ 不可交互 |
| ✅ 字体渲染业界第一 | ❌ 无法真实数据驱动 |
| ✅ 快速探索 N 个方向 | ❌ 无法响应 viewport 变化 |
| ✅ 一图抵千言（设计评审） | ❌ 无法嵌入真实代码库 |

**核心用法**：**视觉决策**，不是"最终产品"。
ConardLi 的 v0 Draft 只能用文字描述（"Here's the color palette..."）。
我们的 v0 是**真的一张图**，用户一眼看懂方向对不对。

### 能力 2：MCP 工具链 ⭐ 我们独有

Windsurf 挂的 MCP 都能为 UI 场景所用：

| MCP | 在 UI 场景的用法 |
|---|---|
| **`shadcn`** | 查组件库、生成 `npx shadcn add` 命令、看真实组件代码 |
| **`magic-21st`** | `21st_magic_component_builder` 生成新组件、`logo_search` 拿真品牌 SVG |
| **`chrome-devtools`** | 代码渲染后真实截屏、性能 audit、无障碍 lighthouse |
| **`playwright`** | 自动化交互验证、多设备截图、DOM 检查 |
| **`context7`** | 查最新 Tailwind / React / 任意库的官方文档 |
| **`postgres-nous` + `redis-nous`** | 拿真实数据给 dashboard 演示用 |

**核心用法**：**消灭 placeholder**。prompt 里只要能被"真东西"替代的 placeholder，都应该用 MCP 抓真东西。

### 能力 3：Prompt 工程（我们已积累的）

| 资源 | 价值 |
|---|---|
| `anti-slop-rules.md` | 反 AI slop 6 大维度规则 |
| `aesthetic-families.md` | 9 大美学家族 + 品牌色 |
| `placeholder-philosophy.md` | 6 种 placeholder 场景 |
| `claude-design-workflow.md` | 6 步工作流 |
| `design-tokens.md` | oklch + 4 个 pre-validated 配对 |

**核心用法**：**决策粘合剂**。三能力能否配合好，全靠 prompt 工程做"关节"。

---

## 🔄 三位一体闭环（核心创新）

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│  [1] 需求                                                   │
│   │                                                        │
│   ↓                                                        │
│  [2] Prompt Declare Design System (能力 3)                  │
│   │    ├─ 选家族 → aesthetic-families.md                    │
│   │    ├─ 写 design tokens (oklch)                         │
│   │    └─ 列 placeholders                                   │
│   ↓                                                        │
│  [3] image-2 出 v0 Draft (能力 1)                           │
│   │    低质 + 1024×1024 ($0.01)                           │
│   │    用户看图 → 确认方向                                   │
│   ↓                                                        │
│  [4] MCP 采集真素材 (能力 2)                                 │
│   │    ├─ logo_search → 真品牌 logo (SVG)                  │
│   │    ├─ shadcn → 真组件代码                               │
│   │    └─ context7 → 最新 API 文档                          │
│   ↓                                                        │
│  [5] image-2 出 v1 Final (能力 1)                           │
│   │    高质 + 2K ($0.22)                                   │
│   │    含真 logo placeholder 位置                           │
│   ↓                                                        │
│  [6] 代码生成 (能力 3 + 外部 LLM)                             │
│   │    参考 v1 图像 + MCP 组件                                │
│   ↓                                                        │
│  [7] MCP 渲染验证 (能力 2)                                   │
│   │    ├─ chrome-devtools: 实际 DOM 截图                    │
│   │    ├─ playwright: 多 viewport / 交互测试                │
│   │    └─ lighthouse: a11y + 性能                          │
│   ↓                                                        │
│  [8] 跨模态对比                                              │
│   │    image-2 mockup ↔ chrome-devtools screenshot         │
│   │    diff 差异 → 定位代码 bug                             │
│   ↓                                                        │
│  [9] 迭代或交付                                              │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**ConardLi 能做的阶段**：[1][2][6]
**我们能做的阶段**：[1]-[9] 全链路

---

## 🎯 三种"能力配比"模式

不同场景用不同的能力配比。**均衡不是三者各占 1/3，而是按任务性质动态分配**。

### 模式 A：探索模式（用户只有模糊想法）

```
能力配比：image-2 50% + Prompt 30% + MCP 20%
```

**使用时机**：
- "做个 SaaS 产品的 landing page"
- "给我看看几种风格的 dashboard"
- "我想画个 AI 产品海报"

**工作流**：
1. Prompt 工程 declare 3 个候选 design system（不同家族）
2. **image-2 批量出 3-5 张 v0**（low 质，约 $0.05）
3. 用户选方向后，MCP 补真 logo、真组件参考
4. image-2 再出 v1 高质终版

**关键动作**：
```powershell
# 批量探索（关键！）
foreach ($family in @("warm-editorial", "data-dense", "cinematic-dark")) {
    .\gen-image.ps1 -PromptFile "prompts/explore-$family.txt" `
                    -Size "1024x1024" -Quality low
}
```

### 模式 B：落地模式（用户有视觉稿要代码）

```
能力配比：MCP 50% + Prompt 30% + image-2 20%
```

**使用时机**：
- "把这张设计稿变成 React"
- "用 shadcn 实现这个 dashboard"
- "这个 Figma 给我做出来"

**工作流**：
1. Prompt 工程：从视觉稿提取 design tokens（oklch + 字体 + 间距）
2. **MCP 查 shadcn 组件**：对应每个 UI 元素找真组件
3. MCP 查 context7：用最新的 Tailwind/React API
4. LLM 生代码 → **chrome-devtools MCP 渲染截图**
5. image-2 把原稿和 chrome-devtools 截图拼在一张对比图里，做 diff

**关键动作**：
```
# MCP 查组件时明确要用生产级真代码
@shadcn/card + @shadcn/table + @shadcn/button
用 mcp10_get_add_command_for_items 生成 npx 命令
```

### 模式 C：验证模式（用户有代码要迭代）

```
能力配比：MCP 60% + image-2 20% + Prompt 20%
```

**使用时机**：
- "为什么我这个 UI 看着 AI 味那么重？"
- "看看我这网站能不能改得更精致"
- "检查下这个页面有没有 AI slop"

**工作流**：
1. **Playwright MCP 访问用户网站** → 截图
2. **chrome-devtools MCP lighthouse audit** → 性能 + a11y 数据
3. Prompt 工程用 `anti-slop-rules.md` 的 checklist 对截图做**AI slop 诊断**
4. image-2 画"修好后"的对比图
5. 生成具体修改清单（哪里改、改成什么、为什么）

**关键动作**：
```
mcp6_browser_navigate(url) → browser_take_screenshot
→ 对照 anti-slop-rules.md 逐条打分
→ image-2 画"修后版本"
→ 列出具体代码改动
```

---

## 🧬 INTP 原则 1：Placeholder → 真素材的升级路径

ConardLi 的 placeholder 哲学教我们**不要编造**。
INTP 升级：**不仅不编造，还能通过 MCP 自动替换成真东西**。

| Placeholder 类型 | ConardLi 做法 | INTP 做法（升级） |
|---|---|---|
| `[Logo]` 灰色几何 | 留着让用户手动替换 | **`mcp4_logo_search`** 直接抓真品牌 SVG |
| `[icon]` 方框 | 留着让用户手动替换 | **`mcp10_view_items_in_registries`** 查 Lucide / shadcn icons |
| `[组件]` 标记 | 留着 | **`mcp10_get_item_examples_from_registries`** 拿真组件代码 |
| `[API 数据]` 占位 | 编示例 | **`mcp7_pg_execute_query`** 从真库拿 demo 数据 |
| `[最新 React 用法]` | 用训练数据里的 | **`mcp3_query-docs`** 查 React 官方最新文档 |

**INTP 口号**：
> Placeholder is not the end — it's the **slot for MCP to fill in reality**.

---

## 🎨 INTP 原则 2：视觉 ↔ 代码 双模态验证

单一 LLM 最大的盲点：**设计意图 vs 实际渲染的差异**。

传统流程：
```
设计师的脑中意图 → LLM 代码 → 代码运行 → 谁检查和意图是否一致？
```

INTP 流程：
```
设计师的意图 → image-2 生 v1 视觉稿（锚定意图）
           ↓
         LLM 代码 → chrome-devtools 截图（锚定实现）
           ↓
       image-2 拼图对比 → 跨模态 diff
           ↓
       LLM 改代码 → 重新 diff → 收敛
```

### 具体实现

```powershell
# Step 1: 生 mockup（意图锚点）
.\gen-image.ps1 -PromptFile mockup.txt -Size "1536x1024" -Quality high `
                -OutPath mockup-intent.png

# Step 2: MCP 渲染真代码
# (在 Windsurf 里)
mcp0_navigate_page(url="file:///path/to/generated.html")
mcp0_take_screenshot(filePath="rendered-actual.png", fullPage=true)

# Step 3: 视觉对比（人眼 + image-2 辅助）
# 可以做 side-by-side 拼图，或 overlay diff
```

**关键点**：每次代码改动后都做 step 2 + 3，**直到渲染图和 mockup 收敛**。

---

## 🧮 INTP 原则 3：决策可追溯表

每个 UI 生成任务维护一份**决策日志**（放项目的 `NOTES.md`）：

```markdown
# UI Generation Notes — {项目名}

## 需求
{用户原始需求}

## 决策表（每一条都可追溯到 skill 文件）

| 决策 | 选择 | 依据文件 | 替代方案 |
|---|---|---|---|
| 美学家族 | Warm Editorial | aesthetic-families.md · 家族 3 | 也考虑过 Editorial Minimalism |
| 主色 | oklch(0.35 0.10 30) warm brown | design-tokens.md · 配对 1 | 未选 Premium Brand 因为品牌非奢 |
| Display 字体 | Tiempos Headline character | design-tokens.md · 推荐字体 | 未选 Canela 因为过于 fashion |
| 字体避开 | Inter/Roboto/Fraunces/system-ui | anti-slop-rules.md · 硬规则 | — |
| Trust bar | abstract geometric placeholders | templates/landing-page.txt 修正版 | 下一步用 logo_search MCP 替真 logo |
| v0 参数 | 1024×1024 low | claude-design-workflow.md · Step 4 | — |
| v1 参数 | 1536×1024 high | 按 dimensions-and-pricing.md · landing 推荐 | — |

## MCP 使用日志
- [ ] logo_search 抓 trust bar 的真品牌 logo
- [ ] shadcn 查 Card/Button 组件
- [ ] chrome-devtools 渲染后对比

## 迭代历史
- v0 (14:32): 3 张家族对比图，用户选 Warm Editorial
- v1 (14:45): 高质终版，用户反馈 trust bar 太平
- v2 (15:10): 用 logo_search 替 3 个真品牌 logo
```

**这份日志的价值**：
- 用户能看到"为什么每个决策是这样"
- 后续维护能知道"改动时哪些约束必须保持"
- AI 自己可以反向阅读，保持设计一致性

---

## 🚀 INTP Way 快速上手（对比 ConardLi）

### ConardLi 的 quick start
```
1. Copy skill → .claude/skills/
2. Ask AI to design
3. AI writes HTML
4. Done
```

### INTP Way 的 quick start
```
Phase 1 · 探索（5 分钟）
  [Prompt] declare 候选 design system
  [image-2] 批量出 v0（low 质）
  [人] 选方向

Phase 2 · 充实（10 分钟）
  [MCP logo_search] 抓真 logo
  [MCP shadcn] 挑真组件
  [MCP context7] 查最新 API
  [Prompt] 整合 design tokens

Phase 3 · 生成（20 分钟）
  [image-2] 出 v1 高质终版（作为意图锚点）
  [LLM + MCP 组件] 生代码
  [MCP chrome-devtools] 实时渲染截图

Phase 4 · 验证（5 分钟）
  [人] 对比 image-2 意图 vs chrome-devtools 实现
  [MCP lighthouse] a11y + 性能检查
  [Prompt anti-slop checklist] 逐条过

Phase 5 · 交付
  [NOTES.md] 决策日志
  代码 + 渲染图 + 意图图三件套
```

**结果**：不仅代码好看，**整个产出有设计依据可追溯**，用户有完整的"为什么这样"答案。

---

## 🎯 相关文件导航

### 核心（INTP Way 独有）
- `intp-triforce.md` ⭐（本文件）—— 三位一体哲学 + 闭环工作流
- `mcp-toolkit.md` —— MCP 工具详细用法（在 UI 场景的每一个）
- `visual-to-code-loop.md` —— image-2 ↔ 代码的反馈循环实操

### Playbooks（三种模式的端到端案例）
- `playbooks/mode-a-explore.md` —— 探索模式案例
- `playbooks/mode-b-ship.md` —— 落地模式案例
- `playbooks/mode-c-audit.md` —— 验证模式案例

### 底层资源（跨模式通用）
- `anti-slop-rules.md` —— 反 AI slop 规则
- `aesthetic-families.md` —— 9 大美学家族
- `placeholder-philosophy.md` —— placeholder 框架
- `design-tokens.md` —— oklch + 字体 + 配对表
- `claude-design-workflow.md` —— 6 步基础流程
- `prompt-fundamentals.md` —— 底层 prompt 规则
- `5-slot-template.md` —— 通用模板骨架
- `templates/*.txt` —— 场景模板库

---

## 🏆 We're not copying ConardLi. We're transcending it.

| 维度 | ConardLi web-design-skill | INTP Way (ours) |
|---|---|---|
| 输出 | HTML/CSS/JS 代码 | 代码 + 视觉意图图 + 真素材 + 验证报告 |
| 反 slop | 规则清单 | 规则清单 + MCP 实时检测 + image-2 对比 |
| Placeholder | 人工手动替换 | MCP 自动补真素材 |
| 验证 | 人眼看浏览器 | chrome-devtools + playwright + 跨模态 diff |
| 决策 | 口头解释 | 结构化 NOTES.md 决策日志 |
| 单模态 | ❌ 只有 LLM | ✅ 图 + 文 + 数据 + 渲染 |
| 端到端 | ❌ 只覆盖 [2][6] | ✅ 覆盖 [1]-[9] |

**ConardLi**：给你一把更好的锤子。
**INTP Way**：给你一整个工坊。
