# WIKI_SCHEMA

This document defines the schema and operational rules for the LLM-maintained personal knowledge base.

## 1. Directory Structure
- `raw/`: Curated source documents (immutable).
- `raw/assets/`: Downloaded images and local media.
- `wiki/`: LLM-managed markdown files representing concepts, entities, summaries, etc.
- `wiki/index.md`: Content-oriented catalog of all wiki pages.
- `wiki/log.md`: Chronological, append-only record of operations.

## 2. Workflows

### A. Ingest Workflow
When a new source is provided in `raw/`:
1. **Read & Extract**: The LLM reads the source and identifies key takeaways, concepts, and entities.
2. **Create Summary**: Create a new page in `wiki/` (e.g., `wiki/Source_Title.md`) summarizing the document.
3. **Update Pages**: Update existing concept or entity pages in `wiki/` with new information. Flag any contradictions with older claims. Create new pages if necessary.
4. **Update Index**: Add entries for new pages to `wiki/index.md`.
5. **Log Operation**: Append an entry to `wiki/log.md` in the format: `## [YYYY-MM-DD] ingest | <Source Title>`.

### B. Query Workflow
When the user asks a question against the wiki:
1. **Search**: The LLM searches `wiki/index.md` to find relevant pages.
2. **Read & Synthesize**: Read the identified pages and synthesize an answer with citations.
3. **File Insights**: If the answer produces a valuable synthesis, comparison, or new connection, file it as a new page in `wiki/` and update `wiki/index.md`.
4. **Log Operation**: Append an entry to `wiki/log.md` in the format: `## [YYYY-MM-DD] query | <User Question>`.

### C. Lint Workflow
When requested to perform a health check:
1. **Check Constraints**: Look for contradictions, stale claims, orphan pages (no inbound links), missing cross-references, and concepts needing their own pages.
2. **Suggest Actions**: Propose creating new links, resolving conflicts, or suggesting external searches.
3. **Log Operation**: Append an entry to `wiki/log.md` in the format: `## [YYYY-MM-DD] lint | Health check results`.

## 3. Formatting Conventions
- Use standard markdown formatting.
- Include YAML frontmatter on wiki pages if appropriate (e.g., tags, date created, related sources).
- Use relative links to connect wiki pages.
