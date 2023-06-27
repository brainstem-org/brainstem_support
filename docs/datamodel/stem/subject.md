---
layout: default
title: Subject
parent: STEM
grand_parent: Data model
nav_order: 2
---

# Subject
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction
The subject model describes your animal subject through a set of standard fields. There is flexibility built through a rich text description field, extra fields, and tags.  Actions, Subject state change, and Subject logs all provides modular construction that flexibly can describe procedures and other things performed on your subject based on three modules: 
1. Actions: Surgical procedures and other actions performed on the environment (e.g.: probe implantations, virus injections, and optic fiber implants)
2. Subject state changes: Any state change performed on a subject (e.g.: perfusion of the brain, lesion, creation of brain slices)
3. Subject logs: Repetitive logs for your subject (e.g.: including Weighing logs, Food and Water deprivation logs, and Housing logs)


## Fields

| Field          | Description  |
|:---------------|:-------------|
| `Name`         | Name of the subject (**[required]**; max length: 100; must be unique) |
| `Description`  | A rich text description of the subject |
| `Strain`       | Animal strain (**[required]**) |
| `Sex`          | Sex of the animal: (Male, Female, or Unknown; **[required]**) |
| `Genetic line` | Genetic line of the subject. Could also be wild type (max length: 100) |
| `Projects`     | Projects the subject belongs to (**[required]**) |
| `Birth date`   | Birth date of the animal subject (e.g. "2023-03-22") |
| `Death date`   | Death date of the animal subject (e.g. "2023-03-25") |
| `Extra fields` | Allows you to add extra fields to the subject. The values can be a string or a numeric value |
| `Name used in repository` | Use this field if you have another name of your subject (max length: 200) |
| `Tags`         | Tags for the subject. Tags are great for organizational purpose, to quickly label a subject and can be used as a filter afterwards. |


## Permissions
Subjects inherit permissions from projects associated with them. Actions, Subject state changes, Subject logs and action logs all inherit permissions through the subject.

Visit the [permissions page] to learn more. 

## Subject API access
The API allows for programmable access to subjects. Learn more about the subjects' fields and data structure on the [Subject API page]. 
