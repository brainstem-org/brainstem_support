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

| Field  | Type  | Description |
|:-------|:--------|-------------|
| `id` | string with UUID identificator | Id of the entry |
| `name` | string **[required]** [max length: 100; must be unique across datasets ]| Name of dataset |
| `description` | string | A rich text description of the dataset |
| `projects` | FK | any projects the dataset belongs to. Learn more about the project inheritance [here]. |
| `date_time` | YYYY-MM-DD string containing date (e.g. "2023-03-22") | Date and time of the onset of the dataset |
| `epochs` | FK | List of epochs associated with the dataset |
| `datarepositories` | FK | Data repositories |
| `extra_content_json` | JSON dictionary | |
| `repository_links_json` | JSON dictionary | name value pairs allowing you to add extra content |
| `experimentdata` | FK | associated experiment data|
| `behaviors` | FK | associated behaviors |
| `manipulations` | FK | associated manipulations|
| `name_used_in_repository` | string [max length: 200]| Custom name for a dataset used in an organization in a repository.  |
| `tags` | list of strings | any tags for the dataset |


### Epoch fields

| Field  | Type  | Description |
|:-------|:--------|-------------|
| `id` | string with UUID identificator | Id of the entry |
| `name` | string **[required]** [max length: 100; must be unique across datasets ]| Name of dataset |
| `description` | string | A rich text description of the dataset |
| `projects` | FK | any projects the dataset belongs to. Learn more about the project inheritance [here]. |
| `date_time` | YYYY-MM-DD string containing date (e.g. "2023-03-22") | Date and time of the onset of the dataset |

## Permissions
The dataset inherits permissions from projects associated with it. Data repositories are shared through the projects groups, and you are only able to add a data repository associated with the same groups as the selected projects. The relationships in module data also depends on the selected projects

 Visit the permissions page to learn more. 