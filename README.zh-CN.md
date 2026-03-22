<!-- language-switch:start -->
[English](./README.md) | [中文](./README.zh-CN.md)
<!-- language-switch:end -->

# POP 角色包

由角色对象协议 (POP) 提供支持的可重用代理角色。

该仓库演示了如何加载和使用角色对象
构建 CrewAI 智能体。

## 一目了然

- 推荐运行时：Python 3.11 或 3.12
- 主要船员条目：`python crew.py`
- CI 烟雾验证：安装依赖项、导入 CrewAI、构建 Crew 对象并验证预期的代理和任务

## 运行时注释

目前建议使用 Python 3.11 或 3.12 使用此仓库。

某些 CrewAI 依赖链可能无法在较新的 Python 版本下安装
（例如 Python 3.14）由于旧依赖项中的传递构建问题。

## 例子

```bash
python demo/multi_role_demo.py
```

## 最少的船员AI 船员

该仓库包括一个由 POP 风格角色对象支持的最小 3 智能体 CrewAI 示例。

代理包括：

- 营销经理
- 软件工程师
- 产品设计师

跑步：

```bash
python crew.py
```

这演示了路径：

```text
persona object -> agent -> task -> crew
```

## CI 验证范围

GitHub Actions 工作流程在 Python 3.11 环境中验证模板结构：

- 安装依赖项
- 导入CrewAI
- 构建 Crew 对象
- 验证预期的代理和任务

它**不会**在 CI 中执行实时 `crew.kickoff()` 调用，因为完整执行通常需要模型/提供者配置和 API 凭证。

## 角色概念

POP 没有将角色嵌入提示中，而是将角色定义为可移植对象。

```text
persona object -> agent config
```
