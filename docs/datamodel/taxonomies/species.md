---
layout: default
title: Species
parent: Taxonomies
grand_parent: Data model
nav_order: 6
---

# Species model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

A biological species is a group of organisms that can reproduce with one another in nature and produce fertile offspring. Species are characterized by reproductive isolation from other groups, meaning organisms in one species are incapable of reproducing with organisms in another species. The term "species" also represents the most basic category in the system of taxonomy, a scientific system that classifies organisms into categories based on their biological characteristics. Additionally, species can be defined based on a shared evolutionary history and ancestry. In BrainSTEM, species is a shared model across users.

## Fields

| Field | Description |
|:------|:------------|
| ``Name of species`` | The scientific name of the species (**required**; string; maximum length: 100 characters; must be unique). Example: "Homo sapiens", "Mus musculus" |
| ``Popular name`` | Common or colloquial name of the species (maximum length: 100 characters). Example: "Human", "House mouse" |
| ``Appearance`` | A description of the physical characteristics of the species (**required**; maximum length: 500 characters). Example: "Small, quadrupedal mammal with fur, whiskers, and a long tail" |
| ``Description`` | A general description of the species, including its biological and ecological attributes (maximum length: 2000 characters). Example: "Small rodent commonly used in laboratory research due to its well-characterized genetics and physiology" |
| ``RRID`` | Research Resource Identifier. Must start with "RRID:". Example: "RRID:NCBI_txid9606" |
| ``External identifiers`` | External identifiers from databases like NCBI, Ensembl, etc.. Include URLs when available. |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

## Submission process

Any user can submit new species entries or propose changes to existing ones. However, all submissions must undergo an approval process before becoming available for use. Please refer to existing entries for examples of appropriate submissions.

## Permissions

Once an entry has been approved, it becomes accessible to all users.

## Species API access

The API provides programmable access to species data, allowing you to read, edit, and delete entries. For more information about the fields and data structure of species entries, please consult the [Species API page]({{"api/taxonomies/species/"|absolute_url}}).
