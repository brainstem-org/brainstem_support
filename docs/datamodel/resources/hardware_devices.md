---
layout: default
title: Hardware devices
parent: Resources
grand_parent: Data model
nav_order: 2
---

# Hardware devices model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Hardware devices refer to durable, often more complex equipment or tools that are not consumed or depleted with use, unlike consumables. These devices are designed for repeated use over a long period and play crucial roles in conducting experiments, data acquisition, performing stimulation and manipulation protocols, and carrying out procedures. In BrainSTEM, hardware devices are a shared model across users.

## Fields

| Field | Description |
|:------|:------------|
| `Name` | The name of the hardware device (**required**; must be unique) |
| `Description` | A description of the hardware device |
| `Supplier` | The supplier of the hardware device (**required**) |

## Submission process

Anyone can submit hardware devices or submit changes to existing ones, but all submissions must be approved before they are available for usage. Please see existing entries for examples of what to submit.

## Permissions

Once an entry has been approved, it becomes available to everyone.

## Hardware devices API access

The API allows for programmable access to hardware devices, enabling you to read, edit, and delete entries through the API. Learn more about the hardware devices' fields and data structure on the [Hardware devices API page]({{"api/resources/hardwaredevice/"|absolute_url}}).
