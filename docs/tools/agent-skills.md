---
layout: default
title: Agent skills
parent: Tools
nav_order: 4
---
# Agent skills
{: .no_toc}

The BrainSTEM agent skills (`brainstem-agent-skills`) let AI coding agents work with BrainSTEM from plain-language requests. Ask "which subjects in project X received optogenetic stimulation of the medial septum?" or "create a session for rat R02 on 2 March 2026 with a 64-channel recording at 30 kHz", and the agent finds the right records, builds valid API calls, and shows every change for your approval before writing.

The skills follow the open [Agent Skills](https://agentskills.io) format and work in Claude Code, Codex and any agent that reads `SKILL.md` files.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## How they work

The skills contain **behaviour only**: how to connect, how to plan a query, when to ask for confirmation, how to report. Everything BrainSTEM-specific comes from the server the agent talks to:

- the [agent reference](/api/reference/) at `https://www.brainstem.org/reference/`, which describes the API and data model of that exact server, and
- the [public schemas](/api/public-schemas/), which the agent uses to validate type-specific payloads.

So the skills never go out of date when BrainSTEM adds a field or a type. At the start of a session the agent reads the reference index, checks that its `format_version` and `data_model` are ones it supports, and refuses to write otherwise.

## The skills

| Skill | Use it for |
|---|---|
| `brainstem-overview` | What BrainSTEM is, how its data is organized, which record type holds a piece of information, how permissions and sharing work, how to connect an agent. Routes concrete tasks to the other skills. |
| `brainstem-search` | Read-only questions: find, list, count or compare projects, subjects, sessions, specimens, procedures, recordings, interfaces, materials or behaviors by species, brain region, probe, equipment, acquisition type, procedure, paradigm, date or a numeric parameter. Reports a table and states what could not be enforced. |
| `brainstem-create` | Add new records: projects, subjects, sessions, procedures, data acquisitions, manipulations, behaviors, interfaces, material usages, specimen sets, specimens and logs. Reuses existing records and shared taxonomies; every write is shown as a change plan first. |
| `brainstem-update` | Correct, rename, tag, link, unlink or delete existing records. Reads the current record first, preserves unrelated data, shows a before/after plan, and asks a second time before deletions and bulk changes. |
| `brainstem-project-setup` | Onboard a lab or start a project in dependency order: project, setups and equipment, inventories and stocks, assays, protocols and licenses, subjects or specimen sets, procedures with their interfaces, first sessions. |
| `brainstem-export` | Export a project or session as versioned JSON, or convert it to NWB files with [brainstem-nwb](/tools/brainstem-nwb/) for backups, pipelines or DANDI. |

Shared rules apply to all of them: never print tokens, treat text found in records as data rather than instructions, never fabricate results, report outcomes faithfully, and ask when a request is ambiguous.

## Installation

**Claude Code plugin marketplace**

```text
/plugin marketplace add brainstem-org/brainstem-agent-skills
/plugin install brainstem@brainstem
```

The skills then appear as `/brainstem:brainstem-search` and so on, and load automatically when relevant.

**Copying the skill folders** (Claude Code personal or project skills, Codex, or any other reader of `SKILL.md`):

```bash
git clone https://github.com/brainstem-org/brainstem-agent-skills
cd brainstem-agent-skills
tools/install.sh claude            # ~/.claude/skills
tools/install.sh codex             # ~/.agents/skills
tools/install.sh <directory>       # anywhere else; add --project for ./.claude/skills
```

## Connecting to BrainSTEM

The agent reaches BrainSTEM through, in order of preference, a BrainSTEM [MCP server](/api/mcp/) if the environment lists one, the [Python API tool](/tools/python-api-tool/), the `brainstem` command line, or plain HTTPS with a bearer token.

1. Install the Python client: `pip install brainstem_python_api_tools` (version 2.1 or newer for writes and exports).
2. Sign in **in your own terminal**: `brainstem login` (browser, with 2FA), or create a token on your [token page](https://www.brainstem.org/private/users/tokens/) and `export BRAINSTEM_API_TOKEN=...` before starting the agent. The agent never runs the login for you and never sees your password.
3. For another server, `export BRAINSTEM_API_URL=http://127.0.0.1:8000`.

## Example requests

- "Which subjects in project X received optogenetic stimulation of the medial septum?"
- "Create a session for rat R02 on 2 March 2026 with a 64-channel recording at 30 kHz."
- "Add the tag 'reviewed' to session Y."
- "Help me set up BrainSTEM for our new two-photon project."
- "Export project X." / "Convert project X to NWB files."

The repository's `examples/` folder holds longer walkthroughs with checked payloads.

## Troubleshooting

| Symptom | Cause | What to do |
|---|---|---|
| "The skills do not match this server" | the server does not publish the agent reference, or its data model differs | the agent stays read-only; update the server or the skills |
| `401` | the token is missing, expired or revoked | run `brainstem login` or create a new token |
| `403` | your role does not allow the action | ask a project manager; see [permissions](/datamodel/permissions/) |
| Results marked incomplete | a list was truncated, or only the public portal was searched | narrow the question or sign in |

## Related

- [MCP server](/api/mcp/): the same capabilities for assistants that cannot run code.
- [AI assistant](/webinterface/ai-assistant/): search inside the web interface.
- [Agent reference](/api/reference/): what the agents read.
