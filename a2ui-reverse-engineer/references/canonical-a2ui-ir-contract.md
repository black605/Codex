# Canonical A2UI IR Contract

Canonical A2UI IR 是组件结构、Token、Guardrail、类型、Tool Schema、Registry 和 Runtime Adapter 的唯一事实源。

每个组件必须包含：

```text
componentId, version, variant, source, slots, props, tokens,
guardrails, actions, implementation, status
```

规则：

- `componentId` 和 `baseClass` 使用 `a2-` kebab-case。
- Slot 使用连续三级结构，页面内唯一。
- Token 使用 `component.<base>.<variant>.<element>.<property>`。
- 每个事实保留 `sourceObservationIds`、confidence 和 status。
- `implementation` 只保存 Registry URI，不内嵌任意代码。
- Candidate 不得声明为 active。

用 `canonical-a2ui-ir.schema.json` 校验结构。下游编译器只能读取已校验 IR。
