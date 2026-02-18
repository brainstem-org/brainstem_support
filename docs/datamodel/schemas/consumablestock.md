---
layout: default
title: Consumable stock types
parent: Schemas
grand_parent: Data model
nav_order: 8
---

# Consumable stock types
{: .no_toc}

Various consumable stock types are available for tracking and managing laboratory supplies and materials used in neuroscience research.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Reagents and Solutions

### Chemical Reagent Stock

Inventory record for chemicals held in bulk, including solvents, detergents, buffers, and fixatives.

| Field | Description |
|:------|:------------|
| `Product ID` | Catalog or supplier product code (string) |
| `Compound Name` | Name of the chemical (string) |
| `Chemical Type` | (**required**) General classification of the reagent (enum) |
| `Molecular Weight` | Molecular weight (float, ≥ 0) |
| `Amount` | Amount held in stock (string; e.g., "500 mL", "2 gram") |
| `Concentration / Strength` | Solution strength if applicable (string; e.g., "1 M", "10X") |
| `Purity / Grade` | Purity or grade designation (string) |
| `Hazard Information` | safety notes or GHS classification (string) |

### Consumable Device Stock

Tracks miniscope baseplates, microdrives, adapters, and other device-level consumables.

| Field | Description |
|:------|:------------|
| `Product ID` | Supplier or catalog identifier (string) |
| `Device Class` | (**required**) General device category (enum; e.g., headstage, fiber cannula assembly) |
| `Compatible Systems` | Supported systems or rigs (string; e.g., Neuropixels, Inscopix) |
| `Physical Dimensions` | Key geometry information (string) |
| `Material` | Primary construction material (string) |
| `Connectivity` | Connector or interface type (string; e.g., LC/PC, Omnetics) |
| `Experimental Use Context` | Intended experimental uses (array of strings) |

### Immuno Reagent Stock

Stock records for antibodies and related immunochemical reagents.

| Field | Description |
|:------|:------------|
| `Product ID` | Supplier product code or catalog number (string) |
| `Reagent Type` | (**required**) General classification (enum; e.g., primary antibody, fluorescent label) |
| `Host Species` | Species the antibody was raised in (string) |
| `Reactivity Species` | Species the reagent recognizes (string) |
| `Target Antigen` | Molecule or structure targeted (string) |
| `Clonality` | Monoclonal, polyclonal, recombinant, or unknown (string) |
| `Conjugated Fluorophore or Enzyme` | Attached reporter, if any (string) |
| `Amount` | Amount supplied (string) |
| `Dilution` | Recommended dilution (string; e.g., "1:500") |
| `Validated Applications` | Supported applications (array of strings; e.g., IHC, Western Blot) |

## Device-Linked Consumables

### Optical Component Stock

Optical elements such as GRIN lenses, cranial windows, or filters stored for experiments.

| Field | Description |
|:------|:------------|
| `Product ID` | Supplier or catalog ID (string) |
| `Optical Component Type` | (**required**) General class of optical element (enum) |
| `Material` | Primary material (string; e.g., glass, quartz) |
| `Physical Dimensions` | Key geometry information (string) |
| `Surface Coating` | Surface treatment (string; e.g., anti-reflective) |
| `Wavelength minimum` | Shortest supported wavelength (float) |
| `Wavelength maximum` | Longest supported wavelength (float) |
| `Sterile` | Indicates if supplied sterile (boolean) |
| `Storage Conditions` | Recommended storage environment (string) |
| `Experimental Use Context` | Typical applications (array of strings; e.g., chronic imaging) |

### Optic Fiber Stock

Tracking system for optic fiber inventory used in optogenetics research and neural recording.

| Field | Description |
|:------|:------------|
| `Fiber IDs` | Unique identifier for each optic fiber (string; required). For tracking specific items |
| `Quantity` | Number of optic fibers in stock (integer, ≥ 0; required). Tracks available inventory |

### Silicon Probe Stock

Inventory management for silicon probes used in high-density neural recording experiments.

| Field | Description |
|:------|:------------|
| `Probe IDs` | Unique identifier for each silicon probe (string; required). For tracking specific probes |
| `Quantity` | Number of probes in stock (integer, ≥ 0; required). Monitors available inventory |

### Single Wire Electrode Stock

Tracking system for single wire electrodes used in neural recording and stimulation.

| Field | Description |
|:------|:------------|
| `Wire IDs` | Unique identifier for wire electrodes (string; required). For tracking specific items |
| `Quantity` | Number of electrodes in stock (integer, ≥ 0; required). Tracks available inventory |
| `Length` | Length of the wire (float, ≥ 0; required). Important specification |

### Virus Construct Stock

Management system for viral constructs used in genetic manipulation experiments.

| Field | Description |
|:------|:------------|
| `Titer` | Concentration of virus solution (float, ≥ 0; required) |
| `Titer unit` | Unit of titer measurement (string; enum: [vg/mL, TU/mL, pfu/mL]). Specifies concentration type |
| `Volume` | Total volume of virus solution (float, ≥ 0; required) |
| `Aliquot count` | Number of separate aliquots (integer, ≥ 0; required). Tracks sample divisions |
| `Aliquot volume` | Volume per aliquot (float, ≥ 0; required). Important for usage |

### Pharmacological Agent Stock

Bulk pharmacological agents kept on hand for surgical anesthesia, analgesia, or experimental manipulation.

| Field | Description |
|:------|:------------|
| `Product ID` | Catalog or supplier ID (string) |
| `Active Ingredient` | Pharmacologically active substance (string) |
| `Concentration` | Strength of the preparation (string) |
| `Dosage Form` | Supplied formulation (enum; e.g., solution, tablet) |
| `Route of Administration` | Typical delivery route (enum) |
| `Pharmacological Category` | Broad category of use (enum; e.g., analgesic, anesthetic) |
| `Pharmacological Class` | Mechanistic class (string) |
| `Formulation` | Excipients or carriers included (string) |
| `Storage Conditions` | Recommended storage environment (string) |
| `Purity / Grade` | Purity or grade designation (string) |
| `Experimental Use Context` | Experimental contexts (array of strings; e.g., surgical, behavioral) |

### Physiological Solution Stock

Reservoirs of buffers or physiological solutions prepared for perfusion, dissection, or storage tasks.

| Field | Description |
|:------|:------------|
| `Composition` | (**required**) Recipe or formula (string) |
| `Target pH value` | Desired pH set point (float) |
| `Osmolality` | Reported osmolality (string; e.g., "300 mOsm") |
| `Storage Conditions` | Recommended storage (string) |
| `Preparation Instructions` | Steps for preparing or sterilising the solution (string) |
| `Sterile` | Indicates whether the solution is sterile (boolean) |
| `Purpose / Use` | Primary use cases selected from a predefined list (array of strings) |

### Tracer or Dye Stock

Tracer dyes and fluorophores held in inventory for histology or circuit-tracing experiments.

| Field | Description |
|:------|:------------|
| `Product ID` | Catalog number or supplier reference (string) |
| `Type of Dye or Tracer` | Functional classification (enum; e.g., fluorescent tracer, histological dye) |
| `Fluorophore` | Fluorophore or spectral tag (string) |
| `Route of Application` | Typical application route (enum; e.g., injection, perfusion) |
| `Excitation Peak` | Excitation wavelength (float) |
| `Emission Peak` | Emission wavelength (float) |
| `Solvent / Vehicle` | Solvent or vehicle used for preparation (string) |
| `Storage Conditions` | Storage recommendations (string) |
| `Preparation Instructions` | Notes on preparation or dilution (string) |
| `Experimental Use Context` | Application contexts (array of strings; e.g., circuit tracing, histology) |

## API access

The API allows for programmable access to Consumable Stock, enabling you to read, edit, and delete stock entries through the API. Learn more about the stock fields and data structure on the [Consumable Stock API page]({{"api/modules/consumablestock/"|absolute_url}}).
