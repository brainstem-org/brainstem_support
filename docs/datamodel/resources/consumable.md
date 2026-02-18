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

## Fields

| Field | Description |
|:------|:------------|
| ``Type of consumable`` | Type of consumable (**required**). Example: "Silicon probe design" |
| ``Name`` | Name of the consumable (**required**; string; maximum length: 100 characters; must be unique). Example: "Neuropixels 1.0 - 384 channels - Option 3" |
| ``Supplier`` | Supplier of the consumable (**required**). Must reference an existing [supplier]({{"datamodel/resources/supplier/"|absolute_url}}). Example: "IMEC" |
| ``Description`` | Description of the consumable (optional; maximum length: 2000 characters). Example: "High-density silicon probe with 384 recording sites distributed across a 10 mm shank..." |
| ``RRID`` | Research Resource Identifier (optional). Must start with "RRID:". Example: "RRID:AB_123456" |
| ``External identifiers`` | External identifiers from databases like NCBI, JAX, DOI, etc. (optional). Include URLs when available. |
| ``Type specific fields`` | Custom fields based on consumable type in JSON format. See [Consumable types schema]({{"datamodel/schemas/consumable/"|absolute_url}}) for type-specific fields |
| ``Adding/editing comments`` | Comments for the submission/approval process (optional). |

## Types of consumable

### Reagents and Solutions

See the schema for field details: [Consumable types]({{"datamodel/schemas/consumable/"|absolute_url}}).

`Chemical reagent`: Chemical compounds and solutions used in experimental procedures.

`Antibody or immunoreagent`: Primary/secondary antibodies and related immunological reagents for IHC, Western blotting, and related techniques.

`Pharmacological agent`: Agents used for anesthesia, analgesia, or experimental manipulation.

`Physiological solution`: Prepared buffers and aqueous solutions for perfusion, dissection, recording, washing, or tissue storage.

`Tracer or dye`: Fluorescent or chromogenic compounds for labeling cells/tissues or tracing neural circuits.

`Virus construct`: Packaged viral vectors for gene delivery and expression in experimental systems.

### Device-Linked Consumables

`Consumable device`: Per‑animal or single‑use hardware consumed by implantation or wear (e.g., baseplates, microdrives, adapters, fasteners).

`Optical component`: Discrete optical elements for imaging or optical access (e.g., GRIN lenses, cranial windows, dichroics, filters).

`Optic fiber design`: Fiber assemblies for light delivery/collection (implants, patch cords) used in optogenetics or photometry.

`Silicon probe design`: Silicon microelectrode arrays for high‑density extracellular recordings.

`Single wire electrode`: Single‑conductor wires used as recording/stimulation electrodes or as reference/ground leads in electrophysiology.

### Surgical Consumables

`Surgical disposable`: Single-use sterile items used during procedures, such as gloves, drapes, scalpel blades, syringes, sutures, and gauze.

`Implant or fixation material`: Materials used to secure implants or support surgical fixation, such as dental cement, bone screws, adhesive compounds, and anchoring hardware.

## Submission process

Anyone can submit consumables or submit changes to existing ones, but all submissions must be approved before they are available for usage. Please see existing entries for examples as to what to submit.

For detailed information about the specific fields for each type of consumable, please refer to the [Consumable types schema page]({{"datamodel/schemas/consumable/"|absolute_url}}).


## Permissions

Once an entry has been approved it becomes available to everyone.

## API access

The API allows for programmable access to consumables, enabling you to read, edit, and delete consumables through the API. Learn more about the consumables' fields and data structure on the [Consumables API page]({{"api/resources/consumable/"|absolute_url}}).
