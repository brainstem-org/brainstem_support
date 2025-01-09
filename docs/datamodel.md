---
layout: default
title: Data model
nav_order: 2
has_children: true
has_toc: false
---
# Data model

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

# A relational model
BrainSTEM is built upon a relational model shown in below relational graph. Below pages describe the relational data model behind BrainSTEM, the table elements and fields and the modular structure of the model.

- [__STEM__](/datamodel/stem/) The STEM models form the core structure of the data management system and includes projects, subjects, sessions, collections and cohorts.
- [__Modules__](/datamodel/modules/) Modules are standardized yet flexible containers for describing various aspects of experimental conditions and data, including procedures, equipment, data acquisition, consumable stocks. 
- [__Personal attributes__](/datamodel/personal_attributes/) Personal attributes are model elements that are typically shared within individual laboratories or research groups and includes setups, inventories, behavioral paradigms and data storage.
- [__Resources__](/datamodel/resources/) Resources represent the various materials, equipment, and entities involved in neuroscience research. These include consumables, hardware devices, and suppliers.
- [__Taxonomies__](/datamodel/taxonomies/) Taxonomies provide standardized vocabularies and classification systems for various aspects of neuroscience research.
- [__Dissemination__](/datamodel/dissemination/) Dissemination focuses on capturing information related to the publication and sharing of research findings.
- [__Users__](/datamodel/users/) The Users models manages the authentication, authorization, and organizational aspects of the platform.

Below pages describe how permissions are inherited in the model, the schemas, and how the data model can be expanded to incorporate new methods, techniques, and resources.

- [__Expandability__](/datamodel/expandability/) The Schemas define the structure and organization of data for various components of the platform. They ensure consistency and standardization across different types of information. The main schema categories are: modules, consumables resources, coordinates-systems and relationships between models.
- [__Permissions implementation and inheritance__](/datamodel/permissions/) Permissions are implemented on an object level, inheriting permissions from users, groups, and projects and personal attributes.
- [__Schemas__](/datamodel/schemas/) The Schemas define the structure and organization of data for various components of the platform. They ensure consistency and standardization across different types of information. The main schema categories are: modules, consumables resources, coordinates-systems and relationships between models.


[![data_model](https://support.brainstem.org/assets/images/data_model_v6.png)](https://support.brainstem.org/assets/images/data_model_v6.png)

Tables represents models, and lines represent connections. A connecting fork on a model represent a 1-to-many connection, or in cases with forks on both ends, a many-to-many relationship. The modules, consumables, and consumable stocks have sub-types, in which relationships and standard fields are shared, but a set of type specific fields allows for further details. More on this on the schemas page described further down the page.

- __Projects__ (pink table) serve as the root node connecting to __Subjects__, __Sessions__, __Cohorts__ (set of __Subjects__), and __Collections__ (set of __Sessions__). Projects can also be associated with __Publications__.
- __Subjects__ can have multiple __Procedures__, __Subject Logs__ associated with it (green tables). Subjects are further described by their __Strain__.
- __Sessions__ can consist of __Behaviors__, __Data Acquisition__, __Manipulations__, and __Epochs__, representing the data collection and experimental conditions (blue tables).
- __Setups__ are described by the __Equipment__ (orange and cream-colored tables).
- __Inventories__ consists of __Consumable stocks__ (orange and cream-colored tables).
- __Data Storage__ (orange table) links to __Sessions__, representing where experimental data is archived.
- __Permission and Ownership__ are linked to Projects and to __Personal attributes__ (grey tables). Learn more about the permissions implementation and inheritance below.

The model can also vertically be separated into three levels:
1. Organization and permissions level
2. Modules
3. The backend with taxonomies and resources

## Example usage of the flexible modular design
{: .no_toc }

To get a better sense of the data model, below table-graph represent an extracellular recording during a behavioral session from a rat. The subject related models are green, and the session related models are blue.

[![data_model_example](https://support.brainstem.org/assets/images/data_model_example_v6.png)](https://support.brainstem.org/assets/images/data_model_example_v6.png)
