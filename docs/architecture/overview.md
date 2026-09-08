# Architecture overview

English | [简体中文](overview.zh-CN.md)

Coordination Loop is a four-product family with a durable coordination kernel, authoritative development control plane, bounded execution plane, and thin bootstrap product.

```mermaid
flowchart TB
  H[CLH: durable contracts and validation]
  E[CLE: authoritative Goal and state graph]
  F[CLF: provider and worker execution]
  T[CLT: thin bootstrap and distribution]
  E -->|serialized bounded WorkOrder| F
  F -->|serialized Receipt and evidence| E
  H --> E
  H --> F
  T -->|provenance and compatibility metadata| H
  P[CoordinationLoop portal] -. public project front door .-> H
  P -. public project front door .-> E
  P -. public project front door .-> F
  P -. public project front door .-> T
```

The arrows between products describe contract relationships, not source imports. The portal is documentation-first and has no runtime dependency role.

Read the [product topology](product-topology.md), [repository model](repository-model.md), and [execution boundary](execution-boundary.md) for the defining limits.
