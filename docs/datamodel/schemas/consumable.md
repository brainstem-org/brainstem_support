---
layout: default
title: Consumable types
parent: Schemas
grand_parent: Data model
nav_order: 7
---

# Consumable types
{: .no_toc}

Several types of consumables are available, each with specific fields to describe their characteristics in detail.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Reagents and Solutions

### Chemical reagent

Chemical reagents cover solvents, fixatives, detergents, and other laboratory chemicals required for preparation and analysis steps.

| Field | Description |
|:------|:------------|
| `Product ID` | Catalog or supplier product code (string). Examples include "T8787" or "P6148" |
| `Compound Name` | Name of the chemical (string). Useful for search and reporting |
| `Chemical Type` | (**required**) General classification of the reagent (enum). Options cover fixatives, detergents, buffers, solvents, dyes, polymers, and more |
| `Concentration / Strength` | Solution strength if supplied pre-diluted (string; e.g., "4%", "1 M", "10X") |
| `Molecular Weight` | Molecular weight of the compound (float, ≥ 0) |
| `Purity / Grade` | Reported purity or grade designation (string; e.g., "≥99%", "Analytical grade") |
| `Storage Conditions` | Recommended storage environment (string; e.g., "Room temp", "4°C", "Protect from light") |
| `Hazard Information` | safety notes or GHS classification (string) |
| `Experimental Use Context` | Typical workflows where the reagent is used (string; e.g., perfusion, fixation, staining) |

### Consumable device

Reusable or single-use devices such as tubing sets, holders, adapters, and other experiment-specific hardware.

| Field | Description |
|:------|:------------|
| `Product ID` | Supplier or catalog identifier (string). Supports procurement and tracking |
| `Device Class` | (**required**) General class of consumable device (string). Helps categorize inventory |
| `Compatible Systems` | Supported platforms or rigs (string). Examples include Neuropixels, Inscopix, Doric |
| `Physical Dimensions` | Key geometry or size information (string). Important for fit and compatibility |
| `Material` | Primary construction material (string). Influences durability and cleaning method |
| `Connectivity` | Connector or interface type (string; e.g., LC/PC, Omnetics) |
| `Storage Conditions` | Recommended storage environment (string) |
| `Experimental Use Context` | Intended or validated experimental uses (array of strings) |

### External identifiers

Use this table to cross-reference consumables with external databases such as NCBI, JAX, DOI, or supplier catalogs.

| Field | Description |
|:------|:------------|
| `Source` | (**required**) Database or provider of the identifier (enum; e.g., NCBI, JAX, DOI) |
| `Identifier` | (**required**) External identifier string (string; e.g., AB_123456) |
| `URL ` | Direct link to the external record (string; must be a valid URL if provided) |

### Immuno reagent

Antibodies and related immunochemical reagents used for staining, tracing, or detection tasks.

| Field | Description |
|:------|:------------|
| `Product ID` | Supplier product code or catalog number (string) |
| `Target Antigen` | (**required**) Target molecule the reagent binds to (string) |
| `Reagent Type` | (**required**) General classification (string; e.g., primary antibody, nanobody) |
| `Host Species` | Animal species in which the antibody was raised (string) |
| `Reactivity Species` | Species the antibody recognizes (string) |
| `Clonality` | Indicates monoclonal or polyclonal (string) |
| `Conjugated Fluorophore or Enzyme` | Attached reporter or enzyme label (string) |
| `Validated Applications` | Confirmed experimental applications (array of strings; e.g., IHC, Western Blot) |
| `Recommended Dilution` | Supplier-recommended dilution range (string) |
| `Storage Conditions` | Storage guidance (string; e.g., "4°C", "-20°C") |

### Pharmacological agent

Pharmacological agents encompass agonists, antagonists, anesthetics, and other compounds administered during experiments.

| Field | Description |
|:------|:------------|
| `Product ID` | Catalog or supplier ID (string) |
| `Active Ingredient` | (**required**) Pharmacologically active substance (string; e.g., Ketamine, Isoflurane) |
| `Concentration` | Stated strength of the preparation (string; e.g., "10 mg/mL", "0.1%") |
| `Dosage Form` | Physical form supplied (enum; e.g., solution, tablet, injection) |
| `Route of Administration` | Typical experimental delivery route (enum; e.g., IP, IV, SC) |
| `Pharmacological Category` | (**required**) Broad category of use (enum; e.g., analgesic, anesthetic) |
| `Pharmacological Class` | Mechanistic or therapeutic class (string; e.g., NSAID, NMDA antagonist) |
| `Formulation` | Excipients or carriers included (string; e.g., "in 10% DMSO + saline") |
| `Storage Conditions` | Recommended storage environment (string; e.g., "4°C", "Protect from light") |
| `Purity / Grade` | Reported purity or grade designation (string) |
| `Experimental Use Context` | Contexts where the agent is applied (array of strings; e.g., surgical, behavioral) |

### Physiological solution

Buffers and physiological solutions prepared for perfusion, slice preparation, or maintaining explants.

| Field | Description |
|:------|:------------|
| `Composition` | (**required**) Full recipe or formula (string; e.g., 0.9% NaCl, aCSF) |
| `Target pH value` | Desired pH set point for the solution (float) |
| `Osmolality` | Reported osmolality (string; e.g., "300 mOsm") |
| `Storage Conditions` | Recommended storage (string; e.g., room temperature, 4°C) |
| `Preparation Instructions` | Steps for preparing or sterilising the solution (string) |
| `Sterile` | Indicates whether the solution is sterile (boolean) |
| `Purpose / Use` | Primary application contexts (array of strings; e.g., perfusion, fixation) |

### Tracer or dye

Tracer and dye formulations used for histology, circuit tracing, vital staining, and injection visualization.

| Field | Description |
|:------|:------------|
| `Product ID` | Catalog number or supplier reference (string) |
| `Type of Dye or Tracer` | (**required**) Functional classification (string; e.g., fluorescent tracer, retrograde tracer) |
| `Fluorophore` | Associated fluorophore or spectral tag (string) |
| `Route of Application` | Delivery method (string; e.g., injection, perfusion, topical) |
| `Excitation Peak` | Excitation wavelength (float) |
| `Emission Peak` | Emission wavelength (float) |
| `Solvent / Vehicle` | Solvent used for preparation (string) |
| `Storage Conditions` | Storage recommendations (string) |
| `Preparation Instructions` | Notes on preparation or dilution (string) |
| `Experimental Use Context` | Typical applications selected from a predefined list (array of strings) |

### Virus construct

A viral vector preparation used for introducing genes into cells. Virus solutions are important for studies involving gene expression, neural circuit tracing, and optogenetics.

| Field | Description |
|:------|:------------|
| `Product id` | Product identifier that must be unique for each viral construct (string). Required for tracking |
| `Virus type` | Classification of virus used (string). Options include "Adenovirus", "AAV", etc. Critical for application |
| `Capsid` | Specification of the viral capsid structure (string). Determines tropism and targeting |
| `Promoter` | Genetic promoter sequence used in construct (string). Controls expression specificity |
| `Gene` | Target gene sequence in the construct (string). Defines the genetic modification |
| `Reporter` | Reporter gene or protein for tracking expression (string). Important for verification |
| `Other element` | Additional genetic elements in construct (string). Documents supplementary components |

## Device-Linked Consumables

### Optic fiber design

A flexible light guide used primarily in optogenetic experiments to deliver light to specific brain regions.

| Field | Description |
|:------|:------------|
| `Product ID` | (**required**) Unique identifier for the fiber design (string) |
| `Numerical aperture` | Optical acceptance angle (float). Defines coupling performance |
| `Wavelength minimum` | (**required**) Shortest supported wavelength (float) |
| `Wavelength maximum` | (**required**) Longest supported wavelength (float) |
| `Fiber type` | (**required**) Fiber classification (string). Distinguishes single-mode vs multi-mode |
| `Core diameter` | (**required**) Diameter of the light-guiding core (float) |
| `Cladding diameter` | Cladding diameter surrounding the core (float) |
| `Coating diameter` | Outside diameter including protective coating (float) |
| `Core material` | Material used for the fiber core (string) |
| `Cladding material` | Material used for the cladding layer (string) |
| `Coating material` | Protective coating material (string) |

### Optical component

Individual optical elements such as GRIN lenses, cranial windows, or microprisms used within experimental rigs.

| Field | Description |
|:------|:------------|
| `Product ID` | Supplier or catalog ID (string) |
| `Optical Component Type` | (**required**) General class of optical element (enum; e.g., GRIN lens, optical filter, microprism) |
| `Material` | Primary material (string; e.g., glass, quartz, sapphire) |
| `Physical Dimensions` | Key geometry information (string; e.g., diameter and length) |
| `Surface Coating` | Special surface treatment such as anti-reflective coatings (string) |
| `Wavelength minimum` | Shortest supported wavelength (float) |
| `Wavelength maximum` | Longest supported wavelength (float) |
| `Sterile` | Indicates if the component is supplied sterile (boolean) |
| `Storage Conditions` | Recommended storage environment (string; e.g., dry box) |
| `Experimental Use Context` | Application contexts (array of strings; e.g., chronic imaging, optogenetics) |

### Silicon probe design

A specialized tool for recording electrical signals from neurons. Silicon probes are vital for experiments focused on understanding brain function through electrophysiological recordings.

| Field | Description |
|:------|:------------|
| `Product id` | Product identifier that must be unique for each probe design (string). Required for inventory tracking and reference |
| `Probe layout` | Description of the probe's physical arrangement (string). Options include "linear", "grid", etc. Required for experimental planning |
| `Number of channels` | Total number of recording channels on the probe (non-negative integer). Critical for determining recording capacity |
| `Number of shanks` | Number of probe shanks (non-negative integer). Affects recording coverage and tissue impact |
| `Spacing between shanks` | Distance between adjacent shanks (float). Important for spatial distribution of recording sites |
| `Thickness of shanks` | Physical thickness of each shank (float). Critical for tissue damage assessment |
| `Length of shanks` | Physical length of each shank (float). Determines recording depth capability |
| `Area of electrode sites` | Surface area of individual recording sites (float). Affects signal quality and impedance |
| `Uniform layout` | Indicates whether recording sites are uniformly spaced (boolean). Important for data analysis |
| `Custom design` | Indicates whether this is a custom probe design (boolean). Relevant for manufacturing and ordering |
| `Vertical spacing between sites` | Distance between recording sites along vertical axis (float). Critical for spatial resolution |

### Single wire electrode

A simple yet effective tool for measuring electrical activity at a single site. Single wire electrodes are commonly used in studies examining neural or muscular electrical activity.

| Field | Description |
|:------|:------------|
| `Product id` | Product identifier that must be unique for each electrode (string). Required for inventory |
| `Material` | Composition of the electrode wire (string). Critical for electrical properties |
| `Insulation/Coating` | Type and material of electrode insulation (string). Affects recording isolation |
| `Diameter` | Core wire diameter (float). Determines tissue impact and signal quality |
| `Insulation diameter` | Total diameter including insulation (float). Important for insertion planning |

## Surgical Consumables

### Implant / fixation material

Materials used for implant anchoring and fixation, such as dental cement, adhesives, and bone screws.

| Field | Description |
|:------|:------------|
| `Product ID` | Catalog number or supplier reference (string) |
| `Type` | (**required**) Material subtype (enum; e.g., dental cement, adhesive, bone screw, skull anchor, bone wax, silicone elastomer, acrylic polymer, cyanoacrylate glue, other) |
| `Preparation Instructions` | Steps needed before use (string) |
| `Storage Conditions` | Recommended storage environment (string; e.g., room temperature, 4°C) |
| `Biocompatible` | Whether the material is biocompatible for in vivo use (boolean) |
| `Additional Notes` | Free-text notes on specs or usage (string) |

### Surgical disposable

Single-use surgical items such as blades, sutures, catheters, and drapes.

| Field | Description |
|:------|:------------|
| `Product ID` | Catalog number or supplier reference (string) |
| `Type` | (**required**) Disposable subtype (enum; e.g., scalpel blade, needle, syringe, suture, gauze/swab, surgical drape, catheter, other) |
| `Material` | Primary material (string; e.g., stainless steel, absorbable polymer) |
| `Specification` | Short size/format descriptor (string; e.g., 30G x 1/2", 6-0 nylon, No. 11 blade) |
| `Sterile` | Whether item is sterile (boolean) |
| `Additional Notes` | Free-text notes on specs or usage (string) |

## API access

The API allows for programmable access to Consumable types, enabling you to read, edit, and delete consumable type data through the API. Learn more about the consumable types' fields and data structure on the [Consumable types API page]({{"api/resources/consumable/"|absolute_url}}).
