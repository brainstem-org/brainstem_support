---
layout: default
title: Projects
parent: Data model
nav_order: 1
---

# Project model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

Projects group the subjects, specimen sets, sessions, cohorts, collections and breedings that belong to one line of work. A project can relate experiments to publications, describe day-to-day experiments, or share experimental data with collaborators. Projects are the permission boundary of BrainSTEM: your access to a subject, a session, a procedure or a data acquisition comes from the projects it belongs to, not from the entry itself.

The lab's own resources (setups and their equipment, inventories and their stock, protocols, licenses, behavioral assays and data storages) sit outside projects and keep their own permissions. See [Personal attributes]({{"datamodel/personal_attributes/"|absolute_url}}).

{% include datamodel_embed.html model="stem.project" %}

## Fields

| Field | Description |
|:------|:------------|
| `Project name` | Name of the project (**required**; string; maximum length: 200 characters; must be unique across BrainSTEM, ignoring case). Include something identifying, such as the lab or the study. Example: "Hippocampal Memory Study 2024" |
| `Authenticated groups` | Groups given Contributor access when the project is created (add form only). After creation, access is managed from the project's **Manage permissions** page, where you can also invite individual people. |
| `Public access` | Private or Public (default: Private). The form shows it as a **Project visibility** toggle and asks for confirmation when you switch it. Public makes the project and everything that inherits from it readable on the public portal without an account. Only owners can change it. |
| `Description` | A rich text description of the project. You can insert images (see the warning below). |
| `Publications` | Related [publications]({{"datamodel/dissemination/publication/"|absolute_url}}). A project can link several publications; this is what lets a reader move from a paper to the underlying entries. A new publication must be approved before other users can see it. |
| `Tags` | Tags for organization and filtering. Tags are shared across all users; the suggestions show tags already used in your projects, and you can always type a new one. Example: "electrophysiology", "hippocampus" |
| `Extra content` | Custom key-value fields that the standard fields do not cover. Values can be text or numbers. Example: {"Ethics_Protocol": "2024-001", "Funding": "NIH R01"} |
| `Project name in storage` | The name of the project in your local data storage, when it differs from the name above (string; maximum length: 200 characters). Shown in the **Online repositories** part of the form. Example: "HPC_MEM_24" |
| `Repository links` | Links to where the data or code live externally, such as a DANDI set, a GitHub repository or an institutional archive. Each link names the repository (DANDI, Zenodo, GitHub, Figshare and others) and its URL. |

{: .warning }
An image inserted in the description is stored at a public address. Anyone with the address can open it, even while the project is private.

**Project name in storage**, **Repository links**, the user roles below and the groups chosen at creation are available only in the web form; the REST API exposes the other fields (**Extra content** is called `extra_fields` there).

{% include schemas/project.md %}

## User roles

The change form of a project has a **User roles** list. Each row names a user who holds Contributor access or more on the project (**User with role**) and a **Role** that describes their contribution to the work: Contact person, Conceptualizer, Data collector, Data curator, Data manager, Formal analyzer, Investigator, Maintainer, Method developer, Producer, Project leader, Project manager or Supervisor. A person can have several roles. The roles are shown on the project page and in its exports, where they describe who did what, in the manner of a contributor statement.

These roles are descriptive only. They have nothing to do with the permission roles (Member, Contributor, Manager, Owner) that decide who can see and edit the project; see [Permissions](#permissions). User roles are not available through the REST API.

## Related entries

- [__Subjects__]({{"datamodel/stem/subject/"|absolute_url}}) and [__Specimen sets__]({{"datamodel/stem/specimenset/"|absolute_url}}) belong to one or more projects.
- [__Sessions__]({{"datamodel/stem/session/"|absolute_url}}) belong to one or more projects.
- [__Cohorts__]({{"datamodel/stem/cohort/"|absolute_url}}), [__Collections__]({{"datamodel/stem/collection/"|absolute_url}}) and [__Breedings__]({{"datamodel/stem/breeding/"|absolute_url}}) belong to exactly one project. Deleting a project deletes them too.

Subjects, specimen sets and sessions are not deleted with a project; they only lose the link to it. One that belonged to no other project is then in no project, so nobody can open it until the project is recovered, which restores its links. See [Deleted entries]({{"webinterface/deleted-entries/"|absolute_url}}).

## Export and download

The **Export** menu on a project page offers a printable view (save as PDF), a Word document, a spreadsheet (CSV, Excel) and a **STAR Methods** report (preview or .docx) built from the project's entries. **Export** → **Download project data** exports the project's entries as JSON, optionally compressed; large exports run in the background and are downloaded when ready. The same export is available through the API (`export/` and `export-jobs/` actions on the project).

## Permissions

A project's access is held directly on it, by user and by group. A user or a group holds one of four permission roles:

| Role | Can |
|:-----|:----|
| Member | Read the project and everything that inherits from it. |
| Contributor | Also create, edit and delete subjects, sessions, specimen sets and their modules. Most forms only offer projects where you are at least a Contributor. |
| Manager | Also add or remove members and groups, and send invitations. |
| Owner | Also edit the project's own fields, make it public and delete it. |

An invitation grants one of these roles. People without a BrainSTEM account can be invited by email; the invitation is applied when they register. A member can leave a project from its page.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to projects. Learn more about the projects' fields and data structure on the [Project API page]({{"api/stem/project/"|absolute_url}}).
