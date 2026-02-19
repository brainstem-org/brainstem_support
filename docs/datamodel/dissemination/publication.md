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
| ``Title`` | The title of the publication (**required**; string; maximum length: 200 characters; must be unique). Example: "Neural mechanisms of spatial memory in hippocampal circuits" |
| ``Authors`` | The authors of the publication (**required**; string; maximum length: 500 characters). Example: "Smith J, Johnson A, Brown B" |
| ``Journal`` | The journal in which the publication appears (**required**). Must reference an existing [journal]({{"datamodel/dissemination/journal/"|absolute_url}}). Example: "Nature Neuroscience" |
| ``Abstract`` | A summary of the publication's content (**required**; text field). Example: "This study investigates the role of hippocampal place cells in spatial memory formation..." |
| ``Publication date`` | Date when the publication was officially released (**required**; date). Example: "2024-03-15" |
| ``DOI`` | Digital Object Identifier for the publication (string; maximum length: 200 characters). Example: "10.1038/s41593-024-01567-2" |
| ``Volume`` | The journal volume in which the publication appears (string; maximum length: 100 characters). Example: "27" |
| ``Publication URL`` | Direct link to the publication (URL; maximum length: 300 characters). Example: "https://www.nature.com/articles/example" |
| ``PDF URL`` | Direct link to a publicly accessible PDF version of the publication (URL; maximum length: 300 characters). Example: "https://www.nature.com/articles/example.pdf" |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

## Submission process

Any user can submit new publication entries or propose changes to existing ones. However, all submissions must undergo an approval process before becoming available for use. Please refer to existing entries for examples of appropriate submissions.

## Permissions

Once a publication entry has been approved, it becomes accessible to all users.

## API access

The API provides programmable access to publication data, allowing you to read, edit, and delete entries. For more information about the fields and data structure of publication entries, please consult the [Publications API page]({{"api/dissemination/publication/"|absolute_url}}).