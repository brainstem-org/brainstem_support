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
| `Name` | The scientific name of the strain (**required**; must be unique) |
| `Popular name` | Common or colloquial name of the strain |
| `Appearance` | A description of the physical characteristics of the strain |
| `Description` | A general description of the strain, including its genetic and behavioral attributes |
| `Species` | The species to which the strain belongs (**required**) |
| `Breeding` | Breeding status of the strain (**required**). Options: Inbred, Outbred, Wild-type, or Unknown |

## Submission process

Any user can submit new strain entries or propose changes to existing ones. However, all submissions must undergo an approval process before becoming available for use. Please refer to existing entries for examples of appropriate submissions.

## Permissions

Once an entry has been approved, it becomes accessible to all users.

## Strains API access

The API provides programmable access to strain data, allowing you to read, edit, and delete entries. For more information about the fields and data structure of strain entries, please consult the [Strains API page]({{"api/taxonomies/strain/"|absolute_url}}).