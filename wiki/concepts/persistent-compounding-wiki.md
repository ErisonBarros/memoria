# Persistent Compounding Wiki

Summary: The defining feature of an LLM Wiki is that synthesis is stored, linked, and maintained rather than regenerated from scratch for each question.

In a retrieval-only workflow, the LLM answers by finding source chunks at query time. That can work for isolated questions, but subtle questions require the same synthesis work repeatedly. Connections made in one session often disappear into chat history.

A persistent compounding wiki changes the unit of progress. Each ingest or useful query leaves behind improved pages: updated concepts, new links, contradiction notes, and revised summaries. Later questions start from that accumulated structure.

## Maintenance implications

For the compounding effect to work, the agent should prefer integration over isolated note creation:

- Update existing pages when new sources change the picture.
- Create new pages for recurring concepts, entities, or comparisons.
- Add links from old pages to new pages and from new pages back to relevant context.
- Preserve conflicts explicitly so later sources can resolve or sharpen them.
- Keep [[concepts/indexing-and-logging|index and log files]] current so navigation remains cheap.

## Sources

- `raw/sources/llm-wiki-pattern.md`
