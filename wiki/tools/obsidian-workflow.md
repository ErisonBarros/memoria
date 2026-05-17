# Obsidian Workflow

Summary: Obsidian can act as the browsing and visualization interface for a wiki that the LLM maintains in git-backed markdown files.

The LLM Wiki pattern works well when the user keeps an agent workspace and Obsidian vault open side by side. The agent edits markdown files; the user reviews pages, follows links, inspects graph structure, and gives direction.

## Useful Obsidian practices

- Use the graph view to identify hubs, isolated pages, and unexpected clusters.
- Use Web Clipper to capture web articles as markdown sources.
- Download remote images into a stable local attachment directory when image context matters.
- Use Dataview if page frontmatter becomes important for dynamic tables.
- Use Marp when wiki content should become a slide deck.

## Optional search tooling

At small scale, `wiki/index.md` is often enough. As the wiki grows, local markdown search can help agents find relevant pages faster. The seed source mentions qmd as one possible local hybrid search option, but the schema does not require a specific search engine.

## Sources

- `raw/sources/llm-wiki-pattern.md`
