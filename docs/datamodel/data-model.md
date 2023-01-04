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

## The data model
The data model is built around a standardized structure that maintains expandability allowing for incorporation of new methods, techniques, data types, resources and expanded taxonomies. 


The data model consists of 6 categories.

__Stem data__

- Projects
- Subjects
- Datasets 
- Collections

__Module data__

- __Actions__: Actions performed on subjects, including implants (e.g. probes, wires, and fibers), injections (e.g. virus injections). Actions allow for recording from a subject or manipulate its state.  
- __Behaviors__: Animal behaviors are described by the physical environment (also included VR) and what behavioral paradigm the animal is doing/trained to do. 
- __Experiment data__: Captures all data collection performed on or centered around a subject. This includes Audio recordings, behavioral tracking with cameras, electrophysiological recordings, and imaging. 
- __Manipulations__: Manipulations are any time-dependent manipulation performed on an animal subject, that changes its state. This includes any electrical, light or sensory stimulation, liquid perturbation, optogentical stimulation, perfusions,  inhalations, superfusions, injections, and ultrasound. Manipulations are described through an action and parameters that are specific to the type of manipulation. E.g. an electrical stimulation is described by its amplitude, duration, duty cycle, and repetitions, while a liquid perturbation by the liquid agent, concentration, the volume, flow rate and repetitions.
- __Action logs__: Action logs are changes applied to an action entry. 
- __Subject logs__: Subject logs are simpler log values applied to a subject, including food consumption, weighing, and water consumption. 

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
