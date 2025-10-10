---
layout: default
title: Journals
parent: Dissemination
grand_parent: Data model
nav_order: 1
---

# Journals model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Journals are scholarly publications that serve as the primary means to share scientific findings, methodologies, and analyses with the scientific community. They provide platforms for peer-reviewed research, ensuring that published studies have been critically evaluated by experts in the field for their methodology, accuracy, and contribution to existing knowledge. In BrainSTEM, journals are a shared model across users.

## Fields

| Field | Description |
|:------|:------------|
| ``Name of journal`` | The name of the journal (**required**; string; maximum length: 500 characters; must be unique). Example: "Nature Neuroscience" |
| ``Description`` | A brief description of the journal's scope and focus (optional; maximum length: 2000 characters). Example: "Peer-reviewed journal covering all aspects of neuroscience research" |
| ``Website`` | The official website of the journal (optional; URL; maximum length: 200 characters). Example: "https://www.nature.com/neuro/" |
| ``Adding/editing comments`` | Comments for the submission/approval process (optional). |

## Submission process

Any user can submit new journal entries or propose changes to existing ones. However, all submissions must undergo an approval process before becoming available for use. Please refer to existing entries for examples of appropriate submissions.

## Permissions

Once a journal entry has been approved, it becomes accessible to all users.

## API access

The API provides programmable access to journal data, allowing you to read, edit, and delete entries. For more information about the fields and data structure of journal entries, please consult the [Journals API page]({{"api/dissemination/journal/"|absolute_url}}).