---
layout: default
title: Subject logs
parent: Modules
grand_parent: Data model
nav_order: 8
---

# Subject logs model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Subject logs refer to records that track various aspects of the subjects' living conditions, physiological states, and behaviors over time. These logs are essential for ensuring the welfare of subjects, maintaining consistent experimental conditions, and accurately interpreting the effects of interventions.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of subject log (**required**). *See options below* |
| `Subject` | The subject associated with the log (**required**) |
| `Description` | Description of the subject log |
| `Notes` | Notes about the subject log (for each log entry) |
| `Date and time` | Timestamp for each log entry (for simple timestamp logs) |
| `Type details` | Type-specific fields for each log entry. *See options below* |

## Types of subject logs

These are the available *Type* options for Subject logs:

- Food consumption log
- Food deprivation log
- Housing log
- Water consumption log
- Water deprivation log
- Weighing log
- Wellness log

A detailed list of the type-specific fields can be found on the [subject log types page]({{"datamodel/schemas/subject_logs/"|absolute_url}}).

## Submission form

The subject log submission form consists of two parts:
1. First part: Fill in the required fields, including the subject and the type of log.
2. Second part: After clicking "Create and continue," you can edit all fields of the log entry.

## Permissions

Subject logs inherit permissions from projects via the subject associated with the entry.

Visit the [permissions page] to learn more.

## Subject log API access

The API allows for programmable access to Subject logs, enabling you to read, edit, and delete subject logs through the API. Learn more about the subject logs' fields and data structure on the [Subject log API page]({{"api/modules/subjectlog/"|absolute_url}}).