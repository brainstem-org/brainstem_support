---
layout: default
title: Material usages
parent: Materials
grand_parent: Data model
nav_order: 1
---

# Material usage model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A material usage is one row in the ordered material list of a parent entry: this material, in this role, from this source, with the values as prepared or applied in this event. The parent is exactly one [procedure]({{"datamodel/modules/procedure/"|absolute_url}}) (what was used in an in-vivo intervention), [specimen procedure]({{"datamodel/modules/specimenprocedure/"|absolute_url}}) (what was applied to ex-vivo material) or [experimental interface]({{"datamodel/modules/experimentalinterface/"|absolute_url}}) (what the installed device is made of). Material usages replace the single consumable stock field that procedures had in earlier releases.

A usage is not product identity (that is the [consumable]({{"datamodel/resources/consumable/"|absolute_url}}) in the shared catalog) and not lot state (that is the [consumable stock]({{"datamodel/modules/consumablestock/"|absolute_url}}) in a lab inventory). A usage concentration is the final, applied value; the catalog's nominal value and the lot's as-received value live on those records. Event-level values such as route, rate and timing belong to the parent procedure, not to the material row. See the [Materials overview]({{"datamodel/materials/"|absolute_url}}) for how the three records relate.

Material usages are edited inside their parent entry, in the materials panel of the procedure, specimen procedure or interface form.

{% include datamodel_embed.html model="modules.materialusage" %}

## Fields

| Field | Description |
|:------|:------------|
| `Parent` | The entry the material belongs to (**required**; exactly one of): [Procedure]({{"datamodel/modules/procedure/"|absolute_url}}), [Specimen procedure]({{"datamodel/modules/specimenprocedure/"|absolute_url}}) or [Experimental interface]({{"datamodel/modules/experimentalinterface/"|absolute_url}}). |
| `Source` | Where the material comes from (**required**; exactly one of): __Inventory__ (a [consumable stock]({{"datamodel/modules/consumablestock/"|absolute_url}}) from one of your inventories; an inventory filter narrows the list), __Catalog__ (a [consumable]({{"datamodel/resources/consumable/"|absolute_url}}) from the shared catalog without a stock entry), or __Manual entry__ (a name and free-text details for a material that is in neither). |
| `Material type` | What the material is in this row (**required**). Chosen from the material types the parent type allows; the type selects the detail fields of the row. In the parent's form and on the schema pages the type is shown under the name of its role on that parent type, for example **Implanted optic fiber** on an Optic fiber implant (type Optic fiber) or **Anesthetic agent** on an Anesthesia. *See [Material types and roles](#material-types-and-roles).* |
| `Stage` | The [procedure stage]({{"datamodel/modules/procedurestage/"|absolute_url}}) the material took part in, when the parent type declares stages. Example: "Induction" for the first bolus of an anesthetic. |
| `Order` | Position of the row in the parent's material list (**required**; number). Rows are reordered by dragging in the web interface. |
| `Details` | Type-specific values as applied: dose, concentration, dilution, volume, lot, coordinates on the device, and so on. Edited in the materials panel of the parent; through the API they are read and written with the parent's `materials/` endpoint. See the [Material usage types schema]({{"datamodel/schemas/materialusage/"|absolute_url}}). |
| `Target specimens` | For specimen procedure parents: the specific [specimens]({{"datamodel/stem/specimen/"|absolute_url}}) the material was applied to. Leave empty when it was applied to all targets of the procedure. |
| `Notes` | Notes about the row (string; maximum length: 500 characters). |
| `Source provenance` | Frozen copy of the source at the time of use (read-only): the stock, the catalog entry or the manual entry as it looked then. Later edits of the catalog or the stock do not change it. |
| `Source tier` | Which kind of source the row has (read-only). Values: Consumable stock, Consumable, Manual entry. |
| `Source identity` | Display name of the material resolved from the source (read-only). Example: "AAV9-hSyn-ChR2-EYFP (lot 2024-11)" |
| `Summary` | One-line summary of the row (read-only). |
| `Copied from procedure` | Set on interface rows that were copied from the creating procedure (read-only). Such rows are refreshed from the procedure and cannot be edited on the interface. |

## Material types and roles

There are 82 material types, grouped as agents and drugs, fluids and vehicles, reagents and labels, media and embedding, biological and experimental payloads, devices, components and supporting materials, collection and supplies, and other. The full list with the detail fields of each type is on the [Material usage types schema page]({{"datamodel/schemas/materialusage/"|absolute_url}}).

Not every type applies to every parent. Each procedure type, specimen procedure type and experimental interface type has its own rules: which material types can be recorded, under which **role name** they appear on that parent (the type Optic fiber is the role **Implanted optic fiber** on an Optic fiber implant; the type Other is **Other anesthesia material** on an Anesthesia), which stock and catalog categories each may draw from, whether a manual entry is allowed, which are required (for example at least one **Anesthetic agent** on an Anesthesia procedure), and which fields must be filled for a row to count as complete. These rules are the "Materials that can be recorded on this type" tables, with columns Material role, Required, Taken from and Complete when, on the [Procedure types]({{"datamodel/schemas/procedure/"|absolute_url}}), [Specimen procedure types]({{"datamodel/schemas/specimenprocedure/"|absolute_url}}) and [Experimental interface types]({{"datamodel/schemas/experimentalinterface/"|absolute_url}}) schema pages. The type of a procedure cannot be changed once it has materials or stages.

## Sources and the frozen copy

The three sources differ in what they can tell later. An inventory stock gives the lot, its acquisition and expiration dates and its storage; a catalog consumable gives the product identity and the supplier; a manual entry gives only what you typed. In every case the row stores a copy of the source as it was at the time of use, so the entry stays faithful even if the stock is later depleted or the catalog entry is corrected. A consumable stock cannot be deleted while material usages point to it.

## Templates

Material usage templates plan the product (a catalog consumable, optionally narrowed to one supplier, or a manual entry) and its role, stage and details; the stock is chosen when the template is applied to a real procedure or interface. Read more on the [Templates page]({{"datamodel/modules/templates/"|absolute_url}}).

## Permissions

Material usages inherit permissions from their parent: through the subject of a procedure, through the specimen set of a specimen procedure, or through the subject or specimen set of an experimental interface, and so from the projects of that record. Rows copied to an interface from its creating procedure are read-only on the interface.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to material usages, both as a resource of their own and through the materials endpoint of each parent. Learn more about the material usages' fields and data structure on the [Material usage API page]({{"api/modules/materialusage/"|absolute_url}}).
