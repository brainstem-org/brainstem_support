---
layout: default
title: Working with AI
parent: Tutorials
nav_order: 12
---

# Working with AI
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

BrainSTEM connects to AI in three ways. All three act with your BrainSTEM permissions: they see the records you see in the web interface, and nothing else.

| | What it does | Where you use it | Setup |
|---|---|---|---|
| **AI assistant** | Semantic search: finds records from a question in plain language | The web interface | None |
| **MCP server** | Gives AI applications such as Claude and Cursor access to the data model and your records: search, export and, after your confirmation, create and update | Your AI application | A personal access token |
| **Agent skills** | Teach coding agents to search, create, export and convert BrainSTEM data with the Python client | Claude Code, Codex and other coding agents | Install the skills and the Python client |

## The AI assistant

The assistant is a semantic search over your records. You ask in plain language; a language model translates the question into a structured query, and BrainSTEM validates the query and runs it on its own server against the records you can access. Vector embeddings of the anatomical regions and of the consumable and hardware catalogs resolve names that are not written exactly as stored, so "dorsal hippocampus" or "GCaMP virus" still reach the right regions and products.

### Search your records
{: .no_toc}

1. Open the assistant with the button in the lower-right corner of any private page, or with **AI assistant** in the **Tools** menu.
2. Type a question in plain language, for example:
   - `Find Long Evans subjects with virus injections in CA1`
   - `Show sessions with silicon probe implants in the hippocampus`
   - `Find subjects with optogenetic manipulations this year`
   - `List consumables from Addgene`
3. Read the result cards. When more records match than the cards show, the assistant links to the list view filtered to all of them.
4. Refine with a follow-up, such as "only last month" or "show the collections of these sessions".

Put exact names in quotation marks (`"Pilot study"`) and name the record type when it matters ("sessions with a silicon probe implant procedure").

### What leaves BrainSTEM
{: .no_toc}

- **A search** sends your question and a description of the data model to the language model provider, together with names from the shared taxonomies when the model asks for them. The query itself runs on BrainSTEM's server; your records stay there.
- **Page context**, off by default, adds approved fields of the record you have open (its subject, project, dates), so a question is read in that context. Identifiers are removed first.
- **AI summary**, off by default, sends the result cards (names, short descriptions and the evidence for each match) to the provider, which grades each card and writes a summary. It is slower and uses more of your allowance.

Questions and answers are not stored on BrainSTEM. Your recent searches are kept in your browser only.

### Allowance and your own key
{: .no_toc}

The assistant runs on BrainSTEM's shared provider key, free up to a monthly allowance; **AI assistant settings** in the avatar menu shows what is left. To search beyond it, or to choose another model, add your own key for OpenRouter, OpenAI or DeepSeek; your provider then bills you directly. Keys are stored encrypted and never sent back to the browser.

{: .note }
> The assistant only reads. It cannot create, change or delete records. See [AI assistant]({{site.baseurl}}/webinterface/ai-assistant/) for everything it can find, its limits and its settings.

## The MCP server

The [Model Context Protocol](https://modelcontextprotocol.io) (MCP) is an open standard that connects AI applications to external data and tools. The BrainSTEM MCP server uses it to give an AI application direct access to BrainSTEM: the application can look up the data model and the schemas, search and export your records, follow recent changes and, after you confirm, create and update records. You then ask in your AI application, for example "Which subjects in project X received optogenetic stimulation of the medial septum?", and the answer comes from your BrainSTEM data.

The server lives at `https://www.brainstem.org/mcp/`. It identifies you by a personal access token and works with your permissions; without a token it reads public projects only.

### Step 1: Create a token
{: .no_toc}

1. Open the avatar menu → **Security & access** → **API tokens**.
2. Click **Create New Personal Access Token**, name it after the application (for example "Cursor") and click **Create Token**. Two-factor authentication must be set up first.
3. Copy the token; it is shown only once. It stays valid for a year and every use extends it by another year.

### Step 2: Connect your AI application
{: .no_toc}

**Claude Code**

```bash
claude mcp add --transport http brainstem https://www.brainstem.org/mcp/ \
    --header "Authorization: Bearer <token>"
```

**Cursor and other applications** that accept a remote MCP server with a request header take an entry like this:

```json
{
  "mcpServers": {
    "brainstem": {
      "type": "http",
      "url": "https://www.brainstem.org/mcp/",
      "headers": {"Authorization": "Bearer <token>"}
    }
  }
}
```

The one-click connectors of claude.ai and ChatGPT need a sign-in flow (OAuth) that BrainSTEM does not offer yet.

### Step 3: Choose read-only or writable
{: .no_toc}

With `https://www.brainstem.org/mcp/?read_only=true` as the URL, the application can only read. Use it for exploring data and for any connection you keep long-term. Use the plain URL only when you want the application to create or change records.

### Example requests
{: .no_toc}

- "List the sessions of subject R02 recorded in 2026 with their data acquisitions."
- "What fields does a virus injection procedure take?"
- "Export project X as JSON and tell me how many sessions it holds."
- "Create a session for rat R02 on 2 March 2026 in project X." (writable connection; the application shows the record and waits for your confirmation)

### Safeguards
{: .no_toc}

- **Confirmation before every write.** The server instructs the application to show the exact record before each create or update and to wait for your confirmation.
- **No deletions** and **no account changes.** Deleting records and managing users, groups and memberships stay in the web interface and the REST API.
- **No accidental publishing.** Making a record public takes a separate, explicit step.
- **Traceable.** Records written through MCP say so in their revision history ("Created via MCP").
- **Revocable.** Deleting the token on the **API tokens** page cuts the connection at once.

See [MCP server]({{site.baseurl}}/api/mcp/) for the tools, resources and limits.

## The agent skills

The [agent skills]({{site.baseurl}}/tools/agent-skills/) teach a coding agent, such as Claude Code or Codex, to work with BrainSTEM: connect, plan a query, ask before writing and report what it did. Because the agent runs code, it can also use the Python client, build a project's structure in bulk and convert exports to NWB. Everything specific to BrainSTEM is read from the server's [agent reference]({{site.baseurl}}/api/reference/), so the skills stay current when BrainSTEM changes.

### Step 1: Install the skills
{: .no_toc}

In Claude Code:

```text
/plugin marketplace add brainstem-org/brainstem-agent-skills
/plugin install brainstem@brainstem
```

For Codex or any other agent that reads `SKILL.md` files, clone the repository and run `tools/install.sh codex` (or `tools/install.sh <directory>`).

### Step 2: Sign in yourself
{: .no_toc}

1. `pip install brainstem_python_api_tools` (2.1 or newer).
2. Run `brainstem login` in your own terminal, or create a token on the **API tokens** page and `export BRAINSTEM_API_TOKEN=...` before starting the agent.

The agent never logs in for you and never sees your password. When the BrainSTEM MCP server is also connected, the agent uses it.

### Step 3: Ask
{: .no_toc}

| Skill | Example request |
|-------|-----------------|
| `brainstem-search` | "Which subjects in project X received optogenetic stimulation of the medial septum?" |
| `brainstem-create` | "Create a session for rat R02 on 2 March 2026 with a 64-channel recording at 30 kHz." |
| `brainstem-update` | "Add the tag 'reviewed' to session Y." |
| `brainstem-project-setup` | "Help me set up BrainSTEM for our new two-photon project." |
| `brainstem-export` | "Export project X." / "Convert project X to NWB files." |

Every write is presented as a change plan first. The update skill asks a second time before deletions and bulk changes. The agent reports what it created, reused and could not do, and never prints your token.

## Which one to use

- **Finding records while you work in BrainSTEM**: the AI assistant.
- **Asking about your data, or drafting records, from an AI application**: the MCP server, read-only until you need to write.
- **Running code, setting up a lab's projects in bulk or converting exports to NWB**: the agent skills.

## Next steps

- **Set up the data an agent will use**: [Get started!]({{site.baseurl}}/tutorials/get_started) and [Setting Up Lab Infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure).
- **Export with an agent**: [Exporting to NWB]({{site.baseurl}}/tutorials/exporting-to-nwb) covers what the `brainstem-export` skill does step by step.
- **Read what the agents read**: the [agent reference]({{site.baseurl}}/api/reference/) and the [public schemas]({{site.baseurl}}/api/public-schemas/).
- **Script it yourself**: the [Python API tool]({{site.baseurl}}/tools/python-api-tool/) and [MATLAB API tool]({{site.baseurl}}/tools/matlab-api-tool/).
