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
| `Name` | Name of the subject (**required**; maximum length: 100 characters; must be unique) |
| `Projects` | Projects the subject belongs to (**required**) |
| `Sex` | Sex of the animal: (Male, Female, or Unknown; **required**) |
| `Species` | Species of the subject (**required**) |
| `Strain` | Strain of the subject (**required**) |
| `Description` | A rich text description of the subject |
| `Genetic line` | Genetic line of the subject. Could also be wild type (string; maximum length: 100 characters) |
| `Birth date` | Birth date of the animal subject (e.g., "2023-03-22") |
| `Death date` | Death date of the animal subject (e.g., "2023-03-25") |
| `Tags` | Tags for the subject. Great for organizational purposes, quick labeling, and filtering. |
| `Subject identifier` | Any identifier used for this subject outside of BrainSTEM, such as an ear tag or RFID number. |
| `Source` | Source of the subject, e.g., Charles River. |
| `Name used in storage` | Use this field if you have another name for your subject in your local data storage (string; maximum length: 100 characters) |
| `Extra fields` | Allows you to add extra fields to the subject. Values can be strings or numeric. |

### Procedure data fields

Please see the dedicated page describing the [Procedure data model]({{"datamodel/modules/procedure"|absolute_url}}).


## Permissions

Subjects inherit permissions from projects associated with them. Procedures, Subject state changes, Subject logs, and Procedure logs all inherit permissions through the subject.

Visit the [permissions page] to learn more. 

## Subject API access

The API allows for programmable access to subjects. Learn more about the subjects' fields and data structure on the [Subject API page]({{"api/stem/subject/"|absolute_url}}).
