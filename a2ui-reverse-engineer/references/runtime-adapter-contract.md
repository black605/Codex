# Runtime Adapter Contract

A2UI Registry 是唯一事实源。其他运行时目录只能作为生成物：

```text
Canonical IR
├── A2UI Registry
├── json-render Catalog
├── OpenUI Library
└── Tool Calling Catalog
```

MVP 优先路径：严格 JSON Schema → A2UI Render Spec → Registry Resolver → 项目 A2UIRenderer。

要求：

- 未知 component、variant、prop、action 或 asset 一律 block。
- 流式传输只能更新已校验节点，不挂载未注册组件。
- json-render/OpenUI 适配器不得复制维护另一份组件事实源。
- Open-ended HTML 只能运行在隔离实验环境，不能进入正式 A2UI Runtime。
