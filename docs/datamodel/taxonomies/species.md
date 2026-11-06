---
layout: default
title: Species
parent: Taxonomies
grand_parent: Data model
nav_order: 1
---

# Species model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A species is one animal species available across BrainSTEM. It sits above [strain]({{"datamodel/taxonomies/strain/"|absolute_url}}): every strain belongs to a species. Every [subject]({{"datamodel/stem/subject/"|absolute_url}}) stores its species directly and may optionally select a strain from that species. [Anatomical references]({{"datamodel/taxonomies/anatomicalreference/"|absolute_url}}) (atlases) also name their species. In BrainSTEM, species is a shared model across users.

{% include datamodel_embed.html model="taxonomies.species" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Name of species`` | The scientific binomial (**required**; string; maximum length: 100 characters; must be unique across BrainSTEM). Example: "Mus musculus", "Homo sapiens" |
| ``Popular name`` | The everyday name (string; maximum length: 100 characters). Worth filling in, because it is how most people search. Example: "House mouse" |
| ``RRID`` | Research Resource Identifier (string; maximum length: 100 characters). **Lookup RRID** beside the field fetches the organism from the registry and fills in the name, popular name, description and external identifiers. Example: "RRID:NCBITaxon_10090" |
| ``External identifiers`` | Identifiers in other registries, such as an NCBI taxonomy ID, each with source, id and URL. |
| ``Appearance`` | Distinguishing physical characteristics, useful where related species are easily confused (maximum length: 500 characters). |
| ``Description`` | What the species is and why it is used in research (maximum length: 2000 characters). Write for someone in another lab. |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

{% include schemas/species.md %}

## Submission process

Any user can submit new species entries or propose changes to existing ones. A submission enters the approval queue and is usable in your own records immediately; it is visible only to you until accepted. Check the list under both the scientific and the common name before submitting. For the approval statuses see the [Resources page]({{"datamodel/resources/#submission-and-approval"|absolute_url}}).

A species cannot be deleted while strains, subjects or anatomical references point to it.

## Permissions

Everyone can read the accepted list. Editing an accepted species is restricted; an edit creates a change request that is reviewed before it takes effect. Your own pending submissions remain yours to edit or cancel.

## API access

The API provides programmable access to species data, returning the accepted list plus your own pending submissions. For more information about the fields and data structure, please consult the [Species API page]({{"api/taxonomies/species/"|absolute_url}}).
