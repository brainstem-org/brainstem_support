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
| Name        | Name of the collection (**required**; string; max length: 100; must be unique within the project) |
| Project     | The project the collection belongs to (**required**) |
| Datasets    | Datasets of the collection. All datasets must belong to the same project (**required**) |
| Description | A text description of the collection, which helps in providing additional context and information. Pictures can be uploaded and inserted. |
| Tags        | Tags for the collection. Tags are great for organizational purpose, to quickly label a collection and can be used as a filter afterwards. |

## Permissions
Collections inherit permissions from the associated project. You can only add datasets to the collection that is part of the same project.

## Collection API access
The API allows for programmable access to collections. Learn more about the collections' fields and data structure on the [Collection API page]({{"api/stem/collection/"|absolute_url}}). 
