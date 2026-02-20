---
layout: default
title: Behavioral Assays
parent: Personal attributes
grand_parent: Data model
nav_order: 1
---

# Behavioral Assay model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction 

A behavioral assay is your lab's specific implementation of a behavioral paradigm. While paradigms describe the shared conceptual task (e.g., "Morris Water Navigation Task"), an assay captures how your lab actually runs it — the specific protocol, parameters, and setup type used.

## How it fits together

BrainSTEM organizes behavioral experiments through a hierarchy that separates shared scientific knowledge from lab-specific implementation details:

- **Behavioral Category** — The broad domain (e.g., "Learning & Memory" → "Spatial Learning")
- **Behavioral Paradigm** — The standardized task shared across the field (e.g., "Morris Water Navigation Task")
- **Behavioral Assay** (this page) — Your lab's specific implementation of a paradigm, linking it to a setup type (e.g., "MWM 4-day acquisition, 60s trials, probe on day 5")
- **Behavior** — The actual execution of an assay within a session, tied to specific subjects and a physical setup

Categories and paradigms are shared taxonomies available to everyone. Assays are lab-specific — they belong to your groups and capture exactly how you run a paradigm.

## Example

| Level | Example |
|:------|:--------|
| Paradigm | Elevated Plus Exploration |
| Assay | "EPM 5-min test" — single 5-min session, 300 lux open arms, setup type: Elevated Plus Maze |
| Behavior | Rat #7, Session 2024-06-01, ran assay "EPM 5-min test" on setup "EPM Rig B" |

## Fields

| Field | Description |
|:------|:------------|
| ``Behavioral assay name`` | A descriptive name for this assay, ideally indicating the paradigm and key protocol details (e.g., "MWM 4-day acquisition" or "EPM 5-min test") (**required**; string; maximum length: 50 characters). |
| ``Setup category`` | Category of setup conditions associated with the selected setup type (e.g., Freely Moving Awake, Head-Fixed Awake). |
| ``Setup type`` | The standardized apparatus type (e.g., "Elevated Plus Maze", "Open Field Arena") (**required**). Must reference an existing [setup type]({{"datamodel/taxonomies/setuptype/"|absolute_url}}). |
| ``Behavioral category`` | The taxonomy category that organizes the selected behavioral paradigm (e.g., "Learning & Memory"). |
| ``Behavioral paradigm`` | The shared paradigm this assay implements (**required**). Must reference an existing [behavioral paradigm]({{"datamodel/taxonomies/behavioralparadigm/"|absolute_url}}). |
| ``Licenses`` | Licenses that authorize this assay for regulatory and compliance tracking. Can include multiple licenses. |
| ``Description`` | Protocol details — trial structure, timing, parameters, and any lab-specific variations. |
| ``Authenticated groups`` | Assign one or more groups during creation. Assigned groups receive change permissions; permissions can be adjusted later on the manage page (**required**). |
| ``Public access`` | Designates if the behavioral assay is publicly available (boolean; default: False). Must be enabled for assays used in public projects. Only owners can modify this setting. |

## Permissions

Behavioral assays have four permission levels: membership (read access), change permissions, managers, and owners. You manage permissions through the management tab.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to behavioral assays, enabling you to read, edit, and delete assays through the API. Learn more about the fields and data structure on the [Behavioral assay API page]({{"api/personal_attributes/behavioralassay/"|absolute_url}}). 
