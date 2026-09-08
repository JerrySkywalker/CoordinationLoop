# Contributing

English | [简体中文](CONTRIBUTING.zh-CN.md)

Thank you for helping make the public front door clear and trustworthy.

## Scope

This repository contains project-facing documentation, original portal branding, and logical composition examples. It does not host runtime source from the four product repositories.

## Before opening a change

1. Keep the English and Simplified Chinese documents meaningfully aligned.
2. Verify product boundaries and public visibility claims from current authoritative sources.
3. Do not add submodules, copied implementation, private evidence, credentials, raw sessions, or private commit identifiers.
4. Keep architecture claims provider-neutral unless a provider-specific contract is explicitly accepted.

## Local checks

```text
python scripts/check_bilingual_docs.py
git diff --check
```

Please use focused commits and preserve work you did not create. Security-sensitive reports belong in the process described in [SECURITY.md](SECURITY.md), not in a public issue.
