# Authoritative development state

English | [简体中文](authoritative-development-state.zh-CN.md)

Coordination Loop distinguishes the **Authoritative Development Goal / State Graph** from a provider-local Agent / Task / Workflow Graph.

The authoritative graph records which Goal is admissible, which resources are bound, which policy applies, and which validated transition may occur. A provider is free to organize its local work however it needs, but its local graph is not automatically authoritative.

Claims of completion are inputs to validation. Only a receipt and evidence that satisfy the required policy and authority checks can advance authoritative state.
