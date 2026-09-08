# Goals, not agents

English | [简体中文](goals-not-agents.zh-CN.md)

A development Goal is the durable logical unit of progress. It has a defined outcome, scope, authority envelope, resource identity, evidence expectations, and relationship to other Goals.

An agent is an execution mechanism. Replacing an agent, provider, or internal task graph must not create a new Goal, discard its history, or widen its authority. Provider-local subagents remain below the execution boundary unless a future Coordination Loop contract explicitly represents them.

This distinction prevents a conversation transcript or a provider workflow DAG from becoming the accidental source of authoritative project truth.
