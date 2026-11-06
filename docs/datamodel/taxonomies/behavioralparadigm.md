---
layout: default
title: Behavioral paradigms
parent: Taxonomies
grand_parent: Data model
nav_order: 7
---

# Behavioral paradigm model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

Behavioral paradigms represent standardized behavioral tasks and protocols shared across the neuroscience community. A paradigm describes the conceptual approach to assessing a particular behavior — independent of any specific lab's implementation or physical apparatus.

{% include datamodel_embed.html model="taxonomies.behavioralparadigm" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Name`` | The name of the behavioral paradigm (**required**; string; maximum length: 200 characters; must be unique). |
| ``Category`` | The behavioral category this paradigm belongs to. Must reference an existing [behavioral category]({{"datamodel/taxonomies/behavioralcategory/"|absolute_url}}). Example: "Spatial Learning", "Anxiety". |
| ``Description`` | Detailed description of the paradigm (text; maximum length: 3000 characters): what behavior it assesses and the conceptual approach. Should not include setup-specific details or data acquisition methods. |
| ``Species`` | Species for which this paradigm is established. Can include multiple [species]({{"datamodel/taxonomies/species/"|absolute_url}}). Leave empty if universal. |
| ``Original publication`` | Citation for the original publication (string; maximum length: 500 characters). Example: "Morris 1984". |
| ``Reference URL`` | URL to reference documentation or the original publication (URL; maximum length: 200 characters). |
| ``RRID`` | Research Resource Identifier, where the task has one (string; maximum length: 100 characters). |
| ``External identifiers`` | Identifiers in other registries or ontologies, each with source, id and URL. |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

{% include schemas/behavioralparadigm.md %}

## How it fits together

![The behavioral track and the setup track: behavioral categories group paradigms, and an assay is your lab's version of a paradigm on a setup type; a setup is your rig of a setup type, with its equipment. A behavior in a session runs one assay on one setup with its subjects.]({{site.baseurl}}/assets/images/diagrams/behavior-tracks-behavioralparadigm.svg)
*The behavioral track (left) and the setup track (right) run from the shared taxonomies through your lab's personal attributes and meet in a behavior recorded in a session. This page describes the behavioral paradigm, drawn solid. The setup type category is a field of the setup type, not a separate record.*

BrainSTEM organizes behavioral experiments through a hierarchy that separates shared scientific knowledge from lab-specific implementation details:

- **Behavioral category** — The broad domain (e.g., "Anxiety & Affect" → "Anxiety")
- **Behavioral paradigm** (this page) — The standardized task shared across the field (e.g., "Elevated Plus Exploration")
- **Behavioral assay** — Your lab's specific implementation of a paradigm under a specific preparation condition, linked to a setup type (e.g., "EPM 5-min test")
- **Behavior** — The actual execution of an assay within a session, tied to specific subjects and a physical setup

Categories and paradigms are shared taxonomies — available to all users once approved. Assays and behaviors are lab-specific and scoped to your groups and projects.

## Examples

| Category | Paradigm | What it assesses |
|:---------|:---------|:-----------------|
| Spatial Learning | Morris Water Navigation Task | Hippocampal-dependent spatial memory |
| Anxiety | Elevated Plus Exploration | Anxiety-like behavior via open arm avoidance |
| Motor Coordination | Rotarod | Balance, coordination, and motor learning |
| Nociception | Von Frey Test | Mechanical pain sensitivity threshold |

## Submission process

Anyone can submit new behavioral paradigms or propose changes to existing ones. A submission enters the approval queue and is usable in your own records immediately; it is visible only to you until accepted. Please review existing entries for guidance on what to submit. A paradigm cannot be deleted while behavioral assays point to it.

## Permissions

Once an entry has been approved, it becomes available to everyone. Editing an accepted entry is restricted; an edit creates a change request that is reviewed before it takes effect. Your own pending submissions remain yours to edit or cancel.

## API access

The API allows for programmable access, enabling you to read and edit entries. For more information about the fields and data structure, please consult the [Behavioral paradigm API page]({{"api/taxonomies/behavioralparadigm/"|absolute_url}}).
