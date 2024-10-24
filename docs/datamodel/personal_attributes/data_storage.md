---
layout: default
title: Data storage
parent: Personal attributes
grand_parent: Data model
nav_order: 2
---

# Dataset model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction 

Data storages describe the storage solution for datasets. A data storage can be accessible with multiple protocols. You must also defined how data is organized in the Data storage.

## Dataset fields

| Field                | Description |
|:---------------------|:------------|
| `Name`                 | Name of the data storage (**required**) |
| `Authenticated groups` | Groups that have change permissions for this data storage (**required**) |
| `Description`          | Text description of the data storage |
| `Data organization`    | How data is organized in the data storage. E.g., by Users/Subjects/Datasets; or simpler by Projects/Datasets |
| `Data storage protocols` | Protocols used (local, network, cloud, web, peer-to-peer). Include path and public status for each |

## Permissions

You manage permissions through the management tab, where you can assign individual users and groups access levels to a data storage. Data storage have four permission levels: membership (read access), change permissions, managers, and owners.

Visit the [permissions page] to learn more. 

## Dataset API access

The API allows for programmable access to Data storage, enabling you to read, edit, and delete data storage through the API. Learn more about the datasets' fields and data structure on the [Dataset API page]({{"api/personal_attributes/datastorage/"|absolute_url}}). 
