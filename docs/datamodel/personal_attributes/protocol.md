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

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A protocol is a reusable written method used by your lab, such as a standard operating procedure (SOP), a published protocol, or a lab procedure document. A [procedure]({{"datamodel/modules/procedure/"|absolute_url}}), [specimen procedure]({{"datamodel/modules/specimenprocedure/"|absolute_url}}), [subject log]({{"datamodel/modules/subjectlog/"|absolute_url}}), [specimen log]({{"datamodel/modules/specimenlog/"|absolute_url}}) or [procedure episode]({{"datamodel/modules/procedureepisode/"|absolute_url}}) can reference the method instead of repeating it. Procedure, specimen procedure and procedure episode [templates]({{"datamodel/modules/templates/"|absolute_url}}) can also reference protocols.

A protocol describes **how work is performed**. It is a reference, not a template: selecting a protocol does not fill in any fields of the record. When you want values to be reused, use a template; a record can have both. A [license]({{"datamodel/personal_attributes/license/"|absolute_url}}) records the authorization for the work; you can link the relevant licenses to the protocol.

{% include datamodel_embed.html model="personal_attributes.protocol" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Name`` | Name shown in protocol selectors (**required**; string; maximum length: 255 characters). Include a version or date if you maintain several revisions. Example: "Craniotomy SOP v3 (2026-01)" |
| ``Protocol type`` | Kind of record the protocol applies to (**required**). Options: Breeding, Procedure, Specimen procedure, Subject log, Specimen log. |
| ``Subtypes`` | Specific types within the protocol type that the protocol covers (multiple selections). Leave empty for a general method. |
| ``Authenticated groups`` | Groups given access when the protocol is created (create only). Manage subsequent access from the protocol's own page, where individual people can also be invited. |
| ``Description`` | Rich text description of the method. |
| ``URL`` | Optional link to the published method, such as protocols.io or a journal article (URL; maximum length: 200 characters). |
| ``Attachment`` | Optional protocol document: PDF, DOCX, XLSX, PPTX, ODT, CSV, Markdown (`.md`), or plain text (`.txt`), up to 15 MB. Downloads use signed URLs. |
| ``Licenses`` | [Licenses]({{"datamodel/personal_attributes/license/"|absolute_url}}) that authorize this method (multiple selections). Adding a license requires Contributor on that license. |
| ``Public access`` | Designates if the protocol is publicly readable (boolean; default: False). Only owners can modify this setting. |

## Protocol type and subtypes

The **protocol type** determines where a protocol can be used:

| Protocol type | API value | Used by | Subtypes drawn from |
|:--------------|:----------|:--------|:--------------------|
| Breeding | `breeding` | Reserved for breeding protocols. Breedings do not yet have a protocol field. | None |
| Procedure | `procedure` | Procedures, procedure templates, procedure episodes and procedure episode templates | [Procedure types]({{"datamodel/schemas/procedure/"|absolute_url}}) |
| Specimen procedure | `specimen_procedure` | Specimen procedures and specimen procedure templates | [Specimen procedure types]({{"datamodel/schemas/specimenprocedure/"|absolute_url}}) |
| Subject log | `subject_log` | Subject logs | [Subject log types]({{"datamodel/schemas/subjectlog/"|absolute_url}}) |
| Specimen log | `specimen_log` | Specimen logs | [Specimen log types]({{"datamodel/schemas/specimenlog/"|absolute_url}}) |

**Subtypes** optionally restrict a protocol to one or more types within the protocol type. A procedure protocol restricted to Craniotomy appears only when the procedure type is Craniotomy; one with no subtypes appears for every procedure type. Leave subtypes empty for a general method.

Selectors offer only protocols where you are at least a Contributor, filtered by type and subtype. Being able to read a colleague's protocol is not enough to assert that your work followed it. Record the actual work and any deviations in the procedure or log itself.

## Creating and using a protocol

1. Go to **Personal Attributes → Protocols** and add a protocol.
2. Enter a descriptive name and choose the protocol type. Select the groups that need access, then create the record.
3. Edit the protocol to add subtypes, a description, a URL or attachment, and any authorizing licenses.
4. Open a record of the matching type and select the protocol in its **Protocol** field.

For example, create "Handling SOP v2" with protocol type **Subject log** and subtype **Handling**. Each subject's Handling log can reference that protocol while keeping its own dated entries and observations.

## Permissions

Protocols have their own permissions, independent of the projects that reference them. The creator becomes an owner, and groups selected during creation receive access. Use the **Manage** tab to assign access to users and groups.

| Role | Capabilities |
|:-----|:-------------|
| Member | Read the protocol. |
| Contributor | Select the protocol on an experimental record. Does not allow editing the protocol itself. |
| Manager | Also manage members and access. |
| Owner | Also edit or delete the protocol, change public access, and assign managers or owners. |

Making a project public does not make its protocols public. An owner must enable **Public access** on each protocol separately. Public protocols and their attachment download links are available through the public portal and API. Linked licenses keep their own sharing settings.

A protocol referenced by a procedure, procedure episode, subject log, or their templates cannot be deleted until those references are removed or reassigned. Deleting a protocol clears the link on specimen procedures, specimen procedure templates and specimen logs.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to protocols, enabling you to read, create, edit, and delete protocols through the API. Learn more about the fields and data structure on the [Protocols API page]({{"api/personal_attributes/protocol/"|absolute_url}}).
