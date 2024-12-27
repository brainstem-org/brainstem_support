---
layout: default
title: Publications
parent: Dissemination
grand_parent: Data model
nav_order: 2
---

# Publications model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Publications refer to articles, papers, or studies in scientific journals. They are the primary means for disseminating new findings, theories, and analyses to the wider scientific community and the public. In BrainSTEM, publications are a shared model across users.

## Fields

| Field | Description |
|:------|:------------|
| `Title` | The title of the publication (**required**) |
| `Authors` | The authors of the publication (**required**) |
| `Journal` | The journal in which the publication appears (**required**) |
| `Abstract` | A summary of the publication's content (**required**) |
| `DOI` | Digital Object Identifier for the publication |
| `Volume` | The journal volume in which the publication appears |
| `Publication URL` | Direct link to the publication |
| `PDF URL` | Direct link to a publicly accessible PDF version of the publication |
| `Publication date` | Date when the publication was officially released |

## Submission process

Any user can submit new publication entries or propose changes to existing ones. However, all submissions must undergo an approval process before becoming available for use. Please refer to existing entries for examples of appropriate submissions.

## Permissions

Once a publication entry has been approved, it becomes accessible to all users.

## Publications API access

The API provides programmable access to publication data, allowing you to read, edit, and delete entries. For more information about the fields and data structure of publication entries, please consult the [Publications API page]({{"api/dissemination/publication/"|absolute_url}}).