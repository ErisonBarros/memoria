# LLM Wiki

A pattern for building personal knowledge bases using LLMs.

This is an idea file designed to be copied into an LLM agent. Its goal is to communicate the high-level idea; the agent and user collaborate to build out the specific implementation.

## The core idea

Most document workflows with LLMs resemble retrieval-augmented generation: upload files, retrieve relevant chunks at query time, and generate an answer. This works, but the LLM rediscovers knowledge from scratch on each question. There is no accumulated synthesis.

The alternative is for the LLM to incrementally build and maintain a persistent wiki: a structured, interlinked collection of markdown files that sits between the user and the raw sources. When a new source arrives, the LLM reads it, extracts key information, and integrates it into the existing wiki by updating entity pages, revising topic summaries, recording contradictions, and strengthening or challenging the evolving synthesis.

The wiki is therefore a persistent, compounding artifact. Cross-references, contradictions, and synthesis are built once and then kept current.

The human curates sources, directs exploration, and asks questions. The LLM performs the summarizing, cross-referencing, filing, and bookkeeping. Obsidian can serve as the IDE, the LLM as the programmer, and the wiki as the codebase.

## Example uses

- Personal goals, health, psychology, self-improvement, journal entries, articles, and podcast notes.
- Long-running research projects over weeks or months.
- Reading companion wikis for books, including characters, themes, plot threads, and places.
- Business or team knowledge bases maintained from Slack threads, meeting transcripts, project documents, and customer calls.
- Competitive analysis, due diligence, trip planning, course notes, and hobby deep dives.

## Architecture

There are three layers:

1. Raw sources: curated source documents such as articles, papers, images, and data files. These are immutable and serve as source of truth.
2. The wiki: LLM-generated markdown files including summaries, entity pages, concept pages, comparisons, overviews, and syntheses. The LLM owns this layer.
3. The schema: an instruction document, such as `AGENTS.md`, that defines structure, conventions, and workflows for ingesting sources, answering questions, and maintaining the wiki.

## Operations

Ingest: the LLM reads a source, discusses or identifies key takeaways, writes a summary page, updates the index, updates relevant entity and concept pages, and appends to the log.

Query: the user asks questions against the wiki. The LLM searches relevant pages, reads them, synthesizes an answer with citations, and can file valuable answers back into the wiki.

Lint: the LLM periodically health-checks the wiki for contradictions, stale claims, orphan pages, missing cross-references, concepts without pages, and data gaps.

## Indexing and logging

`index.md` is content-oriented. It catalogs wiki pages with links, one-line summaries, and optional metadata. The LLM reads it first when answering queries.

`log.md` is chronological. It records ingests, queries, and lint passes using consistent headings that can be parsed with simple shell tools.

## Optional tools

A local markdown search engine can help as the wiki grows. qmd is one option because it provides local hybrid BM25/vector search and an MCP server. Simple custom scripts can also be sufficient at smaller scale.

## Tips

- Obsidian Web Clipper can convert web articles to markdown.
- Download article images locally so agents can inspect them reliably.
- Obsidian graph view helps reveal hubs and orphans.
- Marp can generate slide decks from markdown.
- Dataview can query YAML frontmatter.
- A wiki in git gains version history, branching, and collaboration.

## Why it works

The tedious part of maintaining a knowledge base is bookkeeping: cross-references, consistency, contradiction tracking, and updates across many pages. LLMs can perform that maintenance cheaply. The human focuses on source curation, analysis direction, and judgment.

The idea resembles Vannevar Bush's Memex: a private, curated knowledge store with associative trails between documents. The LLM supplies the missing maintainer.
