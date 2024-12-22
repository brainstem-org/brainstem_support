---
layout: default
title: Modules
parent: Data model
has_children: true
nav_order: 2
has_toc: false
---

# Modules

Modules in BrainSTEM are standardized yet flexible containers for describing various aspects of experimental conditions and data. They provide a structured way to capture and organize detailed information about different components of neuroscience experiments.

## Inventory modules
- [**Consumable stocks**]({{site.baseurl}}/datamodel/modules/consumablestock):Tracks the availability and usage of laboratory consumables, including current quantities, expiration dates, and storage locations. This helps maintain accurate inventory control and ensures timely reordering of essential supplies.

## Session modules
- [**Behaviors**]({{site.baseurl}}/datamodel/modules/behavior): Capture information about animal behaviors, including the experimental setup (which may involve virtual reality) and the specific behavioral paradigm the animal is trained to perform or is engaged in during the experiment.

- [**Data acquisitions**]({{site.baseurl}}/datamodel/modules/dataacquisition): Captures all forms of data collected during an experiment. This module is highly flexible and can describe a wide range of data types. Each data type is described using parameters specific to its acquisition method, ensuring comprehensive documentation of experimental observations.

- [**Manipulations**]({{site.baseurl}}/datamodel/modules/manipulation): Describe any interventions performed on an animal subject that change its state. This includes electrical, light or sensory stimulation, liquid perturbation, optogenetic stimulation, perfusions, inhalations, superfusions, injections, and ultrasound. Each type of manipulation is characterized by specific parameters relevant to that intervention.

## Setup modules
- [**Equipment**]({{site.baseurl}}/datamodel/modules/equipment): Document the setup of equipment and devices in an experimental environment, including camera setups, screens, thermal equipment, speakers, sensors, and microphones. Equipment enable recording from an environment or manipulating its state.

## Subject modules
- [**Procedures**]({{site.baseurl}}/datamodel/modules/procedure): Describe surgical procedures and other interventions performed on subjects, including implants (e.g., probes, wires, and fibers), injections (e.g., virus injections), and other methods that allow for recording from or manipulating a subject's state.

- [**Procedure logs**]({{site.baseurl}}/datamodel/modules/procedurelog): Record changes applied to a procedure entry, providing a history of modifications and adjustments made during an experiment.

- [**Subject logs**]({{site.baseurl}}/datamodel/modules/subjectlog): Capture simpler log values applied to a subject, including food consumption, weighing, and water consumption. These logs help track the day-to-day care and monitoring of experimental subjects.
