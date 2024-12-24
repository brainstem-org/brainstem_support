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

Subject logs refers to records that track various aspects of the subjects' living conditions, physiological states, and behaviors over time. These logs are essential for ensuring the welfare of subjects, maintaining consistent experimental conditions, and accurately interpreting the effects of interventions.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of subject logs (**required**). Selected from predefined types. Example: "Food consumption log", "Housing log". *See options below* |
| `Subject` | The subject of the log (**required**). Must reference a [subject]({{"datamodel/stem/subject/"|absolute_url}}). Example: "Silicon probe implant #A123" |
| `Description` | Description of the subject logs. Can be left empty (string). Example: "Daily food consumption" |
| `Date and time` | Timestamp for each log-entry. There are two types of subject logs with either simple timestamps or time period defined by a start and an end timestamps. Example: "2024-03-15 14:30:00" |
| `Start and end time` | Start and stop timestamp of each log-entry. Example: "2024-03-15 14:30:00" |
| `Type details` | Type-specific fields for each entry in the log. Fields vary by type. Example: For impedance log - impedance values in kOhm. *See options below* |
| `Notes` | Notes about the subject logs for each entry in the log (string). Example: "Observed slight increase in impedance values" |

## Types of subject logs

{% include_relative type_descriptions/subjectlog_types.md %}

## Submission form

The subject logs submission form consists of two parts:
1. First part: Fill in the required fields.
2. Second part: After clicking "Create and continue," you can edit all fields of the entry.

## Permissions

Subject logs inherit permissions from projects via the subject and then the subject associated with the entry.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Subject log API access

The API allows for programmable access to Subject logs, enabling you to read, edit, and delete subject logss through the API. Learn more about the subject logs' fields and data structure on the [Subject logs API page]({{"api/modules/subjectlog/"|absolute_url}}).
