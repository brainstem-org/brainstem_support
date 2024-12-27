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
| `Product id` | Product identifier that must be unique for each probe design (string) |
| `Probe layout` | Description of the probe's physical arrangement (string; e.g., "linear", "grid") |
| `Number of channels` | Total number of recording channels on the probe (non-negative integer) |
| `Number of shanks` | Number of probe shanks (non-negative integer) |
| `Spacing between shanks` | Distance between adjacent shanks (floating-point number; measured in μm) |
| `Thickness of shanks` | Physical thickness of each shank (floating-point number; measured in μm) |
| `Length of shanks` | Physical length of each shank (floating-point number; measured in μm) |
| `Area of electrode sites` | Surface area of individual recording sites (floating-point number; measured in μm²) |
| `Uniform layout` | Indicates whether recording sites are uniformly spaced (boolean value) |
| `Custom design` | Indicates whether this is a custom probe design (boolean value) |
| `Vertical spacing between sites` | Distance between recording sites along the vertical axis (floating-point number; measured in μm) |

## Optic fiber design

A flexible light guide used primarily in optogenetic experiments to deliver light to specific brain regions. Optic fibers are essential in neuroscience for manipulating neural circuits using light.

| Field | Description |
|:------|:------------|
| `Product id` | Product identifier that must be unique for each fiber design (string) |
| `Numerical Aperture` | Optical property defining the acceptance angle of the fiber (floating-point number) |
| `Wavelength minimum` | Lower limit of transmissible wavelengths (floating-point number; measured in nm) |
| `Wavelength maximum` | Upper limit of transmissible wavelengths (floating-point number; measured in nm) |
| `Fiber type` | Classification of the optical fiber type (string) |
| `Core diameter` | Diameter of the fiber's light-conducting core (floating-point number; measured in μm) |
| `Cladding diameter` | Diameter including the light-confining cladding layer (floating-point number; measured in μm) |
| `Coating diameter` | Total diameter including protective coating (floating-point number; measured in μm) |
| `Core` | Material composition of the fiber core (string) |
| `Cladding` | Material composition of the cladding layer (string) |
| `Coating` | Material composition of the protective coating (string) |

## Virus construct

A viral vector preparation used for introducing genes into cells. Virus solutions are important for studies involving gene expression, neural circuit tracing, and optogenetics.

| Field | Description |
|:------|:------------|
| `Product id` | Product identifier that must be unique for each viral construct (string) |
| `Virus type` | Classification of virus used (string; e.g., "Adenovirus", "AAV") |
| `Capsid` | Specification of the viral capsid structure (string) |
| `Promoter` | Genetic promoter sequence used in the construct (string) |
| `Gene` | Target gene sequence in the construct (string) |
| `Reporter` | Reporter gene or protein for tracking expression (string) |
| `Other element` | Additional genetic elements in the construct (string) |

## Single wire electrode

A simple yet effective tool for measuring electrical activity at a single site. Single wire electrodes are commonly used in studies examining neural or muscular electrical activity.

| Field | Description |
|:------|:------------|
| `Product id` | Product identifier that must be unique for each electrode (string) |
| `Material` | Composition of the electrode wire (string) |
| `Insulation/Coating` | Type and material of electrode insulation (string) |
| `Diameter` | Core wire diameter (floating-point number; measured in mm) |
| `Insulation diameter` | Total diameter including insulation (floating-point number; measured in mm) |

## Consumable types API access

The API allows for programmable access to Consumable types, enabling you to read, edit, and delete consumable type data through the API. Learn more about the consumable types' fields and data structure on the [Consumable types API page]({{"api/resources/consumable/"|absolute_url}}).