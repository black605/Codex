# Token Normalizer Contract

保留测量值与编译值：

```text
rawValue → snapPolicy → compiledValue → semanticRef → platform outputs
```

吸附规则：

- spacing、gap：按 4px 阶梯吸附。
- 常规 radius：按 4px 阶梯吸附。
- typography、line-height、border、icon size、absolute position、hero optical bounds：默认不吸附。
- color：允许映射语义 Token，但保留原始色值和色差证据。
- 项目 Token Contract 可以覆盖默认规则。

Style Dictionary 只消费审核后的 Token 并生成平台产物，不负责视觉测量、审批或命名决策。五段式路径必须通过自定义 transform 编译为 CSS Variable。
