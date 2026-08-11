# Prompting Fundamentals（心智锚点）

合并自三大权威来源：
- **OpenAI Cookbook** GPT Image 2 Prompting Guide（生图底层 9 条）
- **fal.ai** GPT Image 2 Prompting Guide（反平庸 6 条军规）
- **Anthropic 官方**《Prompting for Frontend Aesthetics》Cookbook（**前端 4 维驱动法**）

这些规则是**先于所有模板的内功**。

---

## 🎯 Anthropic 官方核心理念：4 维独立驱动

> **关键原文**："Claude has strong knowledge of design principles, typography, and color theory, **but defaults to safe choices unless explicitly encouraged otherwise.**"

翻译：**模型知道怎么做好看，但不被明确要求就永远选"安全但平庸"**。

### 🧭 反 slop 三大策略（Anthropic 原文）

1. **Guide specific design dimensions** — 分维度独立驱动（不写"make it beautiful"）
2. **Reference design inspirations** — 引用具体灵感源（IDE 主题、文化美学、具体品牌）
3. **Call out common defaults** — 显式叫板模型的默认偏好

### 📐 4 维度分别驱动模板

```
Typography: {{具体字体特征 + 性格 + 字号层级}}
Color & Theme: {{主色 + sharp accent + CSS 变量 + IDE/文化灵感}}
Motion: {{动画意图 / 或声明 static editorial}}
Background: {{渐变 / 图案 / 几何 / 氛围层次}}
```

每个维度都要**具体**。`"minimalist typography"` 是废话；`"a refined American grotesque with slight warmth, 72px display with tight tracking"` 是有效指令。

### ❌ 必须显式 Avoid 的 AI 默认（Anthropic 原话）

```
Avoid generic AI-generated aesthetics:
- Overused font families (Inter, Roboto, Arial, system fonts)
- Clichéd color schemes (particularly purple gradients on white backgrounds)
- Predictable layouts and component patterns
- Cookie-cutter design that lacks context-specific character
```

**加料警告**：模型在多代生成中会持续收敛到 `Space Grotesk`——这是 Anthropic 在 alpha 测试中反复发现的 slop trap。

### 🧲 灵感参考的正确姿势

**错**：`"copy Linear"` → 粗糙抄袭
**对**：`"in the spirit of Linear × Mintlify — calm neutrals, one violet accent, generous line-height, narrow humanist grotesque"` → 继承视觉语汇

**推荐灵感源**（Anthropic 官方建议）：
- **IDE themes**：Dracula / Nord / One Dark / Tokyo Night / GitHub Dark
- **Cultural aesthetics**：Swiss / Japanese / Memphis / Brutalism
- **Film color grading**：Wong Kar-wai / Coen Brothers / A24 / Criterion

---

## 🏛 OpenAI 官方 9 条

### 1. Structure + Goal
写 prompt 固定顺序：**background/scene → subject → key details → constraints**。
复杂任务**必须包含 intended use**（`UI mockup` / `ad` / `infographic`），这会把模型切到对应的"模式"和精细度。

### 2. Prompt Format
什么格式都可以（描述段、JSON、指令、tag），**关键是意图和约束清晰**。
生产系统优先选 **可维护的模板**，不是花哨语法。

### 3. Specificity + Quality Cues
- 明确 **材质、形状、纹理、视觉媒介**（photo / watercolor / 3D render）
- "photorealistic" 直接写进 prompt 能强触发写实模式
- 类似触发：`real photograph`, `taken on a real camera`, `professional photography`, `iPhone photo`
- **具体相机参数是风格暗示，不是物理模拟**

### 4. Latency vs Fidelity
- **延迟敏感** / 高并发 → 从 `quality="low"` 开始
- **小字 / 密集信息 / 识别敏感编辑 / 高分辨率** → 对比 `medium` vs `high` 后上线

### 5. Composition
- 明确 framing / viewpoint（close-up, wide, top-down）
- 角度（eye-level, low-angle）
- 光/氛围（soft diffuse, golden hour, high-contrast）
- 布局重要时直接说位置："logo top-right" / "subject centered with negative space on left"

### 6. People, Pose, and Action
描述 scale / body framing / gaze / 物体交互：
- `full body visible, feet included`
- `looking down at the open book, not at the camera`
- `hands naturally gripping the handlebars`

### 7. Constraints（什么改什么不改）
**显式写**：
- `no watermark / no extra text / no logos/trademarks`
- `preserve identity/geometry/layout/brand elements`
- 编辑场景：`change only X` + `keep everything else the same`（每轮重复 preserve 列表，防止漂移）

### 8. Text in Images（UI 关键）
- 字面文字用 **引号** 或 **ALL CAPS**
- 指定 font style, size, color, placement
- 生僻词 / 品牌名 **字母逐个拼**（spell letter-by-letter）
- 小字、密集文本、多字体排版 → 用 `medium` 或 `high`

### 9. Iterate Instead of Overloading
长 prompt 能用，但调试难。先 clean base 再 small single-change refine：
- `make lighting warmer`
- `remove the extra tree`
- `restore the original background`

---

## 🛡️ fal.ai Anti-slop Rules（反平庸 6 条军规）

### Rule 1: Visual Facts over Vague Praise
❌ `stunning, incredible, epic, masterpiece, gorgeous, insane detail`
✅ `overcast daylight, brushed aluminum, chipped paint, clean kerning, 50mm feel, soft bounce light`

**空泛夸奖对模型毫无信息量**；**客观可验证的视觉事实**才有效。

### Rule 2: Style Tags Need Visual Targets
❌ 只写：
```
minimalist brutalist editorial luxury photoreal cinematic modern premium
```
✅ 把每个 style tag 翻译成具体视觉：
```
Cream background, heavy black condensed sans serif, asymmetrical type block,
one hero object, generous negative space, studio tabletop lighting.
```

### Rule 3: Say the Real Thing
如果图里要有**交通信息亭**就说 `transit kiosk`；要有**登机牌**就说 `boarding pass`；要保留**人脸**就说 `preserve the face`。
**不要用情绪词掩盖具体物品**（`"a modern mobility solution"` 是 slop）。

### Rule 4: In Edits, Separate Change from Preserve
`change only X` + `keep everything else the same`，每轮迭代都重复 preserve 列表。

### Rule 5: Treat Text Like Typography
- 字面文字用引号或 ALL CAPS
- 指定 font / size / color / placement
- 生僻词字母逐个拼
- 加 `no extra words` + `no duplicate text`

### Rule 6: One Revision per Turn
✅ 对：
```
Make the light warmer. Remove the extra chair on the left.
Restore the original wall texture. Keep everything else the same.
```
❌ 错：
```
Make it more premium, more realistic, more stylish, more cinematic,
more emotional, more modern, fix the text, change the outfit,
improve the background, and also keep everything.
```

---

## ⚡ UI 场景特别要点（合并两份指南）

### A. 把 UI 当作"已存在的产品"写
> **Describe the product as if it already exists.**
>
> Focus on layout, hierarchy, spacing, and real interface elements,
> and **avoid concept art language** so the result looks like a usable,
> shipped interface rather than a design sketch.

✅ `A realistic mobile app UI mockup for a local farmers market...`
❌ `A concept design of a beautiful app for farmers market with modern vibes...`

### B. UI 必须包含的 6 要素
1. **Screen type**（mobile app / web dashboard / terminal / onboarding）
2. **Hierarchy**（title, subtitle, sections）
3. **Exact copy**（引号里写死的文字）
4. **State**（"one task checked off" / "3 unread notifications"）
5. **Layout logic**（background 色、accent 色、间距、阴影）
6. **Typography behavior**（字体、字号、行高、对齐）

### C. 必加约束
```
No watermark. No real app branding. No extra words. No duplicate text.
Perfect legibility. Generous spacing. Pixel-perfect alignment.
```

### D. 放进设备画框
想要"截屏感"的话，加一句：
- `Place the UI mockup in an iPhone frame.`
- `Shown inside a MacBook Pro 14" frame on a clean studio background.`
- `Browser chrome with Chrome-like top bar, URL bar reads "dashboard.example.com".`

---

## 🧪 常用 quality 档位决策树

```
你需要什么？
├─ 快速打样看构图       → low  (快 + 便宜)
├─ 平均质量的产品资产   → medium
├─ 带文字的 UI          → high ⭐
├─ 高分辨率截屏感       → high + 3840x2160 (experimental)
└─ 只要预览            → low + 1024x1024
```

---

## 💡 UI 场景要**避开**的焚决词（反效果）

做 UI 时，**绝对不要**带这些词（会把模型拖往"画真人"方向）：
- `真人写真 / photojournalism / documentary photography`
- `(urfaceid)` / 冷白皮 / 毛孔
- `Sony A7R V / 85mm f/1.2` 这些器材词
- `golden hour / Wong Kar-wai / film grain / cinematic grading`
- `ethereal / fairy-like / melancholy aura`

**UI 词库是另一套**（见 `design-tokens.md`）。

---

## 📜 Anthropic 官方 DISTILLED_AESTHETICS_PROMPT（终极引用）

这是 Anthropic 官方公开的**可直接注入到任何 UI 生成对话的 system prompt 片段**。适用于 Claude Code、Claude Design、也完全适用于 gpt-image-2 生图 prompt 的 Constraints 段：

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

### 🔧 针对 gpt-image-2 生图场景的浓缩版

对于**生图 prompt**（而不是代码 prompt），把上面的精华浓缩成可拷贝的 Constraints 段：

```
Aesthetic constraints (CRITICAL):
- NO generic "AI slop" design. Avoid Inter, Roboto, Arial, Space
  Grotesk — use distinctive typography with visible character.
- NO purple-to-pink gradients. Use a dominant color + sharp accent,
  NOT timid evenly-distributed palettes.
- Background must have atmosphere (gradient mesh / texture / pattern
  / geometric layering), NOT solid white.
- Layout must have unexpected composition choices — asymmetric grids,
  oversized type, broken rhythm — NOT predictable 3-column feature grids.
- Draw visual inspiration from {{选 1-2 个具体源：IDE theme 或 brand 或
  cultural aesthetic}}.
- This design should feel genuinely chosen for this specific product's
  story, not reusable AI template output.
```

---

## 🏆 完整心智 Checklist（每次生图前过一遍）

```
[ ] Prompt 有 Structure (Scene → Subject → Details → Use case → Constraints)
[ ] 明确了 use case (UI mockup / screenshot / poster)
[ ] Typography 具体（字体特征 + 字号 + 字重，不是"clean sans"）
[ ] Typography 避开了 Inter/Roboto/Space Grotesk
[ ] Color 有主色 + sharp accent，不是 timid 均分
[ ] Color 不是紫-粉渐变
[ ] Background 有纹理/渐变/层次，不是纯白
[ ] 引用了具体灵感源（品牌 / IDE theme / 文化美学）
[ ] 所有 exact text 用引号或 ALL CAPS
[ ] 有 "AVOID" / "NO" 列表叫板 AI slop
[ ] 有具体数字（不是 Lorem ipsum）
[ ] 写了明确的 "no watermark / no logos" 约束
[ ] 如果需要截屏感，加了 device frame / browser chrome
```

**任何一项打钩失败 → 回去改 prompt，不要跑**。
