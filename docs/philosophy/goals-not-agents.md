# Goals, not agents

English | [简体中文](goals-not-agents.zh-CN.md)

A development Goal is a durable logical unit of progress. An agent is a replaceable execution mechanism. Coordination Loop keeps those identities separate on purpose.

This document describes a product principle, not a frozen Goal schema.

## Why the distinction matters

Agent-oriented systems often begin with questions such as which agent should run next, how agents should delegate, or how a planner should split work into a task graph. Those are useful execution questions, but they are not sufficient to define the durable state of a software project.

A provider may restart an agent, replace its model, fan work out to subagents, or reorganize an internal task graph. If those changes redefine the project's Goal identity, then provider-local execution structure has accidentally become the project's source of truth.

Coordination Loop rejects that coupling.

## A Goal survives execution replacement

At the product-philosophy level, a Goal represents an intended development outcome with enough durable identity and boundary to remain meaningful across time. Its implementation representation may evolve, but the following principle should remain stable:

> Replacing an agent, provider, machine, session, or provider-local task graph must not silently create a different development goal, erase its history, or widen its authority.

A Goal may eventually be executed by a single coding agent, a provider-local multi-agent workflow, deterministic automation, CI/CD infrastructure, or a human action. The execution topology is not automatically promoted into the authoritative development graph.

## Goal graph and agent graph are different layers

Conceptually:

```text
Authoritative development layer

Goal A -----> Goal B -----> Goal D
                 \
                  -----> Goal C

---------------- execution boundary ----------------

A selected Goal may be executed by:

- one agent;
- a provider-local task DAG;
- several subagents;
- deterministic tooling;
- a human decision or action.
```

The upper graph answers questions about durable development progress. The lower graph answers questions about how an admitted unit of work gets executed.

## This is not an ontology commitment

The portal deliberately does not define a permanent `Goal -> Task -> WorkOrder -> Receipt` hierarchy. Concrete contracts, cardinalities, state vocabularies, and wire formats belong to the relevant product repositories and may change as CLH, CLE, CLF, and CLT mature.

What the portal commits to is narrower and more durable: **Goal is not Agent, and provider-local execution structure is not authoritative merely because it exists.**
