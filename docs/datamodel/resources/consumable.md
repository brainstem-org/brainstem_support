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

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction 

A consumable is one entry in the shared catalog: the product or design identity of a purchasable material, independent of any lab, lot or use. A reagent product, a probe design, a virus construct. Its quantities are nominal catalog facts as the supplier reports them (concentration, titer, package quantity). Lot-specific facts (a batch number, an expiry date, a titer you measured, how much you have left) belong on your [consumable stock]({{"datamodel/modules/consumablestock/"|absolute_url}}); a record of a lot being used is a [material usage]({{"datamodel/modules/materialusage/"|absolute_url}}). Consumables are shared across users to promote standardization.

{% include datamodel_embed.html model="resources.consumable" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Type of consumable`` | Type of consumable (**required**). Controls the structured product fields and which materials the product can be used as later. Example: "Silicon probe design". *See options below* |
| ``Name`` | Product name as the supplier lists it, including the model or catalogue designation (**required**; string; maximum length: 100 characters; must be unique across BrainSTEM). Example: "Neuropixels 1.0 - 384 channels - Option 3" |
| ``Supplier`` | Supplier of the consumable (**required**). Must reference an existing [supplier]({{"datamodel/resources/supplier/"|absolute_url}}); submit missing suppliers first. Example: "IMEC" |
| ``Description`` | Description of the consumable (maximum length: 2000 characters). |
| ``RRID`` | Research Resource Identifier (string; maximum length: 100 characters). **Lookup RRID** beside the field fetches the product from the SciCrunch registry and fills in the name, description and external identifiers, and suggests suppliers from the registry's vendor list. Example: "RRID:Addgene_176754" |
| ``External identifiers`` | Catalogue numbers and identifiers in other registries (NCBI, JAX, DOI, Addgene and others), each with source, id and URL. |
| ``Type specific fields`` | Product specification fields defined by the type. Most types have one or two required fields. See the [Consumable types schema]({{"datamodel/schemas/consumable/"|absolute_url}}). |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

## Types of consumable

See the schema for field details: [Consumable types]({{"datamodel/schemas/consumable/"|absolute_url}}). The required fields of each type are noted.

### Reagents and Solutions

`Antibody or immunoreagent`: An antibody or binding reagent. Target antigen and reagent type are required; host and reactivity species decide what it can be combined with.

`Biological material`: A cell line, pluripotent stem cell line, primary-cell product, organoid line, hybridoma or tissue product, as the supplier or repository describes it. Kind of material is required; species, strain and tissue of origin, cell type, donor details, genetic modification and biosafety level describe where it comes from. Sera, matrices and purified proteins are reagents; viral vectors are virus constructs. In a STAR Methods report it is listed under Experimental models: Cell lines.

`Chemical reagent`: A defined chemical compound. Chemical type is required. Use this for laboratory chemicals rather than formulated drugs.

`Histology reagent`: A reagent for tissue processing: fixatives, clearing solutions, mounting media. Processing role is required.

`Medical or carrier gas`: A gas product. Gas type is required.

`Pharmacological agent`: A formulated drug. Active ingredient and pharmacological category are required.

`Physiological solution`: A solution tissue or animals are exposed to, such as ACSF or Ringer's. Composition is required.

`Tracer or dye`: A dye or tracer for labelling. Dye type is required; excitation and emission peaks decide optical compatibility.

`Virus construct`: A viral vector as designed: serotype, capsid, promoter, gene, reporter. The titer and aliquots of the batch you hold belong on your stock.

### Device-Linked Consumables

`Connector component`: Connectors, headers and adapters. Connector class is required; contact count and gender decide compatibility.

`Consumable device`: A manufactured device consumed or dedicated to one subject that no more specific type covers. Device class is required.

`ECoG array design`: A surface grid or strip array product. Total contacts and channel count are required; layout, rows and columns, contact size and pitch, materials, footprint, contact groups, per-contact coordinates, reference contacts and package options describe the rest. For a grid or strip, rows times columns must equal the total contacts.

`Electrode component`: Electrode parts and wire stock. Electrode role is required.

`Optic fiber design`: A fiber product. Fiber type and core diameter are required; with numerical aperture they determine what the fiber can deliver.

`Optical component`: Lenses, prisms, filters, windows. Component type is required.

`Silicon probe design`: A probe product. Layout, channel count and shank count are required; they are the design, and everything downstream depends on them.

`Single wire electrode`: A wire electrode product, described by material, insulation and diameter.

### Surgical Consumables

`Adhesive or cement`: Dental cement, glue or resin. Subtype is required; mixing ratio and curing method make a two-part product reproducible.

`Fastener or anchor`: Screws, pins and anchors. Subtype is required; thread size and length are the practical selectors.

`Implant or fixation material`: Bulk material for building or securing an implant. Subtype is required.

`Surgical disposable`: Single-use surgical supplies: sutures, blades, swabs, drapes. Subtype is required.

## Catalog imports and schematics

Silicon probe designs and ECoG array designs are imported from reviewed vendor catalog files maintained with the BrainSTEM source, one file per manufacturer. Silicon probe designs come from ATLAS Neuroengineering, Cambridge Neurotech, IMEC (Neuropixels) and NeuroNexus; ECoG array designs from ATLAS Neuroengineering, Blackrock Neurotech, Cambridge Neurotech, NeuroNexus and PMT Corporation. Only reviewed values are imported, and each imported field records where its value came from.

The catalog page of a silicon probe design, ECoG array design or optic fiber design draws a schematic of the design from its specification (shank and site layout, contact grid, fiber layers). The drawing is generated from the stored fields, so correcting the specification corrects the drawing.

## Submission process

Anyone can submit consumables or submit changes to existing ones. A submission enters the approval queue and is usable in your own records immediately; it is visible only to you until accepted. Search the existing list first, including the catalogue designation; a near-duplicate is the usual reason for rejection. For details of the approval statuses see the [Resources page]({{"datamodel/resources/"|absolute_url}}).

A consumable cannot be deleted while consumable stocks, equipment, material usages or material usage templates point to it.

## Permissions

Everyone can read the accepted list. Editing an accepted entry is restricted, since it would change every stock and material usage that references it; an edit creates a change request that is reviewed before it takes effect. Your own pending submissions remain yours to edit or cancel.

## API access

The API allows for programmable access to consumables, returning the accepted list plus your own pending submissions. Learn more about the consumables' fields and data structure on the [Consumables API page]({{"api/resources/consumable/"|absolute_url}}).
