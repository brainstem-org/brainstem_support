---
layout: default
title: Behavioral assays
parent: Personal attributes
grand_parent: Data model
nav_order: 1
---

# Behavioral assay model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction 

A behavioral assay is your lab's specific implementation of a behavioral paradigm. While paradigms describe the shared conceptual task (e.g., "Morris Water Navigation Task"), an assay captures how your lab actually runs it — the specific protocol, parameters, and setup type used.

{% include datamodel_embed.html model="personal_attributes.behavioralassay" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Behavioral assay name`` | A descriptive name for this assay, ideally indicating the paradigm and key protocol details (e.g., "MWM 4-day acquisition" or "EPM 5-min test") (**required**; string; maximum length: 50 characters). |
| ``Setup category`` | Form-only filter for the setup type field (e.g., Freely Moving Awake, Head-Fixed Awake). Not stored. |
| ``Setup type`` | The preparation condition under which this assay is run — a setup type encodes both the physiological state of the subject (e.g., Freely Moving Awake) and the class of apparatus (e.g., "Elevated Plus Maze"). This constrains which physical setups can be used when recording a behavior (**required**). Must reference an existing [setup type]({{"datamodel/taxonomies/setuptype/"|absolute_url}}). |
| ``Behavioral category`` | Form-only filter for the paradigm field (e.g., "Learning & Memory"). Not stored. |
| ``Behavioral paradigm`` | The shared paradigm this assay implements (**required**). Must reference an existing [behavioral paradigm]({{"datamodel/taxonomies/behavioralparadigm/"|absolute_url}}). |
| ``Licenses`` | [Licenses]({{"datamodel/personal_attributes/license/"|absolute_url}}) that authorize this method, relevant where the task involves food or water restriction, aversive stimuli or anything else your license governs. Can include multiple licenses. |
| ``Description`` | How the task is actually run: stages, durations, reinforcement, criteria. A behavior stores no task parameters of its own, so whatever is not here is not recorded anywhere. |
| ``Authenticated groups`` | Groups given access when the assay is created (create only). Recording a behavior requires Contributor on the assay, so include the people who will run it. After creation, access is managed from the assay's own page, where individual people can also be invited. |
| ``Public access`` | Designates if the behavioral assay is publicly available (boolean; default: False). It makes the assay readable on the public portal, not usable. Only owners can modify this setting. |

A behavioral assay cannot be deleted while behaviors point to it.

## How it fits together

[![The behavioral track and the setup track: behavioral categories group paradigms, and an assay is your lab's version of a paradigm on a setup type; a setup is your rig of a setup type, with its equipment. A behavior in a session runs one assay on one setup with its subjects.]({{site.baseurl}}/assets/images/diagrams/behavior-tracks-behavioralassay.svg)]({{site.baseurl}}/assets/images/diagrams/behavior-tracks-behavioralassay.svg)
*The behavioral track (left) and the setup track (right) run from the shared taxonomies through your lab's personal attributes and meet in a behavior recorded in a session. This page describes the behavioral assay, drawn solid. The setup type category is a field of the setup type, not a separate record.*

BrainSTEM organizes behavioral experiments through a hierarchy that separates shared scientific knowledge from lab-specific implementation details:

- **Behavioral category** — The broad domain (e.g., "Anxiety & Affect" → "Anxiety")
- **Behavioral paradigm** — The standardized task shared across the field (e.g., "Elevated Plus Exploration")
- **Behavioral assay** (this page) — Your lab's specific implementation of a paradigm under a specific preparation condition, linking a paradigm to a setup type (e.g., "EPM 5-min test")
- **Behavior** — The actual execution of an assay within a session, tied to specific subjects and a physical setup

Categories and paradigms are shared taxonomies available to everyone. Assays are lab-specific — they belong to your groups and capture exactly how you run a paradigm.

## Example

| Level | Example |
|:------|:--------|
| Paradigm | Elevated Plus Exploration |
| Assay | "EPM 5-min test" — single 5-min session, 300 lux open arms, setup type: Elevated Plus Maze (Freely Moving Awake) |
| Behavior | Rat #7, Session 2024-06-01, ran assay "EPM 5-min test" on setup "EPM Rig B, Room 108" |

## Permissions

Behavioral assays have four roles: Member (read), Contributor (can record a behavior that uses the assay), Manager (also manages access) and Owner (also edits the assay's own fields and deletes it). You manage permissions through the management tab. Assays are shared with people and groups, never through a project.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to behavioral assays, enabling you to read, edit, and delete assays through the API. Learn more about the fields and data structure on the [Behavioral assay API page]({{"api/personal_attributes/behavioralassay/"|absolute_url}}). 
