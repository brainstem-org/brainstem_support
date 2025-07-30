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
The model is structured into the following main categories:

- [__Projects__](/datamodel/project): Core model for organizing research efforts.
- [__Subjects__](/datamodel/subject): Representing the organisms or entities being studied. Includes related concepts like [Procedures](/datamodel/subjects/procedure), [Subject Logs](/datamodel/subjects/subjectlog), and [Cohorts](/datamodel/subjects/cohort).
- [__Sessions__](/datamodel/session): Detailing experimental sessions. Includes related concepts like [Behaviors](/datamodel/sessions/behavior), [Data Acquisition](/datamodel/sessions/dataacquisition), [Manipulations](/datamodel/sessions/manipulation), and [Collections](/datamodel/sessions/collection).
- [__Personal attributes__](/datamodel/personal_attributes/): Models for lab-specific elements such as [Setups](/datamodel/personal_attributes/setup), [Inventories](/datamodel/personal_attributes/inventory), [Behavioral Paradigms](/datamodel/personal_attributes/behavioralparadigm), and [Data Storage](/datamodel/personal_attributes/datastorage).
- [__Resources__](/datamodel/resources/): Representing materials, equipment, and entities involved in research, including [Consumables](/datamodel/resources/consumable), [Hardware Devices](/datamodel/resources/hardwaredevice), and [Suppliers](/datamodel/resources/supplier).
- [__Taxonomies__](/datamodel/taxonomies/): Standardized vocabularies and classification systems for neuroscience research.
- [__Dissemination__](/datamodel/dissemination/): Capturing information related to the publication and sharing of research findings.
- [__Users__](/datamodel/users/): Managing authentication, authorization, and organizational structure on the platform.

### Expandability, permissions, schemas
The data model is designed for expandability with structured permissions and standardized schemas to support flexible data integration.

- [__Expandability__](/datamodel/expandability/): The model can incorporate new methods, techniques, data types, resources, and taxonomies while maintaining a standardized structure.
- [__Permissions implementation and inheritance__](/datamodel/permissions/): Permissions are applied at the object level, inheriting from users, groups, projects, and personal attributes.
- [__Schemas__](/datamodel/schemas/): Defining the structure and organization of data components.

### Elements of the graph
Tables represent models, while lines represent connections between them. A fork indicates a one-to-many relationship, while forks on both ends indicate a many-to-many relationship. Some models, such as modules and consumables, have subtypes with shared relationships and fields but additional type-specific details.

- __Projects__ serve as a primary organizational unit.
- __Subjects__ are linked to __Procedures__, __Subject Logs__, and __Cohorts__. They are also described by their __Strain__ (Taxonomy).
- __Sessions__ are linked to __Behaviors__, __Data Acquisition__, __Manipulations__, and __Collections__. They can also link to __Data Storage__ (Personal Attribute).
- __Personal Attributes__ like __Setups__ (containing __Equipment__) and __Inventories__ (containing __Consumable Stocks__) define lab-specific configurations.
- __Resources__ like __Consumables__, __Hardware Devices__, and __Suppliers__ represent tangible items or entities.
- __Taxonomies__ provide standardized classifications (e.g., __Species__, __Brain Regions__).
- __Dissemination__ models like __Publications__ link back to __Projects__.
- __Permissions__ are managed through __Users__ and __Groups__ and apply throughout the structure.

## Example usage of the flexible modular design
{: .no_toc }

The graph below illustrates how the data model can be applied to an extracellular recording session during a behavioral experiment involving a rat. Subject-related models are highlighted in green, while session-related models are in blue.

[![data_model_example](https://support.brainstem.org/assets/images/data_model_example_v6.png)](https://support.brainstem.org/assets/images/data_model_example_v6.png)
