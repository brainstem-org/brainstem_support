---
layout: default
title: Setups
parent: Personal attributes
grand_parent: Data model
nav_order: 5
has_toc: false
---

# Setup model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction 

A setup describes a specific physical rig, maze, or apparatus in your lab where experiments are conducted. Setups are where procedures, data acquisition, behaviors, and manipulations take place. Each setup belongs to a setup type and can have equipment and specifications associated with it.

## How it fits together

Setups are part of a two-level hierarchy for describing experimental apparatus:

- **Setup Type Category** — The broad experimental condition (e.g., "Freely Moving Awake", "Head-Fixed Awake", "In Vitro"). This is a field on the setup type.
- **Setup Type** — A shared classification of the experimental preparation: the physiological state of the subject or tissue and the associated class of apparatus (e.g., "Open Field Arena" under Freely Moving Awake, "Surgical Table" under Anesthetized In Vivo). Defined in taxonomies and available to everyone.
- **Setup** (this page) — Your lab's specific physical rig (e.g., "EPM rig B, Room 108" or "Linear track, Room 205"). Belongs to your groups.

In a behavioral experiment, a **behavior** record links a **behavioral assay** (how you run a paradigm) with a **setup** (where you run it) and the **subjects** involved.

## Example

| Level | Example |
|:------|:--------|
| Setup Type Category | Freely Moving Awake |
| Setup Type | Open Field Arena |
| Setup | "Open Field, Room 204" — 50×50 cm arena, Room 204 |

## Fields

| Field | Description |
|:------|:------------|
| ``Setup name`` | Name of the setup (**required**; string; maximum length: 50 characters). Example: "Behavior Room A - Setup 1" |
| ``Setup category`` | Category used to filter available setup types. Selected from predefined setup categories (In Vitro, Ex Vivo, Anesthetized In Vivo, Head-Fixed Awake, Voluntarily Stationary Awake, Freely Moving Awake, Unknown). Example: "Freely Moving Awake" |
| ``Setup type`` | The preparation condition and associated class of apparatus (e.g., "Open Field Arena" under Freely Moving Awake, "Head-fixed disc" under Head-Fixed Awake). Each setup type has a category describing the physiological state of the subject or tissue (**required**). Must reference an existing [setup type]({{"datamodel/taxonomies/setuptype/"|absolute_url}}). |
| ``Location`` | Location of the setup (string; maximum length: 100 characters). Example: "Room 302B, Neuroscience Building" or "Room 201, Surgery room" |
| ``Authenticated groups`` | Groups that have change permissions for this setup (**required**). Example: "Behavior Core Team" |
| ``Description`` | Rich text description of the setup. Can include uploaded images. Example: "Linear track setup with two reward ports and tracking cameras..." |
| ``Image`` | Image of the setup. Uploaded images remain completely private. Example: "setup1_overview.jpg" |
| ``Specifications`` | Specifications to the setup in key-value format. Example: {"length": "200 cm", "width": "10 cm", "height": "15 cm"} |
| ``Public access`` | Designates if the setup is publicly available (boolean; default: False). Must be enabled for setups used in public projects. Only owners can modify this setting. |

## Permissions

Setups define the overall permissions level for equipment. You manage permissions through the management tab, where you can assign individual users and groups access levels to a setup. Setups have four permission levels: membership (read access), change permissions, managers, and owners.

Equipment inherit permissions from their associated setup.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to setups, enabling you to read, edit, and delete Setups through the API. Learn more about the sessions' fields and data structure on the [Setups API page]({{"api/personal_attributes/setup/"|absolute_url}}).
