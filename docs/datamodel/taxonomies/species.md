---
layout: default
title: Species
parent: Taxonomies
grand_parent: Data model
nav_order: 4
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
| `Name` | The scientific name of the species (**required**; must be unique) |
| `Popular name` | Common or colloquial name of the species |
| `Appearance` | A description of the physical characteristics of the species |
| `Description` | A general description of the species, including its biological and ecological attributes |

## Submission process

Any user can submit new species entries or propose changes to existing ones. However, all submissions must undergo an approval process before becoming available for use. Please refer to existing entries for examples of appropriate submissions.

## Permissions

Once an entry has been approved, it becomes accessible to all users.

## Species API access

The API provides programmable access to species data, allowing you to read, edit, and delete entries. For more information about the fields and data structure of species entries, please consult the [Species API page]({{"api/taxonomies/species/"|absolute_url}}).
