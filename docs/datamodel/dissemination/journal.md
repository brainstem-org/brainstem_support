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

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A journal is a scholarly publication venue. [Publications]({{"datamodel/dissemination/publication/"|absolute_url}}) require one, so the journal is what a paper is attributed to when it is linked to a project. Preprint servers and conference proceedings belong here too when that is where the work appeared. In BrainSTEM, journals are a shared model across users.

{% include datamodel_embed.html model="dissemination.journal" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Name of journal`` | The journal's full title (**required**; string; maximum length: 500 characters; must be unique across BrainSTEM). Use the full form rather than an abbreviation. Example: "Nature Neuroscience" |
| ``Description`` | Scope and anything that distinguishes it from a similarly named venue (maximum length: 2000 characters). |
| ``Website`` | The official website of the journal (URL; maximum length: 200 characters). Example: "https://www.nature.com/neuro/" |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

## Submission process

Any user can submit new journal entries or propose changes to existing ones. A submission enters the approval queue and is usable in your own records immediately; it is visible only to you until accepted. Search under the full title and any common abbreviation first. For the approval statuses see the [Resources page]({{"datamodel/resources/#submission-and-approval"|absolute_url}}).

A journal cannot be deleted while publications or pending publication submissions point to it.

## Permissions

Everyone can read the accepted list. Editing an accepted journal is restricted, since it would change every publication attributed to it; an edit creates a change request that is reviewed before it takes effect. Your own pending submissions remain yours to edit or cancel.

## API access

The API provides programmable access to journal data, returning the accepted list plus your own pending submissions. For more information about the fields and data structure, please consult the [Journals API page]({{"api/dissemination/journal/"|absolute_url}}).
