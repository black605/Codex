# Claude Design 内部工作流（泄露精华）· INTP 增强版

> **来源**：
> - 泄露的 `claude.ai/design` 产品完整 system prompt（CL4R1T4S/ANTHROPIC）
> - ConardLi/web-design-skill 的实战升级（Declare DS + v0 draft）
> - INTP Way 的跨模态闭环（见 `intp-triforce.md`）
>
> 这不是单一生图规则，是 **Anthropic 训练的设计师助手** + **实战升级** + **MCP 增强**的完整思维流程。

## 🎯 文件定位

本文件是 **6 步基础流程**。更宏观的 **9 步跨模态闭环**（含 MCP 工具触点 + Visual-to-Code Loop）见：
- `intp-triforce.md` — 9 步闭环全图
- `visual-to-code-loop.md` — 跨模态反馈循环
- `mcp-toolkit.md` — 每一步可配合的 MCP 工具

本文件专注讲"**人脑里该怎么想**"，工具细节去上面 3 个文件看。

---

## 🎯 核心哲学（3 条镇山原则）

### 哲学 1: "Good hi-fi designs do not start from scratch"

**原文**：
> "Good hi-fi designs do not start from scratch — they are rooted in existing design context. Mocking a full product from scratch is a **LAST RESORT** and will lead to poor design."

**翻译成我们的场景**：
- 别让 image-2 "从零发挥"
- 先找**一个真实参考品牌**（不是抄袭，是**继承视觉语汇**）
- 在 prompt 里引用："in the spirit of [品牌名] + [品牌名]"
- 缺乏参考时，强制自己从 `aesthetic-families.md` 选一个家族

**Anti-pattern**：
```
❌ "Design a beautiful dashboard."
❌ "Make me a modern landing page."
```

**Right pattern**：
```
✅ "A dashboard in the visual language of Grafana + Supabase — 
    dark chrome background #111217, signal yellow + green accents, 
    Roobert typography character."
```

---

### 哲学 2: "Give options" - 变体优先

**原文**：
> "Give options: try to give 3+ variations across several dimensions. Mix by-the-book designs that match existing patterns with new and novel interactions. **Start your variations basic and get more advanced and creative as you go!**"

**翻译**：每次做 UI 都跑 3+ 变体，**从保守到激进**排序。

### 🎲 **Variations Ladder（变体阶梯）**

| 阶 | 风格 | image-2 参数 |
|---|---|---|
| 变体 1 | 保守：教科书 editorial minimalism | `-N 1 -Size "1536x1024" -Quality high` |
| 变体 2 | 基础：常见 SaaS 模板演变 | 同上 |
| 变体 3 | 中等：混合两种家族的 remix | 同上 |
| 变体 4 | 激进：novel layout + 非常规字体混搭 | 同上 |
| 变体 5 | 实验：完全 indie/cult 方向 | 同上 |

**实战脚本**：
```powershell
# 批量跑 4 个变体（建议先用 low 质看构图，再 high 出片）
foreach ($variant in @("v1-conservative", "v2-standard", "v3-remix", "v4-bold")) {
    .\gen-image.ps1 -PromptFile "prompts/$variant.txt" `
                    -Model gpt-image-2 `
                    -Size "1536x1024" `
                    -Quality low   # 先 low 打样
}
```

---

### 哲学 3: "Placeholder > 糟糕的真实尝试"

**原文**：
> "If you do not have an icon, asset or component, draw a placeholder: in hi-fi design, **a placeholder is better than a bad attempt at the real thing**."

**翻译**：
- 不确定图标长啥样 → 明确说 `[icon: 24x24 placeholder rectangle with text "ICON"]`
- 不确定数据形状 → 说 `[chart: linear line with upward trend, data points are illustrative only]`
- **不要**让模型"发挥想象"生成假的 logo/avatar

**image-2 prompt 片段**：
```
Avatars: use generic letter-initial placeholders (e.g., "JD" on blue 
circle, "MK" on green circle). DO NOT generate fake photos of people.

Logo placeholder: if a company logo is needed in the trust bar, use 
simple abstract geometric marks (circle / triangle / stripe) — NO 
real company logos, NO fabricated brand names.

Data placeholder: chart values must be visually plausible but labeled 
as illustrative (e.g., watermark "Demo data" in corner at 10% opacity).
```

---

## 🏗 6 步工作流（可直接迁移）

> **双重来源验证**：合并 Claude Design 泄露 system prompt + ConardLi `web-design-skill` 的实战升级版。后者在泄露原文基础上加了两个关键步骤：**Step 3 Declare Design System** 和 **Step 4 v0 draft**。

### Step 1: 理解需求
**问对问题**（原文："asking many good questions is ESSENTIAL"）：
- 输出的 use case 是什么？（mockup / screenshot / pitch deck / marketing asset？）
- 目标 fidelity？（rough sketch / wireframe / hi-fi mockup / pixel-perfect screenshot？）
- 要几个变体？（1 / 3 / 5+？）
- 有哪些 design systems / UI kits / brands 在玩？

### Step 2: 探索资源
**原文**：
> "Read the design system's full definition and relevant linked files."

迁移到生图：
- 打开 `aesthetic-families.md` 选家族
- 打开 `design-tokens.md` 选色板 + 字体
- 打开 `templates/*.txt` 看最接近的模板
- **必读 `anti-slop-rules.md` 一遍**（每次，防 slop 漂移）

### Step 3: ⭐ Declare Design System（ConardLi 核心贡献）

**在写任何 prompt 前**，先用 Markdown 明确写出完整的 design system 声明，让用户确认后再推进：

```markdown
Design Decisions（向用户公示，等确认）:
- Aesthetic family: [挑一个 9 大家族]
- Color palette (oklch):
  - Primary: oklch(L C H) — 描述
  - Accent:  oklch(L C H) — 描述
  - Background: oklch(L C H) — 描述
- Typography:
  - Display: [具体字体特征 + 目标字号]（避开 Inter/Roboto/Arial/Space Grotesk/Fraunces/system-ui）
  - Body: [具体字体特征]
  - Code (if needed): [mono 字体]
- Spacing system: [base unit，如 8px]
- Border-radius strategy: [大 / 小 / 硬边]
- Shadow hierarchy: [elevation 1-5 或 flat]
- Motion style: [CSS-only / staggered / static editorial]
- Content policy: [用 placeholders 还是 real copy]
```

**为什么这步关键**：
- 防止 prompt 写一半发现方向不对，浪费 token
- 用户可以在**动笔前纠偏**，比看到图再改便宜 10 倍
- 强制把抽象直觉变成**可验证的具体决策**

### Step 4: ⭐ v0 Draft（ConardLi 核心贡献）

**别憋大招一次交付完美版**。用 **placeholders + 关键布局 + design tokens** 先搞一个"viewable v0"：

| v0 应包含 | v0 不应包含 |
|---|---|
| ✅ 核心结构 | ❌ 内容细节 |
| ✅ Color/Typography tokens | ❌ 完整组件库 |
| ✅ 关键模块 placeholders（`[image]` `[icon]` `[metric]`） | ❌ 所有交互状态 |
| ✅ 你的 design assumptions 列表 | ❌ 完整动效 |

**v0 的价值**：
> "A v0 with assumptions and placeholders is more valuable than a 'perfect v1' that took 3x the time — if the direction is wrong, the latter has to be scrapped entirely." — ConardLi

**image-2 场景的 v0 做法**：
```powershell
# v0: low 质快速打样 (~$0.01-0.02)
.\gen-image.ps1 -PromptFile prompts/v0-draft.txt `
                -Size "1024x1024" -Quality low

# 用户确认方向 → 升级
.\gen-image.ps1 -PromptFile prompts/v1-final.txt `
                -Size "1536x1024" -Quality high
```

**v0 prompt 要点**：
- 所有数字/logo/头像都是明确 placeholder
- 布局骨架清晰，但细节粗略
- 色彩 tokens 定死，但不追求精致

### Step 5: Full Build

v0 被 approve 后，才写完整 prompt —— 补齐内容、加状态、加细节。
遇到关键决策点（比如选 variant A 还是 B），**暂停再次确认**，别默默推进。

### Step 6: Verification（交付前 checklist）

**Pre-delivery Checklist**（ConardLi，可直接拿来用）：

- [ ] 图像里**无明显字体 slop**（Inter/Roboto/Arial/Space Grotesk/Fraunces/system-ui 迹象）
- [ ] 色彩**不含紫粉渐变**和无脑 tech blue
- [ ] **无 left-border accent 卡片**这类 AI tell
- [ ] **无 emoji 当图标使用**
- [ ] **无编造的 stats / logos / testimonials**（全是 placeholder 或真数据）
- [ ] 文字**全部可读**（无字符畸变）
- [ ] 布局**不是 3 列对称 feature grid**
- [ ] 每个组件都能说出"为什么放这里"（非模板堆砌）
- [ ] 视觉质量达到 **Dribbble / Behance showcase 级别**
- [ ] 如果是响应式/多尺寸需求，各断点都 OK

**原文**：
> "Summarize EXTREMELY BRIEFLY — caveats and next steps only."

不要写"我做了什么"的流水账。只说：
- 这张图你可以用
- 这个地方我没把握 / 需要你确认
- 下一步推荐动作

---

## 🎨 Claude Design 的 "Play With" 元素清单

**原文**：
> "Play with scale, fills, texture, visual rhythm, layering, novel layouts, type treatments, etc."

### 完整的 12 种"实验维度"

做变体时，**每个变体改变 1-2 个维度**：

| 维度 | 保守玩法 | 激进玩法 |
|---|---|---|
| **Scale** | 统一字号系统 | 一个元素 10× 放大 |
| **Fills** | 单色 solid | 多层渐变 mesh / 纹理 fill |
| **Texture** | 纯净表面 | Risograph grain / paper noise |
| **Visual rhythm** | 均匀节奏 | 3-2-1 asymmetric beat |
| **Layering** | 单层 flat | 半透明叠 3+ 层 |
| **Novel layouts** | 12-column grid | 对角切分 / broken grid |
| **Type treatments** | 统一字体 + 层级 | 字体 clash（serif + brutalist） |
| **Color ratios** | 60-30-10 三分 | 95-5 近乎单色 + 一点锐利 |
| **Negative space** | 卡片密集 | 超大空白 + 微小主体 |
| **Orientation** | 水平阅读 | 垂直 / 对角 / 旋转 |
| **Photography** | 产品居中静物 | off-center + 环境叙事 |
| **Ornament** | 零装饰 | 标志性装饰元素（star/circle/squiggle） |

### Prompt 用法
在 variant prompt 开头明确写：
```
This variant emphasizes: {{两个维度}}.
Example: "This variant emphasizes Scale and Type Treatment — 
the product name is rendered at 220px and takes 40% of the canvas, 
while body copy is set in a contrasting serif at regular size."
```

---

## 💡 "Match the Visual Vocabulary" 原则

**原文**：
> "When adding to an existing UI, try to understand the visual vocabulary of the UI first, and follow it. Match copywriting style, color palette, tone, hover/click states, animation styles, shadow + card + layout patterns, density, etc. It can help to **'think out loud' about what you observe**."

### 场景：给已有产品补设计稿

**工作流**：
1. 收集 2-3 张已有 UI 截图（用户提供 / 网站截图）
2. **先"think out loud"描述所观察到的视觉语汇**
3. 再生成新图，显式继承这些特征

### Think-out-loud 示例
```
观察到的视觉语汇：
- Copywriting: 短句 + 第二人称 + 非正式（"Let's get started" 而非 "Initiate onboarding"）
- Color: dominant warm cream, ONE sharp terracotta accent
- Typography: serif body with slight humanist warmth, 1.6 line-height
- Shadows: very subtle, 0 1px 3px rgba(0,0,0,0.08)
- Cards: 16px rounded, 24px internal padding, 1px border #E7E5E1
- Density: spacious — 60% of viewport is negative space
- Ornament: small single-color abstract SVG accents, never photography
```

**然后**在新 prompt 里**逐条引用**：
```
Must match existing visual vocabulary:
- Copywriting tone: casual second-person ("Let's..." "You can...")
- Color: cream #F4F3EE dominant, terracotta #C96442 single accent  
- Typography: Tiempos Text serif body, 1.6 line-height
- Cards: 16px radius, 24px padding, 1px border #E7E5E1, 
  0 1px 3px rgba(0,0,0,0.08) shadow
- Density: 60% negative space, no crowded elements
- Ornament: small monochrome SVG accents only, NO photography
```

---

## 🚀 Output Creation 规则（泄露版）

直接可用的文件组织建议：

### 文件命名
- **描述性文件名**：`Landing Page Hero v1.png` 而不是 `image_1.png`
- **版本化**：大改后用 `v2`，不要覆盖 `v1`
- **资产分类**：
  - `final/` — 交付给用户看的
  - `explorations/` — 尝试阶段的变体
  - `references/` — 收集的灵感图
  - `prompts/` — 对应的 prompt 文件

### 推荐的项目结构
```
my-ui-project/
├── prompts/
│   ├── dashboard-v1-conservative.txt
│   ├── dashboard-v2-remix.txt
│   └── dashboard-v3-bold.txt
├── final/
│   └── dashboard-v2-final-2560x1440.png
├── explorations/
│   ├── dashboard-v1-low.png
│   ├── dashboard-v1-high.png
│   └── dashboard-v2-low.png
├── references/
│   ├── grafana-screenshot.png
│   └── supabase-dashboard.png
└── NOTES.md  # think-out-loud 观察 + 决策理由
```

### NOTES.md 模板
```markdown
# UI Generation Notes

## Brief
{{用户原始需求}}

## Design context (visual vocabulary observed)
- Aesthetic family: {{picked from 9 families}}
- Reference brands: {{X + Y}}
- Copywriting tone: {{formal / casual / witty}}
- Color palette: {{HEX primary / secondary / accent}}
- Typography voice: {{description}}

## Variants shipped
- v1 (conservative): {{one-line description}}
- v2 (remix): {{one-line description}}
- v3 (bold): {{one-line description}}

## Chosen version
{{v2, because...}}

## Known issues / next steps
- Font X is too close to Inter-like defaults, next iteration try...
- Background texture is too subtle, may need to increase grain opacity
```

---

## 🔑 Anthropic 自家品牌的 DNA（值得致敬）

因为泄露 prompt 来自 Anthropic，附带看到 **Anthropic 自己品牌的视觉语汇**：

- **Family**: Warm Editorial（家族 3）
- **Primary**: 奶白 `#F4F3EE`
- **Accent**: 赤陶土 `#C96442`
- **Ink**: 深墨 `#191817`
- **Typography**: 温暖衬线 + 精致 sans 混合
- **Tone**: 学术但不冷漠，权威但不傲慢

想做"Anthropic 风"的 UI，直接引用这套。
