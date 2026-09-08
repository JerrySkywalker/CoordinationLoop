# Evidence and authority

English | [简体中文](evidence-and-authority.zh-CN.md)

Evidence explains what was observed or produced. Authority determines what may be changed or accepted. Coordination Loop keeps these concepts separate because increasingly autonomous execution makes it dangerous to treat a successful action as proof that the action was permitted.

## Evidence answers "what can we prove?"

Examples of evidence include a repository head, a test result, a CI check, a serialized execution result, a generated artifact, or an observation of an external resource.

Evidence can be strong or weak, fresh or stale, complete or partial. Good evidence is exact about identity and honest about uncertainty.

A statement from an agent is therefore not worthless, but it is only one possible input. The system should prefer independently inspectable facts when those facts matter to a transition.

## Authority answers "what may happen?"

Authority is about permission and scope. An executor may be allowed to edit a repository but not create a remote repository. It may be allowed to prepare a candidate but not merge it. It may be allowed to inspect infrastructure but not mutate production.

Successful execution does not retroactively create authority. An unauthorized side effect remains unauthorized even if the technical result is correct.

## Policy connects evidence and authority

Policy interprets what should happen given current facts and granted authority. It can require validation, limit retries, demand human review, or hold when a safe next transition cannot be proven.

This gives four distinct questions:

```text
Evidence:   What was observed or produced?
Authority:  What is permitted?
Policy:     Given the facts and permission, what path is admissible?
Acceptance: What may now become authoritative development state?
```

Collapsing these questions into one "success" flag makes autonomous development harder to reason about.

## Human authority remains explicit

Coordination Loop is designed for agent-assisted development, not the removal of human ownership. High-impact decisions may remain owner-gated even when an agent can technically perform them.

The point is not to force manual approval for every action. It is to make the boundary explicit so that delegation does not widen itself by implication.

## Ambiguity produces HOLD, not invented permission

When identity, authority, or an external side effect cannot be established safely, the correct state may be uncertainty. Coordination Loop treats that uncertainty as a reason to reconcile or involve a human, not as permission to guess, retry, or declare completion.

Concrete receipt formats, validation rules, and authority representations belong to the product implementations. The stable philosophy is simpler: **evidence and authority inform each other, but neither substitutes for the other.**
