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

Data storages describe the storage solution for sessions. A data storage can be accessible with multiple protocols. You must also defined how data is organized in the Data storage.

## Fields

| Field | Description |
|:------|:------------|
| ``Data storage name`` | Name of the data storage (**required**; string; maximum length: 100 characters; must be unique). Example: "Lab Server 01" |
| ``Location`` | Location of the data storage (string; maximum length: 100 characters). Example: "Cabinet A", "Computer B", "Network storage C" |
| ``Description`` | Rich text description of the data storage. Can include uploaded images. Example: "Primary data storage server for electrophysiology recordings..." |
| ``Data organization`` | How data is organized in the data storage in JSON format. Example: "Projects → Subjects → Sessions" |
| ``Data protocols`` | Protocols used for data access in JSON format. Include path and public status for each protocol type (local, network, cloud, web, peer-to-peer). Example: "Network: smb://labserver/data, Private access" |
| ``Authenticated groups`` | Groups that have change permissions for this data storage (**required**). Example: "Lab B Data Team" |
| ``Public access`` | Designates if the data storage is publicly available (boolean; default: False). Must be enabled for data storages linked to public projects. Only owners can modify this setting. |

## Permissions

You manage permissions through the management tab, where you can assign individual users and groups access levels to a data storage. Data storage have four permission levels: membership (read access), contributors, managers, and owners.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to Data storage, enabling you to read, edit, and delete data storage through the API. Learn more about the sessions' fields and data structure on the [Data storage API page]({{"api/personal_attributes/datastorage/"|absolute_url}}). 
