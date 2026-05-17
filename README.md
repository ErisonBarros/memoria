# Memoria

Memoria is a starter vault for the **LLM Wiki** pattern: a personal knowledge base where an LLM incrementally turns immutable raw sources into a persistent, interlinked markdown wiki.

The repository is intentionally lightweight. It gives an agent a schema to follow, a place for raw sources, a wiki layer for generated pages, and a small lint script for basic hygiene checks.

## Repository layout

```text
.
├── AGENTS.md                 # Operating schema for LLM wiki maintenance
├── raw/
│   └── sources/              # Immutable source material
├── scripts/
│   └── wiki_lint.py          # Basic wiki health checks
└── wiki/
    ├── index.md              # Content-oriented catalog
    ├── log.md                # Chronological activity record
    ├── overview.md           # High-level synthesis
    ├── concepts/             # Concept pages
    └── tools/                # Tooling and workflow notes
```

## How to use this repo

1. Add source documents to `raw/sources/` without editing existing source files in place.
2. Ask your LLM agent to ingest one or more sources using the workflow in `AGENTS.md`.
3. Review the resulting wiki pages in Obsidian, a markdown editor, or your agent workspace.
4. Ask questions against the wiki; useful answers can be filed back as new wiki pages.
5. Periodically run the wiki lint check:

```bash
python scripts/wiki_lint.py
```

## Core principle

The raw layer is the source of truth, but the wiki is the compounding artifact. New sources should update existing pages, add cross-references, record contradictions, and append to the log so knowledge accumulates instead of being re-derived from scratch.
