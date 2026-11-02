---
layout: default
title: Permissions
parent: Data model
has_children: false
nav_order: 13
---

# Permissions
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

BrainSTEM applies permissions at the level of individual records. Every record derives its access from a parent: the records of a study from their **project**, a lab's resources from the **groups** they are shared with, and shared catalog entries from an **approval workflow**. This keeps collaboration flexible while every record stays under the control of the people responsible for it.

The diagram shows where every model's roles come from: each model stands under the record it inherits its permissions from. **Expand** opens it with its notes, search, layouts, layers and detail panel.

{% include datamodel_switch.html query="view=permissions" inline="notes=0" title="Permission inheritance" frame_title="Permission inheritance in the BrainSTEM data model" %}

## Permission levels overview

| Permission levels | Groups | Projects | Personal attributes |
|:-----------------|:-------|:---------|:-------------------|
| Permission scope | 3 levels, users only | 4 levels for users and groups | 4 levels for users and groups |
| Members | Inherit the permissions given to the group | Read access to the project, its subjects, specimen sets, sessions and modules | Read access to the attribute and what it contains (equipment, stock) |
| Contributors | - | Create, edit and delete records of the project | Create, edit and delete contained records |
| Managers | Add and remove members | Add and remove members and groups | Add and remove members and groups |
| Owners | Manage group details<br>Add and remove managers | Edit project details, make the project public, delete it<br>Add and remove managers | Edit attribute details, make it public<br>Add and remove managers |

## Permission levels

### Group permissions

Groups are the foundation of the permission system, with three levels:

| Permission level | Capabilities |
|:----------------|:-------------|
| **Owner** | Manage group details and settings, add and remove managers, associate the group with a laboratory, rename the group |
| **Manager** | Add and remove members, create invitations, accept or decline membership requests |
| **Member** | Access group resources, inherit the project permissions assigned to the group, leave the group |

Users can ask to join a group; group managers accept or decline the request. An invitation grants one of these roles. Managers can also invite users who do not have a BrainSTEM account yet by email; the invitation is applied when the account is created.

### Project permissions

Projects have four levels that can be assigned to users and to groups:

| Permission level | Capabilities |
|:----------------|:-------------|
| **Owner** | Edit the project's own fields, make it public, delete it, add and remove managers; everything a Manager can do |
| **Manager** | Add and remove members and groups, send invitations; everything a Contributor can do |
| **Contributor** | Create, edit and delete the subjects, specimen sets, sessions and modules of the project; everything a Member can do |
| **Member** | Read the project and all its records |

{: .note }
When a level is given to a group, every member of the group holds it. A user's effective level is the highest of their own and their groups' levels.

Creating or editing an entry needs Contributor on every project involved; you can only attach entries to projects where you are at least a Contributor. Links that require two records to share a project (a session and its subjects, a specimen set taken from a subject, a cohort and its subjects) are guarded on both sides: a project cannot be removed from a record while such a link depends on it.

### Personal attribute permissions

Setups, inventories, behavioral assays, data storage and licenses carry the same four levels, assigned to users and groups. Group members inherit the level given to their group. Equipment inherits from its setup and consumable stock from its inventory.

### Protocol permissions

[Protocols]({{"datamodel/personal_attributes/protocol/"|absolute_url}}) have their own Member, Contributor, Manager and Owner roles. The creator is an Owner and the groups selected at creation receive Contributor access. Protocol permissions are not inherited from the projects or entries that reference the protocol.

### Shared catalog and taxonomies

Species, strains, anatomical regions, behavioral paradigms, setup types, regulatory authorities, consumables, hardware devices, suppliers, journals and publications are shared by everyone. Any user can propose a new entry or a change; the proposal becomes an **approval request** that an admin team reviews (accept, merge into an existing entry, ask for changes, reject). Until it is accepted, the pending entry is visible to its submitter only. Anatomical regions and atlases are loaded by the system and cannot be edited.

## Permission inheritance

Roles are given to users and to groups on the record at the top of each tree; every record below it inherits them.

### Projects

```
Users and groups
└── Project  (Member, Contributor, Manager or Owner)
    ├── Subjects
    │   ├── Procedures
    │   │   ├── Material usages and stages
    │   │   └── Procedure logs
    │   ├── Procedure episodes
    │   ├── Subject logs
    │   └── Experimental interfaces (subject-based)
    │       └── Material usages
    ├── Specimen sets
    │   ├── Specimens
    │   ├── Specimen procedures
    │   │   └── Material usages and stages
    │   ├── Specimen logs
    │   └── Experimental interfaces (specimen-based)
    ├── Sessions
    │   ├── Behaviors
    │   ├── Data acquisition
    │   ├── Manipulations
    │   └── Epochs
    ├── Collections
    ├── Cohorts
    └── Breedings
```

| Parent | Inheriting records |
|:-------|:-------------------|
| **Project** | Subjects, specimen sets, sessions, collections, cohorts, breedings |
| **Subject** | Procedures (and their material usages, stages and logs), procedure episodes, subject logs, experimental interfaces of the subject |
| **Specimen set** | Specimens, specimen procedures (and their material usages and stages), specimen logs, experimental interfaces of the set |
| **Session** | Behaviors, data acquisition, manipulations, epochs |

An entry linked to several projects is readable with Member on any of them.

### Personal attributes

```
Users and groups
├── Setup  (Member, Contributor, Manager or Owner)
│   └── Equipment
├── Inventory  (Member, Contributor, Manager or Owner)
│   └── Consumable stock
├── Data storage  (Member, Contributor, Manager or Owner)
├── Behavioral assay  (Member, Contributor, Manager or Owner)
├── License  (Member, Contributor, Manager or Owner)
└── Protocol  (its own roles, not inherited from projects)
```

| Parent | Inheriting records |
|:-------|:-------------------|
| **Setup** | Equipment |
| **Inventory** | Consumable stock |

Data storage, behavioral assays, licenses and protocols have no inheriting records. Each personal attribute is owned by the user who created it and is shared by giving roles to other users and to groups.

Templates (procedure, specimen procedure, interface, data acquisition, manipulation and material usage templates) are owned by the user who created them and can be shared with projects; members of those projects can read and apply them.

## Planned entries

Procedures, specimen procedures, sessions and breedings carry a status of **planned**, **performed** or **cancelled**. Planned entries are shown to users with a "Planned" badge and are kept out of counts, public pages and API listings unless asked for explicitly. Permissions are the same as for performed entries.

## Public sharing

### Public sharing of projects
{: .note }
> When a project is made public:
> - its subjects, specimen sets, sessions, modules, cohorts, collections and breedings become readable without an account, in the public portal and the public API;
> - only project owners can make a project public;
> - public access is read-only; members keep their edit rights;
> - planned records are never shown publicly.

### Public sharing of personal attributes
{: .important }
> - Each personal attribute (setup, inventory, behavioral assay, data storage, license, protocol) has its own public setting, changed by its owners.
> - Make the attributes public that readers of a public project should be able to open; otherwise the public record shows the link but not the attribute.

## Permission management

- **Projects**: project page → Manage → Permissions: add or remove users and groups, change levels, set public access, send invitations.
- **Groups**: group page: add or remove members, change roles, handle join requests and email invitations.
- **Personal attributes**: the attribute's page → Permissions: users, groups, levels, public access.
- **API tokens** act with the permissions of their owner; see [API authentication]({{"api/#authentication"|absolute_url}}).
- **Institutional security policy**: your institution can require two-factor sign-in and set session lifetimes for every account of its email domain; see [Two-factor authentication]({{"webinterface/two-factor-authentication/"|absolute_url}}).
