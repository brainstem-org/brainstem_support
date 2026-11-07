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

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction 

A data storage describes where session data physically live and how to reach them: a lab server, a NAS, a cloud bucket, an archive. [Sessions]({{"datamodel/stem/session/"|absolute_url}}) link to one or more data storages, which turns a record in BrainSTEM into a route to the actual files. Three things have to line up: the storage itself, the **data organization** describing how folders are nested, and the **name used in storage** recorded on the project, subject or session when it differs from the name shown there. A storage can be reachable by more than one protocol, each with its own path.

{% include datamodel_embed.html model="personal_attributes.datastorage" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Data storage name`` | Name of the data storage (**required**; string; maximum length: 100 characters; must be unique). Example: "Lab Server 01" |
| ``Location`` | Location of the data storage (string; maximum length: 100 characters). Example: "Cabinet A", "Computer B", "Network storage C" |
| ``Description`` | Rich text description of the data storage. Can include uploaded images. Example: "Primary data storage server for electrophysiology recordings..." |
| ``Data organization`` | How folders are nested inside the storage, as structured JSON, from top level to most specific. Example: "Projects → Subjects → Sessions". [Schema](https://www.brainstem.org/schemas/DataStorage/data_organization.json) |
| ``Data protocols`` | How the storage is reached, as a JSON list. Each entry has a protocol type (Local Storage, SMB/CIFS, NFS, AFP, SFTP, FTP, HTTPS/Web, Globus, S3, Dropbox, Google Drive, OneDrive and others), a path and whether that route is publicly reachable. Example: "SMB/CIFS: smb://labserver/data, private". [Schema](https://www.brainstem.org/schemas/DataStorage/data_protocols.json) |
| ``Authenticated groups`` | Groups given access when the data storage is created (create only). After creation, access is managed from the storage's own page, where individual people can also be invited. |
| ``Public access`` | Whether the data storage is shown on the public portal. It has no switch of its own: saving the storage makes it public when at least one of its data protocols is marked public, and private otherwise. Public access publishes the description of where data live, including the public protocols' paths; it does not make the data themselves reachable. Only owners can change the data protocols. |

{: .important }
Marking a single data protocol public makes the whole data storage public when you save it, and that protocol's path is shown as a download source on the public sessions stored there. Mark only the routes outside readers should see.

## Permissions

You manage permissions through the management tab, where you assign individual users and groups one of four roles: Member (read), Contributor (can select the storage on a session), Manager (also manages access) and Owner (also edits the storage's own fields and deletes it). Data storages are shared with people and groups, never through a project.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to Data storage, enabling you to read, edit, and delete data storage through the API. Learn more about the data storages' fields and data structure on the [Data storage API page]({{"api/personal_attributes/datastorage/"|absolute_url}}). 
