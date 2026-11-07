---
layout: default
title: Procedures
parent: Subjects
grand_parent: Data model
nav_order: 1
---

# Procedure model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A procedure describes one technical, experimental or clinical action performed on one subject: an anesthesia or drug administration, a surgical step, an implant, an injection, a sample collection, a tissue procedure or an endpoint. Procedures have type-specific fields tailored to each procedure type. Use separate procedures when actions have different types, even when they occur during the same intervention.

Three related models complete the picture:

- A [__Procedure episode__]({{"datamodel/modules/procedureepisode/"|absolute_url}}) optionally groups related procedures into one perioperative event, with personnel, protocol, licenses, timing, classified severity and recovery outcome.
- The materials a procedure used (drugs, viruses, probes, cement) are ordered [__Material usage__]({{"datamodel/modules/materialusage/"|absolute_url}}) rows, not fields of the procedure.
- An implant procedure creates an [__Experimental interface__]({{"datamodel/modules/experimentalinterface/"|absolute_url}}): the probe, fiber, cannula, window or sensor that remains available for later sessions.

Ex-vivo tissue work (slicing, sectioning, clearing, staining) is recorded as a [__Specimen procedure__]({{"datamodel/modules/specimenprocedure/"|absolute_url}}) on a specimen set, not as a procedure.

[![Saving an implant procedure creates an experimental interface on the subject. Sessions record through the interface, so a data acquisition inherits where (target region, coordinates) and with what (materials) it was made.]({{site.baseurl}}/assets/images/diagrams/procedure-interface-session.svg)]({{site.baseurl}}/assets/images/diagrams/procedure-interface-session.svg)
*Saving an implant procedure creates an experimental interface on the subject. Sessions record through the interface, so a data acquisition inherits where (target region, coordinates) and with what (materials) it was made.*

{% include datamodel_embed.html model="modules.procedure" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Type of procedure`` | Type of procedure (**required**). Selected from the predefined types listed below. The type controls the type-specific fields and which coordinate systems, regions, equipment and materials apply. Fixed once materials or stages exist (see [What becomes fixed](#what-becomes-fixed)). |
| ``Status`` | Planned, performed or cancelled (default: performed). Performed means the record describes what was done. A planned procedure is prepared ahead of time; its page carries a banner, its title says "Planned", and it is left out of counts, exports and API listings unless asked for. Mark it performed once it has happened (the date and time is then required). Cancelled keeps a dropped plan for the record. |
| ``Subject`` | The subject the procedure was performed on (**required**). Must reference an existing [subject]({{"datamodel/stem/subject/"|absolute_url}}). Fixed once the procedure has created an experimental interface (see [What becomes fixed](#what-becomes-fixed)). |
| ``Procedure episode`` | The [procedure episode]({{"datamodel/modules/procedureepisode/"|absolute_url}}) this action belongs to. The episode and the procedure must refer to the same subject. |
| ``Date and time of the procedure`` | Onset date and time of this individual action. Example: "2024-03-22 10:30:00" |
| ``Performed by`` | The person who physically performed the procedure, which can differ from the user who entered it. Eligible users come from the subject's projects; the current user is suggested. |
| ``Licenses`` | [Licenses]({{"datamodel/personal_attributes/license/"|absolute_url}}) authorizing this specific procedure. You can add licenses where you are at least a Contributor. |
| ``Protocol`` | Optional reusable [protocol]({{"datamodel/personal_attributes/protocol/"|absolute_url}}) describing the method followed. Must have protocol type Procedure and either no subtype restrictions or include this procedure type. Selecting a protocol does not fill in any fields; use a [procedure template]({{"datamodel/modules/templates/"|absolute_url}}) for that. |
| ``Setup`` | Form-only filter for the equipment field. Not stored. |
| ``Equipment`` | Reusable [equipment]({{"datamodel/modules/equipment/"|absolute_url}}) used to perform the action. Only setups where you are at least a Contributor, and their equipment, are offered. Materials used or installed belong in material usage, not here. |
| ``Atlas`` | Form-only filter for target regions, starting from the preferred atlas set in your profile. Not stored. |
| ``Target regions`` | The [anatomical regions]({{"datamodel/taxonomies/anatomicalregion/"|absolute_url}}) targeted by the action, chosen from the active atlas. Several regions can be selected. Hidden for types without an anatomical target. |
| ``Anatomical reference`` | The atlas release ([anatomical reference]({{"datamodel/taxonomies/anatomicalreference/"|absolute_url}})) the coordinates are interpreted against for the coordinate preview. |
| ``Coordinate transform`` | The named, versioned [coordinate transform]({{"datamodel/taxonomies/coordinatetransform/"|absolute_url}}) that maps the selected coordinate system into that atlas. Each transform states its mapping kind and quality (exact or estimated). |
| ``Coordinate system`` | How the location of the action is referenced (**required** when shown). The available systems are narrowed by the procedure type. *See options below* |
| ``Coordinates`` | Position and orientation in the selected coordinate system. Hidden when coordinates do not apply to the type. |
| ``Notes`` | Complications, adverse events, deviations or other detail without a structured field (string; maximum length: 500 characters). |
| ``Type specific fields`` | Structured fields defined by the procedure type. See the [Procedure types schema]({{"datamodel/schemas/procedure/"|absolute_url}}). |
| ``Materials`` | Ordered [material usage]({{"datamodel/modules/materialusage/"|absolute_url}}) rows for the materials actually used: a stock lot from an inventory, a catalog consumable, or a manually described material. Each row has a material type, shown under its role name for this procedure type, and the types allowed depend on the procedure type. Materials can be entered before the procedure is first saved. |
| ``Stages`` | Some types divide the action into ordered [stages]({{"datamodel/modules/procedurestage/"|absolute_url}}): an anesthesia has induction and maintenance stages, a perfusion fixation a flush and a fixation stage. Each material row names the stage it took part in. Stages and their materials are edited together on the Materials tab. |

## Experimental interfaces created by procedures

Procedure types that establish an interface (marked below) automatically create the corresponding [experimental interface]({{"datamodel/modules/experimentalinterface/"|absolute_url}}) when the procedure is saved as performed. The procedure documents the action at a particular time; the interface describes the resulting probe, cannula, window or sensor. The interface also receives a copy of the installed materials (the device, plus materials its own type accepts); materials merely consumed during the action, such as adhesives or irrigation, stay on the procedure. Deleting the procedure leaves the interface in place.

{: .important }
The procedure remains the source of the interface's type, installation date, coordinates, target regions, equipment and copied materials. Later changes on the procedure overwrite these values on the interface, and the interface form shows them locked. Make such corrections on the procedure.

Data acquisitions and manipulations do not link to procedures. They link to the experimental interfaces they used, and the installing procedure is reached through the interface.

## What becomes fixed

- The **Type of procedure** cannot be changed once the procedure has materials or stages.
- The **Subject** cannot be changed once the procedure has created an experimental interface.
- On the interface it created, the values the procedure owns (see above) are edited on the procedure, not on the interface.

## Types of procedures

These are the available type options for procedures. See the schema for field details: [Procedure types]({{"datamodel/schemas/procedure/"|absolute_url}}). Types marked with an asterisk (*) create an experimental interface when saved.

### Anesthesia, Drug and Fluid Administration

The agent and its body-weight dose are recorded on the active-agent material row; the procedure records the event-level route, volume, timing and indication.

`Analgesic`: Administration of a pain-relieving agent, such as buprenorphine or meloxicam, for systemic analgesia before, during or after a potentially painful intervention.

`Anesthesia`: Administration of anesthetic agents to induce unconsciousness, analgesia or sedation. Induction, maintenance, top-ups, reversal and emergence are recorded as stages, each with its route, delivery method, gas concentration, volume, rate and duration.

`Anti-inflammatory`: Administration of a corticosteroid, NSAID or another agent to reduce inflammation.

`Antibiotic`: Administration of an antimicrobial agent, whether preventive, as treatment, or as the experimental manipulation itself.

`Drug administration (other)`: Catch-all for medication that does not fit a dedicated type, such as a hormone, reversal agent, antidote or supplement. File by why the drug was given: meloxicam for pain is an analgesic.

`Fluid therapy`: Administration of a physiological solution, such as saline or Ringer's solution, for hydration or volume support.

`Local anesthetic`: A site-directed nerve block, infiltration or topical application, such as bupivacaine at an incision line. Use Analgesic for systemic pain relief.

`Sedative`: A sedative or anxiolytic given for non-surgical restraint, imaging or transport, as distinct from full anesthesia.

### Surgical Procedures

`Baseplating`: Attachment of a baseplate. This type has no type-specific fields; record the materials used as material usage rows.

`Burr hole`: A small hole drilled in the skull to provide access for electrode placement, cannula insertion or injection while maintaining skull integrity.

`Cranial window` *: A section of skull opened and fitted with a transparent window for direct, often long-term optical access to the brain surface.

`Craniectomy`: Surgical removal of a portion of the skull that is not replaced afterwards.

`Craniotomy`: Temporary removal of a skull section to expose the brain, with the bone flap normally replaced afterwards.

`Head fixation`: Immobilization of the subject's head for stable recordings, manipulations or imaging. Use Headpost for attaching the fixation device.

`Headcap` *: Attachment of a protective covering over cranial implants while retaining any required access points.

`Headpost`: Attachment of a device to the skull that enables later head fixation.

### Implant Procedures

`Blood pressure sensor implant`: Surgical placement of a sensor to monitor blood pressure continuously or repeatedly.

`Breathing sensor implant`: Placement of a sensor used to monitor respiratory patterns or rate.

`Cannula implant`: Implantation of a guide or infusion cannula for targeted delivery, sampling, microdialysis or cerebrospinal-fluid access.

`Catheter implant` *: Insertion of a flexible tube into a vessel or body cavity for delivery, sampling, drainage or pressure monitoring.

`ECG implant (Electrocardiography)` *: Placement of electrodes to record the electrical activity of the heart.

`EEG implant (Electroencephalography)` *: Placement of electrodes on or beneath the skull to record large-scale brain electrical activity.

`ECoG implant (Electrocorticography)` *: Placement of a flexible grid or strip array on the brain surface, above or beneath the dura, or on thinned skull. The array itself is the required ECoG array material row, sourced from your ECoG array stock or the catalog.

`EMG implant (Electromyography)` *: Placement of electrodes in or on muscles to record muscle electrical activity.

`GRIN (Gradient Index) lens implant` *: Implantation of a gradient-index lens for optical access to deep tissue.

`Nerve cuff implant` *: Placement of a cuff electrode around a peripheral nerve for recording or stimulation.

`Optic fiber implant` *: Placement of an optical fiber for delivering or collecting light, as in optogenetic stimulation or fiber photometry.

`Prism implant` *: Placement of a prism that redirects the optical path to make a difficult-to-access tissue plane visible.

`Reference electrode implant` *: Placement of an electrode that supplies a reference signal for other recording electrodes.

`Silicon probe implant` *: Insertion of a silicon-based neural probe with one or more recording sites. The probe is a Silicon probe material row.

`Single wire electrode implant` *: Implantation of a single wire electrode for neural recording or stimulation.

`Temperature sensor implant`: Placement of a sensor used to monitor body or tissue temperature.

`Tetrode wire electrode implant` *: Implantation of a four-wire electrode bundle. The coordinate depth is where the bundle sat when the surgery ended; the Tetrode adjustment log counts from there.

`Generic implant` *: Use only when an implantation does not fit any specific implant type above.

### Injection and Infusion Procedures

`Injection`: Delivery of a solution to a defined anatomical site: pharmacological agents, tracers, cells or other injected materials that are not viral vectors.

`Virus injection`: Injection of a viral vector to introduce or manipulate genetic material in a target population. Each vector and its volume is a material usage row.

### Sample Collection Procedures

`Blood collection`: Collection of blood from a defined site for hematology, serum or plasma preparation, biochemistry, pharmacokinetics or genotyping.

`Tissue collection`: Collection of non-brain tissue, such as a tail tip, ear punch, biopsy or excised tissue.

### Brain and Tissue Procedures

`Brain extraction`: Removal of the brain following an endpoint procedure for subsequent analysis.

`Brain lesion`: Deliberate injury or destruction of a defined brain region to investigate its functional contribution.

`Brain perfusion fixation`: Perfusion of fixative through the circulatory system. It remains a procedure because it is performed on the subject; the perfusion phases are recorded as an ordered table in the details.

### Endpoint Procedures (Euthanasia)

`Cervical dislocation`: A physical method involving separation of the cervical vertebrae.

`Decapitation`: A rapid physical endpoint method, including when tissue must be collected immediately.

`CO₂ chamber euthanasia`: Euthanasia using controlled exposure to carbon dioxide in a chamber.

`Barbiturate injection`: Euthanasia by administration of a barbiturate solution.

`Inhalant overdose`: Euthanasia using an overdose of an inhalant anesthetic.

### Retired types

The in-vivo tissue types `Brain slice`, `Cryosectioning`, `Tissue clearing` and `Vibratome sectioning` were retired in this release. Existing records were converted to [specimen procedures]({{"datamodel/modules/specimenprocedure/"|absolute_url}}), which is where ex-vivo tissue work is now recorded. The abstract stimulation and tracking procedure types (auditory, visual, tactile and odor stimulation, behavioral tracking) were removed; the stimulating or tracking device is now an [experimental interface]({{"datamodel/modules/experimentalinterface/"|absolute_url}}) and the stimulus itself a [manipulation]({{"datamodel/modules/manipulation/"|absolute_url}}).

## Coordinate systems

A procedure records where it was done in one of 17 coordinate systems: external XYZ frames, stereotaxic coordinates from bregma or lambda (absolute, or surface coordinates with depth), landmark-referenced and spinal systems, and the native spaces of the atlases BrainSTEM ships (Allen CCFv3, Waxholm rat, MNI152, NMT macaque, mapzebrain, JRC2018 fly, Brain/MINDS marmoset). The systems offered are narrowed by the procedure type. Each system, its reference points and its fields are described on the [Coordinate systems page]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## Permissions

Procedures inherit permissions through the projects of the subject associated with them. The form limits subjects and related entries to choices you are permitted to use. Material usages inherit their permissions through the procedure, while inventory stock keeps its own permission rules.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to procedures. Structured data uses `details`, and coordinates use `coordinates_system` and `coordinates_details`. Materials and stages are returned with the procedure and can be read or replaced through the procedure's `materials/` endpoint. Learn more about the procedures' fields and data structure on the [Procedures API page]({{"api/modules/procedure/"|absolute_url}}).
