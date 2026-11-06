---
layout: default
title: Regulatory authorities
parent: Taxonomies
grand_parent: Data model
nav_order: 9
---

# Regulatory authority model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

Regulatory authorities are organizations that issue and oversee research approvals, licenses, and compliance requirements. In BrainSTEM, this taxonomy helps standardize authority names used across regulatory records.

{% include datamodel_embed.html model="taxonomies.regulatoryauthority" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Name of regulatory authority`` | Official name of the authority (**required**; string; maximum length: 255 characters; must be unique). Example: "Institutional Animal Care and Use Committee" |
| ``Abbreviation`` | Short name or acronym used for the authority (string; maximum length: 32 characters). Example: "IACUC" |
| ``Authority type`` | Type of authority. Selected from predefined types: National regulatory body, Institutional committee, Regional/state authority, International organization. |
| ``Country`` | Country where the authority operates or issues approvals. Selected from ISO country options. |
| ``Website`` | Official website URL of the authority (URL; maximum length: 200 characters). |
| ``Description`` | Description of the authority scope and role in compliance oversight (text). |
| ``Active`` | Designates whether this authority is currently operational (boolean; default: True). Turn it off rather than deleting when an authority is dissolved or renamed, so historical licenses keep pointing at the body that issued them. |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

## Submission process

Anyone can submit new regulatory authorities or propose changes to existing ones. A submission enters the approval queue and is usable in your own records immediately; it is visible only to you until accepted. An authority cannot be deleted while licenses point to it.

## Permissions

Once an entry has been approved, it becomes available to everyone. Editing an accepted entry is restricted; an edit creates a change request that is reviewed before it takes effect. Your own pending submissions remain yours to edit or cancel.

## API access

The API allows for programmable access, enabling you to read and edit entries. For more information about fields and data structure, please consult the [Regulatory authority API page]({{"api/taxonomies/regulatoryauthority/"|absolute_url}}).
