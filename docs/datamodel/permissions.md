---
layout: default
title: Permissions
parent: Data model
has_children: false
nav_order: 9
---

# Permissions
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

BrainSTEM has a hierarchical permission system that governs access control across the platform. This system enables flexible collaboration while maintaining data security through inheritance-based permissions.

![permissions]({{site.baseurl}}/assets/images/permissions_v3.png)

## Permission Levels Overview

| Permission levels | Groups | Projects | Personal Attributes |
|:-----------------|:-------|:---------|:-------------------|
| Permission scope | 3 levels, users only | 4 levels for groups & users | 4 levels for groups & users |
| Members | Inherit project permissions | Read access to:<br>- subjects<br>- sessions<br>- modules | Read access to:<br>- attributes<br>- equipment |
| Contributors | - | Create/edit/delete models | Create/edit/delete equipment |
| Managers | Add/remove members | Add/remove members & groups | Add/remove members & groups |
| Owners | Manage group details<br>Add/remove managers | Edit project details<br>Add/remove managers | Edit attribute details<br>Add/remove managers |

## Permission Levels

### Group Permissions

Groups are the foundation of BrainSTEM's permission system, offering three distinct permission levels:

| Permission Level | Capabilities |
|:----------------|:-------------|
| **Owner** | - Manage group details and settings<br>- Add/remove managers<br>- Associate group with laboratory<br>- Rename group<br>- Manage public access settings |
| **Manager** | - Add/remove regular members<br>- Create member invitations<br>- Remove users from group|
| **Member** | - Access group resources<br>- Inherit project permissions assigned to group<br>- View group content<br>- Leave group voluntarily |

### Project Permissions

Projects implement four permission levels that can be assigned to both individual users and groups:

| Permission Level | Capabilities |
|:----------------|:-------------|
| **Owner** | - Manage project details<br>- Add/remove managers<br>- Has all Manager permissions |
| **Manager** | - Add/remove project members<br>- Add/remove project groups<br>- Has all Contributor permissions |
| **Contributor** | - Create/edit/delete project related models<br>- Has all Member permissions |
| **Member** | - Read access to project, project-related subjects<br>- Read access to sessions and modules |

{: .note }
When applied to groups, these permissions extend to all group members automatically.

| Group Permission Level | Effect on Group Members |
|:----------------------|:-----------------------|
| **Owner Groups** | - All group members can manage project details<br>- All group members can add/remove managers<br>- Includes all Manager group permissions |
| **Manager Groups** | - All group members can add/remove project members<br>- All group members can add/remove project groups<br>- Includes all Contributor group permissions |
| **Contributor Groups** | - All group members can create/edit/delete project related models<br>- Includes all Member group permissions |
| **Member Groups** | - All group members get read access to project, project-related subjects<br>- All group members get read access to sessions and modules |



## Permission Inheritance

### Projects

The STEM branch follows this hierarchical pattern:
```
Project
├── Subjects
│   ├── Subject Logs
│   └── Procedures
│       └── Procedure Logs
├── Sessions
│   ├── Behaviors
│   ├── Manipulations
│   └── Data acquisition
├── Collections
└── Cohorts
```

#### Inheritance Rules
{: .no_toc}

| Parent Level | Inheritance Pattern | Inheriting Components |
|:-------------|:-------------------|:-------------------|
| **Project** | All project components inherit base permissions | Subjects, Sessions, Collections, Cohorts |
| **Subject** | Direct inheritance with cascading effects | Subject Logs, Procedures, Procedure Logs (via Procedures) |
| **Session** | Module-level inheritance | Behaviors, Data acquisition, Manipulations |

### Personal Attributes

Personal attributes follow their own inheritance structure from groups:
```
Personal Attributes
├── Setups
│   └── Equipment
├── Inventories
│   └── Consumable stocks
├── Data storages
└── Behavioral Paradigms
```

#### Group Level Inheritance
{: .no_toc}

| Parent Level | Inheritance Pattern | Inheriting Components |
|:-------------|:-------------------|:-------------------|
| **Group** | Direct inheritance from associated groups | Personal Attributes (Behavioral Paradigms, Data Storage, Setups, Inventories) |
| **Experimental Setup** | Direct inheritance with module-level access | Equipment |
| **Inventory** | Direct inheritance with module-level access | Consumable Stocks |

* All personal attributes inherit permissions directly from their associated groups
* Group membership automatically grants access to personal attributes

## Public Sharing

### Public Sharing of Projects
{: .note }
> When a Project is made public:
> - All associated components become publicly accessible
> - Only project owners can make a project public
> - Public access is read-only for anonymous users
> - Authorized users retain their edit capabilities

### Public Sharing of Personal Attributes
{: .important }
> - Each Personal Attribute requires individual public sharing settings
> - Only owners can modify public access settings
> - Public status required for behavioral paradigms, data storage, and setups used in public projects

## Permission Management

### Project Permissions
- Access: Project page → Manage → Permissions
- Actions: Add/remove users/groups, modify permission levels, set public access

### Group Permissions
- Access: Group page → Your group
- Actions: Add/remove members, modify member roles
