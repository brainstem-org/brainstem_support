---
layout: default
title: Sessions
parent: Data model
nav_order: 4
has_toc: false
---

# Session model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction 

A session is one experimental occasion: a recording day, an imaging run, a behavioral session. The session itself holds little; it is the container that the modules hang off, and the modules describe what happened. Sessions are primarily described by the following modules:

1. [__Behaviors__]({{"datamodel/modules/behavior"|absolute_url}}): what the subjects were doing, described by a behavioral assay and the setup it ran on.
2. [__Data acquisition__]({{"datamodel/modules/dataacquisition"|absolute_url}}): the recorded streams (electrophysiology, imaging, video, audio, tomography) with their file and acquisition parameters. Each data acquisition is one recording stream; different setups or file separations require separate entries. Each data acquisition names the [experimental interfaces]({{"datamodel/modules/experimentalinterface/"|absolute_url}}) the signal came through.
3. [__Manipulations__]({{"datamodel/modules/manipulation"|absolute_url}}): stimuli or perturbations delivered during the session, such as optogenetic, electrical, pharmacological or sensory stimulation, with their parameters. Each manipulation names the interfaces the stimulus went through.
4. [__Epochs__]({{"datamodel/stem/epoch/"|absolute_url}}): named intervals within the session, with start and end times relative to the session onset. Behaviors, data acquisitions and manipulations can be linked to epochs, which gives a session a timeline.

Sessions can also be grouped in [__Collections__]({{"datamodel/stem/collection"|absolute_url}}). Each of these entries has its own page with its fields; the session itself has only the fields below.

![A session is either subject-based or specimen-based. Both belong to a project and hold data acquisitions, manipulations and epochs; behaviors belong to subject-based sessions only. They differ in what they link (subjects or a specimen set) and therefore in which interfaces their acquisitions and manipulations can use.]({{site.baseurl}}/assets/images/diagrams/session-kinds.svg)
*A session is either subject-based or specimen-based. Both belong to a project and hold data acquisitions, manipulations and epochs; behaviors belong to subject-based sessions only. They differ in what they link (subjects or a specimen set) and therefore in which interfaces their acquisitions and manipulations can use.*

{% include datamodel_embed.html model="stem.session" %}

## Fields

| Field | Description |
|:------|:------------|
| `Session name` | Name of the session (**required**; string; maximum length: 100 characters; must be unique across BrainSTEM). Build the name from the subject and the date so it is distinct. Example: "PV_Recording_20240313" |
| `Session type` | Subject or specimen (**required**; fixed after creation). |
| `Status` | Planned, performed or cancelled (default: performed). See [Planning](#planning). |
| `Projects` | Projects the session belongs to (**required**). Only projects where you are at least a Contributor are offered. Learn more about project inheritance [here]({{"datamodel/stem/project/"|absolute_url}}). |
| `Subjects` | The subjects that took part (subject sessions; required for a performed subject session). The subjects of a [behavior]({{"datamodel/modules/behavior"|absolute_url}}) must be a subset of the session's subjects. |
| `Specimen sets` | The specimen sets worked on (specimen sessions). Replaces Subjects on a specimen session. |
| `Description` | A rich text description of what the session was for and anything unusual about it. Pictures can be uploaded. |
| `Date and time onset` | Date and time of the session onset (datetime format `YYYY-MM-DD HH:mm:ss`). Epoch times are relative to this. |
| `Tags` | Tags for organization and filtering. Shared across all users. |
| `Data storage` | Where the session's data are held. Several [data storages]({{"datamodel/personal_attributes/datastorage/"|absolute_url}}) can be selected; their order is kept. |
| `Session name in data storage` | The session's directory or dataset name when it differs from the name above (string; maximum length: 200 characters). Example: "ses01_mem_2024" |
| `Extra content` | Custom key-value fields that the standard fields do not cover. Values can be text or numbers. Example: {"Room": "B115", "Temperature": "22C"}. [Schema](https://www.brainstem.org/schemas/Session/Array.json) |
| `Repository links` | External locations of this session's data, such as a DANDI set. Each link names the repository (CRCNS, DANDI, Figshare, GitHub, Globus, Mendeley, Zenodo, Webshare or Other) and its URL, both required. [Schema](https://www.brainstem.org/schemas/Session/Repository.json) |

## Subject sessions and specimen sessions

A session is either a **subject session** (in-vivo work on one or more [subjects]({{"datamodel/stem/subject/"|absolute_url}})) or a **specimen session** (ex-vivo work on [specimen sets]({{"datamodel/stem/specimenset/"|absolute_url}})). A subject session offers the Subjects field, and its data acquisitions and manipulations can only link to experimental interfaces installed on those subjects. A specimen session offers the Specimen sets field, and its modules link to interfaces installed on those sets.

{: .note }
The session type is chosen when the session is created and cannot be changed afterwards. A session recorded with the wrong type has to be created again with the right one.

## Planning

Performed is the default and means the session took place. A planned session is prepared ahead of time: nothing in it has been recorded, and its data acquisitions, manipulations, behaviors and epochs are plans too. The page shows a marker beside the title, and the session is left out of counts, public pages and API listings unless asked for. Mark it as performed once it has taken place. Cancelled keeps a dropped plan for the record.

## Export

The **Export** menu on a session page offers a printable view (save as PDF), a Word document and a spreadsheet. The session's entries can also be exported as JSON through the API (`export/` and `export-jobs/` actions).

## Permissions

The session inherits permissions from its associated projects. You need Contributor access through at least one of them to add or edit the session and its modules. Data storages, setups and behavioral assays are shared through groups, not projects: you can only select the ones where you are at least a Contributor.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to sessions. Learn more about the sessions' fields and data structure on the [Session API page]({{"api/stem/session/"|absolute_url}}).
