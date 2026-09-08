# Who Coordination Loop is for

English | [简体中文](who-this-is-for.zh-CN.md)

Coordination Loop is designed first for individual developers and small engineering teams whose coding-agent usage has outgrown a single chat, terminal, repository, or machine.

It is intentionally not positioned first as an enterprise "AI orchestration platform." The original pressure comes from ordinary development becoming operationally complex once autonomous execution is added.

## Individual developers with parallel work

A single developer may maintain several projects, keep multiple worktrees active, run more than one coding-agent session, and leave long-running work executing while attention moves elsewhere.

The problem becomes remembering which session is authoritative for which goal, which repository state was admitted, which work may still be running, and what is actually safe to do next. Coordination Loop aims to make those facts durable instead of reconstructing them from memory and chat history.

## Developers who work across machines

A desktop, laptop, workstation, home server, or cloud runner can each be useful execution locations. They should not become the identity of the development program.

Coordination Loop is relevant when work must survive movement between machines while preserving exact repository identity, authority, evidence, and uncertainty about external effects.

## Developers who expect providers to change

Today's preferred coding agent is not guaranteed to be tomorrow's. A project may move from one provider to another, or use different providers for different capabilities.

Provider independence means the durable development model should request capabilities and enforce boundaries without making one vendor's session model the definition of the project.

## Small teams that need explicit ownership

A small team can benefit from the same principles even without a large orchestration platform: one writer per admitted resource, explicit owner decisions for high-impact actions, durable handoff, bounded delegation, and evidence that can be reviewed independently of an agent's narrative.

The aim is not bureaucracy. The aim is to keep increasingly autonomous work understandable and reversible.

## When Coordination Loop may be unnecessary

If a project is short-lived, single-repository, handled in one interactive session, and has little need for durable delegation or recovery, ordinary Git, CI, issues, and a coding agent may already be enough.

Coordination Loop becomes more useful as development spans time, repositories, machines, providers, autonomous execution, or shared authority.
