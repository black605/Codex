# Registry Lifecycle Contract

正式状态机：

```text
candidate → reviewed → compiled → runtime-validated → visual-validated → active
```

旁路状态：`rejected`、`deprecated`、`superseded`。

晋升条件：

- Candidate Schema、Slot、Token、Guardrail 和 Contract Equivalence Gate 全部通过。
- Runtime 与 Visual Gate 有证据引用。
- 人工审批记录存在，包含 reviewer、approvedAt 和 sourceHash。
- implementation URI、Tool Schema、Token 和 Asset 引用均可解析。

晋升脚本必须写入新文件，禁止原地修改正式 Registry。正式合并由项目总控流程执行。
