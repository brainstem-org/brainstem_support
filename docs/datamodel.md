---
layout: default
title: Data model
nav_order: 2
has_children: true
has_toc: false
---
# Data model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

# Relational data model
The relational model can be separated into three levels:
1. Organization and permissions level
2. Modules
3. Backend with taxonomies and resources.

[![data_model](https://support.brainstem.org/assets/images/data_model_v6.png)](https://support.brainstem.org/assets/images/data_model_v6.png)

Below pages describe the relational data model behind BrainSTEM, the table elements and fields and the modular structure of the model, how permissions are inherited in the model, and how the data model can be expanded to incorporate new methods, techniques, and resources.

- [__STEM__](/datamodel/stem/) The STEM models form the core structure of the data management system and includes projects, subjects, sessions, collections and cohorts.
- [__Modules__](/datamodel/modules/) Modules are standardized yet flexible containers for describing various aspects of experimental conditions and data, including procedures, equipment, data acquisition, consumable stocks. 
- [__Personal attributes__](/datamodel/personal_attributes/) Personal attributes are model elements that are typically shared within individual laboratories or research groups and includes setups, inventories, behavioral paradigms and data storage.
- [__Resources__](/datamodel/resources/) Resources represent the various materials, equipment, and entities involved in neuroscience research. These include consumables, hardware devices, and suppliers.
- [____Taxonomies__](/datamodel/taxonomies/) Taxonomies provide standardized vocabularies and classification systems for various aspects of neuroscience research.
- [__Dissemination__](/datamodel/dissemination/) Dissemination focuses on capturing information related to the publication and sharing of research findings.
- [__Users__](/datamodel/users/) The Users models manages the authentication, authorization, and organizational aspects of the platform.

## Example usage of the flexible modular design
{: .no_toc }

Extracellular recording during a behavioral session from a rat. 

[![data_model_example](https://support.brainstem.org/assets/images/data_model_example_v6.png)](https://support.brainstem.org/assets/images/data_model_example_v6.png)

# Permissions implementation and inheritance
Permissions are implemented on an object level, inheriting permissions from users, groups, and projects and personal attributes. Please see the dedicated page on [permissions](/datamodel/permissions/).

# Expandability
The data model is built around a standardized structure that maintains expandability allowing for incorporation of new methods, techniques, data types, resources and expanded taxonomies.

New entries in Taxonomies and Resources can be submitted by users. Any submission goes through an approval by a dedicated admin team.

### Expansion of the modules structures
{: .no_toc }

The available modules the user can select between in procedures, data acquisitions, consumable stocks, equipment, and manipulations, can be expanded by our admin team. If you wish for this, please submit a request through the issue/discussion forum. 

### Personal attributes
{: .no_toc }

The personal attributes can be fully managed by the users.
