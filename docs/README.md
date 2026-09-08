# Documentation

English | [简体中文](README.zh-CN.md)

This portal documents the Coordination Loop product family and its public boundaries.

## Product philosophy

Start with the public mental model before reading implementation-specific material:

- [Why Coordination Loop exists](philosophy/why-coordination-loop-exists.md)
- [Who Coordination Loop is for](philosophy/who-this-is-for.md)
- [Origin and design evolution](philosophy/origin-and-design-evolution.md)
- [Philosophy index](philosophy/README.md)

These pages intentionally avoid freezing a protocol ontology before the four product implementations settle.

## Architecture

- [Architecture overview](architecture/overview.md): the four products and their contract relationships.
- [Product topology](architecture/product-topology.md): what CLH, CLE, CLF, and CLT own and do not own.
- [Repository model](architecture/repository-model.md): logical composition without source nesting or submodules.
- [Execution boundary](architecture/execution-boundary.md): authoritative development control versus provider-local execution.
- [Component manifest](../components/manifest.yaml): machine-readable logical topology and observed visibility.
- [Release-set example](../compatibility/release-set.example.yaml): non-authoritative logical composition without submodules.

## Authority boundary

The portal owns stable public philosophy, public architecture boundaries, and system mental models. It does not replace authoritative implementation documentation in the individual product repositories or current development-program truth in the separate Program Coordination repository.
