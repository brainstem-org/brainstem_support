---
layout: default
title: Hardware devices
parent: Resources
grand_parent: Data model
nav_order: 2
---

# Hardware device model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A hardware device is a durable instrument as the manufacturer sells it: an amplifier, a camera, a stereotaxic frame. Each entry is one product model. It is the catalog identity that your own [equipment]({{"datamodel/modules/equipment/"|absolute_url}}) entries point at: the catalog says what a device is, while your equipment says which unit sits on which rig. The line between a hardware device and a [consumable]({{"datamodel/resources/consumable/"|absolute_url}}) is durability: if it is depleted by use or belongs to a single animal, it is a consumable. In BrainSTEM, hardware devices are a shared model across users.

{% include datamodel_embed.html model="resources.hardwaredevice" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Name of hardware device`` | The product name and model as the manufacturer lists it (**required**; string; maximum length: 100 characters; must be unique across BrainSTEM). Example: "RHD2000 USB Interface Board" |
| ``Type`` | The type of hardware device (**required**). Hardware device types mirror the [equipment types]({{"datamodel/modules/equipment/#types-of-equipment"|absolute_url}}): data acquisition, behavioral and stimulation tools, environmental controllers, surgical equipment and miscellaneous. Example: "Data acquisition system" |
| ``Supplier`` | The supplier of the hardware device (**required**). Must reference an existing [supplier]({{"datamodel/resources/supplier/"|absolute_url}}). Example: "Intan Technologies" |
| ``RRID`` | Research Resource Identifier (string; maximum length: 100 characters). **Lookup RRID** beside the field fetches the instrument from the SciCrunch registry and fills in the name, description and external identifiers, and matches the supplier where the registry names one you already have. Example: "RRID:SCR_123456" |
| ``External identifiers`` | Catalogue numbers and identifiers in other registries, each with source, id and URL. |
| ``Type specific fields`` | Specification fields for the selected type, in JSON format. Record the manufacturer's specification, not the configuration of your own unit. See the [Hardware device types schema]({{"datamodel/schemas/hardwaredevice/"|absolute_url}}). |
| ``Description`` | What the instrument does and what it is used for (maximum length: 2000 characters). |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

## Submission process

Anyone can submit hardware devices or submit changes to existing ones. A submission enters the approval queue and is usable in your own records immediately; it is visible only to you until accepted. Include the model designation in the name to distinguish variants. For details of the approval statuses see the [Resources page]({{"datamodel/resources/"|absolute_url}}).

A hardware device cannot be deleted while equipment points to it.

## Permissions

Everyone can read the accepted list. Editing an accepted device is restricted, since it would change every equipment entry that references it; an edit creates a change request that is reviewed before it takes effect. Your own pending submissions remain yours to edit or cancel.

## API access

The API allows for programmable access to hardware devices, returning the accepted list plus your own pending submissions. Learn more about the hardware devices' fields and data structure on the [Hardware devices API page]({{"api/resources/hardwaredevice/"|absolute_url}}).
