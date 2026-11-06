---
layout: default
title: Breedings
parent: Subjects
grand_parent: Data model
nav_order: 4
---

# Breeding model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A breeding records one breeding pair and the litter it produced. It links one maternal subject (dam) and one paternal subject (sire), both of which must exist as subjects, and tracks the pairing through its life: when the pair was set up, when the litter was born and weaned, and when the pairing ended. Offspring are linked the other way round: the breeding is recorded on each pup's own subject form. A litter size of eight may therefore have fewer subject records.

{% include datamodel_embed.html model="stem.breeding" %}

## Fields

| Field | Description |
|:------|:------------|
| `Breeding name` | Name of the breeding (**required**; string; maximum length: 100 characters; must be unique within the project). Most labs use the cage or pairing code. Example: "B6J x PV-Cre Spring 2026" |
| `Status` | Planned, performed or cancelled (default: performed). A planned breeding is prepared ahead of time; its parents may still be planned subjects. The pairing date is required when it is marked as performed. Planned breedings are left out of listings unless asked for. |
| `Project` | Project the breeding belongs to (**required**). A breeding belongs to a single project, and both parent subjects must belong to this same project. |
| `Maternal Subject (Dam)` | Female parent subject (**required**). Must have sex set to Female and must belong to the selected project. |
| `Paternal Subject (Sire)` | Male parent subject (**required**). Must have sex set to Male, must belong to the selected project, and must be different from the maternal subject. |
| `Description` | Rich text notes for breeding details. Useful for pairing observations, outcomes, and contextual notes. |
| `Tags` | Tags for organization and filtering. Tags are shared across users and models. |
| `Breeding start date` | Date the breeding started (pairing date; date format `YYYY-MM-DD`). |
| `Breeding end date` | Date the breeding ended (separation date; date format `YYYY-MM-DD`). Leave blank if ongoing. |
| `Birth date` | Date of birth of the offspring (date format `YYYY-MM-DD`). Each pup also carries its own birth date. |
| `Weaning date` | Date the litter was or will be weaned (typically 21-28 days after birth; date format `YYYY-MM-DD`). |
| `Litter size` | Expected or actual number of offspring (positive integer). |
| `Expected genotype` | Expected genotype of the offspring (string; maximum length: 100 characters). |

Deleting a breeding clears the breeding link on its offspring subjects; the subjects themselves are kept.

## Permissions

Breedings inherit permissions from their associated project.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to breedings, enabling you to read, edit, and delete breedings through the API. Learn more about the breedings' fields and data structure on the [Breedings API page]({{"api/stem/breeding/"|absolute_url}}).
