---
sourceFile: "What are skills? - Agent Skills"
exportedBy: "Kortex"
exportDate: "2026-05-17T23:05:02.686Z"
---

# What are skills? - Agent Skills

c9ffd752-f3dc-40c9-9197-dc63223fc8c4

What are skills? - Agent Skills

95ae15ef-f490-4e4e-9488-a20c859dc4a2

https://agentskills.io/what-are-skills

What are skills? - Agent Skills

Skip to main content

https://agentskills.io/what-are-skills#content-area

Agent Skills now has an official

Discord server

https://discord.gg/MKPE9g8aUy

announcement

https://github.com/agentskills/agentskills/discussions/273

for details.

Agent Skills home page Agent Skills

https://agentskills.io/

Ctrl K Ask AI

agentskills/agentskills 15,057

https://github.com/agentskills/agentskills

agentskills/agentskills 15,057

https://github.com/agentskills/agentskills

What are skills?

https://agentskills.io/home

What are skills?

https://agentskills.io/what-are-skills

Specification

https://agentskills.io/specification

Client Showcase

https://agentskills.io/clients

For skill creators

https://agentskills.io/skill-creation/quickstart

Best practices

https://agentskills.io/skill-creation/best-practices

Optimizing descriptions

https://agentskills.io/skill-creation/optimizing-descriptions

Evaluating skills

https://agentskills.io/skill-creation/evaluating-skills

Using scripts

https://agentskills.io/skill-creation/using-scripts

For client implementors

Adding skills support

https://agentskills.io/client-implementation/adding-skills-support

On this page

How skills work

https://agentskills.io/what-are-skills#how-skills-work

The SKILL.md file

https://agentskills.io/what-are-skills#the-skill-md-file

https://agentskills.io/what-are-skills#next-steps

What are skills?

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.

At its core, a skill is a folder containing a

file. This file includes metadata (

description

, at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, templates, and reference materials.

my-skill/
├── SKILL.md          # Required: instructions + metadata
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
└── assets/           # Optional: templates, resources

https://agentskills.io/what-are-skills#how-skills-work

How skills work

progressive disclosure

to manage context efficiently:

: At startup, agents load only the name and description of each available skill, just enough to know when it might be relevant.

: When a task matches a skill's description, the agent reads the full

instructions into context.

: The agent follows the instructions, optionally loading referenced files or executing bundled code as needed.

This approach keeps agents fast while giving them access to more context on demand.

https://agentskills.io/what-are-skills#the-skill-md-file

The SKILL.md file

Every skill starts with a

file containing YAML frontmatter and Markdown instructions:

---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
---

# PDF Processing

## When to use this skill
Use this skill when the user needs to work with PDF files...

## How to extract text
1. Use pdfplumber for text extraction...

## How to fill forms
...

The following frontmatter is required at the top of

: A short identifier

description

: When to use this skill

The Markdown body contains the actual instructions and has no specific restrictions on structure or content. This simple format has some key advantages:

Self-documenting

: A skill author or user can read a

and understand what it does, making skills easy to audit and improve.

: Skills can range in complexity from just text instructions to executable code, assets, and templates.

: Skills are just files, so they're easy to edit, version, and share.

https://agentskills.io/what-are-skills#next-steps

View the specification

https://agentskills.io/specification

to understand the full format.

Add skills support to your agent

https://agentskills.io/client-implementation/adding-skills-support

to build a compatible client.

See example skills

https://github.com/anthropics/skills

Read authoring best practices

https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

for writing effective skills.

Use the reference library

https://github.com/agentskills/agentskills/tree/main/skills-ref

to validate skills and generate prompt XML.

https://agentskills.io/home

Specification

https://agentskills.io/specification

Powered by This documentation is built and hosted on Mintlify, a developer documentation platform

https://www.mintlify.com?utm\_campaign=poweredBy&utm\_medium=referral&utm\_source=agent-skills

Responses are generated using AI and may contain mistakes.

