---
layout: default
title: Suppliers
parent: Resources
grand_parent: Data model
nav_order: 3
---

# Suppliers model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Suppliers refer to companies, organizations, and individuals that provide the essential consumables and hardware devices necessary for conducting experiments and studies in the field. These suppliers play a critical role in the research ecosystem by ensuring that researchers have access to the high-quality materials and equipment they need. In BrainSTEM, suppliers are a shared model across users.

## Fields

| Field | Description |
|:------|:------------|
| `Name` | The name of the supplier (**required**; must be unique) |
| `Description` | A description of the supplier |
| `Website` | The website of the supplier |

## Submission process

Anyone can submit a supplier or suggest changes to an existing one, but all submissions must be approved before they are available for usage. Please see existing entries for examples of what to submit.

## Permissions

Once an entry has been approved, it becomes available to everyone.

## Suppliers API access

The API allows for programmable access to suppliers, enabling you to read, edit, and delete entries through the API. Learn more about the suppliers' fields and data structure on the [Suppliers API page]({{"api/resources/supplier/"|absolute_url}}).