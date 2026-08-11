---
title: Playbook · Mode C 验证模式
mode: Audit / Improve
when_to_use: 用户有现成代码/网站，要检查或改进
capability_ratio:
  mcp:     60%
  image-2: 20%
  prompt:  20%
---

# Playbook: Mode C · 验证模式

> **假设用户需求**：
> "帮我看看 https://nousbooklm.cn 这个网站 UI 怎么样？
> 为什么感觉有点'AI 味'？有哪些可以改进的地方？"

---

## 🎯 这个场景的关键特征

- ✅ 用户有**真实线上网站/代码**
- ❌ 用户**说不出具体哪里不对**（只有感觉）
- ❌ 用户不想**从头做一次**

→ **MCP 主导诊断**：playwright 截图 + prompt 工具做 AI slop 诊断 + image-2 画修正版

---

## 🚀 完整工作流

### Step 1: MCP playwright 截图（2 分钟）

```typescript
// 全设备截图
mcp6_browser_navigate({ 
  url: "https://nousbooklm.cn" 
})

// 桌面
mcp6_browser_resize({ width: 1440, height: 900 })
mcp6_browser_take_screenshot({ 
  filename: "audit/actual-desktop.png",
  fullPage: true 
})

// 移动
mcp6_browser_resize({ width: 375, height: 812 })
mcp6_browser_take_screenshot({ 
  filename: "audit/actual-mobile.png",
  fullPage: true 
})

// 暗色模式（如果支持）
mcp6_browser_evaluate({
  function: "() => document.documentElement.classList.add('dark')"
})
mcp6_browser_take_screenshot({ filename: "audit/actual-dark.png" })
```

### Step 2: MCP lighthouse 性能 + a11y audit

```typescript
mcp0_navigate_page({ 
  type: "url", 
  url: "https://nousbooklm.cn" 
})

mcp0_lighthouse_audit({
  device: "desktop",
  mode: "navigation",
  outputDirPath: "audit/"
})
```

拿到客观数据：
- Performance: 67（偏低，LCP 4.2s）
- Accessibility: 82（有提升空间）
- Best Practices: 91
- SEO: 88

### Step 3: Prompt 工程 · 反 AI slop 诊断

读 `anti-slop-rules.md`，对 `actual-desktop.png` 逐条过 checklist：

```markdown
# AI Slop 诊断报告 — nousbooklm.cn

## Typography 诊断
- ❌ 主字体看起来是 Inter（Anthropic 禁用字体）
- ⚠️ Display 和 body 都是同一 grotesque，缺层次对比
- ❌ 没有 display 字体特征

**评分: 2/10**

## Color 诊断
- ❌ Hero 有紫粉渐变（#8B5CF6 → #EC4899，经典 AI slop）
- ⚠️ 主色 #3B82F6 是 AI 默认 tech blue
- ✅ 暗色模式有考虑
- ⚠️ 对比度只有 4.2:1（未达 AAA）

**评分: 3/10**

## Layout 诊断
- ❌ 下面 features 是经典 3-column symmetric grid
- ❌ 每个 feature card 有 left-border color accent（AI tell #1）
- ⚠️ Hero → Features → Testimonials → CTA 完美套路
- ✅ 移动端响应式 OK

**评分: 3/10**

## Content 诊断
- ❌ Testimonial "Sarah K., Product Manager at Acme Corp" — 明显编造
- ❌ Trust bar 的 6 个客户 logo 看起来是生成的
- ⚠️ "10,000+ happy users" — 数字太圆，疑似编造
- ❌ 至少 3 个 stat cards 数字过于完美（98%, 10x, 24h）

**评分: 2/10**

## Backgrounds 诊断  
- ❌ Hero 全屏紫粉渐变（典型 AI slop 背景）
- ⚠️ 其他区域纯白无纹理
- ❌ 缺少视觉深度和氛围

**评分: 2/10**

## Icons / Graphics 诊断
- ❌ 大量使用 emoji 🚀 ⚡ ✨ 作为 icon
- ❌ 复杂 SVG 插图看起来变形
- ❌ 多处 "data slop"—— meaningless stats 堆砌

**评分: 1/10**

## 综合 AI Slop Score: 13/60 (红色预警)
```

### Step 4: image-2 画"修正版" mockup（$0.16）

基于诊断结果，用 image-2 画一张"修好"的对比图：

```
Create a corrected version of the nousbooklm.cn landing page hero.

Reference: @audit/actual-desktop.png (current version has AI slop issues)

Fix these issues:
1. Replace Inter font with distinctive humanist serif display 
   (Tiempos Headline character) + warm serif body (PP Editorial Old)
2. Replace purple-to-pink gradient with warm cream background 
   oklch(0.97 0.005 40) and single terracotta accent oklch(0.60 0.20 30)
3. Remove left-border accent cards — use subtle shadow elevation instead
4. Remove emoji icons — use abstract geometric placeholder icons
5. Remove fake testimonials — replace with "[Testimonial]" italic placeholders
6. Remove fake stats — use "[illustrative metric]" placeholders
7. Replace 3-column symmetric feature grid with asymmetric editorial layout 
   (one large feature + two smaller, varying card sizes)

Keep the same:
- Page structure (Hero / Features / Trust / CTA)
- Core copy and messaging
- Responsive layout logic

Style: Warm editorial in the spirit of Anthropic × Notion.

Constraints:
- NO Inter, Roboto, Arial, Space Grotesk, Fraunces, system-ui
- NO purple-pink gradients
- NO emoji as icons
- NO fabricated testimonials or stats
- NO 3-column symmetric grid
```

```powershell
.\gen-image.ps1 -PromptFile audit\prompt-corrected.txt `
                -Size "1536x1024" -Quality high `
                -OutPath audit\corrected-mockup.png
```

### Step 5: 生成改进清单

对比 `actual-desktop.png` 和 `corrected-mockup.png`，列具体代码修改清单：

```markdown
# 改进清单 — nousbooklm.cn

优先级 P0（必改，去 AI slop）：

1. **替换字体栈**
   文件: app/layout.tsx + globals.css
   变更:
   ```diff
   - font-family: Inter, system-ui, sans-serif;
   + font-family: 'Tiempos Headline', Georgia, serif;  /* display */
   + font-family: 'PP Editorial Old', 'Times New Roman', serif;  /* body */
   ```
   成本: 1 小时（包括处理 fallback）

2. **去紫粉渐变**
   文件: components/Hero.tsx
   变更:
   ```diff
   - <section className="bg-gradient-to-br from-purple-500 to-pink-500">
   + <section className="bg-[oklch(0.97_0.005_40)]">  /* warm cream */
   ```
   附加: 需要调整 hero 文字颜色从 white 到 oklch(0.20 0.02 30)
   成本: 30 分钟

3. **去 left-border accent cards**
   文件: components/FeatureCard.tsx
   变更:
   ```diff
   - <div className="border-l-4 border-purple-500 p-6">
   + <div className="p-8 shadow-[0_1px_2px_rgba(0,0,0,0.04)]">
   ```
   成本: 20 分钟

4. **去 emoji icons，换真图标**
   方案 A: mcp10_view @shadcn lucide icons 用真图标
   方案 B: 暂时保留但改为 placeholder 风格
   成本: 1-2 小时（取决于 icon 数量）

5. **去假 testimonials**
   变更: 要么找真用户证言，要么改成 placeholder
   ```diff
   - { name: "Sarah K.", role: "PM at Acme", text: "Amazing!" }
   + { placeholder: "[Real testimonial from customer interview]" }
   ```
   成本: 需要业务配合（收集真证言）

6. **去假 stats**
   变更: 同上，改 placeholder 或拿真数据
   成本: 需要产品/数据支持

优先级 P1（建议改）：

7. Lighthouse a11y 82 → 目标 95+
   - 补全 alt 属性
   - 对比度 4.2 → 7:1
   - Focus states
   成本: 2-3 小时

8. 3-column → 非对称 layout
   - 重新设计 Features 区
   成本: 半天（设计 + 实现）

优先级 P2（可选）：

9. 加 background 纹理层次
10. 暗色模式调优
```

### Step 6: （可选）Mode B 重做部分区块

对于 P0 的大改动（比如整个 Features 区重做），可以**触发 Mode B 工作流**单独重做这个区块：

```
进入 Mode B:
- mockup 锚点: corrected-mockup.png 的 Features 区裁切
- 实现: 新的 FeaturesSection.tsx
- 验证: chrome-devtools 渲染 + diff
```

### Step 7: 交付 Mode C 产物

```
audit/
├── actual-desktop.png           # 原版现状
├── actual-mobile.png
├── actual-dark.png
├── corrected-mockup.png         # image-2 画的修正版
├── lighthouse-report.json       # 客观数据
├── ai-slop-diagnosis.md         # 反 slop 诊断（Step 3）
└── improvement-checklist.md     # 改进清单（Step 5）

NOTES.md                          # 给用户的总结
```

---

## 💰 成本和时间总计

| 项 | 花费 |
|---|---|
| image-2 修正版 | $0.16 |
| MCP 截图 + lighthouse | $0 |
| 人工分析 | 约 20 分钟 |
| 输出清单 | 约 20 分钟 |
| **总 API 成本** | **$0.16** |

**价值**：$0.16 得到一份**带可视化对比图 + 客观数据 + 具体改进清单**的完整审计报告。

---

## 🆚 对比传统 UI review

| 方面 | 传统 design review | Mode C |
|---|---|---|
| 诊断依据 | 设计师主观 | **anti-slop-rules.md checklist + lighthouse 客观数据** |
| 问题描述 | "这里不太对" | **具体条目 + 为什么是 slop** |
| 改进方案 | 口述 | **image-2 可视化修正版 + 代码 diff** |
| 优先级 | 模糊 | **P0/P1/P2 + 成本估算** |
| 可追溯 | 邮件聊天记录 | **完整文件夹** |

---

## 🧪 Mode C 的高阶玩法

### 玩法 1：自动 slop 检测（可脚本化）

把 `anti-slop-rules.md` 的 checklist 变成自动扫描脚本：
- `grep` 找 `font-family: Inter` → 报警
- `grep` 找 `from-purple-500 to-pink-500` → 报警
- 找 `emoji unicode` 在 `<Icon>` 组件里 → 报警
- 找编造的 testimonial 模式（`"name":` 后跟随机名字 + 角色） → 报警

### 玩法 2：定期 audit 自己的产品

把 Mode C 做成 cronjob：每周对自己的产品跑一次 slop 诊断，生成报告。

### 玩法 3：为客户做 UI audit 服务

这个 playbook 本身就是**一项服务产品**：
- 客户给 URL
- 跑 Mode C 工作流
- 交付改进清单 + 对比图
- 可计价 $200-500 / 个网站

---

## 🏆 Mode C 的核心价值

> **Mode A 和 Mode B 是"生"，Mode C 是"治"。**
>
> ConardLi 的 skill 只能帮你"生"，不能帮你"治"已有产品。
>
> INTP Way 有 Mode C，所以我们**覆盖了 UI 全生命周期**。
