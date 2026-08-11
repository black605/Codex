---
title: Visual ↔ Code Loop · 跨模态反馈循环
role: 核心方法论
parent: intp-triforce.md
---

# Visual ↔ Code Loop · 跨模态反馈循环

> **这是 INTP Way 的灵魂方法论。**
>
> 没有这个循环，我们和 ConardLi 只是"规则更全"的差距。
> 有了这个循环，我们做出的是"设计意图和代码实现**真的一致**"的系统。

---

## 🧭 为什么传统 AI 生 UI 总是翻车

**根本问题**：设计意图 → 代码 → 渲染，**中间没有校验点**。

```
设计师脑中：优雅的 editorial landing
         ↓ (人口述给 AI)
LLM 以为：  AI 理解成"editorial" = Inter + 中间对齐 + 紫色渐变
         ↓ (生代码)
渲染结果：  和设计师脑中差十万八千里
         ↓
设计师：    改改改（纯靠语言描述差异）
```

**每轮迭代都是"隔空喊话"**。

---

## ⭕ INTP 解法：两个锚点 + 一个差值

```
┌─────────────────────────────────────────────────┐
│                                                 │
│  设计师脑中意图                                   │
│    ↓                                            │
│  [锚点 A]  image-2 视觉稿（视觉意图）              │
│    ↓                                            │
│  LLM 看着 image-2 + MCP 真素材 写代码              │
│    ↓                                            │
│  [锚点 B]  chrome-devtools 渲染截图（实际实现）     │
│    ↓                                            │
│  ⚖️ Diff = [A] vs [B]                           │
│    ↓                                            │
│  差值驱动下一轮代码修改                            │
│                                                 │
│  直到 Diff 收敛到可接受水平 → 交付                 │
│                                                 │
└─────────────────────────────────────────────────┘
```

**关键洞察**：用一张**可视化的图**把"意图"固化下来，代码对齐的对象从"文字描述"变成"可逐像素对比的图"。

---

## 🔧 实操：视觉→代码 Loop 完整流程

### 阶段 0：准备

```
# 项目目录结构
my-landing/
├── design/
│   ├── mockup-v0-low.png      # image-2 草稿（low 质，几块钱）
│   ├── mockup-v1-high.png     # image-2 终稿（high 质，锚点 A）
│   └── design-decisions.md    # prompt 记录
├── src/
│   └── Landing.tsx            # 生成的代码
├── renders/
│   ├── render-desktop.png     # chrome-devtools（锚点 B）
│   ├── render-mobile.png
│   └── render-dark.png
└── NOTES.md                   # 决策日志
```

### 阶段 1：生成锚点 A（image-2 视觉意图）

```powershell
# 先 low 质探索方向（$0.01-0.05）
.\gen-image.ps1 -PromptFile design\prompt-v0.txt `
                -Size "1024x1024" -Quality low `
                -OutPath design\mockup-v0-low.png

# 用户确认方向后，出 high 质锚点（$0.16-0.22）
.\gen-image.ps1 -PromptFile design\prompt-v1.txt `
                -Size "1536x1024" -Quality high `
                -OutPath design\mockup-v1-high.png
```

**锚点 A 的作用**：
- 代码审查时作为"对标样例"
- 验收时作为"是否达标"的证据
- 迭代时作为"设计意图"的物理载体

### 阶段 2：代码生成（用锚点 A + MCP 素材作为参考）

这里的关键是让 LLM 看到 `mockup-v1-high.png`，**不是只读 prompt 描述**。

**Windsurf 里的做法**：
```
@design/mockup-v1-high.png 帮我根据这张 mockup 做 Landing.tsx，
用 shadcn/ui 组件，参照 design-decisions.md 的 design tokens。
所有 trust bar logo 用 mcp4_logo_search 抓真 SVG。
```

Windsurf 会 `read_file` 读图、然后 `mcp4_logo_search` 拿真 logo，然后写代码。

### 阶段 3：生成锚点 B（chrome-devtools 实际渲染）

```
# 在 Windsurf 里调 MCP
mcp0_navigate_page({ 
  type: "url", 
  url: "http://localhost:3000/landing" 
})

mcp0_take_screenshot({
  filePath: "renders/render-desktop.png",
  fullPage: true
})

# 多 viewport
mcp6_browser_resize({ width: 375, height: 812 })
mcp6_browser_take_screenshot({ filename: "renders/render-mobile.png" })
```

### 阶段 4：Diff（跨模态对比）

这是 loop 的核心。有三种对比方式：

#### 方式 1：Side-by-side 人眼对比（最快）

把 `mockup-v1-high.png` 和 `render-desktop.png` 放一起看。
重点关注：
- 字体层级是否对
- 色彩调性是否对
- 间距和密度是否对
- 整体"调子"是否对

#### 方式 2：image-2 拼图辅助（给客户看）

```powershell
# 让 image-2 画一张 "design intent vs actual render" 对比图
# prompt 里附两张参考图（mockup + render）
```

#### 方式 3：Playwright 像素 diff（自动化）

```javascript
// 用 playwright 做像素级对比
const design = await loadImage("mockup-v1-high.png");
const render = await loadImage("render-desktop.png");
const diff = pixelmatch(design, render, { threshold: 0.1 });
// 超过阈值 → 列出差异区域 → LLM 改代码
```

### 阶段 5：迭代

根据 diff 结果，**一次只改一个维度**（遵循 Anthropic 原则 9）：

```
# 第 1 轮
Diff: 字体字重偏轻
Action: "把 headline 从 600 加粗到 700"

# 第 2 轮  
Diff: trust bar 间距太窄
Action: "trust bar gap 从 40px 加到 80px"

# 第 3 轮
Diff: 按钮圆角对不上
Action: "Primary button border-radius 从 8 改到 12"
```

**每轮后重新 chrome-devtools 截图 → 重新 diff**。

### 阶段 6：收敛判定

**什么时候停**？
- 视觉调子匹配 ≥ 95%
- 用户（或你）说"就这样了"
- 剩余差异属于"实现细节无法完全还原 image-2"（比如 image-2 画的字体本项目没装）

---

## 📐 Diff Checklist（逐项对比 mockup vs render）

跑 loop 时对着这个 checklist 过一遍：

### Typography（字体层级）
- [ ] Display 字号对吗？（image-2 画的 72px vs render 的 64px）
- [ ] 字重对吗？（light / regular / medium / bold）
- [ ] 行高对吗？（tight / normal / relaxed / loose）
- [ ] 字间距对吗？（tracking tight / normal / wide）
- [ ] 字体家族"感觉"对吗？（serif / grotesque / rounded）

### Color（色彩调性）
- [ ] 主色的 hue 对吗？（不要蓝画成紫）
- [ ] 主色的 lightness 对吗？
- [ ] 主色的 chroma（饱和度）对吗？
- [ ] Accent 色的"锐利度"对吗？
- [ ] Background 有没有 image-2 里的微纹理 / 渐变？

### Spacing（间距和密度）
- [ ] 内边距（padding）对吗？
- [ ] 组件间 gap 对吗？
- [ ] 整体"紧凑 vs 透气"对吗？
- [ ] 栅格对齐准确吗？（8px grid）

### Layout（布局结构）
- [ ] Hero 文字位置对吗？（居中 / 左对齐 / 右对齐）
- [ ] 图片比例对吗？（16:9 / 4:3 / square）
- [ ] 装饰元素位置对吗？（角落 / 背后 / 覆盖）

### Details（细节）
- [ ] 圆角对吗？（sharp 0 / subtle 4 / standard 8 / soft 12 / pill 999）
- [ ] 阴影层次对吗？
- [ ] 边框存在吗？（image-2 画了 render 没有，or 反过来）
- [ ] 小装饰元素对吗？（分隔线 / 图标 / 徽章）

---

## 🎯 Loop 的进阶技巧

### 技巧 1：用"语言锁定" mockup 的关键决策

在 `design-decisions.md` 里**明确写下 mockup 的关键决策**，防止迭代时漂移：

```markdown
# Mockup v1 关键决策（不可改动）
- Display 字体: Tiempos Headline character
- 主色: oklch(0.35 0.10 30) warm brown
- Hero 布局: 左对齐文字 + 右侧图片
- Trust bar: 6 个真 logo，灰度，opacity 60%
- Background: warm cream #FAF8F2 with subtle paper grain

# 可调整的细节
- 具体间距数值
- 按钮圆角 8-12 之间
- Shadow 深度
```

**迭代时只能改"可调整的细节"，不能改"不可改动"的决策**。如果要改核心决策，必须重生 mockup v2。

### 技巧 2：多 viewport 同时跑 loop

```powershell
# 同时对 3 个 viewport 做 diff
foreach ($vp in @("375x812", "768x1024", "1440x900", "2560x1440")) {
    mcp6_browser_resize($vp.split("x"))
    mcp6_browser_take_screenshot("render-$vp.png")
}
```

然后分别对比 mockup 的对应版本。image-2 可以出同一设计的不同比例版本。

### 技巧 3：暗色模式 loop

```powershell
# 在 image-2 prompt 里同时出 light 和 dark
.\gen-image.ps1 -PromptFile landing-light.txt -OutPath mockup-light.png
.\gen-image.ps1 -PromptFile landing-dark.txt -OutPath mockup-dark.png

# 代码里 toggle darkmode，分别渲染
mcp6_browser_evaluate(`() => document.documentElement.classList.add('dark')`)
mcp6_browser_take_screenshot("render-dark.png")
```

### 技巧 4：用 image-2 辅助 code review

当 render 和 mockup 差异太大不知道怎么改时，**让 image-2 画"修正版"**：

```
Prompt: "Take my current render (see render-desktop.png) and adjust it 
to match the design intent in mockup-v1-high.png. Specifically:
- Increase the headline weight
- Expand trust bar logo spacing
- Use the correct cream background color
Keep everything else the same."
```

image-2 画出的"修正版"可以作为第二代 mockup，代码再向这个目标迭代。

---

## 🧮 ROI 分析：Loop 真的值吗？

### 成本
- image-2 mockup: ~$0.20 × 2-3 张 = $0.60
- chrome-devtools 截图: 免费
- 人工 diff 时间: 每轮 5 分钟
- LLM 修改代码: 免费（用已有 quota）

### 收益
- **避免 5-10 轮"隔空喊话"迭代**（传统方式）
- 设计师不用再"手比划"差异
- 有**客观证据**证明代码达标（mockup 文件 + render 文件）
- 后续维护时有**可视化 spec**

### 结论
**每张 UI 投入 $1 内的 image-2 成本，省掉数小时的沟通时间**。
对 3 分钟一轮的 B 端项目，ROI 爆炸。

---

## 🚨 Loop 的边界和风险

### 风险 1：image-2 也可能 slop

如果你给 image-2 的 prompt 本身就是 AI slop（Inter + 紫色渐变），那 mockup 就是 slop。

**防御**：先读 `anti-slop-rules.md`，prompt 里加"终极反 slop 魔咒"。

### 风险 2：image-2 画的东西代码实现不了

比如 image-2 画了超复杂的 SVG 纹理，代码里很难一比一还原。

**防御**：
- mockup 生成时就考虑"可实现性"（别搞花里胡哨的 blend mode）
- 对实现不了的部分，**降级并记录在 NOTES.md**（"Design intends X, implemented as simplified Y"）

### 风险 3：Loop 陷入局部最优

反复 diff 但整体方向错了。

**防御**：每 3 轮 loop 强制 step back 一次：
- 重读需求
- 问"整个方向还是对的吗"
- 必要时重生 mockup

---

## 📋 Loop 交付的 6 件套

每次跑完 loop，交付物：

1. **`mockup-v1-high.png`** — image-2 设计意图（锚点 A）
2. **`render-desktop.png`** — chrome-devtools 桌面渲染
3. **`render-mobile.png`** — playwright 移动渲染
4. **`render-dark.png`** — 暗色模式渲染
5. **`lighthouse-report.json`** — a11y + 性能数据
6. **`NOTES.md`** — 决策日志 + diff 历史

**只有这 6 件齐了才叫"UI 交付完成"**。

---

## 🏆 ConardLi vs INTP：对比总结

| 环节 | ConardLi | INTP Way |
|---|---|---|
| 意图定义 | 文字描述 | **image-2 视觉稿 + 文字** |
| 代码生成 | LLM 靠想 | LLM 看着图 + MCP 真素材 |
| 渲染验证 | 人工开浏览器看 | **chrome-devtools 自动截图** |
| 多 viewport | 靠 CSS 信仰 | **playwright 真实截图** |
| 性能 / a11y | 忽略 | **lighthouse MCP 强制 audit** |
| 意图↔实现对比 | 靠感觉 | **跨模态 diff checklist** |
| 迭代收敛 | 靠语言反馈 | **像素级差异驱动** |
| 交付物 | 代码 | **代码 + 6 件套证据** |

**核心差异**：ConardLi 给你"一根更好的锤子"。我们给你"一整条装配线 + 质检环节"。
