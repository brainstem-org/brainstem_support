---
layout: default
title: Behavioral categories
parent: Taxonomies
grand_parent: Data model
nav_order: 6
---

# Behavioral category model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

Behavioral categories provide a two-level hierarchical classification for organizing behavioral paradigms into meaningful groups by cognitive domain or experimental focus.

{% include datamodel_embed.html model="taxonomies.behavioralcategory" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Name`` | The name of the behavioral category (**required**; string; maximum length: 100 characters; must be unique). |
| ``Parent category`` | Parent category for hierarchical organization. Maximum hierarchy depth is two levels. |
| ``Description`` | Description of what this category encompasses (text; maximum length: 2000 characters). |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

## How it fits together

[![The behavioral track and the setup track: behavioral categories group paradigms, and an assay is your lab's version of a paradigm on a setup type; a setup is your rig of a setup type, with its equipment. A behavior in a session runs one assay on one setup with its subjects.]({{site.baseurl}}/assets/images/diagrams/behavior-tracks-behavioralcategory.svg)]({{site.baseurl}}/assets/images/diagrams/behavior-tracks-behavioralcategory.svg)
*The behavioral track (left) and the setup track (right) run from the shared taxonomies through your lab's personal attributes and meet in a behavior recorded in a session. This page describes the behavioral category, drawn solid. The setup type category is a field of the setup type, not a separate record.*

BrainSTEM organizes behavioral experiments through a hierarchy that separates shared scientific knowledge from lab-specific implementation details:

- **Behavioral category** (this page) — The broad domain of behavior (e.g., "Anxiety & Affect" → "Anxiety")
- **Behavioral paradigm** — A standardized behavioral task shared across the field (e.g., "Elevated Plus Exploration")
- **Behavioral assay** — Your lab's specific implementation of a paradigm under a specific preparation condition, linked to a setup type (e.g., "EPM 5-min test")
- **Behavior** — The actual execution of an assay within a session, tied to specific subjects and a physical setup

## Category hierarchy

Categories support up to two levels — a parent category and sub-categories. For example:

- **Learning & Memory** (parent)
  - Spatial Learning
  - Working Memory
  - Associative Learning
  - Recognition Memory
  - Fear Learning
- **Anxiety & Affect** (parent)
  - Anxiety
  - Depression
  - Stress Response
- **Sensory Function** (parent)
  - Visual, Auditory, Olfactory, Somatosensory, Gustatory, Thermal, Vestibular, Nociception

## Submission process

Anyone can submit new behavioral categories or propose changes to existing ones. A submission enters the approval queue and is usable in your own records immediately; it is visible only to you until accepted. Please review existing entries for guidance on what to submit. A category cannot be deleted while paradigms point to it.

## Permissions

Once an entry has been approved, it becomes available to everyone. Editing an accepted entry is restricted; an edit creates a change request that is reviewed before it takes effect. Your own pending submissions remain yours to edit or cancel.

## API access

The API allows for programmable access, enabling you to read and make changes to entries. For more information about the fields and data structure, please consult the [Behavioral category API page]({{"api/taxonomies/behavioralcategory/"|absolute_url}}).
