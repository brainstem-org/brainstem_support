---
layout: default
title: Atlases and coordinates
parent: Assistants and references
grand_parent: Web interface
nav_order: 2
---

# Atlases and coordinates
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

BrainSTEM records where in the brain a procedure, implant or recording interface was placed in two ways: as coordinates in a named coordinate system, and as target regions from a brain atlas. For the common lab species an interactive coordinate viewer shows the planned entry point and track inside the atlas. The coordinate schemas themselves are documented on the [Coordinates schema]({{"datamodel/schemas/coordinates/"|absolute_url}}) page.

## Coordinate systems

The **Coordinates** field appears on procedure types that place something in the brain (burr hole, craniotomy, craniectomy, cranial window, the implant types, injection, virus injection and brain lesion), on experimental interfaces and on equipment. Choose a coordinate system first; the fields of that system then appear. The dropdown is grouped:

- **Stereotaxic coordinates**: measured from Bregma or Lambda, either as an absolute point (AP, ML, DV) or as a surface point with a depth (AP, ML, depth).
- **Landmark-referenced coordinates**: the same two forms measured from a landmark you name (**Landmark reference**: obex, interaural zero, anterior commissure, and others).
- **Spinal coordinates**: rostro-caudal, medio-lateral and depth or dorso-ventral positions on the spinal cord.
- **Standardized reference spaces**: x, y and z in the voxel space of a published atlas (Allen Mouse CCFv3, Waxholm Space Rat, MNI152 Human, NIMH Macaque Template, mapzebrain Larval Zebrafish, JRC2018 Fly Brain, Brain/MINDS Marmoset). Each space has its own origin; the macaque template, for example, measures from ear bar zero, the midpoint between the ear bars of the stereotaxic frame.

Surface systems take **AP coordinate** (positive is anterior), **ML coordinate** (positive is right), **Depth** from the brain surface, **AP angle**, **ML angle** and **Rotation**; absolute systems take a **DV coordinate** instead of depth. Lengths can be entered in nm, µm, mm or m (default mm), angles in degrees. Every system, its fields and the sign and angle conventions are listed on the [Coordinate systems]({{"datamodel/schemas/coordinates/"|absolute_url}}) page.

![The stereotaxic axes: AP positive anterior, ML positive to the right, DV positive ventral.]({{site.baseurl}}/assets/images/coordinates/coordinates2.png){: width="40%"}
*The stereotaxic axes. Bregma and Lambda, and the AP and ML angles and the rotation, are drawn on the [Coordinate systems]({{"datamodel/schemas/coordinates/"|absolute_url}}) page.*

## The atlas selector and target regions

The **Atlas** field chooses the reference atlas for the target regions: "The active anatomical atlas. You can set your preferred atlas in your profile". The list holds the active atlases with imported regions, grouped by species, and is preloaded with the **Atlas preference** from your [profile]({{"webinterface/user-profile/#atlas-preference"|absolute_url}}). When the subject's species has exactly one compatible atlas, it is selected automatically. The atlas must match the subject's species ("The atlas must match the subject species."), and a subject's species cannot be changed while its procedures reference an atlas of another species.

![Choosing target regions: typing CA1 lists CA1 : Cornu ammonis 1; CA1 and CA3 are already selected.]({{site.baseurl}}/assets/images/screenshots/atlases-region-picker.png)
{: .screenshot }
*Choosing target regions: typing CA1 lists CA1 : Cornu ammonis 1; CA1 and CA3 are already selected.*

**Target regions** is a searchable picker that loads regions from the selected atlas as you type (**Type to search the selected atlas…**). Type at least one character; names are matched first, then acronyms, and regions are shown as "ACRONYM : Name". Obsolete terms are hidden. All target regions must belong to the selected atlas, and changing the atlas clears the selected regions. The picker is used on procedures, procedure templates, episodes, specimen procedures, specimen sets and experimental interfaces.

In list views the **Anatomical region** filter offers the same regions as a tree with subregions, see [List view]({{"webinterface/list-view/#anatomical-region-filter"|absolute_url}}).

## Atlases with a coordinate viewer

These atlases have region trees and a 2D/3D viewer:

| Species | Atlas | Status |
|---------|-------|--------|
| Mouse | **Allen Mouse Common Coordinate Framework** (CCFv3, 50 µm) | Established |
| Rat | **Waxholm Space Sprague Dawley Rat Brain Atlas** (v4, 78 µm) | Established |
| Marmoset | **Brain/MINDS Marmoset Brain Atlas** (2.0, 100 µm) | Newer; viewer assets published after review |
| Macaque | **NIMH Macaque Template (NMT) v2, symmetric** (250 µm) | Newer; viewer assets published after review |
| Zebrafish (larval) | **mapzebrain (Max Planck Zebrafish Brain Atlas)** (2 µm) | Newer; viewer assets published after review |

The mouse, rat and marmoset atlases are bilateral: left and right regions are folded into one tree. Two further reference spaces are available as coordinate systems only, without regions or a viewer: the **ICBM 152 Nonlinear Asymmetric template** (human MNI152) and the **JRC 2018 Unisex Drosophila Brain Template**.

### How stereotaxic coordinates are placed in an atlas
{: .no_toc}

Coordinates given directly in an atlas space (the XYZ systems) are shown exactly. Stereotaxic coordinates are estimated: mouse Bregma coordinates through a published Bregma-to-CCF estimate, rat Bregma and Lambda coordinates through the Waxholm registration, and marmoset landmark coordinates relative to interaural zero with a caveat of about 1 mm. Lambda-based mouse coordinates and macaque or zebrafish stereotaxic coordinates cannot be previewed.

{: .note }
> A stereotaxic placement in the viewer is an estimate in an atlas average, not your animal's anatomy. Every estimated placement says so: "Estimated stereotaxic placement in an atlas average. This is not a measured registration or ground-truth localization." Confirm the actual position with histology.

## Region-only vocabularies

At the time of writing, thirteen further atlases and ontologies provide region trees for target regions without a coordinate viewer:

- Mouse: Paxinos and Franklin Mouse Brain Atlas (2001), Allen Developing Mouse Brain Atlas, Allen Spinal Cord Atlas, Adult Mouse Gross Anatomy
- Rat: BrainMaps Rat Brain Atlas (4.0), Paxinos and Watson Rat Brain Atlas (1997), Swanson Rat Brain Atlas (2004)
- Human: Allen Human Brain Atlas, Allen Developing Human Brain Atlas
- Non-human primate: Allen Non-Human Primate Brain Atlas
- Zebrafish: Zebrafish anatomy and development ontology (ZFA)
- C. elegans: C. elegans gross anatomy ontology (WBbt)
- Cross-species: Uberon multi-species anatomy ontology

## View coordinates

The **View coordinates** button sits next to the coordinates on the procedure form, on the procedure details page (**Coordinates · {system}**), on procedure rows of the subject page and on the episode form. It is enabled once a subject with a species, a supported coordinate system, a compatible atlas and the required values are set. When disabled, its tooltip says why: "Choose a subject.", "Choose a supported coordinate system.", "No coordinate viewer is available for this species and coordinate system.", "Choose a compatible atlas.", "Coordinate viewer assets are unavailable for this atlas." or "Enter a value for AP coordinate…". XYZ systems need x, y and z; absolute systems AP, ML and DV; surface systems AP, ML and depth (burr holes and ECoG implants need no depth).

{% include slides.html slides="forms-coordinates|The procedure's coordinate system with the View coordinates button that opens the viewer.;;atlases-viewer-rat-3d|A silicon probe implant in the Waxholm Space Sprague Dawley rat atlas: the probe track in 3D.;;atlases-viewer-rat-all-planes|All planes: coronal, sagittal and horizontal sections through the probe tip, with the region under the cursor (Dentate gyrus) at the bottom." %}

### The coordinate viewer
{: .no_toc}

The **Coordinate viewer** ("View coordinates and implantation track in anatomical atlas.") opens in a dialog with these controls:

- Views: **3D**, **All planes**, **Coronal**, **Sagittal**, **Horizontal**, **Reset views**.
- **Coordinates** readout: **Off**, **Atlas** or **Stereotaxic**; **Preview atlas** when more than one atlas fits.
- **Reference**: **Off**, **Axes** or **Planes**; **Scale bars**, **Auto rotate**, **Legend**.
- **Brain opacity** (default 75 %), **Brain regions** overlay with **Region opacity** and **Filled** or **Outlines** (2D only; region volumes are downloaded on demand).
- Readouts **Position:** and **Region:** under the cursor; legend **Entry point**, **Endpoint**, **Implantation axis**. "A faint dashed guide shows a nearby track up to 2 mm away."

The device is drawn from the procedure: a silicon probe with the shank count, pitch and thickness of the probe design recorded in the Materials tab ("No silicon-probe material is saved; a schematic single shank is shown." otherwise), an optic fiber, an injection volume, a single wire or reference electrode, a burr hole or ECoG array on the surface, or a generic implantation trajectory. Atlas attribution and licence are shown in the dialog.

## Related

- [Coordinate systems]({{"datamodel/schemas/coordinates/"|absolute_url}}): every system with its fields, units and sign conventions
- [Anatomical references (atlases)]({{"datamodel/taxonomies/anatomicalreference/"|absolute_url}}) and [Anatomical regions]({{"datamodel/taxonomies/anatomicalregion/"|absolute_url}}): the atlases and their region trees
- [Procedures]({{"datamodel/modules/procedure/"|absolute_url}}) and [Experimental interfaces]({{"datamodel/modules/experimentalinterface/"|absolute_url}}): the entries that carry coordinates and target regions
- [Submission forms]({{"webinterface/forms/#coordinates"|absolute_url}}): the **Coordinates** and **Atlas** fields in the form
- [Probe catalog]({{"webinterface/probe-catalog/"|absolute_url}}): the probe designs the viewer draws
- [User profile]({{"webinterface/user-profile/#atlas-preference"|absolute_url}}): setting your **Atlas preference**
