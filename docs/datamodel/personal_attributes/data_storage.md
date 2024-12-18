---
layout: default
title: Data storage
parent: Personal attributes
grand_parent: Data model
nav_order: 2
---

# Data storage model
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
| `Name`                 | Name of the data storage (**required**; string; maximum length: 100 characters). Example: "Lab Server 01" |
| `Authenticated groups` | Groups that have change permissions for this data storage (**required**). Example: "Lab B Data Team" |
| `Description`          | Rich text description of the data storage. Can include uploaded images. Example: "Primary data storage server for electrophysiology recordings..." |
| `Data organization`    | How data is organized in the data storage. Example: "Projects/Subjects/Sessions/Data" |
| `Data storage protocols` | Protocols used (local, network, cloud, web, peer-to-peer). Include path and public status for each. Example: "Network: smb://labserver/data, Private access" |

## Permissions

You manage permissions through the management tab, where you can assign individual users and groups access levels to a data storage. Data storage have four permission levels: membership (read access), contributors, managers, and owners.

Visit the [permissions page]({{"datamodel/permission/"|absolute_url}}) to learn more. 

## Dataset API access

The API allows for programmable access to Data storage, enabling you to read, edit, and delete data storage through the API. Learn more about the datasets' fields and data structure on the [Dataset API page]({{"api/personal_attributes/datastorage/"|absolute_url}}). 
