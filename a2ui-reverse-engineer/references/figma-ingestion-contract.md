# Figma Ingestion Contract

## 目标

把 Figma MCP 原始上下文转换为可追踪证据，不直接生成正式 Registry、Schema 或运行时代码。

## 固定调用顺序

```text
node-specific Figma URL
→ get_design_context
→ variables / styles
→ Code Connect mappings
→ screenshot
→ download assets
→ evidence package
→ Observation normalizer
```

若 `get_design_context` 超时或截断，先读取节点地图，再对更小的子节点分别调用。不得静默降级为仅截图识别。

## Evidence Package

使用 `figma-evidence-package.schema.json`。至少记录：

- `runId`、`fileKey`、`nodeId`、原始 URL 和采集时间。
- Design Context、Variables、Code Connect、截图和素材的 artifactRef 与 SHA-256。
- 节点尺寸、来源版本和采集工具。
- 临时资源是否已持久化。
- `FigmaSourceGate` 的 checks、issues 与状态。

只保存大响应和二进制文件的引用，不把完整 MCP 响应嵌入状态机上下文。

## Observation 映射

| Figma 事实 | A2UI 字段 |
|---|---|
| node id | `figmaNodeId`、`sourceObservationIds` |
| component/instance | `semanticCandidate`、`componentCandidate` |
| auto layout | `bbox`、`parentCandidate`、布局证据 |
| text layer | `kind=text`、`text` |
| variable binding | `tokenCandidate`、`variableRefs` |
| Code Connect | `codeConnectRef`、Registry 匹配证据 |
| image/vector export | `visualAssetCandidate` |

置信度建议：Code Connect 命中不低于 0.98；组件实例与变量绑定不低于 0.95；仅层名推断不高于 0.75；仅视觉推断按 Perception 阈值处理。置信度不是批准状态。

## FigmaSourceGate

必须检查：

- URL 有明确 node id，且 fileKey/nodeId 与返回内容一致。
- Design Context、截图和变量引用来自同一节点或已声明的子节点。
- Code Connect 指向真实项目路径；未解析映射进入审核。
- 素材已下载或具有明确的数据源策略；临时 URL 不进入正式 Manifest。
- 原始参考代码与正式编译产物分离。
- Evidence Package 通过结构验证。

## 产物目录

```text
artifacts/runs/<runId>/figma/
├── evidence-package.json
├── design-context.json
├── variables.json
├── code-connect.json
├── screenshot.png
└── assets.json
```

通过 Gate 后，将 `evidence-package.json` 和归一化 `observation.json` 交给 Reverse Candidate 阶段。
