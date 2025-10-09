---
layout: default
title: Strains
parent: Taxonomies
grand_parent: Data model
nav_order: 5
---

# Strains model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

In biology, a strain is a low-level taxonomic rank below the rank of species. A mouse or rat strain, for example, is a group of animals that is genetically uniform. In BrainSTEM, strains are a shared model across users.

## Fields

| Field | Description |
|:------|:------------|
| ``Name of strain`` | The scientific name of the strain (**required**; string; maximum length: 100 characters; must be unique). Example: "C57BL/6J", "BALB/c", "129S1/SvImJ" |
| ``Popular name`` | Common or colloquial name of the strain (optional; maximum length: 100 characters). Example: "Black 6", "BALB/c" |
| ``Appearance`` | A description of the physical characteristics of the strain (optional; maximum length: 500 characters). Example: "Black coat color, robust build, white belly" |
| ``Description`` | A general description of the strain, including its genetic and behavioral attributes (optional; maximum length: 2000 characters). Example: "Inbred strain widely used in behavioral and physiological research due to well-characterized genome" |
| ``Species`` | The species to which the strain belongs (**required**). Must reference an existing [species]({{"datamodel/taxonomies/species/"|absolute_url}}). Example: "House mouse" |
| ``Breeding`` | Breeding status of the strain (**required**). Selected from predefined options: Inbred, Outbred, Wild-type, or Unknown |
| ``RRID`` | Research Resource Identifier (optional). Must start with "RRID:". Example: "RRID:Addgene_12345" |
| ``External identifiers`` | External identifiers from databases like JAX, EMMA, etc. (optional). Include URLs when available. |
| ``Adding/editing comments`` | Comments for the submission/approval process (optional). |

## Submission process

Any user can submit new strain entries or propose changes to existing ones. However, all submissions must undergo an approval process before becoming available for use. Please refer to existing entries for examples of appropriate submissions.

## Permissions

Once an entry has been approved, it becomes accessible to all users.

## Strains API access

The API provides programmable access to strain data, allowing you to read, edit, and delete entries. For more information about the fields and data structure of strain entries, please consult the [Strains API page]({{"api/taxonomies/strain/"|absolute_url}}).