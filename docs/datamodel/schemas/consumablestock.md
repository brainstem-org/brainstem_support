---
layout: default
title: Consumable stock
parent: Schemas
grand_parent: Data model
nav_order: 8
---

# Consumable stock
{: .no_toc}

Various consumable stock types are available for tracking and managing laboratory supplies and materials used in neuroscience research.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Optic Fiber Stock

Tracking system for optic fiber inventory used in optogenetics research and neural recording.

| Field | Description |
|:------|:------------|
| `Fiber IDs` | Unique identifier for each optic fiber (string; required). For tracking specific items |
| `Quantity` | Number of optic fibers in stock (integer, ≥ 0; required). Tracks available inventory |

## Silicon Probe Stock

Inventory management for silicon probes used in high-density neural recording experiments.

| Field | Description |
|:------|:------------|
| `Probe IDs` | Unique identifier for each silicon probe (string; required). For tracking specific probes |
| `Quantity` | Number of probes in stock (integer, ≥ 0; required). Monitors available inventory |

## Single Wire Electrode Stock

Tracking system for single wire electrodes used in neural recording and stimulation.

| Field | Description |
|:------|:------------|
| `Wire IDs` | Unique identifier for wire electrodes (string; required). For tracking specific items |
| `Quantity` | Number of electrodes in stock (integer, ≥ 0; required). Tracks available inventory |
| `Length (mm)` | Length of the wire (float, ≥ 0; required; measured in millimeters). Important specification |

## Virus Construct Stock

Management system for viral constructs used in genetic manipulation experiments.

| Field | Description |
|:------|:------------|
| `Titer (units/mL)` | Concentration of virus solution (float, ≥ 0; required). Measured in units per milliliter |
| `Titer unit` | Unit of titer measurement (string; enum: [vg/mL, TU/mL, pfu/mL]). Specifies concentration type |
| `Volume (mL)` | Total volume of virus solution (float, ≥ 0; required; measured in milliliters) |
| `Aliquot count` | Number of separate aliquots (integer, ≥ 0; required). Tracks sample divisions |
| `Aliquot volume (µL)` | Volume per aliquot (float, ≥ 0; required; measured in microliters). Important for usage |

## Consumable Stock API access

The API allows for programmable access to Consumable Stock, enabling you to read, edit, and delete stock entries through the API. Learn more about the stock fields and data structure on the [Consumable Stock API page]({{"api/modules/consumablestock/"|absolute_url}}).