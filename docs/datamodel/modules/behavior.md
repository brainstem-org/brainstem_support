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

1. TOC
{:toc}

## Introduction

A behavior is a module within a session that records which behavioral assay was performed, on which subjects, and using which setup. It ties together the standardized task description (via the assay) with the physical apparatus (via the setup) for a specific experimental session.

## How it fits together

A behavior record is the junction point of two independent hierarchies — both must be defined before you can record a behavior:

| Behavioral track | Setup track |
|:----------------|:-----------|
| *Shared taxonomy — available to all users* | |
| **Behavioral Category** — The broad cognitive domain (e.g., "Anxiety") | **Preparation condition** — The subject's physiological state (e.g., "Freely Moving Awake") |
| **Behavioral Paradigm** — Standardized task across the field (e.g., "Elevated Plus Exploration") | **Setup Type** — Class of apparatus for that preparation (e.g., "Elevated plus maze") |
| *Lab-specific — private attribute belonging to your groups* | |
| **Behavioral Assay** — Your protocol for the paradigm under that preparation (e.g., "EPM 5-min test") | **Setup** — Your physical rig of that type (e.g., "EPM rig B, Room 108") |

A **Behavior** record (this page) combines a behavioral assay with a specific physical setup and the subjects involved, within a session. The assay already encodes the preparation condition via its setup type — selecting a matching physical setup completes the record.

Both the setup and the behavioral assay are private attributes and must be defined separately before filling in the behavior form. They belong to group(s) that must be shared with one of the session's associated projects.

## Example

| Level | Example |
|:------|:--------|
| Behavioral Assay | EPM 5-min test |
| Setup | EPM rig B, Room 108 |
| Subjects | Mouse 01, Mouse 02 |
| Behavior | Session 2026-06-01 — Elevated Plus Exploration, trial 1 |

## Fields

| Field | Description |
|:------|:------------|
| ``Session`` | Session of the behavior (**required**). Must reference an existing [sessions]({{"datamodel/stem/session/"|absolute_url}}). Example: "Training session #5" |
| ``Subjects`` | Subjects taking part in the behavior (**required**). Can include multiple subjects. Example: "Mouse_01", "Mouse_02" |
| ``Setup`` | Setup of the behavior (**required**). Must reference an existing [setup]({{"datamodel/personal_attributes/setup/"|absolute_url}}). Example: "Linear track A" |
| ``Behavioral Assay`` | Behavioral Assay of the behavior (**required**). Must reference an existing [behavioral assay]({{"datamodel/personal_attributes/behavioralassay/"|absolute_url}}). Example: "Spatial alternation task" |
| ``Notes`` | Notes about the behavior (string). Example: "Subject performed normally with 85% accuracy" |

## Permissions

Behaviors inherit permissions through their associated session.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to behaviors. Learn more about the behaviors' fields and data structure on the [Behaviors API page]({{"api/modules/behavior/"|absolute_url}}).
