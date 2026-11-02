---
layout: default
title: Strains
parent: Taxonomies
grand_parent: Data model
nav_order: 2
---

# Strains model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A strain is a genetically defined line within a [species]({{"datamodel/taxonomies/species/"|absolute_url}}): C57BL/6J, Long-Evans, or a canonically named transgenic line. A [subject]({{"datamodel/stem/subject/"|absolute_url}}) stores its species directly and may additionally point at a strain of that species when one applies. In BrainSTEM, strains are a shared model across users.

{% include datamodel_embed.html model="taxonomies.strain" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Name of strain`` | The strain designation as the repository or supplier writes it, substrain suffix included (**required**; string; maximum length: 100 characters; must be unique within the species). The same name may exist for different species. Example: "C57BL/6J", "BALB/c" |
| ``Popular name`` | The everyday name for the line, where it differs from the formal designation (string; maximum length: 100 characters). Example: "Black 6" |
| ``Species`` | The species to which the strain belongs (**required**). Must reference an existing [species]({{"datamodel/taxonomies/species/"|absolute_url}}). |
| ``Breeding`` | How the strain is maintained (**required**): Inbred, Outbred, Wild-type or Unknown. |
| ``RRID`` | Research Resource Identifier, such as an IMSR or MGI identifier (string; maximum length: 100 characters). **Lookup RRID** beside the field fetches the line from the registry and fills in the name, popular name, description, external identifiers and the species. Example: "RRID:IMSR_JAX:000664" |
| ``External identifiers`` | Identifiers in other registries (JAX, EMMA and others), each with source, id and URL. |
| ``Appearance`` | Coat colour and other visible characteristics (maximum length: 500 characters). |
| ``Description`` | A description of the strain's genetic and behavioral attributes (maximum length: 2000 characters). |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

{% include schemas/strain.md %}

## Submission process

Any user can submit new strain entries or propose changes to existing ones. A submission enters the approval queue and is usable in your own records immediately; it is visible only to you until accepted. Use the official nomenclature and the RRID: "C57BL/6" and "C57BL/6J" are different lines. For the approval statuses see the [Resources page]({{"datamodel/resources/#submission-and-approval"|absolute_url}}).

A strain cannot be deleted while subjects point to it.

## Permissions

Everyone can read the accepted list. Editing an accepted strain is restricted; an edit creates a change request that is reviewed before it takes effect. Your own pending submissions remain yours to edit or cancel.

## API access

The API provides programmable access to strain data, returning the accepted list plus your own pending submissions. For more information about the fields and data structure, please consult the [Strains API page]({{"api/taxonomies/strain/"|absolute_url}}).
