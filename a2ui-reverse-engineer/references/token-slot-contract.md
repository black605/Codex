# Token、Slot 与 Sheet 契约

## 五段式 Token

统一名称：

```text
component.<base>.<variant>.<element>.<property>
```

要求：

- `base` 必须以 `a2-` 开头。
- 每段使用小写 kebab-case。
- CSS 编译名为 `--component-<base>-<variant>-<element>-<property>`。
- Token 保存 rawValue、compiledValue、category、sourceObservationIds、confidence、snapPolicy 和 status。

只对 spacing、常规 radius 和 grid gap 执行 4px 吸附。字体、行高、描边、图标尺寸、绝对坐标、光学边界和主视觉尺寸保持测量值，除非项目 Token Contract 明确要求转换。

## 三级 Slot

```text
Level 1：模块，例如 slot-card
Level 2：组件区域，例如 slot-card-header
Level 3：内容叶子，例如 slot-header-title
```

规则：

- 层级连续，禁止 Level 1 直接包含 Level 3。
- `slotId` 在页面范围内唯一。
- 每个 Slot 声明 `min`、`max`、`accepts` 和 `emptyPolicy`。
- Level 3 不得继续包含子 Slot。
- Slot 只描述结构和接受类型，不携带样式值或资源路径。

## Sheet A

只包含组件结构：

```text
componentId, baseClass, variant, layoutMode, slots,
dataRequirements, actionRequirements, guardrails,
sourceObservationIds, registryStatus
```

Guardrail 至少覆盖适用项：minHeight、minTouchTarget、titleMaxLines、prefixShrink、overflowPolicy、emptySlotPolicy。

## Sheet B

只包含视觉 Token：

```text
tokenName, cssVariable, category, rawValue, compiledValue,
snapPolicy, sourceObservationIds, confidence, status
```

不得携带 moduleTree、API 数据或资源文件路径。
