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

1. TOC
{:toc}

## Introduction

Projects serve as a primary means to group subjects, sessions, and collections together. A project can be used to relate experiments for publications, describe day-to-day experiments, or share experimental data with collaborators. Projects define the overall permissions level of most other content.


## Fields

| Field | Description |
|:------|:------------|
| `Project name` | Name of the project (**required**; string; maximum length: 200 characters; must be unique across BrainSTEM). Example: "Hippocampal Memory Study 2024", "Visual Cortex Development Project" |
| `Description` | A rich text description of the project. You can upload and insert images through rich text formatting. Example: "This project investigates place cell activity in the CA1 region of the hippocampus..." |
| `Publications` | Related publications. Can link multiple publications to a project. Example: "Smith et al. 2024 Nature", "Garcia 2023 Science" |
| `Tags` | Tags for the project. Great for organizational purposes and quick labeling, and filtering. Tags are shared across all users. Example: "electrophysiology", "behavior", "hippocampus" |
| `Extra content` | Allows you to add extra fields to the project. Values can be strings or numeric. Saved as key-value pairs. Example: {"Ethics_Protocol": "2024-001", "Funding": "NIH R01"} |
| `Project name in storage` | Use this field if you have another name for your project in your local data storage (string; maximum length: 200 characters). Example: "HPC_MEM_24" |
| `Repository links` | If this project has been shared in an online public repository, link it here. Example: Links to DANDI (dandiset-123456) or OpenNeuro (ds000123) |
| `User with role` | Individual users assigned to the project with specific roles. Roles include: Contact person, Conceptualizer, Data collector, Data curator, Data manager, Formal analyzer, Investigator, Maintainer, Method developer, Producer, Project leader, Project manager, Supervisor. Example: Lab PI as Project leader, postdoc as Investigator, students as Data collectors |
| `Public` | Determines if the project is publicly available (boolean; default: False). When enabled, allows public access according to public inheritance rules |

## Permissions

Projects define the overall permissions level for subjects, sessions, collections, cohorts, and modules. You manage permissions through the management tab, where you can assign individual users and groups access levels to a project.

Projects have four permission levels: membership (read access), contributors, managers, and owners.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to projects. Learn more about the projects' fields and data structure on the [Project API page]({{"api/stem/project/"|absolute_url}}).
