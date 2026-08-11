---
name: ai-image-frontend-ui
description: |
  INTP Way · 三位一体 UI 生成系统—— 用 **image-2 直接生图 + MCP 工具链 + 完整 prompt 工程** 
  打造跨模态闭环，生成前端 UI 截图、Web 界面、移动 app 屏幕、海报、Dashboard、设计系统、Landing page。
  
  融合权威来源：OpenAI Cookbook + fal.ai Anti-slop + Anthropic 官方反 AI slop 规则
  + 泄露的 Claude Design 内部工作流 + ConardLi web-design-skill + 9 大美学家族。
  
  独有能力（ConardLi 做不到）：image-2 视觉意图锚点 + MCP 真素材采集 + 跨模态验证闭环。
tier: 2
tags: [ai-image, gpt-image-2, frontend, ui-mockup, anti-slop, claude-design, mcp, triforce, intp-way]
source:
  - OpenAI Cookbook GPT Image 2 prompting guide
  - fal.ai GPT Image 2 Prompting Guide
  - Anthropic 《Prompting for Frontend Aesthetics》(platform.claude.com/cookbook)
  - 泄露的 Claude Design system prompt (CL4R1T4S/ANTHROPIC)
  - ConardLi/web-design-skill (Declare DS + v0 draft + oklch + placeholder)
  - awesome-claude-design 9 大美学家族
  - linux.do/t/topic/1189324 UI Prompt 模板库
created: 2026-04-23
updated: "2026-04-23 (+INTP Triforce: image-2 × MCP × prompt 工程 三位一体)"
---

# AI 前端 UI 生图 · INTP Way

> **⭐ 北极星口号**：
> **"The bar is stunning, not functional. Every pixel is intentional, every interaction is deliberate."**
> 质量对标 Dribbble / Behance showcase。

> **🎯 我们的独特定位（跨越 ConardLi）**：
> - **单模态工具**（ConardLi）：LLM 生 HTML → 人粗略验证 → 完事
> - **跨模态闭环**（我们）：image-2 视觉意图 → MCP 真素材 → LLM 代码 → chrome-devtools 渲染 → 跨模态 diff → 收敛
>
> 详见中枢文件 `intp-triforce.md`。

> **🧠 核心认知 1**：画 UI 和画真人写真是**两种完全相反的 prompt 风格**。人像要"摄影器材 / 体积光 / 胶片感"，UI 要"layout / typography / exact copy / state"。**混用必翻车**。
>
> **🧠 核心认知 2**（Anthropic 官方）：模型默认收敛到"AI slop"—— Inter 字体 + 紫粉渐变 + 3 列 feature grid。**必须显式叫板默认选择**。详见 `anti-slop-rules.md`。
>
> **🧠 核心认知 3**（ConardLi）：**Placeholder > Fake**。模型会自动编造 logo / stats / testimonials，必须用 placeholder 明确标记。详见 `placeholder-philosophy.md`。
>
> **🧠 核心认知 4**（INTP 独创）：**Placeholder 是 MCP 填真的接口**。能用 MCP 拿真素材的绝不用占位：
> - `[Logo]` → `mcp4_logo_search` ✅
> - `[Component]` → `mcp10_view_items_in_registries` ✅
> - `[Latest API]` → `mcp3_query-docs` ✅
> - `[Rendered result]` → `mcp0_take_screenshot` ✅
>
> 详见 `mcp-toolkit.md`。

## 何时使用本 skill

| 场景 | 适用本 skill？ |
|---|---|
| 画 SaaS dashboard 截图 | ✅ |
| 画移动 app 界面 mockup | ✅ |
| 画 landing page / marketing page | ✅ |
| 画设计系统组件展示图 | ✅ |
| 画海报（含文字排版） | ✅ |
| 画终端/IDE 风格截图 | ✅ |
| 画游戏 HUD | ✅ |
| 画真人写真 / 明星撞脸 | ❌ 用 `ai-image-bypass` skill |
| 画插画 / 动漫 / 3D render | ❌ gpt-image-2 擅长但不在本 skill 范围 |

## 模型选型（UI 场景）

| 需求 | 推荐模型 | 质量档 |
|---|---|---|
| **文字精确渲染**（UI 必需） | **gpt-image-2** ⭐ | `high` |
| 快速预览 | gpt-image-2 | `low` 或 `medium` |
| 艺术海报 / 概念图 | gpt-image-2 | `high` |
| 真人背景 + UI 叠加 | gpt-image-2 (image edit) | `high` |
| **不推荐**用 Grok | grok-imagine-image | — |

**为什么 UI 必选 gpt-image-2**：
1. OpenAI 官方强调 gpt-image-2 是 **业界文字渲染第一**（强过 Midjourney/SD/Flux）
2. 有 4K 级高分辨率，可以塞得下桌面截屏
3. 精确几何 / 网格 / 图标还原能力强
4. **Grok-imagine-image 画 UI 是灾难**（线条扭曲、文字乱码）

## 核心文件导读

**分层架构**（从哲学 → 方法论 → 场景应用）：

### 🌟 Ⅰ 哲学层（先读这里奠定心智）
1. **`intp-triforce.md`** ⭐⭐⭐ — **中枢文件**：INTP Way 三位一体哲学 + 3 种能力配比模式 + 9 步闭环 + ConardLi 对比表
2. **`anti-slop-rules.md`** ⭐ — Anthropic + ConardLi 双重反 AI slop 规则（含**终极反 slop 魔咒**可直接拷贝）
3. **`placeholder-philosophy.md`** — Placeholder > Fake 完整框架（6 种场景 + 可拷贝公约）

### 🔨 Ⅱ 方法论层（掌握工作流）
4. **`mcp-toolkit.md`** ⭐⭐ — **MCP 工具箱全景**（36 个 MCP tool 在 UI 场景的具体用法 + Playbook 组合拳）
5. **`visual-to-code-loop.md`** ⭐ — **跨模态反馈循环**（image-2 意图锚点 ↔ chrome-devtools 渲染锚点 → diff 收敛）
6. **`claude-design-workflow.md`** — 6 步基础流程（3 哲学 + Declare DS + v0 draft）
7. **`prompt-fundamentals.md`** — OpenAI 9 条 + fal.ai 6 条反平庸规则 + 4 维驱动

### 📜 Ⅲ 选型层（选风格、选字体、选色板）
8. **`aesthetic-families.md`** ⭐ — **9 大美学家族**（Editorial Minimalism / Terminal-Core / Warm Editorial / Data-Dense / Cinematic Dark / Playful Color / Glass / Neon Brutalist / Cult Indie），每家族含代表品牌 + HEX 色 + image-2 prompt 片段
9. **`design-tokens.md`** — 设计 token + **oklch 色彩系统** + **4 个 pre-validated 色×字配对**（⚠️ Inter/Roboto/Fraunces/system-ui/Space Grotesk 均被降级为 AI slop 陷阱）
10. **`dimensions-and-pricing.md`** — 尺寸档位 + 价格

### 📚 Ⅳ Playbook 层（端到端案例）
11. **`playbooks/mode-a-explore.md`** ⭐ — 探索模式（用户只有模糊想法 → image-2 主导）
12. **`playbooks/mode-b-ship.md`** ⭐ — 落地模式（用户有视觉稿 → MCP 主导）
13. **`playbooks/mode-c-audit.md`** ⭐ — 验证模式（用户有代码/网站 → AI slop 诊断 + 改进清单）

### 🔧 Ⅴ 执行层（填空、出图、排查）
14. **`5-slot-template.md`** — **5 槽位通用模板**（Scene → Subject → Details → Use case → Constraints）
15. **`templates/*.txt`** — 可直接复制粘贴的场景模板（saas-dashboard / mobile-app / landing / poster / design-system / ide-terminal）
16. **`troubleshooting.md`** — UI 场景常见问题

## 快速上手（按场景进对应 Mode）

有三种不同的进入点，**根据用户给你什么来选**：

### 🎨 Mode A：用户只给模糊想法
→ 读 1 个文件：**`playbooks/mode-a-explore.md`**
核心动作：出 2-3 个候选家族的 image-2 草稿，用户选方向。成本：~$0.20。

### 🔨 Mode B：用户给视觉稿/要代码
→ 读 1 个文件：**`playbooks/mode-b-ship.md`**
核心动作：MCP 拿 shadcn 真组件 + 真 logo + 最新 API 文档 → 代码生成 → visual-to-code-loop。

### 🔍 Mode C：用户给已有代码/网站
→ 读 1 个文件：**`playbooks/mode-c-audit.md`**
核心动作：playwright 截图 + lighthouse audit + anti-slop 诊断 + image-2 画修正版。

---

## ⚙️ 传统单张图快速流（6 步·兼容保留）

如果你只要做一张高质图不走完整 playbook：

```
Step 1: 打开 aesthetic-families.md，用 Picker 三问选 1 个家族
Step 2: 复制该家族的 image-2 prompt 片段到剪贴板
Step 3: 打开 templates/ 找最接近你需求的场景模板
Step 4: 把家族片段填入模板的 Important details 槽
Step 5: 在 prompt 末尾粘贴 anti-slop-rules.md 的"终极反 slop 魔咒"
Step 6: 跑脚本
        .\gen-image.ps1 -PromptFile prompts/xxx.txt `
                        -Model gpt-image-2 `
                        -Size "1536x1024" `
                        -Quality high
```

**批量变体建议**（Claude Design 官方工作流）：
```powershell
# 一次跑 3 个变体，从保守到激进
foreach ($v in @("v1-conservative", "v2-remix", "v3-bold")) {
    .\gen-image.ps1 -PromptFile "prompts/$v.txt" `
                    -Size "1536x1024" -Quality low  # 先 low 打样
}
```

**尺寸建议**：
- 移动 app 屏：`1024x1536` (竖版)
- 桌面 Web/Dashboard：`1536x1024` (横版) 或 `2560x1440` (2K)
- 海报：`1024x1024` 或 `1024x1536` 看版式
- 4K 截屏级：`3840x2160`（官方标记为 experimental，慎用）

**成本**（high 档）：
- 1.5K 档 = $0.16 / 张
- 2K 档 = $0.22 / 张
- 4K 档 = $0.40 / 张（不稳定，建议先 2K 打样）

## 最重要的 6 条铁律（抵万字文档）

### 1. 4 维独立驱动（Anthropic 官方原则）
不要写一句 `"make it beautiful"`。分别驱动 **Typography / Color / Motion / Background** 4 个维度：
```
Typography: {{具体字体 + 性格}}
Color: {{主色 + sharp accent + background}}
Motion: {{暗示动态 / 或声明 static editorial}}
Background: {{纹理 / 渐变 / 几何 / 氛围}}
```

### 2. 显式叫板 AI slop 默认
直接告诉模型"不要默认往那里走"：
```
AVOID: Inter, Roboto, Arial, Space Grotesk fonts.
AVOID: purple-to-pink gradients.
AVOID: 3-column symmetric feature grids.
AVOID: rounded-12px card sameness.
```

### 3. 把 UI 当作"已存在的产品"来描述
❌ 错：`Design a modern dashboard with sleek UI`
✅ 对：`A SaaS analytics dashboard screenshot showing daily active users chart on the left...`

### 4. 精确的 exact text 必须用引号 / ALL CAPS
❌ 错：`A pricing page with three plans`
✅ 对：`Headline (EXACT TEXT): "Simple pricing for every team". Three pricing cards: STARTER $0/mo, PRO $29/mo, ENTERPRISE custom.`

### 5. 说"像产品"而不是"像设计稿"
❌ 错：`with a designer aesthetic, modern vibes, clean look`
✅ 对：`Looks like a real shipped product screenshot, 8px grid, 16px body text, perfect kerning, subtle card shadows, pixel-perfect alignment`

### 6. 先选家族，再填细节（Claude Design 工作流）
> "Good hi-fi designs do not start from scratch — they are rooted in existing design context."

从 0 开始让模型"自由发挥"=必定 AI slop。必须先锚定一个美学家族 + 1-2 个代表品牌参考。

## 🎯 快速决策表

| 我要做... | 先读 | 再读 | 生图模板 |
|---|---|---|---|
| **SaaS dashboard** | `aesthetic-families.md` 家族 4 Data-Dense | `anti-slop-rules.md` | `templates/saas-dashboard.txt` |
| **Anthropic 风 landing** | `aesthetic-families.md` 家族 3 Warm Editorial | `claude-design-workflow.md` | `templates/landing-page.txt` |
| **Dev tool 官网** | `aesthetic-families.md` 家族 2 Terminal-Core | `anti-slop-rules.md` | `templates/landing-page.txt` |
| **AI 产品 hero** | `aesthetic-families.md` 家族 5 Cinematic Dark | `anti-slop-rules.md` | `templates/landing-page.txt` |
| **移动 Todo app** | `aesthetic-families.md` 家族 3 或 7 | `5-slot-template.md` | `templates/mobile-app-screen.txt` |
| **编辑器/IDE 截图** | `aesthetic-families.md` 家族 2 Terminal-Core | `design-tokens.md` 暗色主题 | `templates/ide-terminal.txt` |
| **产品海报** | `aesthetic-families.md` 家族 8 Neon Brutalist 或 3 Warm | `prompt-fundamentals.md` 文字章节 | `templates/marketing-poster.txt` |
| **设计系统展示** | `aesthetic-families.md` 家族 1 Editorial | `design-tokens.md` | `templates/design-system.txt` |

## 伦理与版权
- 禁止仿冒真实产品品牌（不要在 prompt 里写 "Figma / Notion / Linear 的 UI"）
- **引用设计灵感 OK，复制商标 NOT OK**（`in the spirit of Linear` ✅，`copy Linear's logo` ❌）
- 生成的图用于演示、原型、内部评审均 OK
- 商业用途时，前端最终产品应由人工实现，AI 图仅作参考
- 字体版权：生成物像某个商业字体时，勿直接商用原图

## 📊 我们比 ConardLi 强在哪

一张表说清：

| 能力 | ConardLi web-design-skill | INTP Way （我们） |
|---|---|---|
| **视觉意图固定** | — | ✅ image-2 4K 视觉稿做错点 |
| **真素材采集** | — | ✅ MCP logo_search / shadcn / context7 |
| **渲染验证** | 人工开浏览器 | ✅ chrome-devtools / playwright 自动 |
| **a11y + 性能检查** | — | ✅ MCP lighthouse audit |
| **跨模态 diff** | — | ✅ mockup × render 逐维度对比 |
| **Declare Design System** | ✅ | ✅ （同步吸收） |
| **v0 Draft 策略** | ✅ | ✅ （同步吸收） |
| **反 slop 规则** | 2 位字体禁用 | ✅ Anthropic+ConardLi 双重，6 位禁用字体 + 5 大诛 |
| **美学家族** | 6 个 | ✅ 9 个 + 对比品牌 HEX |
| **oklch** | ✅ | ✅ （同步吸收） |
| **Placeholder 哲学** | 文字说明 | ✅ + **MCP 自动填真** |

**一句话**：ConardLi 给你一把更好的锤子。我们给你一整家工坊 + 质检环节。

---

## 📚 关键权威来源（可直接引用）

| 资料 | URL | 核心价值 |
|---|---|---|
| Anthropic《Prompting for Frontend Aesthetics》 | `platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics` | 官方 DISTILLED_AESTHETICS_PROMPT，反 AI slop 规则原文 |
| 泄露的 Claude Design system prompt | `github.com/elder-plinius/CL4R1T4S/blob/main/ANTHROPIC/Claude-Design-Sys-Prompt.txt` | 完整内部工作流，3 哲学 + 12 维实验 |
| **ConardLi/web-design-skill** ⭐ | `github.com/ConardLi/web-design-skill` | Claude Design 代码侧姊妹 skill — Declare DS + v0 draft + oklch + placeholder |
| awesome-claude-design | `github.com/rohitg00/awesome-claude-design` | 9 大美学家族 + Remix 配方 |
| OpenAI Cookbook GPT Image 2 guide | `developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide` | 官方 9 条 prompting 原则 |
| fal.ai GPT Image 2 guide | `fal.ai/learn/tools/prompting-gpt-image-2` | 5 槽位模板 + 6 条 Anti-slop 军规 |
