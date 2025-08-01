---
layout: default
title: Consumable stocks
parent: Inventories
grand_parent: Personal attributes
nav_order: 1
---

# Consumable stock model
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
| `Inventory` | The inventory record that tracks the consumable stocks (**required**). Must reference an existing [inventory]({{"datamodel/personal_attributes/inventory/"|absolute_url}}). Example: "Lab supplies inventory" |
| `Consumable` | The specific consumable associated with the consumable stock. Example: "32-channel silicon probe" |
| `Acquisition date` | The date when the consumable was acquired. Example: "2024-01-15" |
| `Expiration date` | The date when the consumable stock is expected to expire or become unusable. Example: "2025-01-15" |
| `Storage location` | The physical location where the consumable stock is stored (string; maximum length: 100 characters). Example: "Room 302, Cabinet B, Shelf 3" |
| `Storage conditions` | The conditions necessary for storing the consumable stock (string; maximum length: 100 characters). Example: "Store at room temperature in desiccator" |
| `Intended use` | The planned experimental use of the consumable stock (string; maximum length: 100 characters). Example: "For chronic neural recordings" |
| `Cost` | The cost of the consumable stock (string; maximum length: 100 characters). Example: "$500 USD" |
| `Notes` | Additional information or special considerations for the consumable stock (string). Example: "Handle with care, fragile components" |


## Types of consumable stocks

These are the available `type` options for Consumable stock:

### Recording and Stimulation Equipment:
- `OpticFiber`: A flexible light guide used primarily in optogenetic experiments to deliver light to specific brain regions. Optic fibers are essential in neuroscience for manipulating neural circuits using light.
- `SiliconProbe`: A specialized tool for recording electrical signals from neurons. Silicon probes are vital for experiments focused on understanding brain function through electrophysiological recordings.
- `SingleWireElectrode`: A simple yet effective tool for measuring electrical activity at a single site. Single wire electrodes are commonly used in studies examining neural or muscular electrical activity.

### Biological Solutions and Reagents:
- `VirusSolution`: A viral vector preparation used for introducing genes into cells. Virus solutions are important for studies involving gene expression, neural circuit tracing, and optogenetics.
- `ChemicalReagent`: General chemical compounds and solutions used in experimental procedures. This includes anesthetics, pharmacological agents, buffer solutions, and other chemical preparations essential for research protocols.
- `ImmunoReagent`: Specialized biological reagents used in immunological procedures and assays. This includes antibodies, sera, immunological markers, and other immune-related biological materials.

A detailed list of the accepted schemas for the `details` field, related to each `type`, can be found in the [Consumable stock schemas page]({{"/datamodel/schemas/consumablestock/"|absolute_url}}).


## Permissions

Consumable stocks inherit permissions through the inventory associated with them.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to consumable stocks, enabling you to read, edit, and delete consumable stocks through the API. Learn more about the consumable stocks' fields and data structure on the [Consumable stocks API page]({{"api/modules/consumablestock/"|absolute_url}}).