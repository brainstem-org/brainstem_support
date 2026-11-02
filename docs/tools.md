---
layout: default
title: Tools
nav_order: 5
has_children: true
has_toc: false
---
# Tools
{: .no_toc}

BrainSTEM comes with tools for reaching your data from the environments researchers already work in: Python and MATLAB clients, a command line, a browser-based API explorer, agent skills and an MCP server for AI assistants, and a converter that writes Neurodata Without Borders (NWB) files from BrainSTEM exports.

## Available tools

| Tool | What it is for | Page |
|---|---|---|
| **Python API tool** (`brainstem_python_api_tools`) | Load, create, change and delete records, export projects and sessions, read the agent reference. Includes the `brainstem` command line. | [Python API tool](/tools/python-api-tool/) |
| **MATLAB API tool** (`brainstem_matlab_api_tools`) | The same operations from MATLAB, with convenience loaders that return structs. | [MATLAB API tool](/tools/matlab-api-tool/) |
| **Web API tool** | Browse any endpoint in your browser with your existing login; no code needed. | [Web API tool](/tools/web-api-tool/) |
| **Agent skills** (`brainstem-agent-skills`) | Let Claude Code, Codex and other agents search, create, update, set up and export BrainSTEM data from plain-language requests, with every write shown for approval. | [Agent skills](/tools/agent-skills/) |
| **MCP server** | Give AI applications such as Claude Code and Cursor access to the data model and your records, with a token and one configuration entry. | [MCP server](/api/mcp/) |
| **brainstem-nwb** | Convert a project or session export to NWB files, one per session and subject, with a manifest and a validation report. | [brainstem-nwb](/tools/brainstem-nwb/) |
| **ndx-brainstem** | The NWB extension that stores the complete BrainSTEM records inside an NWB file. | [ndx-brainstem](/tools/ndx-brainstem/) |

## Shared conventions

All tools follow the same conventions, so what you learn in one carries over:

- **Environment variables**: `BRAINSTEM_API_TOKEN` holds your Personal Access Token and `BRAINSTEM_API_URL` the server (default `https://www.brainstem.org`). Set them once; no tool needs the token on its command line.
- **Authentication**: a browser-based device sign-in that always enforces two-factor authentication, or a token created on your [token page](https://www.brainstem.org/private/users/tokens/). See [API authentication](/api/#authentication).
- **Model names**: bare lower-case resource names such as `session`, `specimenset`, `experimentalinterface` or `anatomicalregion`; the clients add the app prefix themselves.
- **Paging**: 100 records per page by default and at most 500; `load_all` follows every page.
- **Lists replace**: sending a list field replaces the whole list. Read the record without `include` before changing a list.
- **Versions**: the current clients (Python 2.1, MATLAB 2.1) address every resource of the current data model, including specimens, interfaces and materials, and add exports and anonymous public reads. Older clients still read the classic models but answer "Unknown model" for the new ones.

All tools use the same [API endpoints](/api/), and the server's own [agent reference](/api/reference/) is the authoritative description of what each endpoint accepts.
