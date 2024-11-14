---
layout: default
title: Project
parent: STEM
grand_parent: Data model
nav_order: 1
---

# Project model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Projects serve as an overall way to group subjects, sessions, and collections together. A project can be used to relate experiments for publications, describe day-to-day experiments, or share experimental data with collaborators. Projects define the overall permissions level of most other content.

## Fields

| Field | Description |
|:------|:------------|
| `Name` | Name of the project (**required**; string; maximum length: 200 characters; must be unique) |
| `Description` | A text description of the project. You can upload and insert images. |
| `Publications` | Related publications |
| `Tags` | Tags for the project. Great for organizational purposes, quick labeling, and filtering. |
| `Extra fields` | Allows you to add extra fields to the project. Values can be strings or numeric. |
| `Name used in storage` | Use this field if you have another name for your project in your local data storage (string; maximum length: 200 characters) |
| `Online repositories` | If this project has been shared in a online public repository, link it here. |
| `Users with roles` | Users associated with the project and their assigned roles |

## Permissions

Projects define the overall permissions level for subjects, sessions, collections, cohorts, and modules. You manage permissions through the management tab, where you can assign individual users and groups access levels to a project.

Projects have four permission levels: membership (read access), contributors, managers, and owners.

Visit the [permissions page]({{"datamodel/permission}}) to learn more. 

## Project API access

The API allows for programmable access to projects. Learn more about the projects' fields and data structure on the [Project API page]({{"api/stem/project/"|absolute_url}}).
