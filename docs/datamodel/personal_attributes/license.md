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

1. TOC
{:toc}

## Introduction

Licenses track regulatory and compliance authorizations used by your lab, such as animal research approvals, biosafety permissions, controlled substance licenses, and import/export permits.

## Fields

| Field | Description |
|:------|:------------|
| ``Name`` | Name/title of the license (**required**). Example: "PPL: Septo-hippocampal dynamics 2025-2028" |
| ``License type`` | Type of authorization or license (**required**). Selected from predefined license types. |
| ``Status`` | Current lifecycle state of the license (**required**; default: draft). `Active` requires both validity dates; `Expired` is only valid after the expiration date has passed. |
| ``License number`` | Official identifier shown on the approval document. |
| ``License holders`` | Named users associated with the license. |
| ``Description`` | Rich text description of the license scope and purpose. |
| ``Country`` | Country where the license was issued. |
| ``Regulatory authority`` | Regulatory authority that issued the license . Must reference an existing [regulatory authority]({{"datamodel/taxonomies/regulatoryauthority/"|absolute_url}}). |
| ``Valid from`` | Date when the license becomes valid (optional; format: YYYY-MM-DD). |
| ``Valid until`` | Date when the license expires (optional; format: YYYY-MM-DD). Must be on or after `Valid from` when both dates are provided. |
| ``License document`` | Uploaded approval file (optional; PDF recommended). |
| ``Authenticated groups`` | Groups assigned to this license for collaboration and permissions (**required** during creation). |

## Permissions

Licenses follow personal-attribute permission patterns with group-based access and ownership management.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.
