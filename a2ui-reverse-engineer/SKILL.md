---
name: a2ui-reverse-engineer
description: 将 Figma 节点、Figma 链接、UI 截图或设计稿逆向为可审核、可追踪的 A2UI Observation、Canonical A2UI IR、Sheet A 组件矩阵、Sheet B 五段式 Token、三级 Slot、Guardrail、JSON Schema、Registry Candidate 和受控 Render Spec。用于通过官方 Figma MCP 读取设计证据，执行 Token 归一化、契约等价编译、暂存注册、受控渲染和视觉 QA；在移动智能玩伴项目中必须继承 mobile-assistant-orchestrator 的 Schema、Manifest、Registry 和 Gate。
---

# A2UI 逆向工程 Skill

## 定位

把非结构化设计输入转换成候选 A2UI 契约，再由确定性编译器完成命名、注册匹配和渲染。不要让 LLM 直接写正式 Registry、HTML、CSS 或资源路径。

固定职责链：

```text
给图 → 提取 → 识别 → 归纳 → 使用 → 组合 → 生产
输入 → Observation → Candidate → Sheet A/B → Gate → Render Spec → Runtime/QA
输入 → Evidence → Canonical IR → Normalize/Compile → Staging Registry → Runtime/QA → Promotion
```

## 继承项目总控

位于 `/Users/tal/Documents/ChatGPT/工程化 ⚠️/designs/tomato-card-generation-flow` 时，依次读取并遵循：

1. `/Users/tal/.codex/skills/mobile-assistant-orchestrator/SKILL.md`
2. `.codex/skills/mobile-assistant-orchestrator/SKILL.md`
3. `pipeline/mobile-assistant.pipeline-manifest.json`
4. `pipeline/a2ui-three-node-state-machine.json`
5. Manifest 指向的 Layout、Component Registry、Token Map、Style Pack、Page Composition、Template、Variable、Action、Asset 和 Slot 契约

项目契约优先于本 Skill。找不到项目契约时只允许输出独立候选包，状态标记 `project-contract-unresolved`，不得声称完成注册或生产放行。

## 必读资源

- 生成或校验 Token、Slot、Sheet A/B 时读取 [references/token-slot-contract.md](references/token-slot-contract.md)。
- 调用 LLM 或设计系统提示词时读取 [references/prompt-contract.md](references/prompt-contract.md)。
- 生成最终候选包时读取 [references/reverse-output-contract.md](references/reverse-output-contract.md) 和 `references/a2ui-reverse-output.schema.json`。
- 读取 Figma URL 时读取 [references/figma-ingestion-contract.md](references/figma-ingestion-contract.md) 和 `references/figma-evidence-package.schema.json`。
- 生成统一中间协议时读取 [references/canonical-a2ui-ir-contract.md](references/canonical-a2ui-ir-contract.md) 和 `references/canonical-a2ui-ir.schema.json`。
- 归一化 Token 时读取 [references/token-normalizer-contract.md](references/token-normalizer-contract.md)。
- 编译防崩塌规则时读取 [references/guardrail-compiler-contract.md](references/guardrail-compiler-contract.md)。
- 注册、晋升或接入运行时时读取 [references/registry-lifecycle-contract.md](references/registry-lifecycle-contract.md) 和 [references/runtime-adapter-contract.md](references/runtime-adapter-contract.md)。

## 工作流

### 1. Intake

创建稳定 `runId`，记录输入 URI、source hash、尺寸、项目 Manifest 版本和请求来源。大文件只保存 `artifactRef`。

输入分支：

- Figma：先加载官方 `figma-design-to-code` Skill，再用 Figma MCP 读取目标 node 的 Design Context、Variables、Code Connect、截图和素材；记录 fileKey、nodeId 与证据引用。
- 截图：记录绝对路径、hash、宽高和 viewport。
- 已有 Observation：校验 source hash 后从 PerceptionGate 继续。

#### Figma 输入分支

Figma MCP 是 Intake 与 Perception 之间的证据适配器，不是最终代码生成器。读取 Figma 链接时：

1. 确认 URL 包含明确 `node-id`，解析 `fileKey` 和 `nodeId`。
2. 加载 `figma-design-to-code`，先调用 `get_design_context`；不得用截图代替。
3. 获取 Variables、Code Connect、节点截图和真实素材。
4. 保存原始响应引用，生成 Figma Evidence Package。
5. 按 Figma Ingestion Contract 归一化为 Observation。
6. 运行 `scripts/validate_figma_evidence.py`；通过 FigmaSourceGate 后进入 Reverse Candidate。

证据优先级：

```text
Code Connect > Figma Component > Figma Variable > Auto Layout / Layer > Screenshot > Model inference
```

`get_design_context` 返回的 React/Tailwind 只能作为设计表达参考。正式 JSON Schema 由确定性编译器生成；正式代码必须复用项目组件、Token、Registry 和 Renderer。

### 2. Perception

复用项目的截图提取脚本、Observation Schema、BBox、OCR、包含关系和资源候选审核流程。Perception 只能写 observation、evidence、confidence、bbox 和候选关系。

禁止写入：

```text
moduleTree, styleTokens, assetPaths, apiValues, generatedCode
```

低置信度项必须进入审核，不得自动批准。

### 3. Reverse Candidate

基于已确认 Observation 调用 Prompt Contract，生成：

```text
componentCandidates
slotCandidates
tokenCandidates
dataRequirements
actionRequirements
guardrailCandidates
```

所有候选必须携带 `sourceObservationIds`、`confidence` 和 `status`。LLM 输出只允许为 `candidate` 或 `needs-review`。

### 4. Canonical IR 与确定性编译

用纯代码完成：

1. 把候选归一为 Canonical A2UI IR；IR 是类型、Schema、Registry 和 Runtime Adapter 的唯一事实源。
2. 执行 `a2-` 基类、五段式 Token、三级 Slot 连续性和唯一性校验。
3. 用 `normalize_a2ui_tokens.py` 执行分类吸附；保留 rawValue、compiledValue 和 snapPolicy。
4. 用 `compile_guardrails.py` 把 Guardrail 同时编译为 Slot、Schema、CSS 和 Runtime 规则。
5. 用 `compile_contract_bundle.py` 生成 TypeScript、JSON Schema、Tool Schema、Token 和 Registry Candidate。
6. 匹配 Component Registry、Template Registry、Asset Manifest 和 Slot Binding。

不得由 LLM 决定最终组件注册、跨列规则、资源路径或 Token 注入。

### 5. Gates

按顺序执行：

```text
FigmaSourceGate（Figma 输入）或 PerceptionGate（截图输入）
→ ReverseSchemaGate
→ SlotGate
→ TokenNormalizationGate
→ GuardrailGate
→ ContractEquivalenceGate
→ RegistryCandidateGate
→ CompositionGate
→ RuntimeGate
→ VisualGate
→ PromotionGate
```

任一 Gate 未通过时停止下游正式写入，但保留候选、错误和审核页面。

### 6. Render Spec 与预览

只有 Schema、Slot、Token、Guardrail、契约等价和 Registry Candidate Gate 通过后才能生成 Render Spec。Render Spec 只能引用已注册的 componentId、templateId、variableId、actionId、slotId 和 assetToken。

在移动助手项目中优先复用：

```text
app/a2ui-runtime.ts
app/A2UIRenderer.tsx
pipeline/mobile-assistant.page-composition.json
```

流式传输可以逐步展示候选和校验结果，但不得在 Gate 完成前挂载未注册组件。A2UI Registry 是唯一事实源；json-render Catalog、OpenUI Library 和 Tool Catalog 只能由 Contract Bundle 自动生成。

### 7. QA 与交付

至少验证：Schema、命名、Token 完整性、Slot 连续性、Registry 解析、资源绑定、文字溢出、空 Slot、Reduced Motion 和目标视口。若有基准截图，输出视觉差分证据。

交付目录：

```text
artifacts/runs/<runId>/
├── run-manifest.json
├── observation.json
├── reverse-candidates.json
├── canonical-a2ui-ir.json
├── sheet-a.json
├── sheet-b.json
├── contract-bundle/
├── registry-candidate.json
├── render-spec.json
├── review.html
├── qa-report.json
└── package-manifest.json
```

运行验证器：

```bash
python3 /Users/tal/.codex/skills/a2ui-reverse-engineer/scripts/validate_reverse_output.py \
  artifacts/runs/<runId>/reverse-output.json
```

## 禁止事项

- 不把整张截图包装成 `<img>` 后声称完成设计转代码。
- 不从截图识别结果直接覆盖正式 Schema 或 Registry。
- 不生成任意 HTML 字符串、`eval`、页面 ID 特判或未登记 CDN。
- 不把视觉值写进 LayoutNode，也不让 ArtStyleNode 修改模块树。
- 不自动接受低置信度候选。
- 不在通用 Renderer 未实现时声称生产全放行。
- 不把 Figma MCP 返回的 React/Tailwind 参考代码直接提交为项目标准代码。
- 不把临时 Figma asset URL 写入正式 Asset Manifest。
- 不直接追加正式 Catalog；注册状态必须按 candidate → reviewed → compiled → runtime-validated → visual-validated → active 晋升。
- 不分别手写 TypeScript、Zod、JSON Schema 和 Tool Schema；必须从同一 Canonical IR 生成。
- 不允许晋升脚本原地覆盖正式 Registry。

## 结束报告

必须报告：`runId`、输入来源、各 Node 状态、各 Gate 结果、Sheet A/B 路径、Registry 匹配率、Render Spec 状态、QA 证据、人工确认项、阻断原因和下一步动作。
