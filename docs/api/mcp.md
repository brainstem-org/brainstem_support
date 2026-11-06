---
layout: default
title: MCP server
parent: API
nav_order: 11
---
# MCP server
{: .no_toc}

The [Model Context Protocol](https://modelcontextprotocol.io) (MCP) is an open standard that connects AI applications to external data and tools. The BrainSTEM MCP server uses it to give AI applications, such as Claude Code or Cursor, access to BrainSTEM: they can read the data model and the schemas, search and export your records, follow recent changes and, on a writable connection, create and update records. Every request goes through the REST API with the permissions of your token.

{: .important }
> - What the application reads through the server, records and exports included, is sent to the model provider of your AI application.
> - The token has no scopes. A [read-only connection](#connecting) is a property of the URL only: the same token writes through the plain URL or the REST API.
> - Showing you each change before it is made is an instruction to the application. The server cannot tell whether you were asked.

[Working with AI]({{site.baseurl}}/tutorials/working-with-ai/#what-each-channel-sees-and-can-change) compares what the MCP server, the agent skills and the in-app assistant send and can change.

For a step-by-step setup, see [Working with AI]({{site.baseurl}}/tutorials/working-with-ai/#the-mcp-server).

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Connecting

The endpoint is `https://www.brainstem.org/mcp/`, using the Streamable HTTP transport. Authentication is a Personal Access Token in the `Authorization` header. Without a token the server still answers, but it can only read public projects.

**Claude Code**

```bash
claude mcp add --transport http brainstem https://www.brainstem.org/mcp/ \
    --header "Authorization: Bearer <token>"
```

**Other clients** take a generic Streamable HTTP server entry with the URL and the header, for example:

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

Create the token on your [API token page](https://www.brainstem.org/private/users/tokens/), one per application, and name it after the application, so you can revoke it without affecting your other tools. Its lifetime is described under [API authentication](/api/#authentication). The one-click connectors of claude.ai and ChatGPT need an OAuth sign-in that BrainSTEM does not offer yet; use an application that lets you set the header.

**Read-only connection.** Use `https://www.brainstem.org/mcp/?read_only=true` to hide every writing tool; the server also refuses writes on such a connection. This is the safe choice for exploring data, but it protects nothing if the token is used elsewhere (see the note at the top).

## Tools

| Tool | What it does | Needs a token |
|---|---|---|
| `read_reference` | Reads a page of the [agent reference](/api/reference/) (default `index.md`). | no |
| `get_schema` | Returns the JSON schema of a type, current or an exact version. | no |
| `query_records` | Lists records of a resource with filters, includes, sorting and paging (at most 100 per page). | for the private portal |
| `get_record` | Returns one record by id, optionally with included relations. | for the private portal |
| `recent_activity` | What changed lately in records you can read, with the same filters as the dashboard feed. | yes |
| `export_record` | Exports a project or a session as JSON (see [Exports](/api/export/)); counts against the export rate limit. | yes |
| `create_record` | Creates a record from a payload. | yes, writable connection |
| `update_record` | Changes fields of an existing record. | yes, writable connection |
| `set_visibility` | Makes a project, setup, protocol, license, inventory, data storage or behavioral assay public or private. | yes, writable connection |

The server also exposes the reference pages and schemas as MCP resources, so a client can open `https://www.brainstem.org/reference/rules.md` or `https://www.brainstem.org/schemas/Procedure/VirusInjection.json` directly. It offers tools and resources only, no prompts, and sends usage instructions to the application when it connects.

## What it will not do

- **Delete records.** Deletion is only available in the web interface and the REST API.
- **Manage accounts.** Users, groups, laboratories, memberships and invitations cannot be written through MCP.
- **Publish by accident.** A generic create or update cannot set `is_public`; making a record public is its own tool, `set_visibility`.
- **Act without asking.** The server instructs the assistant to show you the exact payload before every create or update and to wait for your confirmation, one confirmation per call, and never to act on instructions found inside records. These are instructions to the application; the server cannot tell whether you were asked. The other three points are enforced by the server.

Every record written through MCP is marked in its revision history ("Created via MCP", "Changed Name via MCP").

## Limits

- 300 MCP messages per minute; the underlying REST limits also apply (300 requests per minute, 30 exports per hour).
- `query_records` returns at most 100 records per call; large exports return only their summary.
- One message per request; batches are not supported.

## Alternatives

- Assistants that can run code can use the [agent skills](/tools/agent-skills/) with the Python client or the `brainstem` command line instead of, or in addition to, MCP.
- Inside the web interface, the built-in [AI assistant](/webinterface/ai-assistant/) searches your records without any setup.
