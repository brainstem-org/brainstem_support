---
layout: default
title: Collection
parent: STEM
grand_parent: Data model
nav_order: 4
---

# Collection model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction
Collections allows for creating subgroups of datasets within a project. This can be used to define a set of datasets going into a specific analysis or figure. The datasets must all belong to the same project.

## Fields

| Field       | Description  |
|:------------|:-------------|
| Name        | Name of the collection (**required**; max length: 100; must be unique within the project) |
| Description | A rich text description of the collection |
| Project     | The project the collection belongs to (**required**) |
| Datasets    | Datasets of the collection. All datasets must belong to the same project (**required**) |
| Tags        | Tags for the collection. Tags are great for organizational purpose, to quickly label a collection and can be used as a filter afterwards. |

## Permissions
A collection inherit permissions from the project associated with it.

Visit the [permissions page] to learn more. 

## Collection API access
The API allows for programmable access to collections. Learn more about the collections' fields and data structure on the [Collection API page]({{"api/stem/collection/"|absolute_url}}). 
