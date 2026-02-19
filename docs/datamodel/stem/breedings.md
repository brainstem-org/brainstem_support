---
layout: default
title: Breedings
parent: Subjects
grand_parent: Data model
nav_order: 3
---

# Breeding model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Breedings capture parent pairings and litter-level metadata within a project. A breeding links one maternal subject (dam) and one paternal subject (sire), and can track dates and expected offspring details.

## Fields

| Field | Description |
|:------|:------------|
| `Breeding name` | Name of the breeding (**required**; string; maximum length: 100 characters; must be unique within a project). Example: "B6J x PV-Cre Spring 2026" |
| `Project` | Project the breeding belongs to (**required**). A breeding belongs to a single project, and both parent subjects must belong to this same project. |
| `Maternal Subject (Dam)` | Female parent subject (**required**). Must have sex set to Female and must belong to the selected project. |
| `Paternal Subject (Sire)` | Male parent subject (**required**). Must have sex set to Male, must belong to the selected project, and must be different from the maternal subject. |
| `Description` | Rich text notes for breeding details. Useful for pairing observations, outcomes, and contextual notes. |
| `Tags` | Tags for organization and filtering. Tags are shared across users and models. |
| `Birth date` | Date of birth for offspring from this breeding (date format `YYYY-MM-DD`). |
| `Breeding start date` | Date the breeding started (pairing date; date format `YYYY-MM-DD`). |
| `Breeding end date` | Date the breeding ended (separation date; date format `YYYY-MM-DD`). |
| `Weaning date` | Date the litter was or will be weaned (date format `YYYY-MM-DD`). |
| `Litter size` | Expected or actual number of offspring (positive integer). |
| `Expected genotype` | Expected genotype of offspring (string; maximum length: 100 characters). |


## Permissions

Breedings inherit permissions from their associated project.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.
