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

[![data_model](https://petersenpeter.github.io/brainstem_support/assets/images/data_model.png)](https://petersenpeter.github.io/brainstem_support/assets/images/data_model.png)

## The data model
The data model is built around a standardized structure that maintains expandability allowing for incorporation of new methods, techniques, data types, resources and expanded taxonomies.

The data model consists of the 6 categories described below.

### 1. Stem data

- __Projects__: Projects 
- __Subjects__: Animal subjects described by a name, its sex and strain. A subject must further belong to a project. 
- __Datasets__: A dataset consists of various module data. It must belong to a project. 
- __Collections__: Dataset collections groups dataset belonging to the same project. This can be used to describe which datasets makes up a figure or a specific analysis. 

### 2. Module data

- __Actions__: Actions performed on subjects, including implants (e.g. probes, wires, and fibers), injections (e.g. virus injections). Actions allow for recording from a subject or manipulate its state.  
- __Behaviors__: Animal behaviors are described by the physical environment (also included VR) and what behavioral paradigm the animal is doing/trained to do. 
- __Experiment data__: Captures all data collection performed on or centered around a subject. This includes Audio recordings, behavioral tracking with cameras, electrophysiological recordings, and imaging. 
- __Manipulations__: Manipulations are any time-dependent manipulation performed on an animal subject, that changes its state. This includes any electrical, light or sensory stimulation, liquid perturbation, optogentical stimulation, perfusions,  inhalations, superfusions, injections, and ultrasound. Manipulations are described through an action and parameters that are specific to the type of manipulation. E.g. an electrical stimulation is described by its amplitude, duration, duty cycle, and repetitions, while a liquid perturbation by the liquid agent, concentration, the volume, flow rate and repetitions.
- __Action logs__: Action logs are changes applied to an action entry. 
- __Subject logs__: Subject logs are simpler log values applied to a subject, including food consumption, weighing, and water consumption. 

Module data tables are standardized yet flexible containers for describing the experimental conditions. 

### 3. Permissions and ownership

- __Users__: Users of BrainSTEM. All users are public. 
- __Groups__: Groups of BrainSTEM. All groups are public. 
- __Laboratories__: Laboratories are tied to groups in a one-to-one relationship. Linking a group to a lab allows for linking further information to the group, including a website, city, country, university, department, and a principal investigator.

### 4. Resources (+)

- __Suppliers__: Any entity that supplies consumables or hardware devices. Can be a company, a lab or a person. 
- __Consumables__: Consumable are grouped by types. Optic fiber designs, Silicon probes designs, Virus constructs, wire electrodes. Types of consumables can be expanded by our admin team. Consumables are described by type specific fields.
- __Hardware devices__: Hardware devices are any hardware, including computers, acquisition systems and stimulators. 

Resources are expandable through user submissions, that must go through an approval process by our admin team.

### 5. Taxonomies (+)

- __Brain regions atlas__
- __Species and strains__
- __Environment types__

Taxonomies are expandable through user submissions. We are using existing standards and controlled vocabulary when possible and hope to establish standards where none exists.

### 6. Personal attributes

- __Behavioral paradigms__
- __Data repositories__
- __Physical environments__

Personal attributes are model elements that typically are shared within labs: local data storage, various in-house built environments for experiments, and behavioral paradigms, which we chose not to standardized on a wider scale.


## Example usage of the flexible modular design
Extracellular recording during a behavioral session from a rat. 

[![data_model_example](https://petersenpeter.github.io/brainstem_support/assets/images/data_model_example.png)](https://petersenpeter.github.io/brainstem_support/assets/images/data_model_example.png)
