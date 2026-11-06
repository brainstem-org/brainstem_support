---
layout: default
title: Templates
parent: Data model
nav_order: 6
---

# Templates
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A template is a reusable prefill for an entry. Instead of filling in the same anesthesia protocol, probe implant or staining recipe for every animal or every section series, you save it once as a template and apply it when you create the next record. The new entry is a copy that you can then edit; the template itself is not changed.

Templates exist for seven kinds of entry:

1. __Procedure templates__ prefill a [procedure]({{"datamodel/modules/procedure/"|absolute_url}}): type, type-specific fields, coordinate system and coordinates, target regions, equipment, protocol, licenses, notes, and the material rows and stages.
2. __Procedure episode templates__ prefill a [procedure episode]({{"datamodel/modules/procedureepisode/"|absolute_url}}): intervention class, protocol, licenses, severity, recovery outcome and description.
3. __Specimen procedure templates__ prefill a [specimen procedure]({{"datamodel/modules/specimenprocedure/"|absolute_url}}): type, type-specific fields, target regions, equipment, protocol, licenses, notes, and the material rows and stages.
4. __Experimental interface templates__ prefill an [experimental interface]({{"datamodel/modules/experimentalinterface/"|absolute_url}}): type, persistence, target type (subject or specimen set), coordinate system and coordinates, target regions, equipment, notes, and the material rows.
5. __Data acquisition templates__ prefill a [data acquisition]({{"datamodel/modules/dataacquisition/"|absolute_url}}): type, type-specific fields, equipment and notes.
6. __Manipulation templates__ prefill a [manipulation]({{"datamodel/modules/manipulation/"|absolute_url}}): type, type-specific fields, equipment and notes.
7. __Material usage templates__ prefill one [material usage]({{"datamodel/modules/materialusage/"|absolute_url}}) row. They live inside a procedure, specimen procedure or interface template, or stand alone in a material template library.

![A template prefills type, type-specific fields, coordinates and material rows. You still enter the subject, the date, notes and the actual stock items; the same pattern applies to episode, specimen procedure, interface, material usage, acquisition and manipulation templates.]({{site.baseurl}}/assets/images/diagrams/templates.svg)
*A template prefills type, type-specific fields, coordinates and material rows. You still enter the subject, the date, notes and the actual stock items; the same pattern applies to episode, specimen procedure, interface, material usage, acquisition and manipulation templates.*

{% include datamodel_embed.html model="modules.proceduretemplate" %}

## Common fields

Every template has the fields of the entry it prefills, minus the fields that tie an entry to a specific subject, specimen set or session (and minus the planning status). In addition:

| Field | Description |
|:------|:------------|
| `Name` | Name of the template (**required**). Example: "Isoflurane anesthesia, mouse", "Neuropixels 1.0 CA1 implant", "DAPI counterstain" |
| `Projects` | Projects the template is shared with. Leave empty to keep the template personal. Members of a shared project can see and apply the template. |
| `Owner` | The user who created the template (read-only). |
| `Summary` | A one-line summary of the template's content (read-only). |

## Material usage templates

A material usage template plans the product, not the lot. It names a [consumable]({{"datamodel/resources/consumable/"|absolute_url}}) from the shared catalog (optionally narrowed to one supplier) or a manual entry, together with the material role, the stage, the order, the type-specific details and notes. It does not name a [consumable stock]({{"datamodel/modules/consumablestock/"|absolute_url}}), because the stock on the shelf differs between labs and between months. When the template is applied, each planned material row is created on the new entry; where the row calls for a stock, you pick the stock from your inventory at that moment.

Material usage templates can belong to a procedure template, a specimen procedure template or an experimental interface template (they are applied together with it), or they can be library rows of their own with a name and shared projects, applied one at a time to an existing procedure, specimen procedure or interface through its "apply material template" action.

## Applying a template

Templates are applied from the forms in the web interface. On the inline lists of a subject, specimen set or session, the "Insert data from a template" button inserts a new procedure, specimen procedure, manipulation or other entry filled from the template you pick. Experimental interfaces can be added "from a template" where interfaces are selected. The template picker lists the templates you own and the templates shared with your projects, most recently used first.

Applying a template copies its values into the new entry. Material rows that come from a template keep their planned source (catalog consumable or manual entry) until you choose a stock. Interface templates carry a target type, so an interface created from one is locked to subjects or to specimen sets from the start.

## Permissions

Templates do not inherit from a subject or session. A template is visible and editable to its owner, and visible to the members of the projects it is shared with. Material usage templates inside a parent template follow that template; library material templates follow their own owner and shared projects.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

Each template family has its own API resource. Learn more about the fields and data structure on the [Procedure template]({{"api/modules/proceduretemplate/"|absolute_url}}), [Procedure episode template]({{"api/modules/procedureepisodetemplate/"|absolute_url}}), [Specimen procedure template]({{"api/modules/specimenproceduretemplate/"|absolute_url}}), [Experimental interface template]({{"api/modules/experimentalinterfacetemplate/"|absolute_url}}), [Data acquisition template]({{"api/modules/dataacquisitiontemplate/"|absolute_url}}), [Manipulation template]({{"api/modules/manipulationtemplate/"|absolute_url}}) and [Material usage template]({{"api/modules/materialusagetemplate/"|absolute_url}}) API pages.
