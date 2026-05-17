# Memoria Agent Schema

You are maintaining an LLM-generated wiki. Treat the repository as three layers:

- `raw/`: immutable source material. Read from this layer, but do not modify existing source files unless the user explicitly asks you to correct the source archive.
- `wiki/`: maintained knowledge base. Create, update, refactor, and cross-link these markdown pages as knowledge evolves.
- `AGENTS.md`: operating schema. Update this file only when conventions or workflows need to change.

## Wiki conventions

- Use Obsidian-style links for wiki pages: `[[overview]]`, `[[concepts/ingest-query-lint]]`, or `[[tools/obsidian-workflow]]`.
- Prefer stable, lowercase, hyphenated file names.
- Every substantive wiki page should include:
  - A top-level `#` title.
  - A short summary near the top.
  - Links to related pages where useful.
  - A `## Sources` section that points back to raw files or other wiki pages.
- Preserve uncertainty. If sources conflict, record the conflict instead of smoothing it away.
- Keep raw-source citations specific enough that another agent can verify the claim later.
- Do not invent source-backed facts. If a statement is an interpretation, label it as synthesis or inference.

## Required special files

- `wiki/index.md` is the content-oriented catalog. Update it whenever pages are added, renamed, deleted, or substantially changed.
- `wiki/log.md` is chronological and append-only. Add entries using this format:

  ```markdown
  ## [YYYY-MM-DD] type | Short title

  - Summary: one-sentence description of what changed.
  - Touched: `wiki/page.md`, `wiki/other-page.md`.
  - Sources: `raw/sources/source.md`.
  ```

Accepted `type` values include `ingest`, `query`, `lint`, `maintenance`, and `schema`.

## Ingest workflow

When the user asks you to ingest source material:

1. Read the relevant source files in `raw/`.
2. Identify the source's core claims, entities, concepts, evidence, and contradictions with existing pages.
3. Create or update wiki pages so the new knowledge is integrated rather than isolated.
4. Update `wiki/index.md` with new or changed pages.
5. Append an `ingest` entry to `wiki/log.md`.
6. Run `python scripts/wiki_lint.py` when practical and fix any issues it reports.

## Query workflow

When the user asks a question against the wiki:

1. Read `wiki/index.md` first to identify likely relevant pages.
2. Read those pages and any linked pages needed for context.
3. Answer with citations to wiki files and, when relevant, raw sources.
4. If the answer is likely to be useful later, ask whether to file it as a wiki page, or file it directly if the user requested persistence.
5. If filing the answer, update `wiki/index.md` and append a `query` entry to `wiki/log.md`.

## Lint workflow

When the user asks for a wiki health check:

1. Run `python scripts/wiki_lint.py`.
2. Inspect for higher-level issues the script cannot catch: stale claims, contradictions, missing concept pages, shallow summaries, and orphaned but important pages.
3. Fix straightforward hygiene issues.
4. Record unresolved questions or recommended source searches in the relevant page or a new maintenance note.
5. Append a `lint` entry to `wiki/log.md`.
