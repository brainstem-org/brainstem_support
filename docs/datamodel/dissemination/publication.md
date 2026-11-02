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

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A publication is one paper, article or preprint. Linking it to a [project]({{"datamodel/stem/project/"|absolute_url}}) connects the paper to the records behind it, so a reader can move from the citation to the subjects, sessions and procedures the results came from. Publications are attached from the project side. In BrainSTEM, publications are a shared model across users.

{% include datamodel_embed.html model="dissemination.publication" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Title`` | The title of the publication as published, including subtitle (**required**; string; maximum length: 200 characters; must be unique across BrainSTEM). |
| ``Authors`` | The author list in published order (**required**; string; maximum length: 500 characters). Free text, since most co-authors will not have accounts. Example: "Smith J, Johnson A, Brown B" |
| ``Journal`` | The journal in which the publication appears (**required**). Must reference an existing [journal]({{"datamodel/dissemination/journal/"|absolute_url}}); submit a missing journal first. |
| ``Abstract`` | The published abstract (**required**). It makes the entry searchable. |
| ``Publication date`` | Date when the publication was released (**required**; date). Example: "2024-03-15" |
| ``DOI`` | Digital Object Identifier (string; maximum length: 200 characters). Optional, but the field that settles whether a paper is already in BrainSTEM; record it whenever one exists. Example: "10.1038/s41593-024-01567-2" |
| ``Volume`` | The journal volume (string; maximum length: 100 characters). |
| ``Publication URL`` | Direct link to the publication (URL; maximum length: 300 characters). |
| ``PDF URL`` | Direct link to a publicly accessible PDF, such as an open-access or repository copy (URL; maximum length: 300 characters). |
| ``Adding/editing comments`` | Comments for the submission/approval process. |

## Lookup DOI

The publication form has a **Lookup DOI** button beside the DOI field. It fetches the paper from Crossref and fills in the title, authors, abstract, volume, publication URL and publication date. When Crossref has no abstract it falls back to Semantic Scholar for that field. If the journal already exists in BrainSTEM it is matched by name and selected; otherwise the fetched journal name is shown so you can submit it. Everything it fills stays editable. The lookup exists only in the web form; through the API, submit the fields directly.

## Submission process

Any user can submit new publication entries or propose changes to existing ones. A submission enters the approval queue and is usable in your own records immediately; it is visible only to you until accepted. Search by DOI before submitting: a duplicate under a slightly different title is the usual reason a submission is rejected. For the approval statuses see the [Resources page]({{"datamodel/resources/#submission-and-approval"|absolute_url}}).

## Permissions

Everyone can read the accepted list. Editing an accepted publication is restricted, since it is a record of something already published; an edit creates a change request that is reviewed before it takes effect. Your own pending submissions remain yours to edit or cancel.

## API access

The API provides programmable access to publication data, returning the accepted list plus your own pending submissions. For more information about the fields and data structure, please consult the [Publications API page]({{"api/dissemination/publication/"|absolute_url}}).
