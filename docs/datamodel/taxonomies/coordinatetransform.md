---
layout: default
title: Coordinate transforms
parent: Taxonomies
grand_parent: Data model
nav_order: 5
---

# Coordinate transform model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A coordinate transform is a named, versioned mapping from one BrainSTEM [coordinate system]({{"datamodel/schemas/coordinates/"|absolute_url}}) to one atlas ([anatomical reference]({{"datamodel/taxonomies/anatomicalreference/"|absolute_url}})). It is what lets BrainSTEM preview a stereotaxic bregma-based coordinate inside the Allen CCFv3 volume, or a Waxholm Space coordinate inside the rat atlas. Each transform states how the mapping is done, how good it is, where it comes from, and what caveats apply.

Transforms are system-managed and read-only. They are seeded from a reviewed catalogue together with the anatomical references. A [procedure]({{"datamodel/modules/procedure/"|absolute_url}}) can record the anatomical reference and the coordinate transform used for its coordinate preview, so the record says which mapping produced the atlas view.

{% include datamodel_embed.html model="taxonomies.coordinatetransform" %}

## Fields

All fields are read-only.

| Field | Description |
|:------|:------------|
| `Code` | Stable machine-readable identifier of the transform (unique across BrainSTEM). Example: "mouse_bregma_surface_to_ccfv3_ibl_v1" |
| `Name` | Name of the transform. Example: "IBL mouse Bregma surface estimate to Allen CCFv3" |
| `Version` | Version of the transform. Example: "1.0.0" |
| `Source coordinate system` | The BrainSTEM coordinate system the transform maps from. One of the procedure coordinate systems, for example Stereotaxic Bregma-based absolute coordinates, Stereotaxic Bregma-based surface coordinates with depth, Landmark AP/ML/DV absolute, CCF XYZ absolute, WHS XYZ absolute. See the [Coordinate systems page]({{"datamodel/schemas/coordinates/"|absolute_url}}). |
| `Anatomical reference` | The [atlas release]({{"datamodel/taxonomies/anatomicalreference/"|absolute_url}}) the transform maps into. |
| `Mapping kind` | How the mapping is computed. Choices: Identity (the coordinates are already in the atlas space; only units and axis conventions apply), Affine 4×4 (a fixed affine matrix from the landmark frame to the atlas), Stereotaxic surface (the entry point is found on the atlas brain surface from the landmark coordinates, then the insertion follows the recorded angles and depth). |
| `Quality` | How much to trust the result. Choices: Exact (a native-space identity mapping), Estimated (a placement in an atlas average based on published landmark positions, not a measured registration). |
| `Method description` | How the mapping works, in one or two sentences. |
| `Provenance URL` | Where the parameters come from. |
| `Citation` | Reference to cite for the mapping. |
| `Warning` | Caveat shown with the preview. Estimated transforms warn that the result is an estimated stereotaxic placement in an atlas average and not a measured registration or ground-truth localization. |
| `Implementation version` | Version of the code that applies the transform (number). |
| `Is active` | Whether the transform is offered for new records. Inactive transforms keep their links to historical records. |

## Transforms in BrainSTEM

The catalogue declares the following transforms.

__Identity transforms (quality Exact)__, one per atlas with a coordinate space: CCF XYZ to Allen CCFv3; WHS XYZ to Waxholm Space v4; MNI152 XYZ to ICBM 152 2009c; NMT XYZ to NMT v2; BMA XYZ to Brain/MINDS Marmoset Atlas 2.0; mapzebrain XYZ to mapzebrain; JRC2018U XYZ to the JRC 2018 Unisex template.

__Estimated landmark transforms (quality Estimated)__:

| Transform | From | To | Mapping kind |
|:----------|:-----|:---|:-------------|
| IBL mouse Bregma estimate to Allen CCFv3 | Stereotaxic Bregma-based absolute coordinates | Allen CCFv3 (mouse) | Affine 4×4 |
| IBL mouse Bregma surface estimate to Allen CCFv3 | Stereotaxic Bregma-based surface coordinates with depth | Allen CCFv3 (mouse) | Stereotaxic surface |
| Rat Bregma landmark estimate to Waxholm Space v4 | Stereotaxic Bregma-based absolute coordinates | Waxholm Space v4 (rat) | Affine 4×4 |
| Rat Bregma surface estimate to Waxholm Space v4 | Stereotaxic Bregma-based surface coordinates with depth | Waxholm Space v4 (rat) | Stereotaxic surface |
| Rat Lambda landmark estimate to Waxholm Space v4 | Stereotaxic Lambda-based absolute coordinates | Waxholm Space v4 (rat) | Affine 4×4 |
| Rat Lambda surface estimate to Waxholm Space v4 | Stereotaxic Lambda-based surface coordinates with depth | Waxholm Space v4 (rat) | Stereotaxic surface |
| Marmoset interaural landmark estimate to BMA 2.0 | Landmark AP/ML/DV absolute coordinates | Brain/MINDS Marmoset Atlas 2.0 | Affine 4×4 |
| Marmoset interaural surface estimate to BMA 2.0 | Landmark AP/ML surface coordinates with depth | Brain/MINDS Marmoset Atlas 2.0 | Stereotaxic surface |

The estimated transforms place a coordinate in an atlas average from published landmark positions. Cranial landmarks vary between animals, so treat the preview as an orientation aid, not as a measured localization. The marmoset transforms carry an additional warning: the interaural line is not annotated in BMA 2.0, and the position used differs by about 1 mm anterior-posterior between published templates.

## Permissions

Coordinate transforms are shared by everyone and readable by all users. They are maintained by the BrainSTEM team and cannot be edited through the web interface or the API. A transform cannot be deleted while procedures point to it.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for read access to coordinate transforms. Learn more about the coordinate transforms' fields and data structure on the [Coordinate transform API page]({{"api/taxonomies/coordinatetransform/"|absolute_url}}).
