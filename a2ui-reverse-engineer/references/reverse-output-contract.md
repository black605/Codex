# Reverse Output Contract

最终逆向候选包包含：

- `runId`、`projectId`、`sourceRef`、`sourceHash`：运行与输入血缘。
- `status`：candidate、needs-review、passed 或 blocked。
- `observationsRef`：指向 PerceptionNode 产物。
- `sheetA`：组件结构矩阵。
- `sheetB`：五段式 Token 表。
- `renderSpec`：可空；只有前置 Gate 通过后才能存在。
- `gateResults`：每个 Gate 的 status、checks 和 issues。
- `issues`：阻断和人工确认项。

使用 `a2ui-reverse-output.schema.json` 校验基础结构，再用项目 Registry 验证引用是否可解析。JSON Schema 通过不代表 RegistryGate 或 VisualGate 通过。
