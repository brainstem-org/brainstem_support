---
layout: default
title: Anatomical regions
parent: Taxonomies
grand_parent: Data model
nav_order: 3
---

# Anatomical regions model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

An anatomical region is one anatomical structure as defined by one atlas. Regions are what [procedures]({{"datamodel/modules/procedure/"|absolute_url}}), [specimen procedures]({{"datamodel/modules/specimenprocedure/"|absolute_url}}), [experimental interfaces]({{"datamodel/modules/experimentalinterface/"|absolute_url}}) and [specimen sets]({{"datamodel/stem/specimenset/"|absolute_url}}) point at when they record an anatomical target (their **target regions**). Anatomical regions are a shared model across users. They were called "brain regions" in earlier releases; the old API name `taxonomies/brainregion` remains as a deprecated alias.

{% include datamodel_embed.html model="taxonomies.anatomicalregion" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Name`` | The structure's full name as the atlas gives it (**required**; string; maximum length: 200 characters). |
| ``Acronym`` | The atlas's abbreviation (**required**; string; maximum length: 15 characters). This is how regions are usually referred to and how the hierarchy is expressed. |
| ``Anatomical reference`` | The atlas or ontology release that defines this region (**required**). Part of the region's identity. The atlas name is shown with the region. |
| ``Region id`` | The atlas's own numeric identifier for the structure. It lets a region be matched to the same structure in atlas files and analysis tools. Unique within the reference. |
| ``Parent acronym`` | The acronym of the structure directly above this one (string; maximum length: 15 characters). This builds the hierarchy the region tree is drawn from. |
| ``Graph order`` | The structure's position in the atlas's ordering, used to present the tree in the atlas's own sequence. |
| ``Description`` | Additional detail about the structure, where the atlas provides it (maximum length: 2000 characters). |
| ``Obsolete`` | Retired by the source atlas or ontology; kept for historical records. Skip obsolete regions for new work. |
| ``Replaced by`` | The successor region named by the source ontology, when one exists. |
| ``Ontology URL`` | Link to the term's definition in the source ontology, for ontology-based references. |

## Regions belong to an anatomical reference

A region is not a free-standing anatomical concept. It is one atlas's definition of a structure, and it belongs to an [anatomical reference]({{"datamodel/taxonomies/anatomicalreference/"|absolute_url}}): the atlas or ontology release that defines it. The same name can exist in several atlases with different boundaries, a different acronym and a different place in the hierarchy. "Hippocampus" in the Allen Mouse Brain Atlas and in a Paxinos rat atlas are two separate entries. Choose the atlas your coordinates and protocol were written against.

Within an atlas, regions form a hierarchy through their parent acronym. Selecting a parent structure does not select its children, so choose the level of detail that matches what you actually targeted. Some atlases are flat lists without a hierarchy.

## Selecting regions in forms

Region selectors are filtered by an **Atlas** control that starts from the preferred atlas set in your profile. The atlas filter is not stored on the record you are editing; only the regions are. The region field lists nothing until you start typing: matches from the selected atlas stream in as you search, which keeps even the largest vocabularies fast. The region tree shown in the forms is loaded lazily, so large hierarchies open quickly. The API offers a `descendants/` action that returns every region below a given region with its depth.

## Available anatomical references

The atlas selector groups the references by species: volumetric brain atlases for mouse, rat, marmoset, macaque, human, zebrafish and fruit fly, whole-body anatomy ontologies (mouse, zebrafish, fruit fly, C. elegans and the cross-species Uberon), and legacy plate-based atlases kept so older entries stay resolvable. Those with a coordinate space behind them also drive the coordinate preview on procedures. The full list, with versions and preview status, is on the [Anatomical references page]({{"datamodel/taxonomies/anatomicalreference/#atlases-in-brainstem"|absolute_url}}).

## Permissions

Anatomical regions and their references are system-managed: they are loaded from the atlases by the BrainSTEM team and are readable by everyone. There is no approval workflow for regions, and they are not created or edited by users. Please reach out to us if you are missing a publicly available atlas that you would like to have incorporated.

## API access

The API allows for read access to anatomical regions and their descendants. Learn more about the fields and data structure on the [Anatomical regions API page]({{"api/taxonomies/anatomicalregion/"|absolute_url}}).
