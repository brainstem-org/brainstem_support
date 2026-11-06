---
layout: default
title: Suppliers
parent: Resources
grand_parent: Data model
nav_order: 3
---

# Supplier model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A supplier is a company, organization or individual that provides consumables and hardware devices. Both [consumables]({{"datamodel/resources/consumable/"|absolute_url}}) and [hardware devices]({{"datamodel/resources/hardwaredevice/"|absolute_url}}) require one, so the supplier is the top of the catalog: it is how a product is attributed to whoever makes or sells it. [Subjects]({{"datamodel/stem/subject/"|absolute_url}}) can also name the supplier they were bought from. In BrainSTEM, suppliers are a shared model across users.

{% include datamodel_embed.html model="resources.supplier" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Name of supplier`` | The company as it is commonly known (**required**; string; maximum length: 100 characters; must be unique across BrainSTEM). Keep parent and subsidiary separate only where products are branded differently. Example: "IMEC" |
| ``Description`` | What the supplier provides, and anything that distinguishes it from a similarly named company (maximum length: 2000 characters). |
| ``Website`` | The website of the supplier (URL; maximum length: 200 characters). Example: "https://www.imec-int.com" |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

## Submission process

Anyone can submit a supplier or suggest changes to an existing one. A submission enters the approval queue and is usable in your own records immediately; it is visible only to you until accepted. Search under the trading name, the full legal name and any parent company first; suppliers merge and rebrand often. For details of the approval statuses see the [Resources page]({{"datamodel/resources/"|absolute_url}}).

A supplier cannot be deleted while consumables, hardware devices, subjects or pending submissions point to it.

## Permissions

Everyone can read the accepted list. Editing an accepted supplier is restricted, since it would change every product attributed to it; an edit creates a change request that is reviewed before it takes effect. Your own pending submissions remain yours to edit or cancel.

## API access

The API allows for programmable access to suppliers, returning the accepted list plus your own pending submissions. Learn more about the suppliers' fields and data structure on the [Suppliers API page]({{"api/resources/supplier/"|absolute_url}}).
