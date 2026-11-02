---
layout: default
title: Specimen logs
parent: Specimen sets
grand_parent: Data model
nav_order: 3
---

# Specimen log model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A specimen log is a monitoring stream for ex-vivo material. It tracks values that are followed over time for a [specimen set]({{"datamodel/stem/specimenset/"|absolute_url}}): the bath solution, culture-medium changes, temperature, oxygenation, pH, CO₂, humidity, slice health, viability assays or generic observations. Specimen logs are the ex-vivo counterpart of [subject logs]({{"datamodel/modules/subjectlog/"|absolute_url}}).

One specimen log is one log of a single kind for one specimen set, for example the temperature log of a slice series. The log header selects the type and the target; the time-stamped entries are added to the log over time. A specimen log is not a processing event (that is a [specimen procedure]({{"datamodel/modules/specimenprocedure/"|absolute_url}})) and does not change the preparation conditions of the material.

{% include datamodel_embed.html model="modules.specimenlog" %}

## Fields

| Field | Description |
|:------|:------------|
| `Specimen log type` | Kind of log (**required**). Selected from predefined types. Example: "Temperature log". *See options below.* |
| `Specimen set` | The [specimen set]({{"datamodel/stem/specimenset/"|absolute_url}}) the log belongs to (**required**). |
| `Target specimens` | Specific [specimens]({{"datamodel/stem/specimen/"|absolute_url}}) within the set the log applies to. Leave empty when the log applies to the whole set. |
| `Description` | A short description of the log (string; maximum length: 500 characters). Example: "Bath temperature during recording, measured at the chamber inlet" |
| `Protocol` | Optional reusable [protocol]({{"datamodel/personal_attributes/protocol/"|absolute_url}}) describing how the values were obtained. Must have protocol type Specimen log. |
| `Entries` | The time-stamped entries of the log. The fields of an entry depend on the log type (for example temperature and unit, or pH value). Entries are added and edited in the web interface. See the [Specimen log types schema]({{"datamodel/schemas/specimenlog/"|absolute_url}}). |

## Types of specimen logs

These are the 10 available type options. See the schema for the entry fields: [Specimen log types]({{"datamodel/schemas/specimenlog/"|absolute_url}}).

### Solution Logs

`Bath solution log`: The recording or incubation solution the material sits in, and its changes.

`Culture medium change`: Exchanges of the culture medium.

### Environmental Logs

`CO₂ log`: CO₂ level of the incubator or chamber.

`Humidity log`: Humidity of the incubator or chamber.

`Oxygenation log`: Oxygenation of the bath or medium.

`pH log`: pH of the bath or medium.

`Temperature log`: Temperature of the bath, chamber or incubator.

### Health Logs

`Slice health log`: Assessments of slice health over time.

`Viability assay`: Results of viability assays.

### Observation Logs

`Generic observation`: Free observations that do not fit the other types.

{: .note }
> Specimen log entries are edited in the web interface. The REST API exposes the log header (type, specimen set, target specimens, description, protocol) but not the entries.

## Permissions

Specimen logs inherit permissions through the specimen set associated with them, and so from the projects of that set.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to specimen log headers. Learn more about the specimen logs' fields and data structure on the [Specimen log API page]({{"api/modules/specimenlog/"|absolute_url}}).
