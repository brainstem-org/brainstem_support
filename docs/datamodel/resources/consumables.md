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
Consumables refer to items that are intended to be used once or have a limited lifespan before they need to be replaced. These include materials and products that are consumed or depleted during the course of experiments or procedures. Consumables are critical for maintaining the integrity, accuracy, and reproducibility of scientific experiments. In BrainSTEM, consumables are a shared model across users.

## Dataset fields

| Field                | Description |
|:---------------------|:------------|
| Name                 | Name of the consumable (**required**) |
| Type  			   | Type of consumable (**required**) |
| Supplier             | Supplier of the consumable (**required**) |
| Type specific fields | Each type has custom fields (**required**) |
| Description          | A description of the consumable |

## Types of consumable
- Optic fiber designs
- Silicon probe designs
- Virus constructs
- Wire electrodes

## Submission process
Anyone can submit consumables or submit changes to existing ones, but all submissions must be approved before they are available for usage. Please see existing entries for examples as to what to submit.

## Permissions
Once a entry has been approved it becomes available to everyone.

Visit the [permissions page] to learn more. 

## Dataset API access
The API allows for programmable access to Data storage, enabling you to read, edit, and delete data storage through the API. Learn more about the datasets' fields and data structure on the [Dataset API page]({{"api/resources/consumable/"|absolute_url}}). 

