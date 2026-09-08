# 产品拓扑

[English](product-topology.md) | 简体中文

规范的运行时/产品拓扑准确为：

| ID | 产品职责 | 不拥有的职责 |
| --- | --- | --- |
| CLH | 持久协调合同与验证：Requests、Goals、Decisions、Runs、权限、溯源、交接、准入及面向证据的原语。 | 权威 DAG 调度、提供商/会话生命周期、起步分发。 |
| CLE | 权威开发 DAG/状态、安全的下一项工作选择、策略、受限 WorkOrders、资源准入和已验证的权威迁移。 | 编码智能体提供商进程/会话生命周期。 |
| CLF | 受限执行/工作者/提供商生命周期、提供商选择和标准化执行证据/回执。 | 修改 CLE 权威 DAG 状态。 |
| CLT | 轻量引导、分发、起步指引、溯源和兼容性元数据。 | 第五个运行时控制平面或捆绑运行时实现。 |

`PRODUCT = CLH + CLE + CLF + CLT`。

`JerrySkywalker/CoordinationLoop` 是公开入口。Program Coordination 是独立的开发记忆和项目控制。二者都不是运行时产品。当前可见性在[组件清单](../../components/manifest.yaml)中表示，不披露私有源码细节。
