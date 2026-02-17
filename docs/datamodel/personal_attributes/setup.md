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

Setups describe where experiments, procedures, or manipulations takes place. It also describes the environment of a recorded subject. Setups has specifications and equipment associate with it.

## Fields

| Field | Description |
|:------|:------------|
| ``Setup name`` | Name of the setup (**required**; string; maximum length: 50 characters). Example: "Behavior Room A - Setup 1" |
| ``Setup category`` | Category of the setup type (required filter). This category filters the available setup types. Example: "Behavioral Environments" |
| ``Setup type`` | The type of environment the setup is (**required**). Must reference an existing [setup type]({{"datamodel/taxonomies/setuptype/"|absolute_url}}). Example: "Linear track" |
| ``Location`` | Location of the setup (optional). Example: "Room 302B, Neuroscience Building" or "Room 201, Surgery room" |
| ``Authenticated groups`` | Groups that have change permissions for this setup (**required**). Example: "Behavior Core Team" |
| ``Description`` | Rich text description of the setup (optional). Can include uploaded images. Example: "Linear track setup with two reward ports and tracking cameras..." |
| ``Image`` | Image of the setup (optional). Uploaded images remain completely private. Example: "setup1_overview.jpg" |
| ``Specifications`` | Specifications to the setup in key-value format (optional). Example: {"length": "200 cm", "width": "10 cm", "height": "15 cm"} |

## Permissions

Setups define the overall permissions level for equipment. You manage permissions through the management tab, where you can assign individual users and groups access levels to a setup. Setup have four permission levels: membership (read access), contributors, managers, and owners.

Equipment inherit permissions from their associated setup.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to setups, enabling you to read, edit, and delete Setups through the API. Learn more about the sessions' fields and data structure on the [Setups API page]({{"api/personal_attributes/setup/"|absolute_url}}).
