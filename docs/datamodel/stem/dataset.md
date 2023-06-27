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

## Introduction 
A dataset is a modular construction that flexibly can describe varius aspect of experiments based on four basic modules: 
1. Experiment data: Description of the data collected during the experiment
2. Manipulations: Description of any manipulations performed during an expriment
3. Behavior: Description of the behavior of the animal subject. 
4. Epochs: Temporal aspects of the dataset

## Fields

| Field  | Description |
|:-------|:------------|
| `name` | Name of the dataset ( **required**; string; max length: 100; must be unique across datasets)|  |
| `description` | A rich text description of the dataset |
| `projects` | Any projects the dataset belongs to. Learn more about the project inheritance [here]. |
| `date_time` | Date and time of the onset of the dataset (YYYY-MM-DD string containing date, e.g. "2023-03-22")|
| `epochs` | List of epochs associated with the dataset |
| `datarepositories` | Data repositories |
| `extra fields` | Allows you to add a |
| `download_links` | JSON dictionary | name value pairs allowing you to add extra content |
| `experimentdata` | FK | associated experiment data|
| `behaviors` | FK | associated behaviors |
| `manipulations` | FK | associated manipulations|
| `name_used_in_repository` | string [max length: 200]| Custom name for a dataset used in an organization in a repository.  |
| `tags` | any tags for the dataset. Tags are great for organizational purpose, to quickly label a dataset and can be used as a filter afterwards. |


### Epoch fields

| Field  | Description |
|:-------|:------------|
| `name` | Name of the epoch (**[required]**; a string; max length: 100) |
| `start` | Start time of the epochs. The start time is relative to the onset of the dataset (the date and time field of the dataset) |
| `end` | End time of the epochs. The start time is relative to the onset of the dataset (the date and time field of the dataset) |
| `projects` | FK | any projects the dataset belongs to. Learn more about the project inheritance [here]. |
| `date_time` | YYYY-MM-DD string containing date (e.g. "2023-03-22") | Date and time of the onset of the dataset |

## Permissions
The dataset inherits permissions from projects associated with it. Data repositories are shared through the projects groups, and you are only able to add a data repository associated with the same groups as the selected projects. The relationships in module data also depends on the selected projects

 Visit the permissions page to learn more. 

### Dataset API access
The API allows for programmable access to datasets. Learn more about the datasets field and data structure on the [Dataset API page]. 