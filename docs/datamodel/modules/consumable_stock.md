---
layout: default
title: Consumable stocks
parent: Modules
grand_parent: Data model
nav_order: 4
---

# Consumable stocks model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Consumable stocks refer to the various components and materials essential for conducting experiments and recording data. These stocks are integral to maintaining high-quality research conditions and ensuring that experiments are performed using accurate and reliable equipment. Each consumable stock type has unique applications depending on the experimental needs, while the fields associated with these types are designed to capture the specific details of each consumable.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of consumable stock (**required**). *See options below* |
| `Inventory` | The inventory record that tracks the consumable stock (**required**) |
| `Notes` | Additional information or special considerations for the consumable stock |
| `Consumable` | The specific consumable associated with the consumable stock |
| `Acquisition date` | The date when the consumable was acquired |
| `Expiration date` | The date when the consumable stock is expected to expire or become unusable |
| `Storage location` | The physical location where the consumable stock is stored |
| `Storage conditions` | The conditions necessary for storing the consumable stock |
| `Intended use` | The planned experimental use of the consumable stock |
| `Cost` | The cost of the consumable stock |

## Types of consumable stocks

These are the available *Type* options for Consumable stocks:

### Optic Fiber
A flexible light guide used primarily in optogenetic experiments to deliver light to specific brain regions. Optic fibers are essential in neuroscience for manipulating neural circuits using light.

### Silicon Probe
A specialized tool for recording electrical signals from neurons. Silicon probes are vital for experiments focused on understanding brain function through electrophysiological recordings.

### Virus Solution
A viral vector preparation used for introducing genes into cells. Virus solutions are important for studies involving gene expression, neural circuit tracing, and optogenetics.

### Single Wire Electrode
A simple yet effective tool for measuring electrical activity at a single site. Single wire electrodes are commonly used in studies examining neural or muscular electrical activity.

## Permissions

Consumable stocks inherit permissions through the inventory associated with them.

Visit the [permissions page] to learn more.

## Consumable stocks API access

The API allows for programmable access to consumable stocks, enabling you to read, edit, and delete consumable stocks through the API. Learn more about the consumable stocks' fields and data structure on the [Consumable stocks API page]({{"api/modules/consumablestock/"|absolute_url}}).