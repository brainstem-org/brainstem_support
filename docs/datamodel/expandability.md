---
layout: default
title: Expandability
parent: Data model
has_children: false
nav_order: 12
has_toc: false
---
# Expandability
{: .no_toc}

The data model is built around a standardized structure that stays expandable: new methods, techniques, data types, resources and taxonomy entries can be added while every record keeps a validated, versioned shape.

### Types and schemas
{: .no_toc }

Procedures, specimen procedures, data acquisition, manipulations, experimental interfaces, material usages, logs, equipment, consumables and consumable stock each have a vocabulary of **types**. Selecting a type shows the type-specific fields of its JSON schema, and the values are validated against that schema when the entry is saved. Every schema version is published at a permanent URL and entries remember the version they were validated against, so exports and NWB files stay interpretable (see [Public schemas]({{"api/public-schemas/"|absolute_url}})).

New types and new fields are added by the BrainSTEM team. Each addition goes through a review that checks the field against the storage rules of the model (which layer owns a value, whether it is structured, whether two labs would record it the same way), so the vocabulary grows without duplicating concepts. If you need a type or a field, open a request in the [GitHub discussions](https://github.com/brainstem-org/brainstem_support/discussions); the current families and their types are listed on the [Schemas]({{"datamodel/schemas/"|absolute_url}}) pages.

### Taxonomies and resources
{: .no_toc }

Species, strains, behavioral paradigms, setup types, regulatory authorities, consumables, hardware devices, suppliers, journals and publications are shared by all users and can be **submitted by anyone**. A submission becomes an approval request reviewed by an admin team; until it is accepted it is visible to the submitter only. Identifiers speed this up: strains, species, consumables and hardware devices can be looked up by **RRID** and publications by **DOI**, which prefills the form from the registry.

Silicon probe and ECoG array designs are imported from reviewed vendor catalogs (Cambridge NeuroTech, NeuroNexus, Neuropixels and others), with their channel layouts drawn as a schematic. Anatomical regions come from the atlases and anatomy ontologies BrainSTEM ships, covering mouse, rat, marmoset, macaque, human, zebrafish, fruit fly and C. elegans, and are not edited by users. The current list is on the [Anatomical references page]({{"datamodel/taxonomies/anatomicalreference/#atlases-in-brainstem"|absolute_url}}).

### Custom fields and tags
{: .no_toc }

Projects, subjects and sessions accept custom key-value fields (**Extra content**), as do specimen sets (**Custom fields**), with text or numeric values, and every entry accepts **tags**, so lab-specific information fits without waiting for a schema change.

### Personal attributes and templates
{: .no_toc }

Setups, inventories, behavioral assays, data storage, licenses and protocols are fully managed by the users who own them. Templates for procedures, specimen procedures, interfaces, data acquisition, manipulations and material usages let a lab capture its own standard configurations and apply them with one click.
