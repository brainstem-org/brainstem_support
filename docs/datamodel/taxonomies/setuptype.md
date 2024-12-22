---
layout: default
title: Setup types
parent: Taxonomies
grand_parent: Data model
nav_order: 2
---

# Setup types model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Setup types are fundamentally categories of setups and also serve as categories for behavioral paradigms. In BrainSTEM, setup types are a shared model across users. Behavioral paradigms are linked to a specific setup type, ensuring that each paradigm is defined within a particular type of setup.

## Fields

| Field | Description |
|:------|:------------|
| `Name` | The name of the setup type (**required**; must be unique) |
| `Description` | A general description of the setup type |

## Submission process

Anyone can submit new setup types or suggest changes to existing ones. However, all submissions must be approved before they become available for usage. Please refer to existing entries for examples of what to submit.

## Permissions

Once an entry has been approved, it becomes available to all users.

## Setup types API access

The API allows for programmable access to setup types, enabling you to read, edit, and delete entries through the API. Learn more about the setup types' fields and data structure on the [Setup types API page]({{"api/taxonomies/setuptype/"|absolute_url}}).
