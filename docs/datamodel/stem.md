---
layout: default
title: STEM
parent: Data model
has_children: true
nav_order: 1
has_toc: false
---

# STEM models

The STEM models form the core models and provide a flexible and comprehensive framework for organizing and describing neuroscience experiments.

- [**Projects**]({{site.baseurl}}/datamodel/stem/project): Projects serve as the highest-level organizational unit, grouping related subjects, sessions, and collections. They define overall permissions and can be used to organize experiments for publications or day-to-day research activities.

- [**Subjects**]({{site.baseurl}}/datamodel/stem/subject): Subjects are described by essential attributes such as name, sex, species, and strain.

- [**Sessions**]({{site.baseurl}}/datamodel/stem/session): Sessions are modular constructs that provide standardized descriptions of various aspects of experiments. They are composed of four main modules: Behavior, Data acquisition, Manipulations, and Epochs. 

- [**Collections**]({{site.baseurl}}/datamodel/stem/collection): Collections allow for grouping sessions within a project. They can be used to organize sessions for specific analyses or figures.

- [**Cohorts**]({{site.baseurl}}/datamodel/stem/cohort): Cohorts enable organization of subjects into meaningful groups based on shared characteristics, experimental conditions, or time frames.