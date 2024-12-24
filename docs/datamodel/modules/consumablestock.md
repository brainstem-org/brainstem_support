---
layout: default
title: Consumable stocks
parent: Modules
grand_parent: Data model
nav_order: 4
---

# Consumable stocks model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Consumable stocks refer to the various components and materials essential for conducting experiments and recording data. These stocks are integral to maintaining high-quality research conditions and ensuring that experiments are performed using accurate and reliable equipment. Each consumable stock type has unique applications depending on the experimental needs, while the fields associated with these types are designed to capture the specific details of each consumable.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of consumable stock (**required**). Selected from predefined types. Example: "Silicon probe", "Optic fiber". *See options below* |
| `Inventory` | The inventory record that tracks the consumable stock (**required**). Must reference an existing [inventory]({{"datamodel/personal_attributes/inventory/"|absolute_url}}). Example: "Lab supplies inventory" |
| `Notes` | Additional information or special considerations for the consumable stock (string). Example: "Handle with care, fragile components" |
| `Consumable` | The specific consumable associated with the consumable stock. Example: "32-channel silicon probe" |
| `Acquisition date` | The date when the consumable was acquired. Example: "2024-01-15" |
| `Expiration date` | The date when the consumable stock is expected to expire or become unusable. Example: "2025-01-15" |
| `Storage location` | The physical location where the consumable stock is stored (string; maximum length: 100 characters). Example: "Room 302, Cabinet B, Shelf 3" |
| `Storage conditions` | The conditions necessary for storing the consumable stock (string; maximum length: 100 characters). Example: "Store at room temperature in desiccator" |
| `Intended use` | The planned experimental use of the consumable stock (string; maximum length: 100 characters). Example: "For chronic neural recordings" |
| `Cost` | The cost of the consumable stock (string; maximum length: 100 characters). Example: "$500 USD" |


## Types of consumable stocks

{% include_relative ../../type_descriptions/consumablestock_types.md %}

## Permissions

Consumable stocks inherit permissions through the inventory associated with them.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Consumable stocks API access

The API allows for programmable access to consumable stocks, enabling you to read, edit, and delete consumable stocks through the API. Learn more about the consumable stocks' fields and data structure on the [Consumable stocks API page]({{"api/modules/consumablestock/"|absolute_url}}).