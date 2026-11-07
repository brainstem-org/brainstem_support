---
layout: default
title: Setup types
parent: Taxonomies
grand_parent: Data model
nav_order: 8
---

# Setup types model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A setup type classifies the experimental preparation — the physiological and behavioral state of the subject or tissue during the experiment (e.g., freely moving awake in a maze, head-fixed on a disc, or tissue on a surgical table). Each setup type is associated with a class of apparatus that realizes that preparation. Setup types are shared across all users in BrainSTEM and serve as a foundation for both behavioral assays and lab-specific setups.

{% include datamodel_embed.html model="taxonomies.setuptype" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Name`` | The name of the setup type — a standardized name for the preparation environment recognizable across labs (e.g., "Morris water maze", "Head-fixed disc", "Brain slice recording chamber"). Name the physical structure the subject or tissue occupies, not the recording technique or acquisition device (**required**; string; maximum length: 200 characters; must be unique). |
| ``Category`` | The preparation category — In Vitro, Ex Vivo, Anesthetized In Vivo, Head-Fixed Awake, Restrained Awake, Freely Moving Awake, or Unknown (**required**). Three read-only attributes are derived from it: biological preparation, physiological state and constraint level. |
| ``Description`` | A description of the preparation environment — what the subject or tissue occupies, and the experimental context it enables. Avoid naming specific recording techniques or acquisition devices, which belong on the equipment layer (maximum length: 2000 characters). |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

## How it fits together

A setup type classifies the rigs of every lab. Two kinds of record point at it: your [setups]({{"datamodel/personal_attributes/setup/"|absolute_url}}), and the [behavioral assays]({{"datamodel/personal_attributes/behavioralassay/"|absolute_url}}) that name the kind of rig they run on. Through the setups and their equipment, it gives the preparation context of the records that use them.

The preparation state is the primary axis. Setup types sit between the broad preparation category and your lab's specific physical rigs:

- **Setup type category** — The broad experimental condition (e.g., "Freely Moving Awake", "Head-Fixed Awake"). This is a field on each setup type.
- **Setup type** (this page) — A standardized preparation environment shared across labs, named for the physical structure the subject or tissue occupies (e.g., "Open Field Arena", "Elevated plus maze", "Head-fixed disc").
- **Setup** — Your lab's specific physical rig of this type (e.g., "Open Field, Room 204"). A private attribute belonging to your groups.
- **Equipment** — The individual hardware devices installed in a setup (e.g., cameras, amplifiers, sensors).

### In behavioral experiments
{: .no_toc}

[![The behavioral track and the setup track: behavioral categories group paradigms, and an assay is your lab's version of a paradigm on a setup type; a setup is your rig of a setup type, with its equipment. A behavior in a session runs one assay on one setup with its subjects.]({{site.baseurl}}/assets/images/diagrams/behavior-tracks-setuptype.svg)]({{site.baseurl}}/assets/images/diagrams/behavior-tracks-setuptype.svg)
*The behavioral track (left) and the setup track (right) run from the shared taxonomies through your lab's personal attributes and meet in a behavior recorded in a session. The setup type is drawn solid. The setup type category is a field of the setup type, not a separate record.*

A **behavioral assay** links a behavioral paradigm to a setup type, defining how a task is implemented under a particular preparation condition.

## Setup type categories

Each setup type belongs to one of the following preparation categories. This is the defining axis — it describes the physiological and behavioral state of the subject or tissue, not the class of apparatus.

[![Setup type categories from a slice to a freely moving animal: In Vitro (a brain slice recording chamber), Ex Vivo (an isolated whole-brain preparation), Anesthetized In Vivo (a stereotaxic frame), Head-Fixed Awake (a head-fixed treadmill), Restrained Awake (a tube restrainer) and Freely Moving Awake (an open field arena). Below, the biological preparation, physiological state and constraint level derived from each category.]({{site.baseurl}}/assets/images/diagrams/setup-type-categories.svg)]({{site.baseurl}}/assets/images/diagrams/setup-type-categories.svg)
*The categories run from the most experimental control on the left to the most natural behavior on the right, each shown with one setup type of that category. The biological preparation, physiological state and constraint level are derived from the category and cannot be set separately; physiological state and constraint level do not apply to tissue outside the animal.*

The categories are:

- **In Vitro** — Isolated cells or tissues maintained outside of a living organism. Offers maximal experimental control and mechanistic clarity but lacks natural systemic context.
- **Ex Vivo** — Intact or semi-intact tissue preparations retaining some network-level organization. Bridges the gap between single cells and whole organisms.
- **Anesthetized In Vivo** — A living subject under anesthesia, allowing controlled interventions and stable physiological conditions. Ideal for surgical procedures and stable, artifact-free recordings.
- **Head-Fixed Awake** — The subject is awake but head-restrained, enabling stable recordings and controlled stimuli while preserving aspects of natural sensory and cognitive processing.
- **Restrained Awake** — A conscious animal restrained without head fixation, such as in a tube or sling.
- **Freely Moving Awake** — The subject engages in a full range of natural behaviors, often after implantations performed in a separate anesthetized session. Captures behavioral and ecological validity at the cost of reduced environmental control.
- **Unknown** — Use only when the preparation genuinely cannot be determined, such as for imported historical records.

## Example

| Setup Type | Category | Description |
|:-----------|:---------|:------------|
| Open Field Arena | Freely Moving Awake | Open enclosure for locomotor and exploratory behavior |
| Elevated Plus Maze | Freely Moving Awake | Plus-shaped platform with open and closed arms |
| Head-fixed disc | Head-Fixed Awake | Rotating disc on which a head-fixed animal can run during recordings |
| Brain slice recording chamber | In Vitro | Perfused chamber holding an acute brain slice for electrophysiology or imaging |

## Submission process

Anyone can submit new setup types or suggest changes to existing ones. A submission enters the approval queue and is usable in your own records immediately; it is visible only to you until accepted. Please refer to existing entries for examples of what to submit. A setup type cannot be deleted while setups or behavioral assays point to it.

## Permissions

Once an entry has been approved, it becomes available to all users. Editing an accepted type is restricted, since it would change every setup and behavioral assay that references it; an edit creates a change request that is reviewed before it takes effect.

## API access

The API allows for programmable access to setup types, enabling you to read, edit, and delete entries through the API. Learn more about the setup types' fields and data structure on the [Setup types API page]({{"api/taxonomies/setuptype/"|absolute_url}}).
