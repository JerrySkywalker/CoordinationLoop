# Product topology

English | [简体中文](product-topology.zh-CN.md)

The canonical runtime/product topology is exactly:

| ID | Product responsibility | Does not own |
| --- | --- | --- |
| CLH | Durable coordination contracts and validation: Requests, Goals, Decisions, Runs, authority, provenance, handoff, admission, and evidence-oriented primitives. | Authoritative DAG scheduling, provider/session lifecycle, starter distribution. |
| CLE | Authoritative development DAG/state, safe next-work selection, policy, bounded WorkOrders, resource admission, and validated authoritative transitions. | Coding-agent provider process/session lifecycle. |
| CLF | Bounded execution/worker/provider lifecycle, provider selection, and normalized execution evidence/receipts. | Mutation of CLE authoritative DAG state. |
| CLT | Thin bootstrap, distribution, starter guidance, provenance, and compatibility metadata. | A fifth runtime control plane or bundled runtime implementations. |

`PRODUCT = CLH + CLE + CLF + CLT`.

`JerrySkywalker/CoordinationLoop` is the public front door. Program Coordination is separate development memory and program control. Neither is a runtime product. Current visibility is represented in the [component manifest](../../components/manifest.yaml) without exposing private source details.
