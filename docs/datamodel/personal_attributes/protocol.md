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

A protocol is a reusable written method used by your lab, such as a standard operating procedure (SOP), a published protocol, or a lab procedure document. A [procedure]({{"datamodel/modules/procedure/"|absolute_url}}), [subject log]({{"datamodel/modules/subjectlog/"|absolute_url}}), or procedure episode can reference the method instead of repeating it. Procedure templates and procedure episode templates can also reference protocols.

A protocol describes **how work is performed**. A [license]({{"datamodel/personal_attributes/license/"|absolute_url}}) records the authorization for that work; you can link the relevant licenses to the protocol. [Behavioral assays]({{"datamodel/personal_attributes/behavioralassay/"|absolute_url}}) describe behavioral tasks used in session behavior records.

## Protocol type and subtypes

The **protocol type** determines where a protocol can be used:

| Protocol type | API value | Used by |
|:--------------|:----------|:--------|
| Procedure | `procedure` | Procedures, procedure templates, procedure episodes, and procedure episode templates |
| Subject log | `subject_log` | Subject logs |

**Subtypes** optionally restrict a protocol to one or more [procedure types]({{"datamodel/schemas/procedure/"|absolute_url}}) or [subject-log types]({{"datamodel/schemas/subjectlog/"|absolute_url}}). For example, a procedure protocol restricted to Craniotomy is available for Craniotomy procedures. A subject-log protocol restricted to Handling is available for Handling logs. Leave subtypes empty to allow any subtype within the selected protocol type.

Procedure and subject-log selectors include protocols you can read, including public protocols, and filter them by type and subtype. Selecting a protocol does not copy its method into the record; record the actual work and any deviations in the procedure or log itself.

## Fields

| Field | Description |
|:------|:------------|
| ``Name`` | Name shown in protocol selectors (**required**; string; maximum length: 255 characters). Example: "Craniotomy SOP v3 (2026-01)" |
| ``Protocol type`` | Kind of record the protocol applies to (**required**; choice; maximum length: 32 characters). Options: Procedure, Subject log. |
| ``Subtypes`` | Specific types within the protocol type that the protocol covers (multiple selections). Leave empty for a general method. |
| ``Authenticated groups`` | Groups given contributor permissions when creating the protocol (multiple selections from your groups). Manage subsequent access through the Manage tab. |
| ``Description`` | Rich text description of the method. |
| ``URL`` | Optional link to the published method, such as protocols.io or a journal article (URL; maximum length: 200 characters). |
| ``Attachment`` | Optional protocol document: PDF, DOCX, XLSX, PPTX, ODT, CSV, Markdown (`.md`), or plain text (`.txt`), up to 15 MB. Downloads use signed URLs. |
| ``Licenses`` | [Licenses]({{"datamodel/personal_attributes/license/"|absolute_url}}) that authorize this method (multiple selections). Adding a license requires contributor (`change_license`) permission on that license. |
| ``Public access`` | Designates if the protocol is publicly readable (boolean; default: False). Only owners can modify this setting. |

## Creating and using a protocol

1. Go to **Personal Attributes → Protocols** and add a protocol.
2. Enter a descriptive name and choose **Procedure** or **Subject log**. Select the groups that need access, then create the record.
3. Edit the protocol to add subtypes, a description, a URL or attachment, and any authorizing licenses.
4. Open a procedure or subject log of the matching type and select the protocol in its **Protocol** field.

For example, create "Handling SOP v2" with protocol type **Subject log** and subtype **Handling**. Each subject's Handling log can reference that protocol while keeping its own dated entries and observations.

## Permissions

Protocols have their own permissions, independent of the projects that reference them. The creator becomes an owner, and groups selected during creation receive contributor permissions. Use the **Manage** tab to assign access to users and groups.

| Permission level | Capabilities |
|:-----------------|:-------------|
| Member | Read the protocol. |
| Contributor | Read access and the protocol's contributor permission; editing protocol details still requires ownership. |
| Manager | Manage members and contributor access. |
| Owner | Edit or delete the protocol, change public access, and assign managers or owners. |

Making a project public does not make its protocols public. An owner must enable **Public access** on each protocol separately. Public protocols and their attachment download links are available through the public portal and API. Linked licenses retain their own sharing settings.

A protocol referenced by a procedure, subject log, procedure episode, or their templates cannot be deleted until those references are removed or reassigned.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to protocols, enabling you to read, create, edit, and delete protocols through the API. Learn more about the fields and data structure on the [Protocols API page]({{"api/personal_attributes/protocol/"|absolute_url}}).
