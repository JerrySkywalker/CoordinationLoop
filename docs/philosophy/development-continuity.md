# Development continuity

English | [简体中文](development-continuity.zh-CN.md)

Development identity is not a machine, session, provider, or process. Coordination Loop treats continuity as something engineered through durable facts, explicit authority, and safe reconciliation rather than inferred from whatever execution process happens to be alive.

## Sessions are transient

A coding-agent session can be useful context, but it is a poor durable identity. Sessions end, context windows change, processes restart, and providers may not preserve the same lifecycle semantics over time.

Losing a session must not imply losing the project's understanding of what was intended, what was authorized, or what may already have happened.

## Machines are execution locations

A workstation, laptop, server, or cloud runner may host execution, local repositories, credentials, or scarce resources. Those are important operational facts, but a machine is still not the identity of the development program.

Moving execution between machines should therefore be a reconciliation and admission problem, not a project-reset event.

## Interruption does not erase side effects

The most dangerous failure mode is not simply that an agent stops. It is that execution becomes uncertain after an external effect may already have happened.

Examples include a commit created before a crash, a pull request opened before a network timeout, a remote resource mutated without the local caller receiving confirmation, or a provider process disappearing while its final state is unknown.

In those cases, absence of a live session is not evidence that nothing happened. Unknown state is not permission to repeat a side effect.

Coordination Loop therefore favors fail-closed reconciliation: recover the exact durable identity and evidence that can be proven; hold when the external state remains ambiguous.

## Handoff is part of continuity

A durable handoff should let another execution context understand enough to continue without inheriting hidden authority from the previous process. Continuity means preserving identity and constraints, not silently transferring every capability of the interrupted executor.

## Continuity above providers

Provider-specific capabilities and lifecycle behavior can be admitted through explicit execution contracts, but they do not define the durable project model. A project should be able to replace an execution provider without rewriting what its goals mean.

This philosophy does not prescribe a single recovery protocol. Concrete lifecycle and reconciliation contracts belong to the relevant product repositories. The stable principle is that **execution may be transient while development identity remains durable.**
