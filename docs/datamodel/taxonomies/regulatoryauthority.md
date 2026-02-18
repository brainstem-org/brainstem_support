---
layout: default
title: Regulatory authorities
parent: Taxonomies
grand_parent: Data model
nav_order: 4
---

# Regulatory authority model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Regulatory authorities are organizations that issue and oversee research approvals, licenses, and compliance requirements. In BrainSTEM, this taxonomy helps standardize authority names used across regulatory records.

## Fields

| Field | Description |
|:------|:------------|
| ``Name of regulatory authority`` | Official name of the authority (**required**). Example: "Institutional Animal Care and Use Committee" |
| ``Abbreviation`` | Short name or acronym used for the authority. Example: "IACUC" |
| ``Authority type`` | Type/category of authority. Example: "Animal ethics", "Biosafety", "Drug control", "Import/export" |
| ``Country`` | Country where the authority operates or issues approvals. |
| ``Website`` | Official website URL of the authority. |
| ``Description`` | Description of the authority scope and role in compliance oversight. |

## Submission process

Anyone can submit new regulatory authorities or propose changes to existing ones. All submissions require approval before becoming available.

## Permissions

Once an entry has been approved, it becomes available to everyone.

## Regulatory authority API access

The API allows for programmable access, enabling you to read and edit entries. For more information about fields and data structure, please consult the [Regulatory authority API page]({{"api/taxonomies/regulatoryauthority/"|absolute_url}}).
