---
layout: default
title: Behavioral category
parent: Taxonomies
grand_parent: Data model
nav_order: 4
---

# Behavioral category model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Behavioral categories provide a two-level hierarchical classification for organizing behavioral paradigms into meaningful groups by cognitive domain or experimental focus.

## How it fits together

BrainSTEM organizes behavioral experiments through a hierarchy that separates shared scientific knowledge from lab-specific implementation details:

- **Behavioral Category** (this page) — The broad domain of behavior (e.g., "Learning & Memory" → "Spatial Learning")
- **Behavioral Paradigm** — A standardized behavioral task shared across the field (e.g., "Morris Water Navigation Task")
- **Behavioral Assay** — Your lab's specific implementation of a paradigm, linked to a setup type (e.g., "MWM 4-day acquisition, 60s trials, probe on day 5")
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

## Fields

| Field | Description |
|:------|:------------|
| ``Name`` | The name of the behavioral category (**required**; must be unique). |
| ``Parent category`` | Select a parent category for hierarchical organization. Leave empty for top-level categories (optional). |
| ``Description`` | A description of what this category encompasses (optional). |

## Submission process

Anyone can submit new behavioral categories or propose changes to existing ones. All submissions require approval before becoming available. Please review existing entries for guidance on what to submit.

## Permissions

Once an entry has been approved, it becomes available to everyone.

## Behavioral category API access

The API allows for programmable access, enabling you to read and make changes to entries. For more information about the fields and data structure, please consult the [Behavioral category API page]({{"api/taxonomies/behavioralcategory/"|absolute_url}}).
