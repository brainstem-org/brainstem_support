---
layout: default
title: Agent reference
parent: API
nav_order: 10
---
# Agent reference
{: .no_toc}

BrainSTEM publishes a description of its own REST API and data model at `https://www.brainstem.org/reference/`. The pages are generated from the running server's code, so they always describe the exact release that server runs: every resource, every field and its write rules, every schema type with its properties, how resources connect, and the query syntax. They are written for AI agents and tool authors, and the API and schema pages of this site are built from the same documents.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Access

- Public, no token: `GET https://www.brainstem.org/reference/` (or `/reference/index.md`).
- Markdown pages (`text/markdown`) and JSON documents under `/reference/data/`.
- Cached for an hour with `ETag` support; limited to 600 requests per minute per IP.
- The reference holds no records and no user data, only metadata about the API.

```bash
curl https://www.brainstem.org/reference/index.md
curl https://www.brainstem.org/reference/resources/session.md
curl https://www.brainstem.org/reference/data/manifest.json
```

The API tools wrap it: `client.agent_reference("resources/session.md")` in Python and MATLAB, and `brainstem reference rules.md` on the command line.

## Pages

| Page | Content |
|---|---|
| `index.md` | what BrainSTEM is, the versions of this server, how to navigate |
| `rules.md` | structural facts every query and write must respect (read first) |
| `query-syntax.md` | filter, include, sort and paging syntax |
| `data-model.md` | every REST resource grouped by app |
| `resources/<resource>.md` | one page per resource: endpoints, keys, permissions, uniqueness, payloads, delete behaviour, form-only inputs, fields, choices, custom actions |
| `relationships.md` | how resources connect: single-hop routes, multi-branch questions |
| `vocabulary.md` | what users say and what BrainSTEM calls it: aliases, species names, coordinate aliases, units |
| `schemas.md`, `schemas/<Family>.md`, `schemas/<Family>/<Type>.md` | schema families, type tables, property tables, allowed related types, material policies, link to the exact published version |
| `concepts/<Family>.md` | definitions of the field concepts shared across a family |
| `recent-activity.md` | the recent-activity feed |
| `guides/*.md` | curated guides: `api-guide`, `client-usage`, `query-planning`, `validation`, `permissions`, `taxonomies`, `project-setup`, `export` |
| `data/*.json` | the machine-readable documents the pages are rendered from: `manifest`, `api_surface`, `relationships`, `schemas`, `concepts`, `knowledge`, `model_summaries` |

Every page is small (under 40 KB) and begins with a comment that names the format version, the server commit and the page.

## Versions

`index.md` and `data/manifest.json` carry four version numbers that change independently:

| Field | Meaning |
|---|---|
| `format_version` | how to read the pages and documents; the major part changes when a page or key would be misread |
| `data_model` | the generation of the record structure (currently `specimen-1`); agents stop writing when it is not one they support |
| `server_commit` | the build the pages describe |
| `export_format_version` | the [export](/api/export/) format |

## How agents use it

The [BrainSTEM agent skills](/tools/agent-skills/) and the [MCP server](/api/mcp/) keep only agent behaviour (how to connect, when to ask for confirmation) and read everything BrainSTEM-specific from here:

1. Read `index.md` once per session on the server given by `BRAINSTEM_API_URL`, and check `format_version` and `data_model`.
2. Load `rules.md` and the guide for the task.
3. Load individual `resources/...`, `schemas/...` and `relationships.md` pages as needed.
4. Use `data/*.json` only for programmatic checks.

Nothing here requires an AI agent: the same pages are a complete, current API reference for any developer.

## Terms of use

The reference is public but not open source: read, cache and quote it to work with BrainSTEM data through the API, including from software and AI agents acting for you. Copying it into another product or standard, mirroring or redistributing it, or relicensing it needs BrainSTEM's written permission. The ownership line on every page, `license` in `data/manifest.json` and the `Link: rel="license"` header point to the full terms at <https://www.brainstem.org/reference/license.md>.
