---
layout: default
title: Setup types
parent: Taxonomies
grand_parent: Data model
nav_order: 5
---

# Setup types model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

A setup type classifies the experimental preparation — the physiological and behavioral state of the subject or tissue during the experiment (e.g., freely moving awake in a maze, head-fixed on a disc, or tissue on a surgical table). Each setup type is associated with a class of apparatus that realizes that preparation. Setup types are shared across all users in BrainSTEM and serve as a foundation for both behavioral assays and lab-specific setups.

## How it fits together

The preparation state is the primary axis. Setup types sit between the broad preparation category and your lab's specific physical rigs:

- **Setup Type Category** — The broad experimental condition (e.g., "Freely Moving Awake", "Head-Fixed Awake"). This is a field on each setup type.
- **Setup Type** (this page) — A standardized preparation environment shared across labs, named for the physical structure the subject or tissue occupies (e.g., "Open Field Arena", "Elevated plus maze", "Head-fixed disc").
- **Setup** — Your lab's specific physical rig of this type (e.g., "Open Field, Room 204"). A private attribute belonging to your groups.
- **Equipment** — The individual hardware devices installed in a setup (e.g., cameras, amplifiers, sensors).

Setup types also connect to the behavioral side: a **behavioral assay** links a behavioral paradigm to a setup type, defining how a task is implemented under a particular preparation condition.

## Setup type categories

Each setup type belongs to one of the following preparation categories. This is the defining axis — it describes the physiological and behavioral state of the subject or tissue, not the class of apparatus:

- **In Vitro** — Isolated cells or tissues maintained outside of a living organism. Offers maximal experimental control and mechanistic clarity but lacks natural systemic context.
- **Ex Vivo** — Intact or semi-intact tissue preparations retaining some network-level organization. Bridges the gap between single cells and whole organisms.
- **Anesthetized In Vivo** — A living subject under anesthesia, allowing controlled interventions and stable physiological conditions. Ideal for surgical procedures and stable, artifact-free recordings.
- **Head-Fixed Awake** — The subject is awake but head-restrained, enabling stable recordings and controlled stimuli while preserving aspects of natural sensory and cognitive processing.
- **Voluntarily Stationary Awake** — The subject is awake and alert but chooses to remain still without physical restraint. Typically employed with non-invasive measurement techniques under more naturalistic conditions than head fixation.
- **Freely Moving Awake** — The subject engages in a full range of natural behaviors, often after implantations performed in a separate anesthetized session. Captures behavioral and ecological validity at the cost of reduced environmental control.

## Example

| Setup Type | Category | Description |
|:-----------|:---------|:------------|
| Open Field Arena | Freely Moving Awake | Open enclosure for locomotor and exploratory behavior |
| Elevated Plus Maze | Freely Moving Awake | Plus-shaped platform with open and closed arms |
| Head-fixed disc | Head-Fixed Awake | Rotating disc on which a head-fixed animal can run during recordings |
| Brain slice recording chamber | In Vitro | Perfused chamber holding an acute brain slice for electrophysiology or imaging |

## Fields

| Field | Description |
|:------|:------------|
| ``Name`` | The name of the setup type — a standardized name for the preparation environment recognizable across labs (e.g., "Morris water maze", "Head-fixed disc", "Brain slice recording chamber"). Name the physical structure the subject or tissue occupies, not the recording technique or acquisition device (**required**; string; maximum length: 200 characters; must be unique). |
| ``Category`` | The experimental condition category — In Vitro, Ex Vivo, Anesthetized In Vivo, Head-Fixed Awake, Voluntarily Stationary Awake, or Freely Moving Awake (**required**). |
| ``Description`` | A description of the preparation environment — what the subject or tissue occupies, and the experimental context it enables. Avoid naming specific recording techniques or acquisition devices, which belong on the equipment layer (maximum length: 2000 characters). |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

## Submission process

Anyone can submit new setup types or suggest changes to existing ones. However, all submissions must be approved before they become available for usage. Please refer to existing entries for examples of what to submit.

## Permissions

Once an entry has been approved, it becomes available to all users.

## Setup types API access

The API allows for programmable access to setup types, enabling you to read, edit, and delete entries through the API. Learn more about the setup types' fields and data structure on the [Setup types API page]({{"api/taxonomies/setuptype/"|absolute_url}}).
