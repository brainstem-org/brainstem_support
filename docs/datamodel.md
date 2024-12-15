---
layout: default
title: Data model
nav_order: 2
has_children: true
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

- [STEM](/datamodel/stem/)
- [Modules](/datamodel/modules/)
- [Personal attributes](/datamodel/personal_attributes/)
- [Resources](/datamodel/resources/)
- [Taxonomies](/datamodel/taxonomies/)
- [Dissemination](/datamodel/dissemination/)
- [Users](/datamodel/users/)

## Example usage of the flexible modular design
{: .no_toc }

Extracellular recording during a behavioral session from a rat. 

[![data_model_example](https://support.brainstem.org/assets/images/data_model_example_v6.png)](https://support.brainstem.org/assets/images/data_model_example_v6.png)

# Permissions implementation and inheritance
Permissions are implemented on an object level, inheriting permissions from users, groups, and projects. Subjects, datasets and collections inherits permissions from projects and modules inheits permissions from subjects and datasets. The personal attributes inherits permissions from groups.


[![permissions](https://support.brainstem.org/assets/images/permissions_v3.png)](https://support.brainstem.org/assets/images/permissions_v3.png)

### Projects
{: .no_toc }

Projects have four permission levels that can be defined for individual groups and users:
- Members: have read access to project-related subjects, datasets, and modules.
- Change permissions: allows for creation, editing and deletion of project related models.
- Managers: can add and remove project members and project groups.
- Owners: can manage project details and add and remove managers.

### Groups
{: .no_toc }

Groups have three permission levels:  
- Members inherit project-permissions assigned to group: including change, manager and owner project-permissions.
- Managers can add and remove group members.
- Owners can manage Group details and add and remove managers.

# Expandability
The data model is built around a standardized structure that maintains expandability allowing for incorporation of new methods, techniques, data types, resources and expanded taxonomies.

New entries in Taxonomies and Resources can be submitted by users. Any submission goes through an approval by a dedicated admin team.

### Expansion of the modules structures
{: .no_toc }

The available modules the user can select between in procedures, experiment data, manipulations, and subject state changes, can be expanded by our admin team. If you wish for this, please submit a request through the issue/discussion forum. 

### Personal attributes
{: .no_toc }

The personal attributes can be fully managed by the users.
