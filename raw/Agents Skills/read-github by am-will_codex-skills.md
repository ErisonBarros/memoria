---
sourceFile: "read-github by am-will/codex-skills"
exportedBy: "Kortex"
exportDate: "2026-05-17T23:05:02.686Z"
---

# read-github by am-will/codex-skills

b0159efc-1758-4b76-96aa-5e8fb9aa31bd

read-github by am-will/codex-skills

7ed670ba-243e-49c1-b3b6-4ff7f4bb4283

https://skills.sh/am-will/codex-skills/read-github

https://skills.sh/am-will

codex-skills

https://skills.sh/am-will/codex-skills

/ read-github

read-github

Read GitHub Docs

Access GitHub repository documentation and code via the gitmcp.io MCP service.

URL Conversion

#### Convert GitHub URLs to gitmcp.io:

github.com/owner/repo  →  gitmcp.io/owner/repo

https://github.com/karpathy/llm-council  →  https://gitmcp.io/karpathy/llm-council

The  scripts/gitmcp.py  script provides CLI access to repository docs.

List Available Tools

python3 scripts/gitmcp.py list-tools owner/repo

Fetch Documentation

#### Retrieves the full documentation file (README, docs, etc.):

python3 scripts/gitmcp.py fetch-docs owner/repo

Search Documentation

#### Semantic search within repository documentation:

python3 scripts/gitmcp.py search-docs owner/repo  "query"

Search Code

#### Search code using GitHub Search API (exact match):

python3 scripts/gitmcp.py search-code owner/repo  "function\_name"

Fetch Referenced URL

#### Fetch content from URLs mentioned in documentation:

python3 scripts/gitmcp.py fetch-url owner/repo  "https://example.com/doc"

Direct Tool Call

#### Call any MCP tool directly:

python3 scripts/gitmcp.py call owner/repo tool\_name  '{"arg": "value"}'

#### Tool names are dynamically prefixed with the repo name (underscored):

karpathy/llm-council  →  fetch\_llm\_council\_documentation

facebook/react  →  fetch\_react\_documentation

my-org/my-repo  →  fetch\_my\_repo\_documentation

Available MCP Tools

#### For any repository, these tools are available:

fetch\_{repo}\_documentation

- Fetch entire documentation. Call first for general questions.

search\_{repo}\_documentation

- Semantic search within docs. Use for specific queries.

search\_{repo}\_code

- Search code via GitHub API (exact match). Returns matching files.

fetch\_generic\_url\_content

- Fetch any URL referenced in docs, respecting robots.txt.

When given a GitHub repo, first fetch documentation to understand the project

Use search-docs for specific questions about usage or features

Use search-code to find implementations or specific functions

Use fetch-url to retrieve external references mentioned in docs

Weekly Installs 5.3K Repository

am-will/codex-skills

https://github.com/am-will/codex-skills

GitHub Stars 460 First Seen Jan 23, 2026 Security Audits

Gen Agent Trust Hub Fail

https://skills.sh/am-will/codex-skills/read-github/security/agent-trust-hub

Socket Pass

https://skills.sh/am-will/codex-skills/read-github/security/agent-trust-hub

https://skills.sh/am-will/codex-skills/read-github/security/agent-trust-hub

Installed on codex 5.3K opencode 5.3K gemini-cli 5.3K github-copilot 5.3K cursor 5.3K amp 5.3K

