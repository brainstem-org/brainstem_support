---
layout: default
title: Data model
nav_order: 2
has_children: true
has_toc: false
---
[![data_model](https://support.brainstem.org/assets/images/data_model_v6.png)](https://support.brainstem.org/assets/images/data_model_v6.png)

# Data model

BrainSTEM is built upon a relational data model, as shown in the relational graph above. Click the graph to see it in full size.

### Organization of the models
The model is structured into the following apps, each containing related models:

- [__STEM__](/datamodel/stem/): Core models for data management, including projects, subjects, sessions, collections, and cohorts.
- [__Modules__](/datamodel/modules/): Flexible containers for experimental conditions and data, covering procedures, equipment, data acquisition, and consumable stocks.
- [__Personal attributes__](/datamodel/personal_attributes/): Models for lab-specific elements such as setups, inventories, behavioral paradigms, and data storage.
- [__Resources__](/datamodel/resources/): Representing materials, equipment, and entities involved in research, including consumables, hardware devices, and suppliers.
- [__Taxonomies__](/datamodel/taxonomies/): Standardized vocabularies and classification systems for neuroscience research.
- [__Dissemination__](/datamodel/dissemination/): Capturing information related to the publication and sharing of research findings.
- [__Users__](/datamodel/users/): Managing authentication, authorization, and organizational structure on the platform.

### Expandability, permissions, schemas 
The data model is designed for expandability with structured permissions and standardized schemas to support flexible data integration.

- [__Expandability__](/datamodel/expandability/): The model can incorporate new methods, techniques, data types, resources, and taxonomies while maintaining a standardized structure.
- [__Permissions implementation and inheritance__](/datamodel/permissions/): Permissions are applied at the object level, inheriting from users, groups, projects, and personal attributes.
- [__Schemas__](/datamodel/schemas/): Schemas define the structure and organization of data components, ensuring consistency across modules, resources, coordinate systems, and inter-model relationships.

### Elements of the graph
Tables represent models, while lines represent connections between them. A fork indicates a one-to-many relationship, while forks on both ends indicate a many-to-many relationship. Some models, such as modules and consumables, have subtypes with shared relationships and fields but additional type-specific details.

- __Projects__ (pink table) serve as the root node connecting to __Subjects__, __Sessions__, __Cohorts__ (set of __Subjects__), and __Collections__ (set of __Sessions__). Projects can also link to __Publications__.
- __Subjects__ can have multiple __Procedures__, __Subject Logs__ associated with it (green tables). Subjects are further described by their __Strain__.
- __Sessions__ can consist of __Behaviors__, __Data Acquisition__, __Manipulations__, and __Epochs__, representing the data collection and experimental conditions (blue tables).
- __Setups__ are described by the __Equipment__ (orange and cream-colored tables).
- __Inventories__ consists of __Consumable stocks__ (orange and cream-colored tables).
- __Data Storage__ (orange table) links to __Sessions__, representing where experimental data is archived.
- __Permission and Ownership__ are linked to Projects and to __Personal attributes__ (grey tables). Learn more about the permissions implementation and inheritance below.

The model can be viewed in three vertical layers:
1. __Organization and Permissions Level__
2. __Modules Level__
3. __Backend Level__ (Taxonomies and Resources)

## Example usage of the flexible modular design
{: .no_toc }

The graph below illustrates how the data model can be applied to an extracellular recording session during a behavioral experiment involving a rat. Subject-related models are highlighted in green, while session-related models are in blue.

[![data_model_example](https://support.brainstem.org/assets/images/data_model_example_v6.png)](https://support.brainstem.org/assets/images/data_model_example_v6.png)
