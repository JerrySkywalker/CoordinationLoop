#!/usr/bin/env python3
"""Validate the Coordination Loop public portal's bilingual documentation shape."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROOT = (
    "README.md",
    "README.zh-CN.md",
    "MANIFESTO.md",
    "MANIFESTO.zh-CN.md",
    "AGENTS.md",
    "AGENTS.zh-CN.md",
    "CONTRIBUTING.md",
    "CONTRIBUTING.zh-CN.md",
    "SECURITY.md",
    "SECURITY.zh-CN.md",
    "LICENSE",
    "LICENSE.zh-CN.md",
)
REQUIRED_BRAND = (
    "docs/assets/brand/coordination-loop-mark.svg",
    "docs/assets/brand/coordination-loop-logo.svg",
    "docs/assets/brand/coordination-loop-banner.svg",
    "docs/assets/brand/coordination-loop-banner.zh-CN.svg",
)


def english_counterpart(chinese: Path) -> Path:
    return chinese.with_name(chinese.name.replace(".zh-CN.md", ".md"))


def chinese_counterpart(english: Path) -> Path:
    return english.with_name(english.stem + ".zh-CN.md")


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_ROOT + REQUIRED_BRAND:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    markdown = sorted(ROOT.rglob("*.md"))
    for path in markdown:
        if path.name.endswith(".zh-CN.md"):
            counterpart = ROOT / "LICENSE" if path.name == "LICENSE.zh-CN.md" else english_counterpart(path)
            if not counterpart.is_file():
                errors.append(f"Chinese document lacks English counterpart: {path.relative_to(ROOT)}")
        else:
            counterpart = chinese_counterpart(path)
            if not counterpart.is_file():
                errors.append(f"English document lacks Chinese counterpart: {path.relative_to(ROOT)}")

    english_readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""
    chinese_readme = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8") if (ROOT / "README.zh-CN.md").is_file() else ""
    if "README.zh-CN.md" not in english_readme:
        errors.append("root English README lacks a Chinese language link")
    if "README.md" not in chinese_readme:
        errors.append("root Chinese README lacks an English language link")
    if (ROOT / ".gitmodules").exists():
        errors.append(".gitmodules must not exist")

    if errors:
        print("BILINGUAL_DOCS=FAIL")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"BILINGUAL_DOCS=PASS markdown_documents={len(markdown)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
