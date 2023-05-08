---
layout: default
title: Dataset
parent: STEM
grand_parent: Data model
nav_order: 3
---

# Dataset
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field  | Type  | Description |
|:-------|:--------|-------------|
| `id` | string with UUID identificator | Id of the entry |
| `name` | string **[required]** [max length: 100; must be unique]|  |
| `description` | string |
| `projects` | FK | any projects the dataset belongs to |
| `date_time` | YYYY-MM-DD string containing date (e.g. "2023-03-22") | Date and time of the onset of the dataset |
| `epochs` | FK | List of epochs associated with the dataset |
| `datarepositories` | FK | Data repositories |
| `extra_content_json` | JSON dictionary | |
| `repository_links_json` | JSON dictionary | |
| `experimentdata` | FK | associated experiment data|
| `behaviors` | FK | associated behaviors |
| `manipulations` | FK | associated manipulations|
| `name_used_in_repository` | string [max length: 200]| Custom name for a dataset used in an organization in a repository.  |
| `tags` | list of strings | any tags for the dataset |

