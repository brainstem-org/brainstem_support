---
layout: default
title: Cohorts
parent: STEM
grand_parent: Data model
nav_order: 5
---

# Cohort model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Cohorts facilitate the creation of subgroups of subjects within a project. They allow users to define specific sets of subjects for analysis or visualization purposes. All subjects in a cohort must belong to the same project, enabling organized and structured grouping of research subjects.

## Fields

| Field | Description |
|:------|:------------|
| `Name` | Name of the cohort (**required**; string; max length: 100 characters; must be unique within the project). Example: "Control Group A", "Treatment Group 2024" |
| `Project` | The project the cohort belongs to (**required**). A cohort can belong to a single project. Example: "Drug Treatment Study" |
| `Subjects` | Subjects in the cohort. All subjects must belong to the same project (**required**). Example: "Mouse_01", "Mouse_02", "Mouse_03" |
| `Description` | A text description of the cohort, providing additional context and information. Pictures can be uploaded and inserted through rich text formatting. Example: "Control group of 6-month-old male mice..." |
| `Tags` | Tags for the cohort. Great for organizational purposes, quick labeling, and filtering. Tags are shared across all users. Example: "control-group", "batch-1", "6-month-old" |

## Permissions

Cohorts inherit permissions from their associated project. You can only add subjects to the cohort that are part of the same project.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Cohorts API access

The API allows for programmable access to cohorts. Learn more about the cohorts' fields and data structure on the [Cohorts API page]({{"api/stem/cohort/"|absolute_url}}).