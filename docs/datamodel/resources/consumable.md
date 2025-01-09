---
layout: default
title: Consumables
parent: Resources
grand_parent: Data model
nav_order: 1
---

# Consumable model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction 

Consumables are items used in scientific experiments that have a limited lifespan or are intended for single use. These materials and products are essential for maintaining experimental integrity, accuracy, and reproducibility. In BrainSTEM, consumables are shared across users to promote standardization and ease of use.

## Session fields

| Field                | Description |
|:---------------------|:------------|
| `Name`                 | Name of the consumable (**required**; string; maximum length: 100 characters). Example: "Neuropixels 1.0 - 384 channels - Option 3" |
| `Type`  			   | Type of consumable (**required**). Example: "Silicon probe" |
| `Supplier`             | Supplier of the consumable (**required**). Must reference an existing [supplier]({{"datamodel/resources/supplier/"|absolute_url}}). Example: "IMEC" |
| `Description`          | Rich text description of the consumable. Can include uploaded images. Example: "High-density silicon probe with 384 recording sites distributed across a 10 mm shank..." |
| `Type specific fields` | Custom fields based on consumable type. See [Consumable types schema]({{"datamodel/schemas/consumable/"|absolute_url}}) for type-specific fields |

## Types of consumable

- Optic fiber designs
- Silicon probe designs
- Virus constructs
- Wire electrodes

## Submission process

Anyone can submit consumables or submit changes to existing ones, but all submissions must be approved before they are available for usage. Please see existing entries for examples as to what to submit.

For detailed information about the specific fields for each type of consumable, please refer to the [Consumable types schema page]({{"datamodel/schemas/consumable/"|absolute_url}}).


## Permissions

Once a entry has been approved it becomes available to everyone.

## API access

The API allows for programmable access to Data storage, enabling you to read, edit, and delete data storage through the API. Learn more about the sessions' fields and data structure on the [Session API page]({{"api/resources/consumable/"|absolute_url}}). 
