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
| `Product id` | Product identifier that must be unique for each probe design (string). Required for inventory tracking and reference |
| `Probe layout` | Description of the probe's physical arrangement (string). Options include "linear", "grid", etc. Required for experimental planning |
| `Number of channels` | Total number of recording channels on the probe (non-negative integer). Critical for determining recording capacity |
| `Number of shanks` | Number of probe shanks (non-negative integer). Affects recording coverage and tissue impact |
| `Spacing between shanks` | Distance between adjacent shanks (float, μm). Important for spatial distribution of recording sites |
| `Thickness of shanks` | Physical thickness of each shank (float, μm). Critical for tissue damage assessment |
| `Length of shanks` | Physical length of each shank (float, μm). Determines recording depth capability |
| `Area of electrode sites` | Surface area of individual recording sites (float, μm²). Affects signal quality and impedance |
| `Uniform layout` | Indicates whether recording sites are uniformly spaced (boolean). Important for data analysis |
| `Custom design` | Indicates whether this is a custom probe design (boolean). Relevant for manufacturing and ordering |
| `Vertical spacing between sites` | Distance between recording sites along vertical axis (float, μm). Critical for spatial resolution |

## Optic fiber design

A flexible light guide used primarily in optogenetic experiments to deliver light to specific brain regions. Optic fibers are essential in neuroscience for manipulating neural circuits using light.

| Field | Description |
|:------|:------------|
| `Product id` | Product identifier that must be unique for each fiber design (string). Required for inventory management |
| `Numerical Aperture` | Optical property defining the acceptance angle (float). Critical for light transmission efficiency |
| `Wavelength minimum` | Lower limit of transmissible wavelengths (float, nm). Important for experimental compatibility |
| `Wavelength maximum` | Upper limit of transmissible wavelengths (float, nm). Determines usable light spectrum |
| `Fiber type` | Classification of the optical fiber type (string). Affects performance characteristics |
| `Core diameter` | Diameter of the fiber's light-conducting core (float, μm). Critical for light transmission |
| `Cladding diameter` | Diameter including light-confining cladding layer (float, μm). Important for mechanical stability |
| `Coating diameter` | Total diameter including protective coating (float, μm). Relevant for tissue insertion |
| `Core` | Material composition of the fiber core (string). Determines optical properties |
| `Cladding` | Material composition of the cladding layer (string). Affects light confinement |
| `Coating` | Material composition of the protective coating (string). Important for durability |

## Virus construct

A viral vector preparation used for introducing genes into cells. Virus solutions are important for studies involving gene expression, neural circuit tracing, and optogenetics.

| Field | Description |
|:------|:------------|
| `Product id` | Product identifier that must be unique for each viral construct (string). Required for tracking |
| `Virus type` | Classification of virus used (string). Options include "Adenovirus", "AAV", etc. Critical for application |
| `Capsid` | Specification of the viral capsid structure (string). Determines tropism and targeting |
| `Promoter` | Genetic promoter sequence used in construct (string). Controls expression specificity |
| `Gene` | Target gene sequence in the construct (string). Defines the genetic modification |
| `Reporter` | Reporter gene or protein for tracking expression (string). Important for verification |
| `Other element` | Additional genetic elements in construct (string). Documents supplementary components |

## Single wire electrode

A simple yet effective tool for measuring electrical activity at a single site. Single wire electrodes are commonly used in studies examining neural or muscular electrical activity.

| Field | Description |
|:------|:------------|
| `Product id` | Product identifier that must be unique for each electrode (string). Required for inventory |
| `Material` | Composition of the electrode wire (string). Critical for electrical properties |
| `Insulation/Coating` | Type and material of electrode insulation (string). Affects recording isolation |
| `Diameter` | Core wire diameter (float, mm). Determines tissue impact and signal quality |
| `Insulation diameter` | Total diameter including insulation (float, mm). Important for insertion planning |

## API access

The API allows for programmable access to Consumable types, enabling you to read, edit, and delete consumable type data through the API. Learn more about the consumable types' fields and data structure on the [Consumable types API page]({{"api/resources/consumable/"|absolute_url}}).
