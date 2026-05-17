# Ingest, Query, and Lint

Summary: The wiki is maintained through three recurring operations: ingest new sources, query accumulated knowledge, and lint the graph for health issues.

## Ingest

Ingest turns a raw source into integrated wiki knowledge. The agent reads the source, extracts key claims and concepts, creates or updates relevant pages, updates [[concepts/indexing-and-logging|the index]], and records the work in the log.

Good ingest work touches all pages affected by the source. A source summary is useful, but it is not enough if the source also changes an existing concept page or introduces a contradiction.

## Query

Query uses the wiki as the primary context. The agent starts with `wiki/index.md`, reads relevant pages, and synthesizes an answer. If the answer is durable, it can become a new page so that exploration compounds instead of vanishing into chat.

## Lint

Lint is periodic wiki maintenance. The agent checks for broken links, orphan pages, stale claims, missing concept pages, unresolved contradictions, and data gaps. Scripted checks can catch mechanical issues, while LLM review catches semantic issues.

## Sources

- `raw/sources/llm-wiki-pattern.md`
- `AGENTS.md`
