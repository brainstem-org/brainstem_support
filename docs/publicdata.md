---
layout: default
title: Public data
has_children: false
nav_order: 7
has_toc: false
---

# Public data
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

The BrainSTEM public portal makes published experimental metadata available to anyone, without an account. Labs publish a project with its **Public access** checkbox; the project and everything that belongs to it then appears in the public portal and the public API, where it can be browsed, cited and reused.

**For data sharers:**
- Make your research discoverable and reusable by publishing it through the public portal.
- Link your entries to external repositories (for example DANDI, OpenNeuro or Zenodo) for persistent access to raw data and code.
- Keep your work citable: publications and journals linked to a project are part of its public record.

**For data reusers:**
- Browse public projects, subjects, sessions, collections and the shared catalogues of species, strains, consumables and hardware, no login required.
- Read the full metadata of every public entry, with the same details pages as the private portal.
- Query the same data through the public API, the reference pages and the published schemas described below.

## The public portal

The public portal is at [www.brainstem.org/public/](https://www.brainstem.org/public/). It is read-only and shows:

- A **Dashboard** with counts and the newest public entries, plus statistics such as strain, consumable and hardware device usage across public projects.
- List views of every model, with 50 entries per page. Anonymous visitors see the lists without filters, sorting, column settings, bulk actions or exports; **Show all** is disabled. Signed-in users can use filters and columns in the public portal as in the private portal.
- Details pages for every public entry with its related entries, the probe schematics of catalog designs and the **Coordinates** of procedures.
- The **Pending approvals** page listing catalogue submissions under review.

Anonymous browsing of the public portal pages is rate limited to 300 page views per five minutes per address; signed-in users are exempt.

## Interactive data model and data graph

The **Interactive data model** (**Help & Documentation** menu) shows every model with its fields and relations; the **Data graph** (**Tools** menu or the **Graph** button on a details page) counts your entries by kind and narrows them to a selected entry. Both require a signed-in account, also in the public portal. A self-hosted version of the diagram that needs no account is on this site at [Interactive data model]({{"datamodel/"|absolute_url}}?view=interactive).

## Public API

Everything in the public portal is also available through the public API at `/api/public/`, read-only and without a token: `https://www.brainstem.org/api/public/{app}/{model}/`. It uses the same filters, includes and pagination as the private API, see the [API documentation]({{"api/"|absolute_url}}). Anonymous requests are limited to 60 per minute per address.

Two further public endpoints need no account:

- **Reference pages** at `/reference/`: Markdown and JSON pages generated from the application that describe the data model, query syntax, relationships, vocabularies and per-type schemas, written for developers and AI agents. See the [reference API]({{"api/reference/"|absolute_url}}).
- **Schemas** at `/schemas/`: the JSON schemas of every type-specific details block, current and versioned (`/schemas/{Family}/{Type}.json`, `/schemas/{Family}/{Type}/{version}.json`). See [Public schemas]({{"api/public-schemas/"|absolute_url}}).

The [MCP server]({{"api/mcp/"|absolute_url}}) also answers read-only requests for public data without a token.

## What becomes public

Making a project public publishes the project and everything that inherits from it:

- Subjects, cohorts and breedings of the project; subject logs.
- Sessions, collections and epochs; the behaviors, data acquisitions and manipulations of those sessions.
- Procedures, procedure episodes and procedure logs of the subjects; experimental interfaces.
- Specimen sets, specimens, specimen procedures and specimen logs.
- Templates shared with the project (read-only in the public portal).

Independently of projects, these personal attributes have their own **Public access** checkbox: setups (with their equipment), inventories (with their consumable stocks), protocols, licenses and behavioral assays. Data storages become public through their public data protocols. Publications, journals, taxonomies and resources (consumables, hardware devices, suppliers) are always public.

Never public: project and group membership lists, permissions, email addresses, uploaded files and API tokens. Public user pages show only the profile image and affiliation.

{: .important }
> Planned records are never public. Planned subjects, specimen sets and specimens, and planned or cancelled procedures, sessions and breedings stay private even when their project is public, and so do the behaviors, data acquisitions and manipulations inside a planned session. See [Planning]({{"webinterface/planning/"|absolute_url}}).

## How to share your data publicly

For a step-by-step guide see the tutorial [How to share data publicly]({{"tutorials/sharing-project-publicly/"|absolute_url}}).

1. Open the project, click **Edit** and check **Public access**. You need to be an Owner of the project. The dialog **Make this project public?** warns: "Are you sure you want to make this project public? This will make all related content visible to the public (subjects, sessions, and modules associated with the project)."
2. Everything that inherits from the project becomes public at once, see the [public sharing inheritance model]({{"datamodel/permissions/#public-sharing"|absolute_url}}).
3. Add links to external repositories and publications to your project and sessions to make the raw data and citations reachable.
4. Uncheck **Public access** and confirm **Make private** in the **Stop sharing publicly?** dialog to withdraw the project from the public portal and API.
