#!/usr/bin/env python3
"""Basic hygiene checks for the Memoria markdown wiki."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
INDEX = WIKI / "index.md"
LOG = WIKI / "log.md"

WIKI_LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
LOG_HEADING_RE = re.compile(r"^## \[\d{4}-\d{2}-\d{2}\] (ingest|query|lint|maintenance|schema) \| .+")


def markdown_files() -> list[Path]:
    return sorted(WIKI.rglob("*.md"))


def resolve_wiki_link(source: Path, target: str) -> Path:
    target_path = Path(target)
    candidates: list[Path]
    if target_path.suffix == ".md":
        candidates = [WIKI / target_path, source.parent / target_path]
    else:
        candidates = [WIKI / f"{target}.md", source.parent / f"{target}.md"]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def check_required_files(errors: list[str]) -> None:
    for required in (INDEX, LOG):
        if not required.exists():
            errors.append(f"Missing required file: {required.relative_to(ROOT)}")


def check_titles(errors: list[str]) -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        if not text.startswith("# "):
            errors.append(f"Missing top-level title: {path.relative_to(ROOT)}")


def check_wiki_links(errors: list[str]) -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in WIKI_LINK_RE.finditer(text):
            target = match.group(1).strip()
            resolved = resolve_wiki_link(path, target)
            if not resolved.exists():
                errors.append(
                    f"Broken wiki link in {path.relative_to(ROOT)}: [[{target}]] -> {resolved.relative_to(ROOT)}"
                )


def check_log_headings(errors: list[str]) -> None:
    if not LOG.exists():
        return
    for line_number, line in enumerate(LOG.read_text(encoding="utf-8").splitlines(), start=1):
        if line.startswith("## ") and not LOG_HEADING_RE.match(line):
            errors.append(f"Malformed log heading at {LOG.relative_to(ROOT)}:{line_number}: {line}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_titles(errors)
    check_wiki_links(errors)
    check_log_headings(errors)

    if errors:
        print("Wiki lint failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Wiki lint passed: {len(markdown_files())} markdown files checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
