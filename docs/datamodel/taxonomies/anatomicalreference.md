---
layout: default
title: Anatomical references (atlases)
parent: Taxonomies
grand_parent: Data model
nav_order: 4
---

# Anatomical reference model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

An anatomical reference is one release of an anatomical atlas or anatomy ontology: the Allen Mouse Common Coordinate Framework CCFv3 (2017), the Waxholm Space rat atlas v4.01, the Brain/MINDS marmoset atlas 2.0, and so on. It records the identity of the release (code, name, version), the species and organ it covers, its coordinate space (axes orientation, origin, native unit) and where it comes from (source, homepage, citation, license). Anatomical references are system-managed: they are created and updated by the BrainSTEM team from a reviewed catalogue, and they are read-only for users. Please reach out to us if you would like a publicly available atlas added.

Every [anatomical region]({{"datamodel/taxonomies/anatomicalregion/"|absolute_url}}) belongs to one anatomical reference. The same acronym (for example "CA1") exists in several atlases, so a region is always identified together with its reference. Procedures, experimental interfaces, specimen sets and specimen procedures record their anatomy as target regions, and the atlas filter in those forms is a choice of anatomical reference. A [procedure]({{"datamodel/modules/procedure/"|absolute_url}}) can also name the anatomical reference and the [coordinate transform]({{"datamodel/taxonomies/coordinatetransform/"|absolute_url}}) used to preview its coordinates in that atlas.

{% include datamodel_embed.html model="taxonomies.anatomicalreference" %}

## Fields

All fields are read-only.

| Field | Description |
|:------|:------------|
| `Code` | Stable machine-readable identifier of the release (unique across BrainSTEM). Example: "allen_mouse_ccfv3_2017", "whs_sd_rat_v4" |
| `Name` | Name of the atlas or ontology. Example: "Allen Mouse Common Coordinate Framework" |
| `Version` | Version of the release. Example: "CCFv3 2017", "v4.01", "2.0" |
| `Species` | The [species]({{"datamodel/taxonomies/species/"|absolute_url}}) the atlas covers. Empty for cross-species vocabularies such as Uberon. |
| `Organ` | What the atlas covers. Choices: Brain, Spinal cord, Whole body. Whole-body references are anatomy ontologies without a coordinate space. |
| `Region atlas code` | Short legacy atlas code used as the stable public identifier in payloads and as the atlas label on regions. Example: "AIA", "WHS4", "BMA2" |
| `Coordinate space identifier` | Name of the coordinate space of the release. For metadata-only legacy entries this reads "Metadata-only legacy atlas catalogue entry". |
| `Axes orientation` | Which anatomical direction each of the x, y and z axes points to. Example: x right, y posterior, z superior. |
| `Native unit` | Unit of the atlas coordinates. Example: "mm" (most atlases), "µm" (mapzebrain, JRC2018U). |
| `Source` | The organization or project that published the release. |
| `Homepage` | Website of the atlas. |
| `Citation` | Reference to cite when you use the atlas. |
| `License name` and `License URL` | License the atlas is distributed under. Example: "CC BY 4.0" |
| `Asset manifest URL` | Location of the published visualization assets (annotation volumes and lookups) built from the release. Empty when no assets are published. |
| `Visualization status` | Whether the coordinate preview is available for this release. Choices: Available (coordinates can be previewed in the atlas), Metadata only (the release is described and its regions can be used, but there is no preview), Disabled. |
| `Is active` | Whether the release is offered in atlas pickers. Inactive releases keep their links to historical records but are not offered for new ones. |

## Atlases in BrainSTEM

The following references are declared in the BrainSTEM atlas catalogue. Which of them carry regions and a coordinate preview on a given server depends on which atlases have been imported.

### Volumetric atlases

| Atlas | Species | Version | Code | Coordinate preview |
|:------|:--------|:--------|:-----|:-------------------|
| Allen Mouse Common Coordinate Framework | Mouse (*Mus musculus*) | CCFv3 2017 | AIA | Available |
| Waxholm Space Sprague Dawley Rat Brain Atlas | Rat (*Rattus norvegicus*) | v4.01 | WHS4 | Available |
| Brain/MINDS Marmoset Brain Atlas | Marmoset (*Callithrix jacchus*) | 2.0 | BMA2 | Available |
| NIMH Macaque Template (NMT) v2, symmetric | Rhesus macaque (*Macaca mulatta*) | 2.1 | NMT2 | Available |
| mapzebrain (Max Planck Zebrafish Brain Atlas) | Zebrafish (*Danio rerio*) | reference v2 / annotation 2.0 | MZB | Available |
| ICBM 152 Nonlinear Asymmetric template (MNI152) | Human (*Homo sapiens*) | 2009c | MNI152 | Metadata only |
| JRC 2018 Unisex Drosophila Brain Template | Fruit fly (*Drosophila melanogaster*) | 2018 | JRC18U | Metadata only |

### Anatomy ontologies (whole body, no coordinate space)

| Ontology | Species | Code |
|:---------|:--------|:-----|
| Adult Mouse Gross Anatomy (EMBL-EBI) | Mouse | MA |
| Uberon multi-species anatomy ontology | Cross-species | UBERON |
| Zebrafish anatomy and development ontology | Zebrafish | ZFA |
| C. elegans gross anatomy ontology | *Caenorhabditis elegans* | WBbt |
| Drosophila gross anatomy ontology | Fruit fly | FBbt (inactive until its release is imported) |

### Legacy atlases (metadata only)

These references carry regions from earlier BrainSTEM releases but have no coordinate space or preview: Paxinos and Franklin Mouse Brain Atlas (2001), Allen Developing Mouse Brain Atlas, Allen Spinal Cord Atlas (mouse), BrainMaps Rat Brain Atlas 4.0, Paxinos and Watson Rat Brain Atlas (1997), Swanson Rat Brain Atlas (2004), Allen Human Brain Atlas, Allen Developing Human Brain Atlas and Allen Non-Human Primate Brain Atlas.

## Coordinate preview

For references with visualization status "Available", BrainSTEM can show the coordinates of a procedure or experimental interface inside the atlas, using the annotation volumes published at the asset manifest URL. Coordinates entered in a BrainSTEM coordinate system (for example stereotaxic bregma-based coordinates) are mapped into the atlas through a [coordinate transform]({{"datamodel/taxonomies/coordinatetransform/"|absolute_url}}); coordinates entered directly in the atlas space (for example CCF XYZ) use the identity transform of that atlas. Whole-body ontologies never have a preview.

## Permissions

Anatomical references are shared by everyone and readable by all users. They are created and maintained by the BrainSTEM team; there is no approval workflow and no user editing. A reference cannot be deleted while regions, coordinate transforms or procedures point to it.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for read access to anatomical references. Learn more about the anatomical references' fields and data structure on the [Anatomical reference API page]({{"api/taxonomies/anatomicalreference/"|absolute_url}}).
