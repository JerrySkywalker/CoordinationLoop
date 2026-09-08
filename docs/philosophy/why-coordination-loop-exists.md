# Why Coordination Loop exists

English | [简体中文](why-coordination-loop-exists.zh-CN.md)

Coordination Loop starts from a practical problem: coding agents are becoming capable enough to do meaningful work for long periods, but the durable identity of a software project cannot safely live inside an agent conversation.

A single developer can quickly accumulate several repositories, several branches and worktrees, multiple agent sessions, more than one machine, and eventually more than one provider. At that point, a chat transcript or a terminal process is no longer a reliable answer to basic development questions:

- What goal is actually being advanced?
- What state is currently accepted as true?
- What work is allowed to happen next?
- Which repository or resource is in scope?
- What authority was granted, and what remains forbidden?
- What evidence is sufficient to accept a transition?
- What should happen after a session, machine, or provider disappears?

Coordination Loop exists to keep those answers durable while execution remains replaceable.

## The problem is not a shortage of agents

A developer already has many ways to make an agent write code, call tools, run tests, or delegate to subagents. The harder problem appears one layer above execution: preserving development continuity when the execution mechanism changes.

An agent can be interrupted. A provider can change behavior. A laptop can go offline. A process can crash after an external side effect. A repository can move from one machine to another. None of those events should silently redefine the goal, erase authority, or turn uncertainty into permission to retry.

Coordination Loop therefore treats agent execution as a replaceable substrate rather than the durable center of the program.

## Development needs an authoritative layer

Software development already has durable engineering primitives: repositories, commit identities, branches, pull requests, CI results, artifacts, reviews, and releases. These are valuable because they can be inspected independently of a model conversation.

Coordination Loop builds on that Git/DevOps tradition while adding a development-control concern: a claim, log, commit, or CI result is evidence, but it does not automatically decide what the project is authorized to accept as its next state.

The durable control layer must preserve intent, identity, scope, authority, evidence, and handoff across time. It must also be willing to hold when truth is ambiguous.

## Goal-centric rather than agent-centric

The highest-level question is not "Which agent should run next?" It is "What development transition is currently safe and admissible?"

An execution provider may use one agent, many agents, a local task graph, or no agent at all. Those choices can change without becoming the durable identity of the development program.

This is why Coordination Loop is goal-centric, provider-independent, and machine-independent. The project should remain intelligible even if every current execution tool is replaced.

## A public philosophy, not a frozen protocol

This document states product philosophy rather than a protocol object model. Terms and wire formats inside CLH, CLE, CLF, or CLT may evolve as implementation evidence accumulates. The stable commitment is the separation between durable development control and replaceable execution.

A useful test for this portal is: **if an implementation component were rewritten tomorrow, would this principle still be true?** If yes, it belongs here. If not, its authoritative definition belongs in the relevant product repository.
