# 已安装 Skill 整理与分类说明

本文整理当前环境中可用的 skill，并补充每个 skill 的主要用途、适用场景和使用说明。  
整理范围包含：

- `$CODEX_HOME/skills`
- 系统内置 skill
- 当前插件带来的 skill

不把测试夹具或示例 skill 混入“正式常用 skill”中。

## 怎么使用 Skill

- Skill 一般不需要你手动“运行命令”，更多是当你的需求匹配它的描述时，系统会自动选择。
- 如果你明确知道要用哪个 skill，可以直接在需求里点名，例如“用 `docx` 帮我整理成 Word 文档”。
- 有些 skill 是“前置 skill”，尤其是 Figma 相关，必须和指定工具配套使用。

## 分类总览

1. 系统与平台能力
2. 文档与办公产物
3. 设计、Figma 与前端开发
4. 求职与职业发展
5. 学术研究与写作
6. 技能开发与工作流封装
7. 示例与测试用途 skill

---

## 1. 系统与平台能力

| Skill | 来源 | 主要用途 | 什么时候用 | 使用说明 |
|---|---|---|---|---|
| `imagegen` | 系统 | 生成或编辑位图图像 | 需要生成插画、海报、照片风格图、贴图、透明背景素材时 | 适合“产出图片资产”，不适合 SVG/HTML/CSS 原生界面改造 |
| `openai-docs` | 系统 | 查询 OpenAI 官方文档与最新模型能力 | 问 OpenAI API、模型选择、升级路径、官方能力差异时 | 优先走 OpenAI 官方资料，适合需要准确信息和引用的场景 |
| `browser` | 插件 | 使用 Codex 内置浏览器操作页面 | 需要打开 localhost、本地网页、截图、点击、检查页面时 | 偏向当前 App 内置浏览器场景 |
| `agent-browser` | 本地 | 更通用的浏览器自动化与网站交互 | 需要表单填写、自动点击、抓取页面、测试网站、操作网页应用时 | 比内置浏览器更偏“自动化代理”能力，适合复杂浏览器任务 |
| `find-skills` | 本地 | 帮你发现可用或可安装的 skill | 你不确定有没有对应 skill，想先找能力时 | 用于“找 skill”，不是直接完成业务任务 |
| `skill-installer` | 系统 | 安装新 skill | 想从 curated 列表或 GitHub 安装 skill 时 | 适合扩展能力，不负责 skill 内容设计 |

---

## 2. 文档与办公产物

| Skill | 来源 | 主要用途 | 什么时候用 | 使用说明 |
|---|---|---|---|---|
| `docx` | 本地 | 读写和编辑 Word 文档 | 需要 `.docx` 报告、信函、模板、带目录或页眉页脚的 Word 文件时 | 偏通用 Word 处理，适合生成和修改文档内容 |
| `documents` | 插件 | 高质量文档生成、审阅和渲染校验 | 需要更严格的 Word / Google Docs 交付、红线批注、版式核查时 | 比 `docx` 更强调“渲染后验证”的交付流程 |
| `Presentations` | 插件 | 生成 PPTX 演示文稿 | 需要做 PowerPoint、汇报 deck、PPT 方案时 | 适合结构化生成幻灯片 |
| `Spreadsheets` | 插件 | 生成、分析和修改表格 | 需要处理 `.xlsx`、`.csv`、公式、图表、表格分析时 | 适合做预算表、数据表、分析表和带格式电子表格 |

---

## 3. 设计、Figma 与前端开发

### 3.1 通用设计与前端

| Skill | 来源 | 主要用途 | 什么时候用 | 使用说明 |
|---|---|---|---|---|
| `frontend-design` | 本地 | 生成高质量前端界面与页面 | 需要落地网页、组件、落地页、仪表盘、UI 页面时 | 强调视觉质量，适合直接产出前端代码与样式 |
| `ui-ux-pro-max` | 本地 | 提供 UI/UX 设计知识库和风格建议 | 想做网站、后台、SaaS、移动端 UI/UX 方案时 | 偏“设计智能库”，适合规划、优化、审查界面 |
| `web-design-guidelines` | 本地 | 做 Web 界面规范审查 | 需要检查无障碍、交互规范、界面合规性时 | 适合 UI 评审而非直接从零设计 |
| `product-design-pipeline` | 本地 | 把需求脚本转成可执行设计交付 | 有脚本、纪要、需求草稿，想整理成 PRD、原型、Figma 设计时 | 适合从“需求材料”到“设计产物”的流水线 |
| `teaching-poster-rtf` | 本地 | 教学海报与数学课件视觉规则抽取 | 需要从参考图中总结版式、色彩、字体规则时 | 偏教育内容和中文教学海报场景 |
| `multi-object-compare-prompt` | 本地 | 批量生成中文数学教学页的提示词包 | 想把课程 JSON 和页面规则封装成可复用 prompt 包时 | 适合教学内容生产，而不是通用 UI 项目 |

### 3.2 Figma 专项

| Skill | 来源 | 主要用途 | 什么时候用 | 使用说明 |
|---|---|---|---|---|
| `figma-use` | 插件 | Figma 工具调用前置技能 | 需要在 Figma 中写入、编辑、检查节点、变量、布局时 | `use_figma` 工具前必须先走它，是核心前置 skill |
| `figma-create-new-file` | 插件 | 新建 Figma / FigJam / Slides 文件 | 需要新建空白 Figma 文件时 | `create_new_file` 工具前必须先走它 |
| `figma-generate-design` | 插件 | 把页面或界面生成到 Figma | 想把网页、模块、弹窗、面板写进 Figma 时 | 通常要和 `figma-use` 配合使用 |
| `figma-generate-diagram` | 插件 | 在 FigJam 生成流程图、架构图、时间线等 | 需要画流程图、架构图、时序图、ERD、状态图时 | `generate_diagram` 工具前必须先走它 |
| `figma-generate-library` | 插件 | 在 Figma 中构建设计系统与组件库 | 需要做 tokens、变量、组件、主题、设计系统对齐时 | 和 `figma-use` 搭配最佳 |
| `figma-code-connect` | 插件 | 维护 Figma Code Connect 模板文件 | 需要将 Figma 组件映射到代码片段时 | 适合设计到代码映射工作流 |
| `figma-use-figjam` | 插件 | FigJam 场景下使用 Figma 工具 | 主要做白板、流程、协作图时 | 是 `figma-use` 的 FigJam 场景补充 |
| `figma-use-slides` | 插件 | Slides 场景下使用 Figma 工具 | 在 Figma Slides 中制作幻灯片时 | 是 `figma-use` 的 Slides 场景补充 |

### 3.3 React / 前端工程专项

| Skill | 来源 | 主要用途 | 什么时候用 | 使用说明 |
|---|---|---|---|---|
| `vercel-react-best-practices` | 本地 | React / Next.js 性能优化与最佳实践 | 写 React、Next.js、数据获取、性能优化、重构时 | 偏工程与性能，不是视觉设计 skill |
| `vercel-composition-patterns` | 本地 | React 组合式组件架构模式 | 组件 boolean prop 太多、要做 compound components、context 设计时 | 适合组件 API 和架构层面的重构 |
| `vercel-react-native-skills` | 本地 | React Native / Expo 最佳实践 | 做 React Native、Expo、动画、列表性能、原生模块时 | 偏移动端工程实践 |
| `remotion-best-practices` | 本地 | Remotion 视频制作最佳实践 | 用 React 做视频、动效、脚本化生成视频时 | 适合视频内容和动态图像生产 |

### 3.4 前端评审类

| Skill | 来源 | 主要用途 | 什么时候用 | 使用说明 |
|---|---|---|---|---|
| `frontend-review` | 示例 | 前端代码评审 | 需要做 React / UI / 表单 / a11y / 安全 / 状态覆盖审查时 | 当前环境里有多个版本，说明它更像“示例 skill 家族”，可参考思路 |

---

## 4. 求职与职业发展

| Skill | 来源 | 主要用途 | 什么时候用 | 使用说明 |
|---|---|---|---|---|
| `career-assistant` | 本地 | 职业相关任务总入口 | 想统一管理简历、LinkedIn、求职信、面试准备、职业定位时 | 像一个职业教练总控台 |
| `getting-started` | 本地 | career-helper 使用入门指南 | 不知道职业技能包该怎么开始时 | 更像 onboarding 指南 |
| `resume-career-coach` | 本地 | 简历、求职信、LinkedIn、ATS、求职策略全套辅导 | 想改简历、写求职信、做 LinkedIn 优化、准备面试、提升 ATS 匹配时 | 是最完整的求职教练类 skill |
| `Resume Quantifier` | 本地 | 为简历补数字与量化表达 | 简历描述太虚，缺少指标、结果、规模信息时 | 适合补“提升了多少、负责了多大规模”等量化信息 |
| `tailored-resume-generator` | 本地 | 根据 JD 定制简历 | 有明确职位描述，想做定制版简历时 | 偏“一岗一版”的简历匹配优化 |

---

## 5. 学术研究与写作

| Skill | 来源 | 主要用途 | 什么时候用 | 使用说明 |
|---|---|---|---|---|
| `academic-research-writer` | 本地 | 学术研究文稿写作 | 论文、文献综述、技术报告、学术提案、毕业论文时 | 强调学术规范、可信来源和 IEEE 风格引用 |
| `scientific-writing` | 本地 | 科学论文 IMRAD 结构写作 | 需要按 IMRAD 结构撰写或修订研究稿件时 | 更偏论文结构、报告指南和学术写作规范 |

---

## 6. 技能开发与工作流封装

| Skill | 来源 | 主要用途 | 什么时候用 | 使用说明 |
|---|---|---|---|---|
| `skill-creator` | 系统 + 本地 | 创建或优化 skill | 想把一个工作流整理成 skill，或者改写现有 skill 时 | 当前环境里有系统版和本地版，目标接近，可视为同类能力 |
| `plugin-creator` | 系统 | 创建 Codex 插件骨架 | 想做本地 plugin、插件目录、manifest、市场条目时 | 用于 plugin 搭建，不是 skill 编写本身 |
| `yao-meta-skill` | 本地 | 把流程、提示词、文档打包成技能 | 想把重复流程沉淀成 skill，并做评估与打包时 | 偏高级“skill 工厂”能力 |
| `note-cleanup` | 示例 | 会议纪要清洗与结构化 | 想把凌乱笔记整理成清晰 Markdown 纪要时 | 可直接借鉴到日常纪要整理工作流 |
| `release-orchestrator` | 示例 | 软件发布准备与发布包编排 | 需要发布前检查、回滚计划、沟通材料、go/no-go 决策时 | 偏发布管理与协调 |
| `incident-command-governor` | 示例 | 事故指挥包和事件标准化 | 做事故分级、事件回顾、沟通口径整理时 | 偏 incident management 流程 |

---

## 7. 示例与测试用途 Skill

这类内容不建议作为“正式业务 skill”来使用，更多是给开发、测试和示范用。

| Skill | 来源 | 说明 |
|---|---|---|
| `frontend-review` 多版本 | `yao-meta-skill/examples/...` | 同名 skill 的演化示例，用于展示 skill 如何迭代 |
| `invalid-governance-skill` | `yao-meta-skill/tests/fixtures/...` | 治理校验测试夹具 |
| `broken-yaml-skill` | `yao-meta-skill/tests/fixtures/...` | 非法 YAML 测试夹具 |
| `broken-skill` | `yao-meta-skill/tests/fixtures/...` | 打包失败测试夹具 |

---

## 快速选型建议

如果你想更快找到合适 skill，可以按下面方式理解：

- 想做图片：`imagegen`
- 想查 OpenAI 官方能力：`openai-docs`
- 想操作网页或测试页面：`browser` 或 `agent-browser`
- 想做 Word：`docx` 或 `documents`
- 想做 PPT：`Presentations`
- 想做 Excel / 表格：`Spreadsheets`
- 想做网页界面：`frontend-design`
- 想做设计系统或把界面写进 Figma：`figma-*`
- 想优化 React / Next.js：`vercel-react-best-practices`
- 想做 React Native：`vercel-react-native-skills`
- 想做简历和求职材料：`resume-career-coach`
- 想写论文：`academic-research-writer` 或 `scientific-writing`
- 想做新 skill：`skill-creator` 或 `yao-meta-skill`

## 备注

- 当前环境里有一些“同类 skill 并存”的情况，例如 `docx` 和 `documents`、`browser` 和 `agent-browser`、`skill-creator` 的不同版本。这不是冲突，更像能力层次不同。
- Figma 相关 skill 中，`figma-use`、`figma-create-new-file`、`figma-generate-diagram` 这类前置 skill 要特别注意，它们不是“可有可无”的说明，而是工具调用前的必要准备。
- 示例和测试 skill 可以参考其结构和思路，但不建议直接当成正式生产技能。
