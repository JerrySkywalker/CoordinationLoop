# Repository model and logical composition

English | [简体中文](repository-model.zh-CN.md)

The four products remain independent repositories. The portal links and documents them; it does not nest their files, import their source trees, or use Git submodules.

Cross-product composition is logical. A future accepted release set can name the exact component identity, version, commit identity, artifact/protocol identity, and compatibility-set identity required together. The [release-set example](../../compatibility/release-set.example.yaml) is deliberately non-authoritative and has placeholders rather than private commit identities.

This mechanism records **logical composition of exact product states, not filesystem nesting**. Compatibility is validated through producer-owned serialized contracts, artifacts, and conformance evidence—not a submodule pointer or a source checkout embedded in another repository.

The separate Program Coordination repository retains development memory, architecture, roadmaps, decisions, and handoffs. It is not imported at runtime. This public portal likewise has no runtime dependency role.
