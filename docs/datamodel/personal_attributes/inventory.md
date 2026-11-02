---
layout: default
title: Inventories
parent: Personal attributes
grand_parent: Data model
nav_order: 3
has_toc: false
---

# Inventory model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

An inventory is a place where [consumable stock]({{"datamodel/modules/consumablestock/"|absolute_url}}) is managed: a lab's reagent store, a freezer, a shared facility stock. It is the container for stock lots and the permission boundary for them. The chain runs [consumable]({{"datamodel/resources/consumable/"|absolute_url}}) (the catalog product), consumable stock (the lot you hold) and [material usage]({{"datamodel/modules/materialusage/"|absolute_url}}) (that lot being used); the inventory is what makes the middle step yours.

Anywhere a material selector offers a stock lot (procedures, specimen procedures, experimental interfaces), the choices come from inventories where you are at least a Contributor.

{% include datamodel_embed.html model="personal_attributes.inventory" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Inventory name`` | Name of the inventory (**required**; string; maximum length: 50 characters). Name it for the store rather than for the lab. Example: "Silicon Probe Storage" |
| ``Authenticated groups`` | Groups given access when the inventory is created (create only). After creation, access is managed from the inventory's own page, where individual people can also be invited. |
| ``Location`` | Where the store is: room, freezer, shelf (string; maximum length: 100 characters). Each stock lot also has its own storage location. Example: "-80°C Freezer, Bay 3" |
| ``Description`` | Rich text description of what the inventory holds and any local rules for using it. Can include uploaded images. |
| ``Public access`` | Designates if the inventory is publicly available (boolean; default: False). It makes the store and its stock readable on the public portal, not usable. Only owners can modify this setting. |

An inventory cannot be deleted while consumable stocks point to it.

## Permissions

You manage permissions through the management tab, where you assign individual users and groups one of four roles. Members can see the inventory. Contributors can add, edit and remove its stock and select its lots when recording materials. Managers also manage access. Owners also edit the inventory's own fields and delete it. This is independent of project access, so sharing data does not share control of your reagents.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to inventories, enabling you to read, edit, and delete inventories through the API. Learn more about the inventories' fields and data structure on the [Inventories API page]({{"api/personal_attributes/inventory/"|absolute_url}}).
