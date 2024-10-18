---
layout: default
title: STEM
parent: Data model
has_children: true
nav_order: 1
---

# STEM models

The STEM (Subjects, Time, Experiments, Manipulations) models form the core structure of the BrainSTEM data management system. These models provide a flexible and comprehensive framework for organizing and describing neuroscience experiments.

- __Projects__: Projects serve as the highest-level organizational unit, grouping related subjects, datasets, and collections. They define overall permissions and can be used to organize experiments for publications or day-to-day research activities.

- __Subjects__: Animal subjects are described by essential attributes such as name, sex, species, and strain. Subjects must belong to one or more projects and can be associated with various procedures.

- __Datasets__: Datasets are modular constructs that provide standardized descriptions of various aspects of experiments. They are composed of four main modules: Behavior, Experiment data, Manipulations, and Epochs. Datasets must belong to one or more projects.

- __Collections__: Collections allow for grouping datasets within a project. They can be used to organize datasets for specific analyses or figures. All datasets in a collection must belong to the same project.

Please see the dedicated pages below for detailed information on each of the STEM models: