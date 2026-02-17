---
layout: default
title: Subjects
parent: Data model
nav_order: 2
has_toc: false
---

# Subject model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

The subjects model describes your animal subject through a set of standard fields. Flexibility is built in through a rich text description field, extra fields, and tags. Subject-related records can be further described through:

1. [__Procedures__]({{"datamodel/modules/procedure"|absolute_url}}): Experimental or husbandry interventions associated with a subject (for example surgeries, injections, or handling protocols).
2. [__Subject logs__]({{"datamodel/modules/subjectlog"|absolute_url}}): Time-stamped notes and tracked observations for a subject (for example weight changes, health checks, and routine monitoring).
3. [__Breedings__]({{"datamodel/stem/breedings"|absolute_url}}): Parent pairing records (dam/sire) and litter-level metadata linked to offspring subjects.
4. [__Cohorts__]({{"datamodel/stem/cohort"|absolute_url}}): Project-level groupings of subjects used for organization, filtering, and analysis.

## Fields

| Field | Description |
|:------|:------------|
| `Subject name` | Name of the subject (**required**; string; maximum length: 100 characters; must be unique across BrainSTEM). Example: "Mouse_01", "Rat_2024_A" |
| `Projects` | Projects the subject belongs to (**required**). Can belong to multiple projects. Example: Added to both "Memory Study" and "Aging Study". Learn more about project inheritance [here]({{"datamodel/stem/project/"|absolute_url}}). |
| `Sex` | Sex of the animal: (Male, Female, or Unknown; **required**). Selected from predefined choices. Example: "Female" |
| `Status` | Current participation status in research activities. Choices: planned, active, inactive, transferred, deceased, unknown (default: active). |
| `Species` | Species is derived from the selected strain (not a direct field on Subject). Please add in taxonomies section if not available. Example: "Mus musculus" |
| `Strain` | Strain of the subject (**required**). Please add in taxonomies section if not available. Example: "C57BL/6J" |
| `Description` | A rich text description of the subject. Can be left empty. Example: "Male C57BL/6J mouse, exhibits normal behavior..." |
| `Genetic line` | Genetic line of the subject. Could also be wild type (string; maximum length: 100 characters). Example: "Wild type" or "PV-Cre" |
| `Genotype` | Confirmed genotype of the subject (string; maximum length: 200 characters). Example: "PV-Cre/wt; Ai32/wt" |
| `Birth date` | Birth date of the animal subject. Can be left empty. Example: "2023-03-22" |
| `Death date` | Death date of the animal subject. Can be left empty. Example: "2024-03-25" |
| `Breeding` | The breeding from which this subject was born. Can be left empty. |
| `Tags` | Tags for the subject. Great for organizational purposes, quick labeling, and filtering. Example: "control-group", "lesion" |
| `Subject identifier` | Any identifier used for this subject outside of BrainSTEM, such as an ear tag or RFID number (string; maximum length: 100 characters). Example: "Ear tag #A1234" |
| `Supplier` | Source/supplier of the subject. Can be left empty. Example: "Charles River", "The Jackson Laboratory", "In-house breeding" |
| `Licenses` | Licenses covering this subject for regulatory reporting and compliance. Can be left empty and may include multiple licenses. |
| `Subject name used in data storage` | Use this field if you have another name for your subject in your local data storage (string; maximum length: 200 characters; optional). Example: "M01_2024_exp3" |
| `Additional fields` | Allows you to add additional fields to the subject. Values can be strings or numeric. Example: {"Weight": "25g", "Litter": "A3"} |

### Procedures data fields

Please see the dedicated page describing the [Procedures data model]({{"datamodel/modules/procedure"|absolute_url}}).

### Subject logs data fields

Please see the dedicated page describing the [Subject logs data model]({{"datamodel/modules/subjectlog"|absolute_url}}).

### Cohorts data fields

Please see the dedicated page describing the [Cohorts data model]({{"datamodel/stem/cohort"|absolute_url}}).

### Breedings data fields

Please see the dedicated page describing the [Breedings data model]({{"datamodel/stem/breedings"|absolute_url}}).


## Permissions

Subjects inherit permissions from projects associated with them. Procedures, Subject logs, and Procedure logs all inherit permissions through the subject.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to subjects. Learn more about the subjects' fields and data structure on the [Subject API page]({{"api/stem/subject/"|absolute_url}}).
