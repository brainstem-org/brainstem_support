---
layout: default
title: Relational data model
parent: Data model
nav_order: 1
---
# Relational data model
The relational model can be separated into three levels:
1. Organization and permissions level
2. Module data
3. Backend with taxonomies and resources.

![data_model](https://petersenpeter.github.io/brainstem_support/assets/images/data_model.png)

## Employment of standardization while maintaining expandability
The data model consists of 6 categories

__Stem data__

- Projects
- Subjects
- Datasets 
- Collections

__Module data__

- Actions
- Behaviors
- Experiment data
- Manipulations

__Permissions and ownership__

- Users
- Groups
- Laboratories

__Resources (+)__

- Suppliers
- Consumables
- Hardware devices

__Taxonomies (+)__

- Brain regions atlas
- Species and strains
- Environment types

__Personal attributes__

- Behavioral paradigms
- Data repositories
- Physical environments

Module data are standardized yet flexible containers for describing the experimental conditions. 

Resources & taxonomies are expandable through user submissions. We are using existing standards and controlled vocabulary when possible and hope to establish standards where none exists.

Personal attributes are model elements that typically are shared within labs: local data storage, various in-house built environments for experiments, and behavioral paradigms, which we chose not to standardized on a wider scale.


## Example usage of the flexible modular design
Extracellular recording during a behavioral session from a rat. 

![data_model_example](https://petersenpeter.github.io/brainstem_support/assets/images/data_model_example.png)
