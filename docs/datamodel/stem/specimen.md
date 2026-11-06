---
layout: default
title: Specimens
parent: Specimen sets
grand_parent: Data model
nav_order: 1
---

# Specimen model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A specimen is one individually trackable item inside a [specimen set]({{"datamodel/stem/specimenset/"|absolute_url}}): a single slice, section, well, culture item, organoid or tissue piece. Specimens give you per-item granularity when you need it. A set that does not need per-item tracking simply records an item count and creates no specimens.

A specimen is not the batch (that is the specimen set), not a live animal (that is the [subject]({{"datamodel/stem/subject/"|absolute_url}})), and not a processing event. The processing history that drives a specimen's state is recorded as [specimen procedures]({{"datamodel/modules/specimenprocedure/"|absolute_url}}) on the set, which can target the whole set or specific specimens. [Specimen logs]({{"datamodel/modules/specimenlog/"|absolute_url}}), [experimental interfaces]({{"datamodel/modules/experimentalinterface/"|absolute_url}}) and [material usages]({{"datamodel/modules/materialusage/"|absolute_url}}) can also target specific specimens of a set.

{% include datamodel_embed.html model="stem.specimen" %}

## Fields

| Field | Description |
|:------|:------------|
| `Specimen set` | The [specimen set]({{"datamodel/stem/specimenset/"|absolute_url}}) this item belongs to (**required**). |
| `Local identifier` | Stable identifier of the specimen within its set (**required**; string; maximum length: 100 characters; must be unique within the specimen set). Example: "S01", "A3" (a well), "slice_04" |
| `Type` | Kind of item (**required**; default: Other). Selected from predefined types. *See options below.* |
| `Status` | Current availability of the item (**required**; default: Available). Choices: Planned, Available, In use, Reserved, Consumed, Discarded, Lost. Same vocabulary as the specimen set. |
| `Quality` | Quality assessment of the item. Choices: Excellent, Good, Fair, Poor, Not assessed. |
| `Laterality` | Which side of the brain or body the item comes from. Choices: Left, Right, Bilateral, Not applicable. |
| `Order` | Ordering of the item within the set (number; default 0). Example: the position of a section in the series. |
| `Source specimen` | The specimen this item was derived from, if applicable. Lineage must stay acyclic. |
| `Preparation conditions` | The set's starting conditions plus the conditions added by specimen procedures on the whole set or on this item (read-only; recomputed automatically). Choices: Fixed, Cryoprotected / frozen, Embedded, Cleared, Stained / labelled, Mounted; none means fresh / unprocessed. |
| `Storage location` | Current physical storage location, container or slot (string; maximum length: 100 characters). Example: "Slide box 7, slot 12" |
| `Storage conditions` | Current storage conditions, such as temperature and medium (string; maximum length: 100 characters). |
| `Termination date and time` | When the item was consumed, discarded, lost or otherwise terminated. |
| `Notes` | Free-text notes about the item. |
| `Type specific fields` | Fields that depend on the selected type, such as the thickness or position of a slice or section. See the [Specimen types schema]({{"datamodel/schemas/specimen/"|absolute_url}}). |

## Types of specimens

These are the available type options. See the schema for field details: [Specimen types]({{"datamodel/schemas/specimen/"|absolute_url}}).

`Slice`: One slice of a slice series, typically a thick acute or organotypic slice.

`Section`: One thin histological section of a section series.

`Well`: One well of a well plate.

`Culture item`: One item of a culture, such as a dish or an insert.

`Organoid`: One organoid of an organoid batch.

`Tissue piece`: One piece of tissue, such as a dissected block.

`Other`: An item that does not fit the types above.

## Permissions

Specimens inherit permissions through their specimen set, and so from the projects of that set.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to specimens. Learn more about the specimens' fields and data structure on the [Specimen API page]({{"api/stem/specimen/"|absolute_url}}).
