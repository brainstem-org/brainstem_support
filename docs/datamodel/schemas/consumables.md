---
layout: default
title: Consumable types
parent: Schemas
grand_parent: Data model
nav_order: 7
---

# Consumable types
{: .no_toc}

Several types of consumables are available, each with specific fields to describe their characteristics in detail.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Silicon probe design

A specialized tool for recording electrical signals from neurons. Silicon probes are vital for experiments focused on understanding brain function through electrophysiological recordings.

| Field | Description |
|:------|:------------|
| `Product id` | Unique identifier for the product |
| `Probe layout` | Layout of the probe (e.g., linear) |
| `Number of channels` | Total number of channels on the probe |
| `Number of shanks` | Number of shanks on the probe |
| `Spacing between shanks (μm)` | Distance between shanks in micrometers |
| `Thickness of shanks (μm)` | Thickness of the shanks in micrometers |
| `Length of shanks (μm)` | Length of the shanks in micrometers |
| `Area of electrode sites (μm^2)` | Area of individual electrode sites in square micrometers |
| `Uniform layout` | Boolean indicating if the layout is uniform |
| `Custom design` | Boolean indicating if it's a custom design |
| `Vertical spacing between sites (μm)` | Vertical distance between electrode sites in micrometers |

## Optic fiber design

A flexible light guide used primarily in optogenetic experiments to deliver light to specific brain regions. Optic fibers are essential in neuroscience for manipulating neural circuits using light.

| Field | Description |
|:------|:------------|
| `Product id` | Unique identifier for the product |
| `Numerical Aperture` | Numerical aperture of the fiber |
| `Wavelength minimum (nm)` | Minimum wavelength the fiber can transmit in nanometers |
| `Wavelength maximum (nm)` | Maximum wavelength the fiber can transmit in nanometers |
| `Fiber type` | Type of the optical fiber |
| `Core diameter (μm)` | Diameter of the fiber core in micrometers |
| `Cladding diameter (μm)` | Diameter of the fiber cladding in micrometers |
| `Coating diameter (μm)` | Diameter of the fiber coating in micrometers |
| `Core` | Material of the fiber core |
| `Cladding` | Material of the fiber cladding |
| `Coating` | Material of the fiber coating |

## Virus construct

A viral vector preparation used for introducing genes into cells. Virus solutions are important for studies involving gene expression, neural circuit tracing, and optogenetics.

| Field | Description |
|:------|:------------|
| `Product id` | Unique identifier for the product |
| `Virus type` | Type of virus (e.g., Adenovirus) |
| `Capsid` | Capsid information |
| `Promoter` | Promoter used in the construct |
| `Gene` | Gene of interest in the construct |
| `Reporter` | Reporter gene or protein |
| `Other element` | Any other relevant genetic elements |

## Single wire electrode

A simple yet effective tool for measuring electrical activity at a single site. Single wire electrodes are commonly used in studies examining neural or muscular electrical activity.

| Field | Description |
|:------|:------------|
| `Product id` | Unique identifier for the product |
| `Material` | Material of the wire electrode |
| `Insulation/Coating` | Type of insulation or coating on the electrode |
| `Diameter (mm)` | Diameter of the wire in millimeters |
| `Insulation diameter (mm)` | Diameter of the insulation in millimeters |

## Consumable types API access

The API allows for programmable access to Consumable types, enabling you to read, edit, and delete consumable type data through the API. Learn more about the consumable types' fields and data structure on the [Consumable types API page]({{"api/resources/consumable/"|absolute_url}}).