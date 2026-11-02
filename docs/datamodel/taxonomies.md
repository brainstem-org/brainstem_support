---
layout: default
title: Taxonomies
parent: Data model
has_children: true
nav_order: 9
has_toc: false
---

# Taxonomies

Taxonomies provide standardized vocabularies and classification systems for various aspects of neuroscience research. They ensure consistency in naming and categorization across experiments and research groups. Most taxonomies are expandable: anyone can submit an entry, which is usable immediately in your own records and becomes visible to everyone once approved. Species, strains and behavioral paradigms carry an RRID and external identifiers; species and strains also carry a popular name. The main categories of taxonomies are:

- [**Anatomical regions**]({{site.baseurl}}/datamodel/taxonomies/anatomicalregion): Anatomical structures as defined by an atlas or ontology, used as target regions on procedures, specimen procedures, experimental interfaces and specimen sets. System-loaded, with no approval workflow. Formerly called brain regions.

- [**Anatomical references**]({{site.baseurl}}/datamodel/taxonomies/anatomicalreference): The atlas and ontology releases that regions belong to, with their species, coordinate space and visualization status. System-managed.

- [**Coordinate transforms**]({{site.baseurl}}/datamodel/taxonomies/coordinatetransform): Named, versioned mappings from a coordinate system to an atlas, used for the coordinate preview on procedures. System-managed.

- [**Behavioral categories**]({{site.baseurl}}/datamodel/taxonomies/behavioralcategory): A two-level hierarchical classification for organizing behavioral paradigms by cognitive domain or experimental focus.

- [**Behavioral paradigms**]({{site.baseurl}}/datamodel/taxonomies/behavioralparadigm): Standardized behavioral tasks shared across the neuroscience community, with their category, applicable species and original publication, independent of any lab's implementation.

- [**Regulatory authorities**]({{site.baseurl}}/datamodel/taxonomies/regulatoryauthority): Organizations that issue and oversee research approvals and licenses.

- [**Setup types**]({{site.baseurl}}/datamodel/taxonomies/setuptype): Classes of experimental preparation and apparatus, each in a preparation category, used by setups and behavioral assays.

- [**Species**]({{site.baseurl}}/datamodel/taxonomies/species): The animal species used in research. Every subject stores its species directly.

- [**Strains**]({{site.baseurl}}/datamodel/taxonomies/strain): Genetically defined lines within a species. Strain names are unique within their species.
