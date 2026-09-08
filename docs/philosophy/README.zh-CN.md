# 设计理念

[English](README.md) | 简体中文

Coordination Loop 让开发连续性保持持久，同时把执行基底视为可替换对象。这些文档有意描述长期稳定的产品原则，而不会在四个产品实现尚未收敛时提前冻结协议对象模型。

## 从这里开始

- [为什么需要 Coordination Loop](why-coordination-loop-exists.zh-CN.md)——项目背后的实际问题。
- [Coordination Loop 面向谁](who-this-is-for.zh-CN.md)——首先面向个人开发者和小团队。
- [起源与设计演进](origin-and-design-evolution.zh-CN.md)——随着开发规模增长，会话、机器和提供商独立性如何自然出现。

## 核心原则

- [以目标为中心，而不是以智能体为中心](goals-not-agents.zh-CN.md)
- [开发连续性](development-continuity.zh-CN.md)
- [权威开发状态](authoritative-development-state.zh-CN.md)
- [提供商与机器独立](provider-machine-independence.zh-CN.md)
- [原生 Git/DevOps 实践](git-devops-native.zh-CN.md)
- [证据与权限](evidence-and-authority.zh-CN.md)
- [非目标](non-goals.zh-CN.md)

## 文档边界

门户拥有稳定的公开产品哲学和系统心智模型。具体 schema、生命周期状态、协议字段和实现事实属于 CLH、CLE、CLF 或 CLT；当前私有开发状态属于独立的 Program Coordination 仓库。

可以用一条简单原则判断边界：**产品哲学可以先于实现，领域对象模型应当跟随实现证据收敛。**
