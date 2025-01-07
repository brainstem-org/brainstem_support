---
layout: default
title: Collections
parent: STEM
grand_parent: Data model
nav_order: 4
---

# Collection model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Collections allow for creating subgroups of sessions within a project. They can be used to define a set of sessions for a specific analysis or figure. All sessions in a collection must belong to the same project.

## Fields

| Field | Description |
|:------|:------------|
| `Name` | Name of the collection (**required**; string; max length: 100 characters; must be unique within the project). Example: "Place Cell Analysis", "Learning Sessions Day 1-5" |
| `Project` | The project the collection belongs to (**required**). A collection can belong to a single project. Example: "Spatial Memory Project" |
| `Sessions` | Sessions in the collection. All sessions must belong to the same project (**required**). Example: "Recording1", "Recording2", "Recording3" |
| `Description` | A text description of the collection, providing additional context and information. Pictures can be uploaded and inserted through rich text formatting. Example: "Collection of all place cell recording sessions during the learning phase..." |
| `Tags` | Tags for the collection. Great for organizational purposes, quick labeling, and filtering. Tags are shared across all users. Example: "place-cells", "learning-phase", "figure-1-data" |

## Permissions

Collections inherit permissions from their associated project. You can only add sessions to the collection that are part of the same project.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Collections API access

The API allows for programmable access to collections. Learn more about the collections' fields and data structure on the [Collections API page]({{"api/stem/collection/"|absolute_url}}).
