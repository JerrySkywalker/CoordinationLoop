# Origin and design evolution

English | [简体中文](origin-and-design-evolution.zh-CN.md)

Coordination Loop is not based on the assumption that a larger swarm of agents is automatically a better development system. Its design direction follows a different sequence of pressures: as personal agent-assisted development scales, execution identity becomes increasingly transient while project identity must remain stable.

This page records that design logic without treating private development history as public product state.

## Stage 1 — Human and one agent

The simplest model works well: a person has a repository, opens one coding-agent session, asks for a change, reviews it, and commits the result.

In this environment, the active conversation can feel almost equivalent to the active development context. The distinction between session state and project state is easy to ignore.

## Stage 2 — Many sessions

Once several sessions work on different problems, conversation identity becomes fragile. A developer needs to know which session owns which change, which assumptions are still current, and whether another session has already changed the relevant repository state.

The first important separation appears:

**session identity is not development identity.**

## Stage 3 — Many repositories and workspaces

Real projects often span more than one repository, while one developer may also maintain unrelated projects in parallel. Git worktrees, branches, CI runs, and integration boundaries become part of the coordination problem.

The durable unit can no longer be "whatever is open in this terminal."

## Stage 4 — Many machines

Moving work between a workstation, laptop, server, or cloud runner makes machine-local state insufficient. A process can disappear while a repository mutation or external side effect remains.

The next separation becomes necessary:

**machine identity is not development identity.**

## Stage 5 — Many providers and internal agent graphs

Different providers may expose different lifecycle models, subagent systems, capabilities, and evidence. Binding the project model to any one of them would make provider replacement an architectural migration.

Therefore:

**provider and agent topology belong below the durable development-control boundary.**

## Stage 6 — Authoritative development continuity

The resulting design goal is not to build a bigger agent graph. It is to preserve a durable development program whose goals, authority, repository/resource identity, evidence, and accepted state survive changes in execution substrate.

This leads to the core philosophy now expressed by the portal:

- Goal is not Agent.
- Development identity is not Machine / Session / Provider.
- Claimed completion is not an authoritative state transition.

The four Coordination Loop products are an evolving implementation of this philosophy. The philosophy constrains direction; implementation evidence determines the eventual protocol details.
