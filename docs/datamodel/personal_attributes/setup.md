---
layout: default
title: Setups
parent: Personal attributes
grand_parent: Data model
nav_order: 6
has_toc: false
---

# Setup model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction 

A setup is one physical rig or workstation in your lab: an ephys station, a two-photon scope, a behavioral box, a surgery bench. It is the container for the [equipment]({{"datamodel/modules/equipment/"|absolute_url}}) installed in it and the permission boundary for that equipment. Each setup belongs to a shared setup type.

{% include datamodel_embed.html model="personal_attributes.setup" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Setup name`` | Name of the setup (**required**; string; maximum length: 50 characters). Use whatever is written on the door or the bench. Example: "Behavior Room A - Setup 1" |
| ``Setup category`` | Form-only filter for the setup type field. Not stored. |
| ``Setup type`` | The class of station (**required**). Must reference an existing [setup type]({{"datamodel/taxonomies/setuptype/"|absolute_url}}); submit missing types in the taxonomies section. |
| ``Authenticated groups`` | Groups given access when the setup is created (create only). After creation, access is managed from the setup's own page, where individual people can also be invited. |
| ``Location`` | Where the rig is: room, building, floor (string; maximum length: 100 characters). Example: "Room 302B, Neuroscience Building" |
| ``Description`` | Rich text description of the rig as a whole. Individual instruments belong in equipment. Can include uploaded images. |
| ``Image`` | A photo of the rig. |
| ``Specifications`` | Key-value details about the station, such as dimensions, weight or power requirements, in JSON format. Example: {"length": "200 cm", "width": "10 cm"} |
| ``Public access`` | Designates if the setup is publicly available (boolean; default: False). It makes the rig readable on the public portal, not usable: selecting its equipment still requires Contributor. Only owners can modify this setting. |

A setup cannot be deleted while equipment or behaviors point to it.

{% include schemas/setup.md %}

## How it fits together

A setup is where the work happens, and its equipment is what the work is done with. Most records reach a setup through its equipment; behaviors point at the setup itself.

![A setup is built as a setup type and holds its equipment, and each piece of equipment can name its model in the shared catalog. Procedures, specimen procedures, experimental interfaces, data acquisitions and manipulations name the equipment they used; a behavior names the whole setup.]({{site.baseurl}}/assets/images/diagrams/setup-hub-setup.svg)
*Procedures, specimen procedures and experimental interfaces on a subject or specimen set, and data acquisitions and manipulations in a session, name the [equipment]({{"datamodel/modules/equipment/"|absolute_url}}) they used; their templates can prefill it. A behavior names the whole setup. This page describes the setup, drawn solid.*

Setups are part of a two-level hierarchy for describing experimental apparatus:

- **Setup type category**: the broad preparation state (In Vitro, Ex Vivo, Anesthetized In Vivo, Head-Fixed Awake, Restrained Awake, Freely Moving Awake, Unknown). This is a field on the setup type.
- **Setup type**: a shared classification of the preparation and the class of apparatus (e.g., "Open Field Arena" under Freely Moving Awake, "Surgical Table" under Anesthetized In Vivo). Defined in [taxonomies]({{"datamodel/taxonomies/setuptype/"|absolute_url}}) and available to everyone.
- **Setup** (this page): your lab's specific physical rig (e.g., "EPM rig B, Room 108"). Shared with your people and groups.

Anywhere a form offers equipment (procedures, specimen procedures, experimental interfaces, data acquisitions and manipulations, and their templates), the choices come from setups where you are at least a Contributor. A record names the individual pieces of equipment it used, not the setup.

### In behavioral experiments
{: .no_toc}

![The behavioral track and the setup track: behavioral categories group paradigms, and an assay is your lab's version of a paradigm on a setup type; a setup is your rig of a setup type, with its equipment. A behavior in a session runs one assay on one setup with its subjects.]({{site.baseurl}}/assets/images/diagrams/behavior-tracks-setup.svg)
*The behavioral track (left) and the setup track (right) run from the shared taxonomies through your lab's personal attributes and meet in a behavior recorded in a session. This page describes the setup, drawn solid. The setup type category is a field of the setup type, not a separate record.*

A **behavior** record links a **behavioral assay** with a **setup** and the **subjects** involved. The setup must be of the assay's setup type; the behavior form refuses other combinations.

## Example

| Level | Example |
|:------|:--------|
| Setup type category | Freely Moving Awake |
| Setup type | Open Field Arena |
| Setup | "Open Field, Room 204": 50×50 cm arena, Room 204 |

## Permissions

Setups define the permissions of their equipment. You manage permissions through the management tab, where you assign individual users and groups one of four roles. Members can see the setup. Contributors can select its equipment on procedures, data acquisitions, manipulations and experimental interfaces, and can add, edit and remove the equipment installed in it. Managers also manage access. Owners also edit the setup's own fields and delete it.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to setups, enabling you to read, edit, and delete setups through the API. Learn more about the setups' fields and data structure on the [Setups API page]({{"api/personal_attributes/setup/"|absolute_url}}).
