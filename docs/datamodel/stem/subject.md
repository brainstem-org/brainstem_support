---
layout: default
title: Subject
parent: STEM
grand_parent: Data model
nav_order: 2
---

# Subject model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

The subject model describes your animal subject through a set of standard fields. Flexibility is built in through a rich text description field, extra fields, and tags. Procedures offer a modular framework that can be used to describe processes related to your subject.

## Fields

| Field | Description |
|:------|:------------|
| `Name` | Name of the subject (**required**; string; maximum length: 100 characters; must be unique across BrainSTEM). Example: "Mouse_01", "Rat_2024_A" |
| `Projects` | Projects the subject belongs to (**required**). Can belong to multiple projects. Example: Added to both "Memory Study" and "Aging Study". Learn more about project inheritance [here]({{"datamodel/stem/project/"|absolute_url}}). |
| `Sex` | Sex of the animal: (Male, Female, or Unknown; **required**). Selected from predefined choices. Example: "Female" |
| `Species` | Species of the subject (**required**). Please add in taxonomies section if not available. Example: "Mus musculus" |
| `Strain` | Strain of the subject (**required**). Please add in taxonomies section if not available. Example: "C57BL/6J" |
| `Description` | A rich text description of the subject. Can be left empty. Example: "Male C57BL/6J mouse, exhibits normal behavior..." |
| `Genetic line` | Genetic line of the subject. Could also be wild type (string; maximum length: 100 characters). Example: "Wild type" or "PV-Cre" |
| `Birth date` | Birth date of the animal subject. Can be left empty. Example: "2023-03-22" |
| `Death date` | Death date of the animal subject. Can be left empty. Example: "2024-03-25" |
| `Tags` | Tags for the subject. Great for organizational purposes, quick labeling, and filtering. Example: control-group", "lesion" |
| `Subject identifier` | Any identifier used for this subject outside of BrainSTEM, such as an ear tag or RFID number. Example: "Ear tag #A1234" |
| `Source` | Source of the subject. Can be left empty. Example: "Charles River", "In-house breeding" |
| `Name used in storage` | Use this field if you have another name for your subject in your local data storage (string; maximum length: 200 characters). Example: "M01_2024_exp3" |
| `Extra fields` | Allows you to add extra fields to the subject. Values can be strings or numeric. Example: {"Weight": "25g", "Litter": "A3"} |

### Procedure data fields

Please see the dedicated page describing the [Procedure data model]({{"datamodel/modules/procedure"|absolute_url}}).


## Permissions

Subjects inherit permissions from projects associated with them. Procedures, Subject logs, and Procedure logs all inherit permissions through the subject.

Visit the [permissions page]({{"datamodel/permission/"|absolute_url}}) to learn more. 

## Subject API access

The API allows for programmable access to subjects. Learn more about the subjects' fields and data structure on the [Subject API page]({{"api/stem/subject/"|absolute_url}}).
