# 文档

[English](README.md) | 简体中文

本门户记录 Coordination Loop 产品家族及其公开边界。

## 产品哲学

在阅读实现特定资料前，建议先理解公开的系统心智模型：

- [为什么需要 Coordination Loop](philosophy/why-coordination-loop-exists.zh-CN.md)
- [Coordination Loop 面向谁](philosophy/who-this-is-for.zh-CN.md)
- [起源与设计演进](philosophy/origin-and-design-evolution.zh-CN.md)
- [设计理念索引](philosophy/README.zh-CN.md)

这些页面有意避免在四个产品实现尚未收敛时提前冻结协议领域模型。

## 架构

- [架构概览](architecture/overview.zh-CN.md)：四个产品及其合同关系。
- [产品拓扑](architecture/product-topology.zh-CN.md)：CLH、CLE、CLF、CLT 各自拥有和不拥有的职责。
- [仓库模型](architecture/repository-model.zh-CN.md)：不通过源码嵌套或子模块实现的逻辑组合。
- [执行边界](architecture/execution-boundary.zh-CN.md)：权威开发控制与提供商内部执行的分离。
- [组件清单](../components/manifest.yaml)：机器可读的逻辑拓扑和已观察可见性。
- [发行集示例](../compatibility/release-set.example.yaml)：不使用子模块的非权威逻辑组合示例。

## 权威边界

门户拥有稳定的公开产品哲学、公开架构边界和系统心智模型。它不会替代各产品仓库中的权威实现文档，也不会替代独立 Program Coordination 仓库中的当前开发程序事实。
