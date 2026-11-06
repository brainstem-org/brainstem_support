---
layout: default
title: Licenses
parent: Personal attributes
grand_parent: Data model
nav_order: 4
---

# License model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A license is a regulatory authorization that permits work: an animal research license, an ethics approval, a biosafety authorization, a controlled-substance license. Attaching it to a [subject]({{"datamodel/stem/subject/"|absolute_url}}), a [procedure]({{"datamodel/modules/procedure/"|absolute_url}}), a [procedure episode]({{"datamodel/modules/procedureepisode/"|absolute_url}}), a [specimen procedure]({{"datamodel/modules/specimenprocedure/"|absolute_url}}), a [behavioral assay]({{"datamodel/personal_attributes/behavioralassay/"|absolute_url}}) or a [protocol]({{"datamodel/personal_attributes/protocol/"|absolute_url}}) records the legal basis for that work.

A license records what you are permitted to do and until when. It does not check anything: BrainSTEM will not stop you recording a procedure under an expired license. Keep the status and validity dates current.

{% include datamodel_embed.html model="personal_attributes.license" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Name`` | Name or title of the license (**required**; string; maximum length: 255 characters). Example: "PPL: Septo-hippocampal dynamics 2025-2028" |
| ``License type`` | Type of authorization (**required**). Choices: Animal Research Authorization, Human Research Authorization, Biosafety / GMO Authorization, Wildlife / Fieldwork Permit, Controlled Substance License, Chemical Use Authorization, Import/Export Permit. |
| ``Status`` | Lifecycle state (**required**; default: Draft). Choices: Draft, Pending Review/Issue, Active, Suspended, Expired, Revoked. `Active` requires both validity dates; `Expired` is only valid after the expiration date has passed. |
| ``Country`` | Country where the license was issued (ISO country code). |
| ``Regulatory authority`` | Authority that issued the license. Must reference an existing [regulatory authority]({{"datamodel/taxonomies/regulatoryauthority/"|absolute_url}}); submit missing authorities in the taxonomies section. |
| ``License number`` | Official identifier on the approval document (string; maximum length: 128 characters). |
| ``License document`` | The official license document as a PDF (10 MB maximum). |
| ``Valid from`` | Date when the license becomes valid (format: YYYY-MM-DD). |
| ``Valid until`` | Date when the license expires (format: YYYY-MM-DD). Must be on or after `Valid from` when both dates are provided. |
| ``License holders`` | Named users associated with the license, such as PIs and authorized personnel. |
| ``Description`` | Rich text description of the license scope and purpose. |
| ``Authenticated groups`` | Groups given access when the license is created (create only). After creation, access is managed from the license's own page, where individual people can also be invited. |
| ``Public access`` | Designates if the license information is publicly available (boolean; default: False). Only owners can modify this setting. |

The license page lists the subjects, procedures and behavioral assays that reference it.

## License types

- **Animal research authorization**: the permit covering work on animals (a Home Office project license, an IACUC protocol approval or the national equivalent). This is the one most procedures reference.
- **Human research authorization**: ethics approval for work involving human participants or human-derived material.
- **Biosafety / GMO authorization**: approval for work with genetically modified organisms or at a defined containment level. Viral vector work usually needs this in addition to an animal license.
- **Wildlife / fieldwork permit**: permission to capture, sample or work with wild animals in the field.
- **Controlled substance license**: authorization to hold and use scheduled drugs, such as controlled anesthetics and analgesics.
- **Chemical use authorization**: approval for hazardous chemicals that are not controlled substances.
- **Import / export permit**: permission to move animals, tissue or regulated material across a border.

## Permissions

Licenses are shared with individual people or whole groups, never through a project. Members can see the license. Contributors can attach it to experimental work; reading a colleague's license is not enough to claim your work runs under it. Managers also manage access. Owners also edit the license's own fields and delete it. A license already recorded on an older entry stays visible when you edit that entry.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to licenses, enabling you to read, create, edit, and delete licenses through the API. Learn more about the fields and data structure on the [License API page]({{"api/personal_attributes/license/"|absolute_url}}).
