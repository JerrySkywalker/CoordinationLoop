# 架构概览

[English](overview.md) | 简体中文

Coordination Loop 是由持久协调内核、权威开发控制平面、受限执行平面和轻量引导产品组成的四产品家族。

```mermaid
flowchart TB
  H[CLH：持久合同与验证]
  E[CLE：权威目标与状态图]
  F[CLF：提供商与工作者执行]
  T[CLT：轻量引导与分发]
  E -->|序列化的受限 WorkOrder| F
  F -->|序列化的回执与证据| E
  H --> E
  H --> F
  T -->|溯源与兼容性元数据| H
  P[CoordinationLoop 门户] -. 公开项目入口 .-> H
  P -. 公开项目入口 .-> E
  P -. 公开项目入口 .-> F
  P -. 公开项目入口 .-> T
```

产品间箭头描述合同关系，而不是源码导入。门户以文档为先，没有运行时依赖角色。

请阅读[产品拓扑](product-topology.zh-CN.md)、[仓库模型](repository-model.zh-CN.md)和[执行边界](execution-boundary.zh-CN.md)，了解其定义性限制。
