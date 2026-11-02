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

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A consumable stock is one lot, batch, vial, package, prepared solution or subject-specific component held in an [inventory]({{"datamodel/personal_attributes/inventory/"|absolute_url}}). It is a physical thing your lab has, not a product you could order. Create a separate entry per lot, so that a material used in an experiment can be traced to the exact batch it came from.

The chain runs catalog, stock, use: a [consumable]({{"datamodel/resources/consumable/"|absolute_url}}) is the shared catalog identity (what the product is, who makes it); the consumable stock is your lot of that product, with its own dates, storage, status and lot-specific details; a [material usage]({{"datamodel/modules/materialusage/"|absolute_url}}) records that lot being used in a procedure, specimen procedure or experimental interface. See [Materials]({{"datamodel/materials/"|absolute_url}}). Reusable apparatus that persists across sessions is [equipment]({{"datamodel/modules/equipment/"|absolute_url}}), not stock.

{% include datamodel_embed.html model="modules.consumablestock" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Type of consumable stock`` | Type of consumable stock (**required**). Controls the lot-specific fields and which materials the lot may be used as later. Example: "Silicon probe", "Virus solution". *See options below* |
| ``Status`` | Current availability of the lot (**required**; default: Available). Choices: Available, In use, Reserved, Depleted, Used, Failed/Broken, Expired, Maintenance, Discontinued, Unknown. |
| ``Inventory`` | The inventory that holds the lot (**required**). Must reference an existing [inventory]({{"datamodel/personal_attributes/inventory/"|absolute_url}}) where you are at least a Contributor. The inventory decides who may see and edit the stock. |
| ``Consumable supplier`` | Form-only filter for the consumable field. Not stored. |
| ``Consumable`` | The catalog entry this lot is an instance of (**required**). The consumable types allowed depend on the stock type; a stock of type Silicon probe must point at a Silicon probe design, an ECoG array at an ECoG array design, a Virus solution at a Virus construct, an Optic fiber at an Optic fiber design. |
| ``Acquisition date`` | Date the lot was acquired (format: YYYY-MM-DD). |
| ``Expiration date`` | Date the lot is expected to expire or become unusable (format: YYYY-MM-DD). |
| ``Storage location`` | Where the lot is stored (string; maximum length: 100 characters). Example: "Room 302, Cabinet B, Shelf 3" |
| ``Storage conditions`` | Conditions for storing the lot (string; maximum length: 100 characters). Example: "-80°C" |
| ``Intended use`` | Planned experimental use (string; maximum length: 100 characters). Example: "Chronic recordings, cohort 3" |
| ``Cost`` | Cost of the lot (string; maximum length: 100 characters). Example: "$500 USD" |
| ``Notes`` | Additional information (string; maximum length: 500 characters). |
| ``Type specific fields`` | Lot-specific fields based on the stock type. Most types record a batch or product identifier; that identifier is what makes a later material usage traceable. See the [Consumable stock types schema]({{"datamodel/schemas/consumablestock/"|absolute_url}}). |

## Types of consumable stocks

These are the available type options for consumable stock. They mirror the [consumable catalog types]({{"datamodel/resources/consumable/"|absolute_url}}), with instance names for the design/instance pairs (Silicon probe for Silicon probe design, ECoG array for ECoG array design, Optic fiber for Optic fiber design, Virus solution for Virus construct). See the schema for field details: [Consumable stock types]({{"datamodel/schemas/consumablestock/"|absolute_url}}).

### Reagents and Solutions

`Antibody or immunoreagent`: An antibody or related binding reagent for immunolabeling. Record host and reactivity species. Fields: reagent type (required), batch ID, host and reactivity species, target antigen, clonality, conjugate, amount, dilution.

`Biological material`: Vials or a lot of cells, a cell line, primary cells, organoids or tissue held in the lab, bought or banked from your own culture. Choose it for the material a culture or injection is started from; virus preparations are virus solutions. Fields: batch ID, vials or units in the lot, viable cells per vial or unit, viability, passage at freeze, cryopreservation medium.

`Chemical reagent`: A defined chemical compound; for laboratory chemicals rather than a formulated drug or a buffer you mixed. Fields: chemical type (required), batch ID, compound name, molecular weight, amount, concentration, purity or grade, hazard information.

`Histology reagent`: A reagent prepared for tissue processing, such as a fixative, buffer or clearing solution. Fields: batch ID, amount, concentration, pH, preparation date and instructions.

`Medical or carrier gas`: A gas cylinder, such as oxygen, carbon dioxide or an inhalant carrier. Fields: cylinder or batch ID, amount, regulator setting.

`Pharmacological agent`: A formulated drug given to a subject: anesthetics, analgesics, antibiotics. Fields: pharmacological category (required), batch ID, active ingredient, amount, concentration, dosage form, route, pharmacological class, formulation.

`Physiological solution`: A solution the tissue or animal is exposed to, such as ACSF, saline or Ringer's. Fields: solution name, composition, amount, target pH, osmolality, preparation instructions, sterility, purpose.

`Tracer or dye`: A dye or tracer used to label structures or follow connectivity. Fields: dye type (required), batch ID, fluorophore, route of application, excitation and emission peaks, amount, solvent, preparation instructions.

`Virus solution`: A viral vector preparation. Fields: batch ID, titer, volume, number of aliquots, volume per aliquot.

### Device-Linked Consumables

`Connector component`: Connectors, headers and adapters used to build an implant or headstage assembly. Fields: batch ID, quantity, assembled by.

`Consumable device`: A manufactured device consumed or dedicated to one subject that no more specific type covers. Fields: device class (required), product ID, compatible systems, dimensions, material, connectivity, use context.

`Electrode component`: Electrode parts and wire stock, as distinct from a finished probe. Fields: batch ID, quantity, length, measured impedance, sterility.

`Optic fiber`: Fiber stock or assembled fiber implants. Fields: fiber IDs and quantity.

`Optical component`: Lenses, prisms, filters and windows. Fields: optical component type (required), product ID, material, dimensions, surface coating, wavelength range, sterility, use context.

`Silicon probe`: Silicon probes held as stock. Record the probe IDs; this is how a specific probe is traced from the shelf into a subject and back out if recovered. Fields: probe IDs and quantity.

`ECoG array`: ECoG surface arrays held as stock, each lot linked to an ECoG array design in the catalog. Arrays are durable: they can be marked failed or in maintenance, not depleted or expired. Fields: array IDs and quantity.

`Single wire electrode`: Individual wire electrodes held as stock. Fields: wire IDs, quantity, length.

### Surgical Consumables

`Adhesive or cement`: Dental cement, glue or resin used to fix implants. Fields: batch ID, amount, mixing ratio, preparation instructions, sterility.

`Fastener or anchor`: Screws, pins and anchors that hold an implant to bone. Fields: batch ID, quantity, sterility.

`Implant or fixation material`: Bulk material used to build or secure an implant, such as biocompatible polymer or wax. Fields: batch ID, amount, preparation instructions, sterility.

`Surgical disposable`: Single-use surgical supplies: sutures, blades, swabs, drapes. Fields: batch ID, quantity, sterility.

## Deleting a stock

A consumable stock cannot be deleted while material usages point to it. Mark it Depleted, Used or Discontinued instead, so the records that used it keep their trace.

## Permissions

Consumable stocks inherit permissions through the inventory associated with them. Contributors of the inventory can add and edit its stock and select its lots when recording materials.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to consumable stocks, enabling you to read, edit, and delete consumable stocks through the API. Learn more about the consumable stocks' fields and data structure on the [Consumable stocks API page]({{"api/modules/consumablestock/"|absolute_url}}).
