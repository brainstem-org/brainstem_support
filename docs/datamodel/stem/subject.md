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

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A subject is one animal (or planned animal) in the lab: its identity, where it came from, its genetics, lifecycle status and project membership. It is the anchor for everything done in vivo. Flexibility is built in through a rich text description, custom fields (**Extra content**) and tags. Subject-related entries are described through:

1. [__Procedures__]({{"datamodel/modules/procedure"|absolute_url}}): one-off actions performed on the subject, such as surgeries, implants, injections, drug administrations and endpoints.
2. [__Procedure episodes__]({{"datamodel/modules/procedureepisode/"|absolute_url}}): the perioperative event that groups related procedures with personnel, licenses, severity and recovery outcome.
3. [__Experimental interfaces__]({{"datamodel/modules/experimentalinterface/"|absolute_url}}): the probes, fibers, cannulas, windows and other access points installed in the subject. Implant procedures create them automatically.
4. [__Subject logs__]({{"datamodel/modules/subjectlog"|absolute_url}}): repeated, dated observations such as weight, welfare, consumption, housing and training.
5. [__Breedings__]({{"datamodel/stem/breeding/"|absolute_url}}): parent pairings (dam and sire) and litter metadata linked to offspring subjects.
6. [__Cohorts__]({{"datamodel/stem/cohort"|absolute_url}}): project-level groupings of subjects.

[Sessions]({{"datamodel/stem/session/"|absolute_url}}) link their subjects directly, and [specimen sets]({{"datamodel/stem/specimenset/"|absolute_url}}) record the subject the tissue was taken from. The distinction between a procedure and a log is one-off versus recurring: something done once is a procedure; something measured repeatedly is a log with dated entries. Each of these entries has its own page with its fields; the subject itself has only the fields below.

{% include datamodel_embed.html model="stem.subject" %}

## Fields

| Field | Description |
|:------|:------------|
| `Subject name` | Name of the subject (**required**; string; maximum length: 100 characters; must be unique across BrainSTEM). A purely local name such as "M1" will often collide; prefix it with your lab or project. |
| `Projects` | Projects the subject belongs to (**required**). Can belong to multiple projects. Only projects where you are at least a Contributor are offered. Learn more about project inheritance [here]({{"datamodel/stem/project/"|absolute_url}}). |
| `Sex` | Sex of the animal: Female, Male or Unknown (**required**). |
| `Species` | The species of the subject (**required**). Stored directly on the subject so that animals without a defined strain are represented accurately. Must reference an existing [species]({{"datamodel/taxonomies/species/"|absolute_url}}); submit missing species in the taxonomies section. Example: "Mus musculus" |
| `Strain` | Strain of the subject (optional). Must belong to the selected species. Leave blank when no strain applies; do not create placeholder strains. Must reference an existing [strain]({{"datamodel/taxonomies/strain/"|absolute_url}}). Example: "C57BL/6J" |
| `Status` | Current participation status (**required**). Choices: planned, active, inactive, transferred, deceased, unknown (default: active). Keep it current; setting a death date does not change the status. |
| `Description` | A rich text description of the subject. |
| `Genetic line` | Genetic line of the subject, including wild type (string; maximum length: 100 characters). Example: "PV-Cre x Ai32 line A" |
| `Genotype` | Confirmed genotype (string; maximum length: 200 characters). The Genotyping subject log holds the assay and result; this field holds the conclusion. Example: "PV-Cre/wt; Ai32/wt" |
| `Birth date` | Birth date of the subject (date format `YYYY-MM-DD`). Used to compute age at a procedure or session. |
| `Death date` | Death date of the subject (date format `YYYY-MM-DD`). |
| `Breeding` | The [breeding]({{"datamodel/stem/breeding/"|absolute_url}}) this subject was born from, when bred in-house. This links the animal to its parents. |
| `Subject identifier` | Any identifier used for this subject outside of BrainSTEM, such as an ear tag or RFID number (string; maximum length: 100 characters). |
| `Supplier` | Source of the subject. Must reference an existing [supplier]({{"datamodel/resources/supplier/"|absolute_url}}). Example: "The Jackson Laboratory" |
| `Licenses` | [Licenses]({{"datamodel/personal_attributes/license/"|absolute_url}}) covering work on this animal as a whole. Individual procedures and procedure episodes carry their own licenses too. |
| `Tags` | Tags for organization and filtering. Shared across all users. |
| `Subject name used in data storage` | The name of your subject in your local data storage, when it differs from the name above (string; maximum length: 200 characters). |
| `Extra content` | Custom key-value fields that the standard fields do not cover. Values can be text or numbers. Example: {"Weight": "25g", "Litter": "A3"}. [Schema](https://www.brainstem.org/schemas/Subject/Array.json) |

## Changing species and strain

The species is required when a subject is created. A strain alone is not accepted. Changing the species of a subject with a saved strain requires selecting a compatible strain, or clearing the strain, in the same save. The species cannot change while a procedure on the subject uses an atlas of another species.

## Deleting a subject

{: .warning }
Deleting a subject also deletes its procedures, subject logs and experimental interfaces. **Recover** on the subjects list restores the subject together with them; see [Deleted entries]({{"webinterface/deleted-entries/"|absolute_url}}).

A subject cannot be deleted while a breeding or a procedure episode points to it, or while a data acquisition or manipulation uses one of its experimental interfaces. Specimen sets derived from the subject keep their records; only the link to the subject is cleared.

## Permissions

Subjects inherit permissions from the projects associated with them. Procedures, procedure episodes, experimental interfaces, subject logs and procedure logs inherit permissions through the subject. You need Contributor access through at least one of the subject's projects to add or edit it.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to subjects. Learn more about the subjects' fields and data structure on the [Subject API page]({{"api/stem/subject/"|absolute_url}}).
