# UI 生图故障排查

---

## 🐛 常见问题 → 根因 → 对策

### 1. 文字变形 / 字母错乱 / 拼写错误

**现象**：`"WELCOME TO"` 变成 `"WELOCM TO"` 或乱码

**根因**：
- 质量档位过低
- 字体选择含特殊字符（如衬线字体复杂装饰）
- 单词太长或含生僻拼写

**对策**（按优先级）：
1. **升 quality 到 `high`** — 这是文字问题 90% 的解法
2. **用引号或 ALL CAPS** 标记字面文字：
   ```
   Headline (EXACT TEXT): "Welcome to Forge"
   ```
3. **拼写生僻词时字母隔开**：
   ```
   The brand name is "F-O-R-G-E" (FORGE)
   ```
4. **加 constraint**：
   ```
   No extra words. No duplicate text. No misspellings.
   Render text verbatim.
   ```
5. **换更简单的字体**：避免 "Playfair Display", "Canela" 这种繁复衬线

---

### 2. 生成的图偏"设计稿"感，不像真实产品

**现象**：图里有"Lorem ipsum"、明显的栅格线、装饰性占位符

**根因**：
- Prompt 里用了 "design concept" / "mockup" / "wireframe" 等词
- 没有具体 copy / 数据
- 缺少真实产品的"毛边"

**对策**：
1. **明确说"shipped product"**：
   ```
   Use case: Realistic screenshot of a shipped production app, 
             not a design mockup.
   ```
2. **填充真实 copy**：
   ```
   Not "Lorem ipsum" — use real content like "Daily active users dropped 
   3.2% this week compared to last week's 12,483 peak."
   ```
3. **加真实细节**：
   ```
   Show: unread notification badge "3", last updated timestamp "2 min ago", 
         user avatar initials "JD", active green dot.
   ```
4. **去掉"design-y"词汇**：
   - ❌ `modern aesthetic, sleek UI, trendy design`
   - ✅ `14px body text, 8px grid, #3B82F6 primary, realistic data`

---

### 3. 文字渲染清晰但排版错位

**现象**：文字能读，但位置不对 / 对不齐 / 跟其他元素撞

**根因**：
- 布局描述不够具体
- 缺少 "grid" 约束

**对策**：
1. **明确声明网格**：
   ```
   Strict 8px grid system. 24px padding inside cards. 
   16px gap between elements. Pixel-perfect alignment.
   ```
2. **具体描述每个元素位置**：
   ```
   Logo: top-left corner, 24px from edge.
   Primary CTA: centered horizontally, 32px below subheadline.
   Trust bar: bottom of viewport, full width, centered.
   ```
3. **迭代修复**（目前需 image edit，未来支持）：
   ```
   "Move the logo 16px down. Keep everything else the same."
   ```

---

### 4. 生成的数据 / 图表看起来假

**现象**：图表里数字都是 `1, 2, 3` 或数字超级夸张（如 `$99999999`）

**根因**：
- 没有给出具体数字
- 模型默认填演示数据

**对策**：
1. **明确写具体数字**：
   ```
   KPI cards:
   - MRR: $48,291 (+12.4% vs last month)
   - Active Users: 12,483 (+5.1%)
   - Churn: 2.3% (-0.8%)
   ```
2. **指定数据范围**：
   ```
   Line chart y-axis: 0 to 5,000 users. 
   30 data points along x-axis (dates from Mar 24 to Apr 23).
   Show a gentle upward trend with some daily fluctuation.
   ```
3. **加 constraint**：
   ```
   All numbers must be plausible for a mid-stage SaaS company. 
   No obvious placeholder values.
   ```

---

### 5. 图标用得不对 / 看起来不像真图标

**现象**：生成的"设置图标"看起来是个毛糙手绘

**根因**：
- 没指定图标风格
- 图标描述太泛

**对策**：
1. **指定图标系统**：
   ```
   Icons: Lucide style (thin stroke, 1.5px weight, rounded corners, 
          24x24 viewBox) 
   OR 
   Icons: Material Design (filled, 24x24, with outlined variants)
   OR  
   Icons: Heroicons outline style
   ```
2. **具体描述每个图标**：
   ```
   Sidebar icons: 
   [📊 BarChart3] Dashboard
   [👥 Users] Customers
   [⚙️ Settings] Settings
   ```
3. **别用 emoji 做生产图**（emoji 渲染因模型而异）
   ✅ 用 "a gear icon" 而不是 "⚙"（给语言描述）

---

### 6. 整体色调不对

**现象**：要了蓝色但出来偏紫 / 灰阶不够层次

**根因**：色值写不准

**对策**：
1. **必写 HEX**：
   ```
   Primary: #3B82F6 (exact blue, NOT purple, NOT teal)
   Secondary: #6B7280 (medium gray)
   ```
2. **加"not"否定**：
   ```
   Background: pure white #FFFFFF (NOT off-white, NOT cream, NOT gray).
   ```
3. **指定对比**：
   ```
   Text color #111827 on background #FFFFFF — 
   strong contrast for AAA accessibility.
   ```

---

### 7. 被内容审查拦截

**现象**：HTTP 200 但返回 `data: []`，或直接 `moderation_violation`

**根因**：UI 生图很少被拦，但这些会：
- Prompt 里提到特定真实公司名 / 品牌
- 含有政治 / 医疗 / 金融敏感内容
- 无意间触发人脸识别（UI 里放了名人照）

**对策**：
1. **替换品牌名为虚构名**：
   - ❌ `Stripe-like dashboard` 
   - ✅ `A payment platform dashboard called "PAYFLOW"`
2. **避免敏感领域具体术语**
3. **用 placeholder 人物**：
   - ❌ `User avatar: photo of Elon Musk`
   - ✅ `User avatar: generic initials "JD" on blue circle background`

---

### 8. 生成速度慢 / 超时

**现象**：请求 120 秒还没返回

**根因**：
- 4K + high 需要 2-3 分钟
- prompt 极长（> 2000 字）
- 并发生成 > 2 张

**对策**：
1. **降档**：
   - 先跑 `low` 确认构图（10-30 秒）
   - 最终版跑 `high`
2. **缩 prompt**：
   - 合并重复信息
   - 用 constraints 代替描述
3. **单张调试**：不要一开始就 `-N 4`
4. **超时设置**：脚本里加 `Invoke-RestMethod -TimeoutSec 300`

---

### 9. 输出比例不对

**现象**：要了 16:9 结果是 4:3

**根因**：
- `-Size` 参数没加引号（PowerShell 把 `x` 当算符）
- 长短比超过 3:1 被模型强制修正

**对策**：
1. **`-Size "3840x2160"` 加引号**
2. **检查尺寸约束**：
   - 两边必须 16 倍数
   - 长短比 ≤ 3:1
   - 总像素 in [655,360, 8,294,400]
3. **用 `auto`** 让模型自己选（放弃精确控制但省心）

---

### 10. 生成的 UI 看起来"太 AI"

**现象**：一眼就能看出是 AI 生成（symmetric 过度 / 奇怪渐变 / 假质感）

**根因**：过度依赖模型默认偏好，没给具体约束

**对策 Combo**（以下全部套用）：
1. **客观视觉描述代替主观夸奖**（Anti-slop Rule 1）
2. **具体的 state 描述**（不要全部"空闲"状态）：
   - 一个通知有 3 个未读
   - 某个元素是 hover 状态
   - 购物车里有 2 件商品
3. **realistic imperfections**：
   ```
   Show a subtle used feel: one card has "12 new" badge, 
   another shows "loading..." state, one avatar is cropped 
   showing only initials.
   ```
4. **真实的 data 方差**：不要所有数字都 +12%
5. **看 Dribbble / Mobbin** 找真实产品截图 → 描述它 → 生成

---

## 🆘 终极救援：如果都不行

### 换模型（不同模型不同毛病）
- gpt-image-2 文字强但偏保守
- 试 Nano Banana（Gemini 2.5 Flash Image Pro）
- 或者接受"mockup 不是截图"，用 Figma/设计工具做

### 接受局限
UI 生图现阶段**能到 85% 像真产品**，剩 15% 需要人工修：
- 文字微调（用 Photoshop / Figma 覆盖）
- 图标替换（用 Lucide 图标覆盖）
- 色彩微调（PS 调色）

**AI 图是起点，不是终点**。
