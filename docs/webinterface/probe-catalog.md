---
layout: default
title: Probe catalog
parent: Assistants and references
grand_parent: Web interface
nav_order: 3
---

# Probe catalog
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

Silicon probes and ECoG arrays are recorded in BrainSTEM through the material chain: a shared catalog entry describes the manufacturer's design, a consumable stock entry describes the physical probe your lab owns, and an implant procedure records which probe went into which subject. BrainSTEM ships a catalog of probe designs from the main vendors so that you rarely have to type probe geometry yourself. The chain itself is explained on the [Materials]({{"datamodel/materials/"|absolute_url}}) page.

## Designs as consumables

Probe designs are consumables of the type **Silicon probe design** or **ECoG array design** (under **Resources** → **Consumables**). Each design carries the geometry of the probe in its type-specific details: number of shanks, shank length, width and pitch, number of channels, site layout and pitch, reference sites, and where available the individual site coordinates. Like all shared catalog entries they are visible to every user.

{% include slides.html slides="probe-catalog-list|The consumables list searched for Buzsaki probe designs, with their type, supplier and description.;;probe-catalog-page|The top of a silicon probe design's details page: name, supplier, type and the type-specific details, such as the recording-site layout, the number of shanks and the shank dimensions.;;probe-catalog-form|The same design's form, scrolled to the external identifiers and the type-specific details: product ID, recording-site layout, site column alignment, channels, recording sites and the shank geometry." %}

At the time of writing the catalog holds 366 silicon probe designs and 95 ECoG array designs:

| Type | Vendor | Designs |
|------|--------|---------|
| Silicon probe design | NeuroNexus | 175 |
| Silicon probe design | ATLAS Neuroengineering | 126 |
| Silicon probe design | Cambridge NeuroTech | 43 |
| Silicon probe design | IMEC (Neuropixels) | 22 |
| ECoG array design | Blackrock Neurotech | 36 |
| ECoG array design | NeuroNexus | 34 |
| ECoG array design | PMT Corporation | 12 |
| ECoG array design | ATLAS Neuroengineering | 8 |
| ECoG array design | Cambridge NeuroTech | 5 |

Catalog designs are maintained from vendor data. Edits made by users to a catalog design are kept and are not overwritten by later catalog updates. Optic fiber designs from Thorlabs and a large set of virus constructs are shipped the same way.

## The probe schematic

The details page of a silicon probe, ECoG array or optic fiber design shows a drawing generated from its details: "Open the drawing in a new tab to zoom in and hover its parts for details."

{% include slides.html slides="probe-catalog-schematic|The schematic of a 16-shank probe: the overview at true proportion with the recording sites in orange, and the tip detail enlarged.;;probe-catalog-ecog|The contact map of an ECoG array: 128 contacts on an 8 × 16 grid with a 3 mm pitch." %}

- **Overview** shows the probe at true proportion; **Tip detail** enlarges the recording end. "Orange marks recording sites; hollow marks reference contacts."
- Rulers label **Pitch**, **Column pitch**, **Tip** (or **Estimated tip**) and **Shank pitch**. Hovering a site shows "Site {id} · shank {n}" with its position in µm.
- A caption states where the geometry came from: measured site coordinates, a scaled catalog drawing, or nominal dimensions. "Site IDs are diagram numbering, not manufacturer contact IDs or channel wiring."
- ECoG arrays show an **ECoG array contact map**.

A thumbnail of the schematic appears in the hover summary of a consumable in lists and pickers. Stock entries do not show the schematic; in implant procedures the shanks are drawn inside the [coordinate viewer]({{"webinterface/atlases-and-coordinates/#view-coordinates"|absolute_url}}).

## Picking a design for a stock entry

To record a probe your lab owns, add a consumable stock of type **Silicon probe** or **ECoG array** in one of your inventories. The **Consumable** field is required ("Select the consumable you are adding as a consumable stock.") and only offers designs of the matching type; narrow the list by **Supplier** first if you like. Add the lot or serial number, acquisition and expiration dates, status and storage location. The stock entry keeps its own status (Available, In use, Reserved, Depleted, Used, Failed/Broken, Expired, …), which you set by hand.

## Recording an implant

In a **Silicon probe implant** or **ECoG implant** procedure, the probe is a required material in the **Materials** tab. Choose a source:

- **Consumable stock**: the probe from your inventory (recommended; records the lot and keeps a snapshot of the stock).
- **Consumable**: a catalog design when you have no stock entry.
- **Manual entry**: a name and specification when the design is not in the catalog.

With a stock or catalog source, the coordinate viewer draws the probe with its real shank count and pitch, and the procedure, stock and catalog pages all link to each other through the usage history.

## Requesting a missing design

If your probe is not in the catalog, add it yourself: **Resources** → **Consumables** → **Add consumable**, type **Silicon probe design** or **ECoG array design**, and fill in the geometry you know. New catalog entries go through the shared approval flow: your entry is saved at once and you can use it immediately, but it is visible only to you until the BrainSTEM team approves it ("PENDING: This submission is under review. It is only visible to the creator until approved and can be used privately."). You are emailed when the status changes. Designs with incomplete required fields are not published until they are completed.

## Related

- [Materials]({{"datamodel/materials/"|absolute_url}}): the chain from catalog design to stock entry to implant
- [Consumables]({{"datamodel/resources/consumable/"|absolute_url}}) and [Consumable stocks]({{"datamodel/modules/consumablestock/"|absolute_url}}): the two kinds of entry a probe is recorded as
- [Procedures]({{"datamodel/modules/procedure/"|absolute_url}}): the implant procedure types
- [Atlases and coordinates]({{"webinterface/atlases-and-coordinates/#view-coordinates"|absolute_url}}): the viewer that draws the probe in the atlas
- [Submission forms]({{"webinterface/forms/#materials-editor"|absolute_url}}): the Materials tab where the probe is chosen
- [Resources & Taxonomies]({{"tutorials/submit-resource-and-taxonomies/"|absolute_url}}): submitting a design that is missing from the catalog
