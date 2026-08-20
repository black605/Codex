# Skills Backup

> Synced by [Skills Manager](https://github.com/cchao123/skills-managers) — a desktop app for managing AI coding agent skills.

## Use as a Claude Code marketplace

This repository is auto-generated as a [Claude Code plugin marketplace](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces). Each skill below is exposed as an individually installable plugin.

In Claude Code, add this marketplace:

```bash
/plugin marketplace add Black605/Codex
```

Then install any skill you want:

```bash
/plugin install a2ui-reverse-engineer@codex
```

Browse all available skills with `/plugin` after adding the marketplace, or see the full list in [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json).

## Skills (30)

| # | Skill | Description |
|---|-------|-------------|
| 1 | **a2ui-reverse-engineer** | 将 Figma 节点、Figma 链接、UI 截图或设计稿逆向为可审核、可追踪的 A2UI Observation、Canonical A2UI IR、Sheet A 组件矩阵、Sheet B 五段式 Token、三级 Slot、Guardrail、JSON Schema、Registry Candidate 和受控 Render Spec。用于通过官方 Figma MCP 读取设计证据，执行 Token 归一化、契约等价编译、暂存注册、受控渲染和视觉 QA；在移动智能玩伴项目中必须继承 mobile-assistant-orchestrator 的 Schema、Manifest、Registry 和 Gate。 |
| 2 | **academic-paper-composer** | 中文说明：基于真实项目与论文初稿生成可提交的本科论文定稿及返工报告。 原始触发说明：Use when the user needs to turn a real software engineering / computer science project and an existing thesis draft into a submission-ready undergraduate thesis manuscript. Trigger for requests such as "根据项目把论文改成定稿", "按学校模板排版成最终版", "复制初稿后生成定稿 Word", "为定稿降查重", "根据PaperPass报告降AIGC", "继续在手改初稿上改", "恢复原来的图表和数据库说明", or when academic-paper-strategist has already produced an evidence-backed rewrite plan. Outputs a cleaned manuscript, final DOCX workflow, and a separate rework report. |
| 3 | **academic-paper-strategist** | 中文说明：基于真实代码与学校要求规划论文结构、证据映射和改写方案。 原始触发说明：Use when the user needs to plan, de-risk, or ground a software engineering / computer science undergraduate thesis from a real codebase before final writing. Trigger for requests such as "根据项目写毕业论文", "先做论文大纲", "用真实项目材料规划论文", "检查论文是否脱离代码", "根据检测报告降查重", "根据AIGC报告改写定稿", "继续在手改初稿上改", or when an existing draft thesis must be reworked against a school format sample. Produces an evidence-backed outline, chapter rewrite plan, figure plan, and handoff package for academic-paper-composer. |
| 4 | **ai-image-frontend-ui** | INTP Way · 三位一体 UI 生成系统—— 用 **image-2 直接生图 + MCP 工具链 + 完整 prompt 工程**  打造跨模态闭环，生成前端 UI 截图、Web 界面、移动 app 屏幕、海报、Dashboard、设计系统、Landing page。  融合权威来源：OpenAI Cookbook + fal.ai Anti-slop + Anthropic 官方反 AI slop 规则 + 泄露的 Claude Design 内部工作流 + ConardLi web-design-skill + 9 大美学家族。  独有能力（ConardLi 做不到）：image-2 视觉意图锚点 + MCP 真素材采集 + 跨模态验证闭环。  |
| 5 | **ai-image-generation** | 中文说明：用于执行“ai image generation”相关任务，并提供结构化流程与专业产出支持。 原始触发说明：Generate AI images with GPT-Image-2, FLUX, Gemini, Grok, Seedream, Reve and 50+ models via inference.sh CLI. Models: GPT-Image-2, FLUX Dev LoRA, FLUX.2 Klein LoRA, Gemini 3 Pro Image, Grok Imagine, Seedream 4.5, Reve, ImagineArt. Capabilities: text-to-image, image-to-image, inpainting, LoRA, image editing, upscaling, text rendering. Use for: AI art, product mockups, concept art, social media graphics, marketing visuals, illustrations. Triggers: flux, image generation, ai image, text to image, stable diffusion, generate image, ai art, midjourney alternative, dall-e alternative, text2img, t2i, image generator, ai picture, create image with ai, generative ai, ai illustration, grok image, gemini image, gpt image, openai image, chatgpt image |
| 6 | **ai-learning-coach** | 中文说明：制定AI学习路线、拆解知识主题并生成练习、复习与进度计划。 原始触发说明：面向个人 AI 学习的中文学习教练。适用于制定 AI 学习路线、拆解大模型/Agent/MCP/RAG/提示词/AI 产品/AI 编程等主题，设计项目练习，整理学习笔记，生成复习计划，跟踪学习进度，并把资料转化为可执行学习任务。 |
| 7 | **ai-learning-coach-zh** | 中文说明：用中文制定技能学习路线、练习计划、阶段测试与复盘方案。 原始触发说明：当用户想用 AI 学习一项新技能，或者请求学习路线图、7天计划、概念讲解、练习设计、错误分析、阶段测试、作品批改、30天升级计划时，使用这个技能。也适用于用户希望 AI 扮演教练、导师、陪练或复盘助手的场景，尤其适合从零基础到初级进阶的技能学习支持。 |
| 8 | **ai-news-scout** | 中文说明：搜索、筛选并整理高价值AI动态，生成精简日报或周报。 原始触发说明：AI领域信息差日报生成工具。通过3批并行搜索高效采集全网AI新闻，筛选去重后输出精炼的信息差日报。当用户提到"搜集AI新闻"、"AI信息差"、"今日AI动态"、"AI新闻整理"、"帮我找AI新闻"、"AI日报"、"AI周报"、"信息差选题"时触发。 |
| 9 | **ai-slop-cleaner** | [OMX] Run an anti-slop cleanup/refactor/deslop workflow |
| 10 | **analyze** | [OMX] Run read-only deep repository analysis and return a ranked synthesis with explicit confidence, concrete file references, and clear evidence-vs-inference boundaries. Use when a user says 'analyze', 'investigate', 'why does', 'what's causing', or needs grounded cross-file explanation before any changes are proposed. |
| 11 | **animejs** | 中文说明：为HyperFrames编写可控、可定位且可稳定渲染的Anime.js动画。 原始触发说明：Anime.js adapter patterns for HyperFrames. Use when writing Anime.js animations or timelines inside HyperFrames compositions, registering animations on window.__hfAnime, making Anime.js seek-driven and deterministic, or translating Anime.js examples into render-safe HyperFrames HTML. |
| 12 | **article-to-ppt-outline** | 中文说明：将长文转为带视觉建议和讲师逐字稿的结构化PPT大纲。 原始触发说明：将长篇文档、业务教材或文章，转换为带有"视觉排版建议"和"讲师口语化逐字稿"的结构化 PPT 大纲。适用于需要快速备课、制作汇报演示文稿的场景。当用户提供长文本并要求生成 PPT、演示大纲、幻灯片内容时触发此技能。 |
| 13 | **autoresearch** | [OMX] Stateful validator-gated research loop with native-hook persistence |
| 14 | **autoresearch-goal** | [OMX] Durable professor-critic research workflow over Codex goal mode without reviving deprecated omx autoresearch |
| 15 | **baoyu-design** | 中文说明：生成黑白线框图、可交互HTML原型、高保真界面和设计系统。 原始触发说明：Create polished design artifacts as self-contained HTML: UI mockups, interactive prototypes, wireframes, landing pages, dashboards, app screens, mobile apps, slide decks (a.k.a. PPT / PowerPoint presentations), and visual explorations. Use whenever the user asks to design, mock up, prototype, wireframe, visualize, explore, or make a PPT/deck for an interface, product screen, user flow, content layout, visual artifact, or pitch/deck concept, even if they do not say "design". Also use to export a deck built with this skill to PowerPoint (PPT/PPTX) — but only decks authored here (deck-stage / this skill's slide-structured HTML), NOT arbitrary HTML, so confirm the target is such a deck first. Also use for setting up, importing, or authoring reusable design systems, UI kits, brand tokens, or component libraries. Harness-agnostic for Claude Code, Cursor, Codex Agent, and similar file-capable agents. |
| 16 | **best-practice-research** | [OMX] Bounded best-practice research wrapper using official/upstream evidence first |
| 17 | **cancel** | [OMX] Cancel any active OMX mode (autopilot, ralph, ultrawork, ecomode, ultraqa, swarm, ultrapilot, pipeline, team) |
| 18 | **cc-design** | 中文说明：通过需求澄清与设计规划生成高保真、可交互的HTML界面。 原始触发说明：High-fidelity HTML design and prototype creation. Use this skill whenever the user asks to design, prototype, mock up, or build visual artifacts in HTML — including slide decks, interactive prototypes, landing pages, UI mockups, animations, or any visual design work. Also use when the user mentions Figma, design systems, UI kits, wireframes, presentations, or wants to explore visual design directions. Even if they just say "make it look good" or "design a screen for X", this skill applies. |
| 19 | **cli-creator** | 中文说明：根据API、SDK或操作流程创建可复用、稳定的命令行工具。 原始触发说明：根据 API 文档、OpenAPI 规范、curl 示例、SDK、Web 后台、管理脚本或本地工具，创建可复用的命令行工具。适用于把重复操作封装成稳定 CLI，让 Codex 或用户可以在任意项目目录中调用。 |
| 20 | **clone-website** | 中文说明：分析目标网站的内容、资源和样式并重建可运行的高还原页面。 原始触发说明：Reverse-engineer and clone one or more websites in one shot — extracts assets, CSS, and content section-by-section and proactively dispatches parallel builder agents in worktrees as it goes. Use this whenever the user wants to clone, replicate, rebuild, reverse-engineer, or copy any website. Also triggers on phrases like "make a copy of this site", "rebuild this page", "pixel-perfect clone". Provide one or more target URLs as arguments. |
| 21 | **code-safety-reviewer** | 中文说明：检查代码变更中的漏洞、危险操作、数据丢失和上线风险。 原始触发说明：在提交、合并、上线或大范围重构前，对代码变更做安全和风险审查。适用于检查 bug、危险文件操作、密钥泄露、权限绕过、注入风险、数据丢失、危险命令、缺失测试、回滚风险和生产事故隐患。 |
| 22 | **css-animations** | 中文说明：为HyperFrames编写可定位、可预览且可稳定渲染的CSS动画。 原始触发说明：CSS animation adapter patterns for HyperFrames. Use when authoring CSS keyframes, animation-delay based timing, animation-fill-mode, animation-play-state, or CSS-only motion that HyperFrames must seek deterministically during preview and rendering. |
| 23 | **design-taste-frontend** | 中文说明：提升前端界面的视觉品位、品牌辨识度和整体设计差异化。 原始触发说明：Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design systems when applicable, audit-first on redesigns, strict pre-flight check. |
| 24 | **design-tip-coach** | 中文说明：针对界面设计问题提供精简、清晰且可执行的设计优化建议。 原始触发说明：[TODO: Complete and informative explanation of what the skill does and when to use it. Include WHEN to use this skill - specific scenarios, file types, or tasks that trigger it.] |
| 25 | **doc** | 中文说明：读取、创建和编辑Word文档，并检查排版与视觉还原效果。 原始触发说明：Use when the task involves reading, creating, or editing `.docx` documents, especially when formatting or layout fidelity matters; prefer `python-docx` plus the bundled `scripts/render_docx.py` for visual checks. |
| 26 | **excalidraw-diagram** | 中文说明：创建可编辑的Excalidraw流程图、架构图和概念关系图。 原始触发说明：Create Excalidraw diagram JSON files that make visual arguments. Use when the user wants to visualize workflows, architectures, or concepts. |
| 27 | **fireworks-tech-graph** | 中文说明：将系统、架构或工作流描述转换为专业SVG和PNG图表。 原始触发说明：Use when the user wants to create any technical diagram - architecture, data flow, flowchart, sequence, agent/memory, or concept map - and export as SVG+PNG. Trigger on: "画图" "帮我画" "生成图" "做个图" "架构图" "流程图" "可视化一下" "出图" "generate diagram" "draw diagram" "visualize" or any system/flow description the user wants illustrated. |
| 28 | **github-trending-sketch** | 中文说明：将GitHub热门项目整理成清晰、有趣的手绘风格信息图。 原始触发说明：[TODO: Complete and informative explanation of what the skill does and when to use it. Include WHEN to use this skill - specific scenarios, file types, or tasks that trigger it.] |
| 29 | **hatch-pet** | Create, repair, validate, visually QA, and package Codex-compatible v2 animated pets from character art, generated images, company or prospect brand cues, or visual references. Use for any new Codex pet, custom mascot, non-pixel pet style, brand-inspired pet, existing-pet repair, or 8x11 spritesheet workflow requiring all 9 standard animation rows, 16 look directions, deterministic assembly, QA artifacts, and spriteVersionNumber 2 packaging. |
| 30 | **workplace-english-coach** | 中文说明：润色职场英语表达并提供发音、重音、连读和实用口语训练。 原始触发说明：Automatically coach any English word, phrase, sentence, or passage the user sends, especially for practical workplace use. Explain meaning and usage, correct and polish English, prepare emails, chat messages, meetings, presentations, status updates, interviews, and role-play, and teach pronunciation with IPA, stress, rhythm, linking, reductions, and speaking chunks. Trigger whenever the user's message is primarily English, even if they do not explicitly request teaching or invoke the skill. Also use for 工作英语, 职场英语, 英语表达, 翻译工作消息, 邮件润色, 会议口语, 汇报表达, 发音, 连读, 跟读, or workplace conversation practice. |

