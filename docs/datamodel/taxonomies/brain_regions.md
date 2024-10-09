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
| Name | The name of the brain region (**required**) |
| Acronym | Acronym used for the brain region (**required**) |
| Atlas | The brain atlas in which the brain region is defined (**required**). *See options below* |
| Description | A general description of the brain region |
| Region id | A unique identifier for the brain region within the atlas |
| Parent acronym | The acronym of the parent region in the hierarchical structure of the brain atlas |
| Graph order | A numerical value representing the order of the region in the hierarchical graph of the brain atlas |


## Brain Atlases
The following brain atlases are available in BrainSTEM:

- Allen Mouse Brain Atlas
- Allen Developing Mouse Brain Atlas
- Allen Human Brain Atlas
- Allen Developing Human Brain Atlas
- Allen Non-Human Primate Brain Atlas
- Allen Spinal Column Atlas
- Brain Maps 4.0 - Rat brain Atlas
- Paxinos & Franklin 2001 Mouse Brain Atlas (Second edition)
- Paxinos & Watson 1997 Rat Brain Atlas (Third edition)
- Swanson 2004 Rat Brain Atlas (Third edition)

A detailed list of the brain atlases can be found on the [brain atlases page]({{"datamodel/schemas/brain_atlases/"|absolute_url}}).

## Permissions
Once a new brain atlas has been implemented, it becomes available to everyone.

## Brain regions API access
The API allows for programmable access to brain regions, enabling you to read entries through the API. Learn more about the brain regions' fields and data structure on the [Brain regions API page]({{"api/taxonomies/brainregion/"|absolute_url}}).