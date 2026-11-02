---
layout: default
title: Materials
parent: Data model
nav_order: 5
has_children: true
has_toc: false
---

# Materials
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Materials are the probes, fibers, viruses, drugs, reagents, media and supplies that go into an experiment. BrainSTEM records them as a chain of three entries, each answering a different question, and it records the phases of a procedure that materials take part in as stages. To reuse a set of material rows, save it in a [template]({{"datamodel/modules/templates/"|absolute_url}}).

## The material chain

![A material usage row records what was actually applied; it points at a lot in your inventory, at the shared catalog entry, or at a manual entry, and sits on a procedure, specimen procedure or experimental interface.]({{site.baseurl}}/assets/images/diagrams/material-chain.svg)
*A material usage row records what was actually applied; it points at a lot in your inventory, at the shared catalog entry, or at a manual entry, and sits on a procedure, specimen procedure or experimental interface.*

| Entry | Question it answers | Values it holds |
|:-------|:--------------------|:----------------|
| [Consumable]({{"datamodel/resources/consumable/"|absolute_url}}) (catalog) | Which product or design is this? | __Nominal__ values as the supplier reports them: catalog concentration, titer, package quantity, probe design. Shared across all labs. |
| [Consumable stock]({{"datamodel/modules/consumablestock/"|absolute_url}}) (inventory) | Which lot or batch do we have in the lab, and in what state? | __As-received__ or currently available values: what the label says, acquisition and expiration dates, storage, status. Kept in a lab [inventory]({{"datamodel/personal_attributes/inventory/"|absolute_url}}). |
| [Material usage]({{"datamodel/modules/materialusage/"|absolute_url}}) | What was used in this event or built into this device, in which role, and how? | __Applied__ values as prepared or delivered in this event: dose, dilution, volume, final concentration. One row per material in a procedure, specimen procedure or experimental interface. |

A material usage points at its source: a consumable stock from an inventory, a consumable from the shared catalog, or a manual entry when the material is in neither. Whichever source is used, the usage freezes a snapshot of what the source looked like at that moment, so later edits of the catalog or the stock do not rewrite the record of what was used.

The parent of a material usage is exactly one [procedure]({{"datamodel/modules/procedure/"|absolute_url}}), [specimen procedure]({{"datamodel/modules/specimenprocedure/"|absolute_url}}) or [experimental interface]({{"datamodel/modules/experimentalinterface/"|absolute_url}}). A procedure records what it used; an interface records what it is made of. Which materials a parent type allows, in which roles, which are required and when a row counts as complete is set per type. These rules are listed in the "Materials that can be recorded on this type" tables of the [Procedure types]({{"datamodel/schemas/procedure/"|absolute_url}}), [Specimen procedure types]({{"datamodel/schemas/specimenprocedure/"|absolute_url}}) and [Experimental interface types]({{"datamodel/schemas/experimentalinterface/"|absolute_url}}) schema pages.

## Stages

A [procedure stage]({{"datamodel/modules/procedurestage/"|absolute_url}}) is a phase of a procedure or specimen procedure that several materials take part in together: the induction and maintenance of an anesthetic, the flush and fixation of a perfusion, the baths of a staining protocol. The stage carries the shared conditions once (route, rate, duration, temperature, agitation, cycles), and each material row can name the stage it took part in. Stage types are declared per procedure type.

## Pages in this section

1. [__Material usages__]({{"datamodel/modules/materialusage/"|absolute_url}}): One material in one role from one source, with the values as applied.
2. [__Procedure stages__]({{"datamodel/modules/procedurestage/"|absolute_url}}): Ordered phases of a procedure or specimen procedure that materials take part in.

## Permissions

Material usages inherit permissions from their parent entry (procedure, specimen procedure or experimental interface), and so from the subject or specimen set and its projects. Stages are part of their parent record.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.
