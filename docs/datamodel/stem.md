---
layout: default
title: STEM
parent: Data model
has_children: true
nav_order: 1
has_toc: false
---

# STEM models

The STEM (STructured Experimental Metadata) models form the core structure of the BrainSTEM data management system. These models provide a flexible and comprehensive framework for organizing and describing neuroscience experiments.

- [**Projects**]({{site.baseurl}}/datamodel/stem/project): Projects serve as the highest-level organizational unit, grouping related subjects, sessions, and collections. They define overall permissions and can be used to organize experiments for publications or day-to-day research activities.

- [**Subjects**]({{site.baseurl}}/datamodel/stem/subject): Animal subjects are described by essential attributes such as name, sex, species, and strain. Subjects must belong to one or more projects and can be associated with various procedures.

- [**Sessions**]({{site.baseurl}}/datamodel/stem/session): Sessions are modular constructs that provide standardized descriptions of various aspects of experiments. They are composed of four main modules: Behavior, Data acquisition, Manipulations, and Epochs. Sessions must belong to one or more projects.

- [**Collections**]({{site.baseurl}}/datamodel/stem/collection): Collections allow for grouping sessions within a project. They can be used to organize sessions for specific analyses or figures. All sessions in a collection must belong to the same project.

- [**Cohorts**]({{site.baseurl}}/datamodel/stem/cohort): Cohorts enable organization of subjects into meaningful groups based on shared characteristics, experimental conditions, or timeframes. These groupings facilitate comparative analyses and help track subjects across related studies within a project.
