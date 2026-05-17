# LLM Wiki Overview

Summary: An LLM Wiki is a personal knowledge base where an agent compiles raw sources into a maintained, interlinked markdown wiki so knowledge compounds over time.

The central move is to put a maintained wiki between the user and the source archive. Instead of asking an LLM to rediscover relevant chunks on every question, the agent integrates each source into a durable synthesis: pages are created, existing pages are revised, contradictions are recorded, and cross-references are added.

This makes the wiki a persistent artifact rather than a transient answer. The human remains responsible for curation, direction, and judgment, while the LLM handles the repetitive bookkeeping that usually causes personal wikis to decay.

## Architecture

- `raw/` stores immutable sources and acts as the source of truth.
- `wiki/` stores generated summaries, concept pages, entity pages, comparisons, and syntheses.
- `AGENTS.md` defines the schema and workflows that discipline the LLM's maintenance behavior.

## Operating loop

The wiki grows through three recurring operations: [[concepts/ingest-query-lint|ingest, query, and lint]]. These operations keep pages current, turn useful answers into durable notes, and surface maintenance needs before the graph becomes inconsistent.

## Why it matters

The value comes from accumulation. Cross-references and syntheses are created once, then reused and refined. This is especially useful for long-running research, personal reflection, team knowledge, book notes, competitive analysis, course notes, and any domain where knowledge arrives incrementally.

## Related pages

- [[concepts/persistent-compounding-wiki]]
- [[concepts/ingest-query-lint]]
- [[concepts/indexing-and-logging]]
- [[tools/obsidian-workflow]]

## Sources

- `raw/sources/llm-wiki-pattern.md`
