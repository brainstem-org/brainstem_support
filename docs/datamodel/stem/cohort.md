---
layout: default
title: Cohorts
parent: Subjects
grand_parent: Data model
nav_order: 5
---

# Cohort model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

Cohorts facilitate the creation of subgroups of subjects within a project, for example an experimental group or the subjects of one analysis. All subjects in a cohort must belong to the same project. The membership is ordered: subjects keep the order you give them.

{% include datamodel_embed.html model="stem.cohort" %}

## Fields

| Field | Description |
|:------|:------------|
| `Cohort name` | Name of the cohort (**required**; string; maximum length: 100 characters; must be unique within the project). Example: "Control Group A", "Treatment Group 2024" |
| `Project` | The project the cohort belongs to (**required**). A cohort belongs to a single project. Example: "Drug Treatment Study" |
| `Subjects` | Subjects in the cohort (**required**). All subjects must belong to the same project. Add subjects and reorder them using drag-and-drop; the order is stored. Example: "Mouse_01", "Mouse_02", "Mouse_03" |
| `Description` | A text description of the cohort. Pictures can be uploaded and inserted through rich text formatting. |
| `Tags` | Tags for organization and filtering. Tags are shared across all users. Example: "control-group", "batch-1" |

## Permissions

Cohorts inherit permissions from their associated project. You can only add subjects to the cohort that are part of the same project. Deleting the project deletes its cohorts.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to cohorts. Learn more about the cohorts' fields and data structure on the [Cohort API page]({{"api/stem/cohort/"|absolute_url}}).
