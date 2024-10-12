---
layout: default
title: Environment types
parent: Taxonomies
grand_parent: Data model
nav_order: 2
---

# Environment types model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Environment types are fundamentally categories of setups and also serve as categories for behavioral paradigms. In BrainSTEM, environment types are a shared model across users. Behavioral paradigms are linked to a specific environment type, ensuring that each paradigm is defined within a particular type of environment.

## Fields

| Field | Description |
|:------|:------------|
| `Name` | The name of the environment type (**required**; must be unique) |
| `Description` | A general description of the environment type |

## Submission process

Anyone can submit new environment types or suggest changes to existing ones. However, all submissions must be approved before they become available for usage. Please refer to existing entries for examples of what to submit.

## Permissions

Once an entry has been approved, it becomes available to all users.

## Environment types API access

The API allows for programmable access to environment types, enabling you to read, edit, and delete entries through the API. Learn more about the environment types' fields and data structure on the [Environment types API page]({{"api/taxonomies/environmenttype/"|absolute_url}}).
