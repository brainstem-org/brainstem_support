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
| `Name` | Name of the inventory (**required**; must describe contents or purpose) |
| `Authenticated groups` | Groups that have change permissions for this inventory (**required**) |
| `Description` | Text description of the inventory |
| `Public access` | Determines if the inventory is publicly available or accessible only through the private portal |

## Permissions

You manage permissions through the management tab, where you can assign individual users and groups access levels to an inventory. Inventories have four permission levels: membership (read access), change permissions, managers, and owners.

Consumable stocks inherit permissions from their associated inventory.

Visit the [permissions page] to learn more. 

## Inventory API access

The API allows for programmable access to inventories, enabling you to read, edit, and delete inventories through the API. Learn more about the inventories' fields and data structure on the [Inventory API page]({{"api/personal_attributes/inventory/"|absolute_url}}).