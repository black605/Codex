---
name: cli-creator
description: >-
  中文说明：根据API、SDK或操作流程创建可复用、稳定的命令行工具。
  原始触发说明：根据 API 文档、OpenAPI 规范、curl 示例、SDK、Web 后台、管理脚本或本地工具，创建可复用的命令行工具。适用于把重复操作封装成稳定 CLI，让 Codex 或用户可以在任意项目目录中调用。
---

# CLI 工具创建器

创建真正可长期使用的命令行工具，而不是一次性脚本。目标是让未来的 Codex 线程或用户可以直接通过命令名调用它。

## 适用场景

- 把 API 文档封装成 CLI。
- 把常用 curl 请求变成稳定命令。
- 把后台管理操作变成可复用工具。
- 把本地脚本升级为可安装命令。
- 给 MCP、插件、内部平台、日志系统、部署系统做专用 CLI。
- 需要稳定 JSON 输出，方便 Codex 后续自动调用。

如果一个短脚本就能解决当前仓库里的临时任务，不要强行创建 CLI。

## 开始前确认

先明确：

- 工具名称：例如 `ci-logs`、`sentry-cli`、`figma-tool`、`buildkite-logs`。
- 来源材料：API 文档、OpenAPI、SDK、curl 示例、网页后台、已有脚本、历史命令。
- 核心任务：例如列出草稿、下载失败日志、搜索消息、上传媒体、读取队列。
- 安装方式：是否要放到 `~/.local/bin`，是否需要全局可用。

如果用户要个人工具且没有指定仓库，优先创建在：

```text
~/code/clis/<tool-name>
```

创建前检查命令名是否已被占用：

```bash
command -v <tool-name> || true
```

如果已存在，选择更清晰的命令名，或询问用户是否覆盖。

## 选择运行时

先检查机器上的可用工具链：

```bash
command -v cargo rustc node pnpm npm python3 uv || true
```

选择原则：

- 默认优先 Rust：适合长期可用 CLI，单二进制、速度快、参数解析和 JSON 处理稳定。
- 选择 TypeScript/Node：当官方 SDK、认证流程、浏览器自动化或现有项目生态更适合 Node。
- 选择 Python：当任务偏数据处理、本地文件转换、Notebook、SQLite、CSV/JSON 分析。

不要为了技术偏好选择会增加用户配置成本的语言。若最佳工具链缺失，要说明原因，并选择下一个可用方案。

在动手前，用一句话说明选择：

```text
我会用 <语言/工具链> 做这个 CLI，因为 <原因>，当前机器已安装 <工具链>。
```

## 命令设计原则

编码前先在对话中给出命令面设计：

- 二进制名称
- `--help`
- `doctor`
- 初始化配置
- 发现类命令
- 解析 ID 类命令
- 读取类命令
- 写入类命令
- 原始请求兜底命令
- 认证和配置方式
- 安装到 PATH 的命令

CLI 应尽量具备：

```bash
tool-name --help
tool-name --json doctor
tool-name init
tool-name list ...
tool-name get ...
tool-name search ...
tool-name create ...
tool-name update ...
tool-name delete ...
tool-name request ...
```

## JSON 输出约定

所有需要给 Codex 自动消费的命令都应支持：

```bash
--json
```

JSON 输出要稳定，错误也要机器可读：

```json
{
  "ok": false,
  "error": {
    "code": "missing_auth",
    "message": "缺少认证令牌"
  }
}
```

不要在 JSON 或错误里输出完整 token、密钥、cookie。

## 认证和配置

优先顺序：

1. 环境变量，例如 `GITHUB_TOKEN`、`SENTRY_AUTH_TOKEN`。
2. 用户配置文件，例如 `~/.<tool-name>/config.toml`。
3. 一次性参数，例如 `--api-key`，只用于临时测试。

`doctor --json` 应返回：

- 是否找到认证信息。
- 认证来源：`env`、`config`、`flag`、`provider`、`missing`。
- 当前版本。
- 目标 endpoint 是否可访问。
- 缺失的配置步骤。

永远不要打印完整 token。

## 写操作安全规则

- 写操作必须是明确动作：`create`、`update`、`delete`、`upload`、`retry`、`comment`。
- 写操作要尽量接受稳定 ID，而不是模糊名称。
- 如果服务支持，提供 `--dry-run`、`--preview` 或草稿模式。
- 不要把写操作隐藏在 `fix`、`debug`、`auto` 这类宽泛命令里。
- 删除、覆盖、批量修改必须有确认机制或 dry-run。

## 实现步骤

1. 理解来源材料和目标任务。
2. 设计命令面。
3. 选择语言和项目结构。
4. 搭建 CLI 项目。
5. 实现配置、认证、错误处理和 JSON 输出。
6. 实现核心读命令。
7. 实现必要写命令，并加 dry-run。
8. 添加 README：安装、配置、命令示例、JSON 约定。
9. 运行 `--help`、`doctor` 和至少一个真实/模拟命令验证。
10. 告诉用户安装路径和使用示例。

## 目录建议

```text
~/code/clis/<tool-name>/
  README.md
  src/
  tests/
  fixtures/
  examples/
```

## 参考资源

- `references/agent-cli-patterns.md`：面向 Codex/Agent 调用的 CLI 设计模式。
