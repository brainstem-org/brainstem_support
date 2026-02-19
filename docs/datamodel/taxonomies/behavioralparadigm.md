---
layout: default
title: Behavioral paradigm
parent: Taxonomies
grand_parent: Data model
nav_order: 2
---

# Behavioral paradigm model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Behavioral paradigms represent standardized behavioral tasks and protocols shared across the neuroscience community. A paradigm describes the conceptual approach to assessing a particular behavior — independent of any specific lab's implementation or physical apparatus.

## How it fits together

BrainSTEM organizes behavioral experiments through a hierarchy that separates shared scientific knowledge from lab-specific implementation details:

- **Behavioral Category** — The broad domain (e.g., "Learning & Memory" → "Spatial Learning")
- **Behavioral Paradigm** (this page) — The standardized task shared across the field (e.g., "Morris Water Navigation Task")
- **Behavioral Assay** — Your lab's specific implementation of a paradigm, linked to a setup type (e.g., "MWM 4-day acquisition, 60s trials, probe on day 5")
- **Behavior** — The actual execution of an assay within a session, tied to specific subjects and a physical setup

Categories and paradigms are shared taxonomies — available to all users once approved. Assays and behaviors are lab-specific and scoped to your groups and projects.

## Examples

| Category | Paradigm | What it assesses |
|:---------|:---------|:-----------------|
| Spatial Learning | Morris Water Navigation Task | Hippocampal-dependent spatial memory |
| Anxiety | Elevated Plus Exploration | Anxiety-like behavior via open arm avoidance |
| Motor Coordination | Rotarod | Balance, coordination, and motor learning |
| Nociception | Von Frey Test | Mechanical pain sensitivity threshold |

## Fields

| Field | Description |
|:------|:------------|
| ``Name`` | The name of the behavioral paradigm (**required**; string; maximum length: 200 characters; must be unique). |
| ``Category`` | The behavioral category this paradigm belongs to. Must reference an existing [behavioral category]({{"datamodel/taxonomies/behavioralcategory/"|absolute_url}}). Example: "Spatial Learning", "Anxiety". |
| ``Description`` | Detailed description of the paradigm (text; maximum length: 3000 characters): what behavior it assesses and the conceptual approach. Should not include setup-specific details or data acquisition methods. |
| ``Species`` | Species for which this paradigm is applicable. Can include multiple [species]({{"datamodel/taxonomies/species/"|absolute_url}}). |
| ``Original publication`` | Citation for the original publication (string; maximum length: 500 characters). Example: "Morris 1984". |
| ``Reference URL`` | URL to reference documentation or the original publication (URL; maximum length: 200 characters). |
| ``RRID`` | Research Resource Identifier if available. |
| ``External identifiers`` | External identifiers from various databases. |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

## Submission process

Anyone can submit new behavioral paradigms or propose changes to existing ones. All submissions require approval before becoming available. Please review existing entries for guidance on what to submit.

## Permissions

Once an entry has been approved, it becomes available to everyone.

## Behavioral paradigm API access

The API allows for programmable access, enabling you to read and edit entries. For more information about the fields and data structure, please consult the [Behavioral paradigm API page]({{"api/taxonomies/behavioralparadigm/"|absolute_url}}).
