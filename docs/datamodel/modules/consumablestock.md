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
| ``Type of consumable stock`` | Type of consumable stock (**required**). Selected from predefined types. Example: "Silicon probe", "Optic fiber". *See options below* |
| ``Inventory`` | The inventory record that tracks the consumable stocks (**required**). Must reference an existing [inventory]({{"datamodel/personal_attributes/inventory/"|absolute_url}}). Example: "Lab supplies inventory" |
| ``Consumable supplier`` | Supplier filter for consumables (optional). Used to filter the available consumables by supplier. |
| ``Consumable`` | The specific consumable associated with the consumable stock (**required**). Example: "32-channel silicon probe" |
| ``Acquisition date`` | The date when the consumable was acquired (format: YYYY-MM-DD). Example: "2024-01-15" |
| ``Expiration date`` | The date when the consumable stock is expected to expire or become unusable (format: YYYY-MM-DD). Example: "2025-01-15" |
| ``Storage location`` | The physical location where the consumable stock is stored (string; maximum length: 100 characters). Example: "Room 302, Cabinet B, Shelf 3" |
| ``Storage conditions`` | The conditions necessary for storing the consumable stock (string; maximum length: 100 characters). Example: "Store at room temperature in desiccator" |
| ``Intended use`` | The planned experimental use of the consumable stock (string; maximum length: 100 characters). Example: "For chronic neural recordings" |
| ``Cost`` | The cost of the consumable stock (string; maximum length: 100 characters). Example: "$500 USD" |
| ``Notes`` | Additional information or special considerations for the consumable stock (string). Example: "Handle with care, fragile components" |


## Types of consumable stocks

These are the available type options for Consumable stock:

See the schema for field details: [Consumable stock types]({{"/datamodel/schemas/consumablestock/"|absolute_url}}).

### Reagents and Solutions

`Chemical reagent`: Bulk chemicals (powders or liquids) used to prepare solutions or carry out procedures; includes solvents, salts, detergents, fixatives.

`Pharmacological agent`: Agents administered for anesthesia, analgesia, sedation, or controlled physiological manipulation during experiments.

`Physiological solution`: Prepared buffers and aqueous solutions used for perfusion, dissection, recording, washing, or tissue storage (e.g., PBS, ACSF, Ringer’s).

`Tracer or dye`: Fluorescent or chromogenic compounds for labeling cells/tissues or tracing neural circuits in histology and anatomy workflows.

`Virus solution`: Packaged viral vectors used for in vivo gene delivery (e.g., expression of reporters, recombinases, optogenetic tools) and trans‑synaptic tracing.

`Antibody or immunoreagent`: Primary/secondary antibodies and related immunochemical reagents for detection and labeling in IHC/ICC, Western blot, ELISA, etc.

### Device-Linked Consumables

`Consumable device`: Per‑animal or single‑use hardware consumed by implantation or wear, such as baseplates, microdrives, adapters, or implant fasteners.

`Optical component`: Discrete optical elements used for imaging or optical access, including GRIN lenses, cranial windows, dichroics, and emission/excitation filters.

`Optic fiber`: Fiber assemblies for delivering or collecting light (implant ferrule fibers, patch cords, rotary‑joint compatible fibers) for optogenetics or photometry.

`Silicon probe`: Silicon microelectrode arrays for high‑density extracellular recordings (e.g., Neuropixels and similar multi‑shank arrays).

`Single wire electrode`: Single‑conductor metal wires used as recording/stimulation electrodes or as reference/ground leads in electrophysiology.



## Permissions

Consumable stocks inherit permissions through the inventory associated with them.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to consumable stocks, enabling you to read, edit, and delete consumable stocks through the API. Learn more about the consumable stocks' fields and data structure on the [Consumable stocks API page]({{"api/modules/consumablestock/"|absolute_url}}).
