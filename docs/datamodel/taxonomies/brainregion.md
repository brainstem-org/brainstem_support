---
layout: default
title: Brain regions
parent: Taxonomies
grand_parent: Data model
nav_order: 1
---

# Brain regions model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Brain regions are a type of taxonomy defined by brain atlases. In BrainSTEM, brain regions are a shared model across users. New brain atlases and therefore brain regions are added by the admin team. Please reach out to us if you are missing a brain atlas that is publicly available, that you would like to have incorporated.

## Fields

| Field | Description |
|:------|:------------|
| `Name` | The name of the brain region (**required**) |
| `Acronym` | Acronym used for the brain region (**required**) |
| `Atlas` | The brain atlas in which the brain region is defined (**required**) |
| `Description` | A general description of the brain region |
| `Region id` | A unique identifier for the brain region within the atlas |
| `Parent acronym` | The acronym of the parent region in the hierarchical structure of the brain atlas |
| `Graph order` | A numerical value representing the order of the region in the hierarchical graph of the brain atlas |

## Brain Atlases

The following brain atlases are available in BrainSTEM:

- Allen Mouse Brain Atlas: A genome-wide, three-dimensional map of gene expression in the adult mouse brain, based on wild type C57BL/6J mice.
- Allen Developing Mouse Brain Atlas: A detailed map of gene expression changes during mouse brain development, from embryo through adulthood.
- Allen Human Brain Atlas: A multi-modal atlas mapping gene expression across the healthy human brain, including RNA microarray data and in situ hybridization images.
- Allen Developing Human Brain Atlas: Provides anatomical analysis of gene expression across multiple stages of early human brain development.
- Allen Non-Human Primate Brain Atlas: Explores the cellular and molecular architecture of the developing postnatal brain of the rhesus macaque.
- Allen Spinal Column Atlas: A comprehensive map of gene expression in the healthy mouse spinal cord at ages p56 and p4.
- Brain Maps 4.0 - Rat brain Atlas: An open access atlas with global nervous system nomenclature ontology and flatmaps for the rat brain.
- Paxinos & Franklin 2001 Mouse Brain Atlas (Second edition): Based on adult C57BL/J6 Mouse (weight range 26-30 g).
- Paxinos & Watson 1997 Rat Brain Atlas (Third edition): Based on adult male Wistar rats (weight range 270-310 g).
- Swanson 2004 Rat Brain Atlas (Third edition): Based on adult Sprague-Dawley rats.

## Permissions

Once a new brain atlas has been implemented, it becomes available to everyone.

## Brain regions API access

The API allows for programmable access to brain regions, enabling you to read entries through the API. Learn more about the brain regions' fields and data structure on the [Brain regions API page]({{"api/taxonomies/brainregion/"|absolute_url}}).