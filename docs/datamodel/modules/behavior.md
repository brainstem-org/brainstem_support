---
layout: default
title: Behaviors
parent: Sessions
grand_parent: Data model
nav_order: 1
---

# Behavior model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A behavior records one behavioral assay actually performed, with particular subjects, on a particular rig, during one session. It links the standardized task description (via the assay) with the physical apparatus (via the setup). A behavior has no type of its own; the assay supplies that, and the behavior stores no task parameters.

{% include datamodel_embed.html model="modules.behavior" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Session`` | Session of the behavior (**required**). Must reference an existing [session]({{"datamodel/stem/session/"|absolute_url}}). |
| ``Subjects`` | Every subject that took part (**required**). The choices come from the session's own subjects, so add a subject to the session first if it is missing here. Select all participants rather than creating one behavior per animal. |
| ``Setup`` | The physical rig the behavior ran on (**required**). Must reference an existing [setup]({{"datamodel/personal_attributes/setup/"|absolute_url}}) where you are at least a Contributor. |
| ``Behavioral assay`` | The lab method performed (**required**). Must reference an existing [behavioral assay]({{"datamodel/personal_attributes/behavioralassay/"|absolute_url}}) where you are at least a Contributor. |
| ``Order`` | Where this behavior appears among the session's behaviors. Does not imply a start time. |
| ``Notes`` | What was specific to this occurrence: deviations, technical problems, notable outcomes (string; maximum length: 500 characters). Anything that repeats every run belongs on the assay. |

Behaviors can be linked to [epochs]({{"datamodel/stem/epoch/"|absolute_url}}) of the session.

## How it fits together

![The behavioral track and the setup track: behavioral categories group paradigms, and an assay is your lab's version of a paradigm on a setup type; a setup is your rig of a setup type, with its equipment. A behavior in a session runs one assay on one setup with its subjects.]({{site.baseurl}}/assets/images/diagrams/behavior-tracks-behavior.svg)
*The behavioral track (left) and the setup track (right) run from the shared taxonomies through your lab's personal attributes and meet in a behavior recorded in a session. This page describes the behavior, drawn solid. The setup type category is a field of the setup type, not a separate record.*

A behavior is the junction point of two independent hierarchies. Both must be defined before you can record a behavior:

| Behavioral track | Setup track |
|:----------------|:-----------|
| *Shared taxonomy, available to all users* | |
| **Behavioral category**: the broad cognitive domain (e.g., "Anxiety") | **Setup type category**: the preparation state (e.g., "Freely Moving Awake") |
| **Behavioral paradigm**: the standardized task across the field (e.g., "Elevated Plus Exploration") | **Setup type**: the class of apparatus for that preparation (e.g., "Elevated plus maze") |
| *Lab-specific personal attributes, shared through your groups* | |
| **Behavioral assay**: your implementation of the paradigm on a setup type (e.g., "EPM 5-min test") | **Setup**: your physical rig of that type (e.g., "EPM rig B, Room 108") |

A **behavior** (this page) combines a behavioral assay with a specific physical setup and the subjects involved, within a session. The setup type of the chosen setup is shown beside the field so you can check the rig suits the assay.

The assay and the setup are personal attributes reached through their groups, while the behavior belongs to the session's projects. You need to be at least a Contributor on both the assay and the setup to record a behavior with them.

## Example

| Level | Example |
|:------|:--------|
| Behavioral assay | EPM 5-min test |
| Setup | EPM rig B, Room 108 |
| Subjects | Mouse 01, Mouse 02 |
| Behavior | Session 2026-06-01: Elevated Plus Exploration, trial 1 |

## Permissions

Behaviors inherit permissions through the projects of their associated session. The subject, setup and assay selectors are separately restricted to entries you may use.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to behaviors. Learn more about the behaviors' fields and data structure on the [Behaviors API page]({{"api/modules/behavior/"|absolute_url}}).
