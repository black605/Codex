# Guardrail Compiler Contract

把每条 Guardrail 同步编译到四个目标：

```text
Slot Contract + Props/JSON Schema + CSS Rules + Runtime Validation
```

至少支持：`prefixShrink`、`actionShrink`、`mainMinWidth`、`titleMaxLines`、`bodyMaxLines`、`minHeight`、`emptySlotPolicy` 和 `overflowPolicy`。

规则：

- prefix/action 的 `flex-shrink: 0` 只在对应规则声明时生成。
- main 的 `min-width: 0` 和 `flex: 1` 必须成对生成。
- line clamp 必须同时生成最大行数 Schema 约束或运行时截断策略。
- 空 Slot 仅按 `collapse` 规则折叠；不得全局应用 `[data-slot]:empty`。
- Guardrail 不得改变业务结果或读取未声明数据。
