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
The project model is a overall way to group subjects, datasets and collections together. A project can relate to the experiments going into a publication, but works just as well for describing day-to-day experiments or for sharing experimental data with collaborators. 

## Fields

| Field        | Description  |
|:-------------|:-------------|
| Name         | Name of the project (**required**; max length: 200; must be unique)|
| Description  | A rich text description of the project |
| Publications | Related publications |
| Extra fields | Allows you to add extra fields to the project. The values can be a string or a numeric value |
| Public project | Determines if the project is publicly available or only through the private portal |
| Name used in repository | Use this field if you have another name of your project (max length: 200) |
| Tags         | Tags for the project. Tags are great for organizational purpose, to quickly label a project and can be used as a filter afterwards. |


## Permissions
Projects are the overall permissions level. Subjects, Datasets, Collections and module data all inherit permissions through projects. You manage permissions through the management tab, where you can provide individual users and groups access-levels to a project.

Visit the [permissions page] to learn more.

## Project API access
The API allows for programmable access to projects. Learn more about the projects' fields and data structure on the [Project API page]({{"api/stem/project/"|absolute_url}}). 
