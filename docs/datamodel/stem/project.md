---
layout: default
title: Project
parent: STEM
grand_parent: Data model
nav_order: 1
---

# Project model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction
Projects serve as an overall way to group subjects, datasets, and collections together. A project can be used to relate experiments for publications, as well as to describe day-to-day experiments or sharing experimental data with collaborators. Projects define the overall permissions level of most other content.

## Fields

| Field        | Description  |
|:-------------|:-------------|
| Name         | Name of the project (**required**; string; maximum length: 200 characters; must be unique)|
| Description  | A text description of the project. You can upload and insert images.  |
| Publications | Related publications |
| Extra fields | Allows you to add extra fields to the project. The values can be a string or a numeric value |
| Public project | Determines if the project is publicly available or only through the private portal (boolean value). |
| Name used in repository | Use this field if you have another name of your project (string; maximum length: 200 characters) |
| Tags         | Tags for the project. Tags are great for organizational purpose, to quickly label a project and can be used as a filter afterwards. |


## Permissions
Projects define the overall permissions level for subjects, datasets, collections, and modules. You manage permissions through the management tab, where you can assign individual users and groups access levels to a project. Projects have four permission levels: membership (read access), change permissions, managers, and owners. For more information on permissions, please visit the permissions page.

Visit the [permissions page] to learn more.

## Project API access
The API allows for programmable access to projects. Learn more about the projects' fields and data structure on the [Project API page]({{"api/stem/project/"|absolute_url}}). 
