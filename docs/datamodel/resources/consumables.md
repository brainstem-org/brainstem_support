---
layout: default
title: Consumables
parent: Resources
grand_parent: Data model
nav_order: 1
---

# Dataset model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction 

Consumables are items used in scientific experiments that have a limited lifespan or are intended for single use. These materials and products are essential for maintaining experimental integrity, accuracy, and reproducibility. In BrainSTEM, consumables are shared across users to promote standardization and ease of use.

## Dataset fields

| Field                | Description |
|:---------------------|:------------|
| `Name`                 | Name of the consumable (**required**) |
| `Type`  			   | Type of consumable (**required**) |
| `Supplier`             | Supplier of the consumable (**required**) |
| `Description`          | A description of the consumable |
| `Type specific fields` | Custom fields based on consumable type (**required**) |

## Types of consumable

- Optic fiber designs
- Silicon probe designs
- Virus constructs
- Wire electrodes

## Submission process

Anyone can submit consumables or submit changes to existing ones, but all submissions must be approved before they are available for usage. Please see existing entries for examples as to what to submit.

For detailed information about the specific fields for each type of consumable, please refer to the [Consumable types schema page]({{"datamodel/schemas/consumables/"|absolute_url}}).


## Permissions

Once a entry has been approved it becomes available to everyone.

## Dataset API access

The API allows for programmable access to Data storage, enabling you to read, edit, and delete data storage through the API. Learn more about the datasets' fields and data structure on the [Dataset API page]({{"api/resources/consumable/"|absolute_url}}). 
