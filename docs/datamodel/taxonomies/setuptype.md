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

Setup types are fundamentally categories of setups and also serve as categories for behavioral assays. In BrainSTEM, setup types are a shared model across users. Behavioral Assays are linked to a specific setup type, ensuring that each paradigm is defined within a particular type of setup.

## Fields

| Field | Description |
|:------|:------------|
| ``Name of setup type`` | The name of the setup type (**required**; string; maximum length: 200 characters; must be unique) |
| ``Category of the setup type`` | The category of the setup type (**required**). Selected from predefined categories (In Vitro, Ex Vivo, Anesthetized In Vivo, Head-Fixed Awake, Voluntarily Stationary Awake, Freely Moving Awake, Unknown) |
| ``Description`` | A general description of the setup type (optional; maximum length: 2000 characters) |
| ``Adding/editing comments`` | Comments for the submission/approval process (optional). |

## Submission process

Anyone can submit new setup types or suggest changes to existing ones. However, all submissions must be approved before they become available for usage. Please refer to existing entries for examples of what to submit.

## Permissions

Once an entry has been approved, it becomes available to all users.

## Setup types API access

The API allows for programmable access to setup types, enabling you to read, edit, and delete entries through the API. Learn more about the setup types' fields and data structure on the [Setup types API page]({{"api/taxonomies/setuptype/"|absolute_url}}).
