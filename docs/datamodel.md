---
layout: default
title: Data model
nav_order: 3
has_children: true
has_toc: false
---
# Data model
{: .no_toc}

A recording means little on its own. To interpret, compare or reproduce it, one needs to know which animal or tissue it came from, what was done to it beforehand, where in the brain the electrode or fiber sat, which hardware and reagents were used, what the animal was doing, and under which approval the work was done. In most labs this context is spread over surgery sheets, notebooks, spreadsheets and file names, and much of it leaves with the people who wrote it.

BrainSTEM records this context as linked, structured records in a relational data model. Each record describes one thing: a subject, a procedure, a session, an implanted probe. The links between records carry the scientific relations. An implant procedure creates an experimental interface; a data acquisition names the interfaces it recorded through and so inherits their anatomical target and hardware; a session links the subjects or specimen sets it was performed on. A question such as *which mice received a virus injection in CA1 and were later recorded with a silicon probe during a running task* becomes a query over records instead of a search through notes.

Three principles shape the model:

- **Shared vocabularies for comparison.** Species, strains, brain regions, behavioral paradigms and regulatory authorities come from shared taxonomies; anatomical positions are coordinates in a named atlas; reagents and devices come from a shared catalog, where an entry can carry its RRID. Records from different labs use the same terms.
- **Method-specific detail.** Procedures, recordings, manipulations, interfaces, materials and logs have a type, such as a silicon probe implant, a virus injection or two-photon imaging. Each type has its own fields, validated against a versioned JSON schema, so a record holds the parameters that matter for that method.
- **Metadata, not raw data.** BrainSTEM describes the experiment and records where the data are stored; the recordings themselves stay in the lab's storage. Records export as JSON or convert to Neurodata Without Borders (NWB) files for archiving and sharing, for example on DANDI.

Records belong to projects, which decide who can see and edit them, so a lab keeps its work private until it chooses to share or publish it.

### The model at a glance
{: .no_toc}

The **Overview** below is a drawing of the whole model; the **Interactive** view is the complete current model, copied from the BrainSTEM server's public reference: every model as a card with its fields, every relation, where each model inherits its permissions from, and the fields of every type. **Expand** opens it with its search, layouts, layers and detail panel. The same diagram is embedded on each model page, focused on that model, and is available inside BrainSTEM from the Help menu and the Graph tab of every help dialog.

{% include datamodel_switch.html image="/assets/images/diagrams/data-model-overview.svg" alt="Overview of the BrainSTEM data model: users and groups hold roles on projects; projects own subjects, specimen sets and sessions with their modules; personal attributes are owned and shared by users and groups, like projects; the shared catalog and taxonomies are used by everyone" title="Interactive data model" query="view=overview&show=shared" max_height="1400" %}

### Where do I record it?
{: .no_toc}

What happened decides which kind of entry records it: an action on a subject, an observation over time, a device that stays in place, tissue taken out, or what was measured, delivered or done in a session.

[![Which kind of entry records what happened: procedures, subject logs, interfaces, specimen sets, data acquisition, manipulations, behaviors, epochs and material usage]({{site.baseurl}}/assets/images/diagrams/where-to-record.svg)]({{site.baseurl}}/assets/images/diagrams/where-to-record.svg)
*Which kind of entry records what happened. Each kind has its own page under [Organization of the models](#organization-of-the-models).*

### Organization of the models
{: .no_toc}

The model is structured into these main categories:

- [__Projects__]({{"datamodel/stem/project/"|absolute_url}}): the organizational unit of a study. Projects hold the subjects, specimen sets and sessions, define who can see and edit them, and link to publications.
- [__Subjects__]({{"datamodel/stem/subject/"|absolute_url}}): the animals studied in vivo, with their species, strain, sex and lifecycle status. Related records: [Procedures]({{"datamodel/modules/procedure/"|absolute_url}}), [Procedure episodes]({{"datamodel/modules/procedureepisode/"|absolute_url}}), [Subject logs]({{"datamodel/modules/subjectlog/"|absolute_url}}), [Procedure logs]({{"datamodel/modules/procedurelog/"|absolute_url}}), [Experimental interfaces]({{"datamodel/modules/experimentalinterface/"|absolute_url}}), [Breedings]({{"datamodel/stem/breeding/"|absolute_url}}) and [Cohorts]({{"datamodel/stem/cohort/"|absolute_url}}).
- [__Specimen sets__]({{"datamodel/stem/specimenset/"|absolute_url}}): ex-vivo material prepared together, such as a slice series, a section series, an organoid batch, a culture or a well plate, usually taken from a subject. Related records: [Specimens]({{"datamodel/stem/specimen/"|absolute_url}}), [Specimen procedures]({{"datamodel/modules/specimenprocedure/"|absolute_url}}) and [Specimen logs]({{"datamodel/modules/specimenlog/"|absolute_url}}).
- [__Sessions__]({{"datamodel/stem/session/"|absolute_url}}): experimental sessions on subjects or specimen sets. Related records: [Behaviors]({{"datamodel/modules/behavior/"|absolute_url}}), [Data acquisition]({{"datamodel/modules/dataacquisition/"|absolute_url}}), [Manipulations]({{"datamodel/modules/manipulation/"|absolute_url}}), [Epochs]({{"datamodel/stem/epoch/"|absolute_url}}) and [Collections]({{"datamodel/stem/collection/"|absolute_url}}).
- [__Materials__]({{"datamodel/materials/"|absolute_url}}): the chain from the shared consumable catalog through a lab's stock to the [material usage]({{"datamodel/modules/materialusage/"|absolute_url}}) rows that record what a procedure used or what an interface is made of, and the [stages]({{"datamodel/modules/procedurestage/"|absolute_url}}) materials take part in.
- [__Templates__]({{"datamodel/modules/templates/"|absolute_url}}): reusable prefills for procedures, episodes, specimen procedures, experimental interfaces, data acquisitions, manipulations and material usages.
- [__Personal attributes__]({{"datamodel/personal_attributes/"|absolute_url}}): a lab's own resources, shared through groups: [Setups]({{"datamodel/personal_attributes/setup/"|absolute_url}}) with their equipment, [Inventories]({{"datamodel/personal_attributes/inventory/"|absolute_url}}) with their consumable stock, [Behavioral assays]({{"datamodel/personal_attributes/behavioralassay/"|absolute_url}}), [Data storage]({{"datamodel/personal_attributes/datastorage/"|absolute_url}}), [Licenses]({{"datamodel/personal_attributes/license/"|absolute_url}}) and [Protocols]({{"datamodel/personal_attributes/protocol/"|absolute_url}}).
- [__Resources__]({{"datamodel/resources/"|absolute_url}}): the shared catalog used by every lab: [Consumables]({{"datamodel/resources/consumable/"|absolute_url}}) (probe designs, ECoG arrays, virus constructs, reagents), [Hardware devices]({{"datamodel/resources/hardwaredevice/"|absolute_url}}) and [Suppliers]({{"datamodel/resources/supplier/"|absolute_url}}).
- [__Taxonomies__]({{"datamodel/taxonomies/"|absolute_url}}): controlled vocabularies: species, strains, [anatomical regions]({{"datamodel/taxonomies/anatomicalregion/"|absolute_url}}) organized by [atlas]({{"datamodel/taxonomies/anatomicalreference/"|absolute_url}}), coordinate transforms, behavioral categories and paradigms, setup types and regulatory authorities.
- [__Dissemination__]({{"datamodel/dissemination/"|absolute_url}}): publications, submitted by DOI, and journals.
- [__Users__]({{"datamodel/users/"|absolute_url}}): users, groups and laboratories, and the permissions built on them.

### Expandability, permissions, schemas
{: .no_toc}

- [__Expandability__]({{"datamodel/expandability/"|absolute_url}}): how the model grows through new types, taxonomies and resources while every record stays standardized.
- [__Permissions__]({{"datamodel/permissions/"|absolute_url}}): object-level permissions that inherit from projects, groups and personal attributes.
- [__Schemas__]({{"datamodel/schemas/"|absolute_url}}): the type-specific, versioned JSON schemas behind every modular record.

## Example usage of the flexible modular design
{: .no_toc }

The figure below shows how the data model applies to an extracellular recording session during a behavioral experiment in a rat. Colours follow the apps of the interactive data model: the project, subject and session (STEM data) are purple, the procedures, interface and session modules (Modules) teal, and the coordinates, which are fields of a procedure, grey. The implant procedure carries its materials and coordinates and creates the experimental interface that the recording names, so the recording inherits where and with what it was made.

[![Example: a project with a rat, its silicon probe implant and virus injection with materials and coordinates, the interface the implant created, and a session with an extracellular recording, behavioral tracking and a behavior entry]({{site.baseurl}}/assets/images/diagrams/data-model-example.svg)]({{site.baseurl}}/assets/images/diagrams/data-model-example.svg)
*Click the figure to open it at full size.*
