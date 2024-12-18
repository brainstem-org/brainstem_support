---
layout: default
title: Inventories
parent: Personal attributes
grand_parent: Data model
nav_order: 4
---

# Inventories model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Inventories in BrainSTEM provide a way to track and manage consumable resources within a laboratory or research group. They allow for organized tracking of supplies and materials needed for experiments. Each inventory can be associated with specific groups and can be either public or private.

## Fields

| Field | Description |
|:------|:------------|
| `Name` | Name of the inventory (**required**; string; maximum length: 50 characters). Example: "Silicon Probe Storage" |
| `Authenticated groups` | Groups that have change permissions for this inventory (**required**). Example: "Equipment Management Team" |
| `Description` | Rich text description of the inventory. Can include uploaded images. Example: "Storage location for all silicon probes, organized by probe type and usage status..." |
| `Public access` | Determines if the inventory is publicly available or accessible only through the private portal. Example: "False" for private access |

## Permissions

You manage permissions through the management tab, where you can assign individual users and groups access levels to an inventory. Inventories have four permission levels: membership (read access), contributors, managers, and owners.

Consumable stocks inherit permissions from their associated inventory.

Visit the [permissions page]({{"datamodel/permission/"|absolute_url}}) to learn more. 

## Inventory API access

The API allows for programmable access to inventories, enabling you to read, edit, and delete inventories through the API. Learn more about the inventories' fields and data structure on the [Inventory API page]({{"api/personal_attributes/inventory/"|absolute_url}}).