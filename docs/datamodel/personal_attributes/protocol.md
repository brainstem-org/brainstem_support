---
layout: default
title: Protocols
parent: Personal attributes
grand_parent: Data model
nav_order: 5
---

# Protocol model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

A protocol is a written method used by your lab, such as a standard operating procedure (SOP), a published protocol, or a lab procedure document. You attach a protocol to work that followed it. A [procedure]({{"datamodel/modules/procedure/"|absolute_url}}), specimen procedure, [subject log]({{"datamodel/modules/subjectlog/"|absolute_url}}), or procedure episode can then point to the method instead of repeating it.

## Protocol type and subtypes

The **protocol type** decides which model can use a protocol. For example, a procedure protocol appears only in procedure selectors. **Subtypes** narrow this within that model: a procedure protocol restricted to Craniotomy appears only for Craniotomy procedures. Leave subtypes empty for a general method.

## Fields

| Field | Description |
|:------|:------------|
| ``Name`` | Name shown in protocol selectors (**required**; string; maximum length: 255 characters). Example: "Craniotomy SOP v3 (2026-01)" |
| ``Protocol type`` | Kind of record the protocol applies to (**required**; choice; maximum length: 32 characters). Options: breeding, procedure, specimen procedure, subject log, specimen log. |
| ``Subtypes`` | Specific types within the protocol type that the protocol covers (multiple selections). Leave empty for a general method. |
| ``Authenticated groups`` | Groups given access to the protocol (multiple selections; set during creation only). |
| ``Description`` | Rich text description of the method. |
| ``URL`` | Link to the published method, such as protocols.io or a journal article (string). |
| ``Attachment`` | Uploaded protocol document (file). Only users who can read the protocol can access it. |
| ``Licenses`` | [Licenses]({{"datamodel/personal_attributes/license/"|absolute_url}}) that authorize this method (multiple selections). |
| ``Public access`` | Designates if the protocol is publicly readable (boolean; default: False). Only owners can modify this setting. |

## Permissions

You manage permissions through the management tab, where you can assign individual users and groups access levels to a protocol. Protocols have four permission levels: membership (read access), contributors, managers, and owners.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to protocols, enabling you to read, create, edit, and delete protocols through the API. Learn more about the fields and data structure on the [Protocols API page]({{"api/personal_attributes/protocol/"|absolute_url}}).
