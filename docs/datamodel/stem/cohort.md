---
layout: default
title: Cohort
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
| `Name` | Name of the cohort (**required**; string; max length: 100 characters; must be unique within the project) |
| `Project` | The project the cohort belongs to (**required**) |
| `Subjects` | Subjects in the cohort. All subjects must belong to the same project (**required**) |
| `Description` | A text description of the cohort, providing additional context and information. Pictures can be uploaded and inserted. |
| `Tags` | Tags for the cohort. Great for organizational purposes, quick labeling, and filtering. |

## Permissions

Cohorts inherit permissions from their associated project. You can only add subjects to the cohort that are part of the same project.

Visit the [permissions page]({{"datamodel/permission}}) to learn more. 

## Cohort API access

The API allows for programmable access to cohorts. Learn more about the cohorts' fields and data structure on the [Cohort API page]({{"api/stem/cohort/"|absolute_url}}).