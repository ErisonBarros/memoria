# Indexing and Logging

Summary: `wiki/index.md` is the wiki's content map, while `wiki/log.md` is its chronological memory.

## Index

The index is organized by content category. It lists pages, short descriptions, and source summaries so agents can quickly identify which pages matter for a query or update. At moderate scale, this can replace heavier retrieval infrastructure.

## Log

The log is append-only and chronological. Each entry records what happened, what files changed, and which sources were used. Consistent headings make the log parseable with shell tools and help future agents understand recent activity.

## Relationship

The index answers, “What exists and where should I look?” The log answers, “What happened recently and why did the wiki change?” Both are required for reliable long-running maintenance.

## Sources

- `raw/sources/llm-wiki-pattern.md`
- `wiki/index.md`
- `wiki/log.md`
