---
layout: default
title: Working with AI
parent: Tutorials
nav_order: 13
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
| **AI assistant** | Finds records from a question in plain language | The web interface | None |
| **MCP server** | Gives AI applications such as Claude and Cursor access to the data model and your records: search, export and, on a writable connection, create and update | Your AI application | A personal access token |
| **Agent skills** | Teach coding agents to search, create, export and convert BrainSTEM data with the Python client | Claude Code, Codex and other coding agents | Install the skills and the Python client |

{: .warning }
> Before you connect an AI application, read [What each channel sees and can change](#what-each-channel-sees-and-can-change): with the MCP server and the agent skills, the records the AI reads are sent to that application's model provider.

## The AI assistant

The assistant finds records for you. You ask in plain language; BrainSTEM turns the question into a search, runs it on its own server against the records you can access, and shows the matches as cards. Names do not have to be written exactly as stored: "dorsal hippocampus" or "GCaMP virus" still reach the right regions and products.

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

### What leaves BrainSTEM, allowance and your own key
{: .no_toc}

A search sends your question to a language model provider, but not your records; the switches **Page context** and **AI summary** send more. The assistant runs on BrainSTEM's shared provider key up to a monthly allowance, and you can add your own key. [AI assistant]({{site.baseurl}}/webinterface/ai-assistant/#privacy) lists exactly what is sent in each mode and how keys are kept; [Settings page]({{site.baseurl}}/webinterface/ai-assistant/#settings-page) covers the allowance and your own key.

The assistant only reads. It cannot create, change or delete records. See [AI assistant]({{site.baseurl}}/webinterface/ai-assistant/) for everything it can find, its limits and its settings.

## The MCP server

The [Model Context Protocol](https://modelcontextprotocol.io) (MCP) is an open standard that connects AI applications to external data and tools. The BrainSTEM MCP server uses it to give an AI application direct access to BrainSTEM: the application can look up the data model and the schemas, search and export your records, follow recent changes and, after you confirm, create and update records. You then ask in your AI application, for example "Which subjects in project X received optogenetic stimulation of the medial septum?", and the answer comes from your BrainSTEM data.

The server lives at `https://www.brainstem.org/mcp/`. It identifies you by a personal access token and works with your permissions; without a token it reads public projects only.

### Step 1: Create a token
{: .no_toc}

1. Open the avatar menu → **Security & access** → **API tokens**.
2. Click **Create New Personal Access Token**, name it after the application (for example "Cursor") and click **Create Token**. Two-factor authentication must be set up first.
3. Copy the token; it is shown only once. It is valid for one year from creation (see [API authentication]({{site.baseurl}}/api/#authentication)). Use a separate token for each AI application, so you can revoke one without affecting the others.

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

With `https://www.brainstem.org/mcp/?read_only=true` as the URL, the server offers the application no writing tools. Use it for exploring data and for any connection you keep long-term. Use the plain URL only when you want the application to create or change records.

{: .warning }
> Read-only is a setting of the connection, not of the token. The same token also works on the writable URL and in the REST API, where it can delete records. Treat every token as able to write and delete, and keep it in the application's configuration only.

### Example requests
{: .no_toc}

- "List the sessions of subject R02 recorded in 2026 with their data acquisitions."
- "What fields does a virus injection procedure take?"
- "Export project X as JSON and tell me how many sessions it holds."
- "Create a session for rat R02 on 2 March 2026 in project X." (writable connection; the application shows the record and waits for your confirmation)

### Safeguards
{: .no_toc}

- **Confirmation before every write.** The server instructs the application to show the exact record before each create or update and to wait for your confirmation. This is an instruction to the application, not a check the server can make: whether you are asked depends on the application and its settings.
- **No deletions** and **no account changes.** Deleting records and managing users, groups and memberships stay in the web interface and the REST API.
- **No accidental publishing.** A create or update that sets a record public is refused; making a record public takes the separate `set_visibility` tool.
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
2. Run `brainstem login` in your own terminal, or create a token on the **API tokens** page and run `export BRAINSTEM_API_TOKEN="<token>"` before starting the agent.

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

The skills instruct the agent to present every write as a change plan first, to ask a second time before deletions and bulk changes, to report what it created, reused and could not do, and never to print your token. These are instructions to the agent; the server only checks your token's permissions.

{: .warning }
> The agent works in your terminal, where it can reach the token, and through the REST API it can delete every record your token may delete. Read each change plan before you approve it.

## What each channel sees and can change

All three act with your BrainSTEM permissions. They differ in what reaches an AI model provider, what they can change, and which safeguards the BrainSTEM server enforces rather than asks the AI to follow.

| | AI assistant | MCP server | Agent skills |
|---|---|---|---|
| **Sent to an AI model provider** | Your question and a description of the data model; with **Page context** or **AI summary**, also parts of records (see [Privacy]({{site.baseurl}}/webinterface/ai-assistant/#privacy)). The search runs on BrainSTEM. | Every record, query result and export the application reads goes to the model provider of your AI application. | Every record, export and command output the agent reads goes to the model provider of your coding agent. |
| **What it can change** | Nothing. | With a writable connection: create and update records, and make records public or private with `set_visibility`. It cannot delete. | Everything your token allows through the REST API, including deleting records. |
| **Enforced by the server** | Read-only; your read permissions. | Your token's permissions; no writing tools with `read_only=true`; no delete tool; no writes to users, groups, laboratories, memberships or invitations; no `is_public` through create or update. | Your token's permissions and the REST API's validation. |
| **Instructions to the AI, not enforced** | None needed. | Show the payload and wait for your confirmation before each write; ignore instructions found inside records. | Show a change plan and wait for your approval; ask again before deletions and bulk changes; never print the token; ignore instructions found inside records. |

Give each AI application its own token and revoke it on the **API tokens** page when you stop using the application.

## Which one to use

- **Finding records while you work in BrainSTEM**: the AI assistant.
- **Asking about your data, or drafting records, from an AI application**: the MCP server, read-only until you need to write.
- **Running code, setting up a lab's projects in bulk or converting exports to NWB**: the agent skills.

## Next steps

- **Set up the data an agent will use**: [Get started!]({{site.baseurl}}/tutorials/get_started) and [Setting Up Lab Infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure).
- **Export with an agent**: [Exporting to NWB]({{site.baseurl}}/tutorials/exporting-to-nwb) covers what the `brainstem-export` skill does step by step.
- **Read what the agents read**: the [agent reference]({{site.baseurl}}/api/reference/) and the [public schemas]({{site.baseurl}}/api/public-schemas/).
- **Script it yourself**: the [Python API tool]({{site.baseurl}}/tools/python-api-tool/) and [MATLAB API tool]({{site.baseurl}}/tools/matlab-api-tool/).
