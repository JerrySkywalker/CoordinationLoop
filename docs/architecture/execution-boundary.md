# Execution boundary

English | [简体中文](execution-boundary.zh-CN.md)

The execution boundary separates authoritative development control from provider-local execution detail.

```text
Authoritative Goal / State Graph (CLE)
  -> bounded serialized WorkOrder
  -> provider eligibility and execution lifecycle (CLF)
  -> normalized Receipt and evidence
  -> deterministic validation, policy, and authority checks (CLE)
  -> accepted state transition or HOLD
```

CLF may resolve an eligible provider and manage its execution-side lifecycle. It does not mutate CLE's authoritative DAG. CLE may request capabilities in a WorkOrder; it does not own provider process/session lifecycle or use provider-local workflow structure as authoritative state.

An internal provider may use subagents, a local task DAG, or another implementation strategy. Those details are replaceable and bounded by the admitted WorkOrder. They cannot widen resources, authority, budget, deadline, or delegation. Unknown external state fails closed.

The architecture is provider-neutral. Current provider validation may still be primarily Codex-oriented; that observation is not an architectural dependency or a production claim.
