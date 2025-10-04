---
layout: default
title: Behavioral Paradigms
parent: Tutorials
nav_order: 20
---
# Behavioral Paradigms in BrainSTEM
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC

## Introduction

Behavioral paradigms are standardized experimental protocols or tasks (such as T-maze alternation, open field exploration, or Morris water maze) that are performed within a specific setup environment. Defining paradigms in BrainSTEM ensures consistency, reproducibility, and clear documentation of behavioral experiments across your lab.

## What is a Behavioral Paradigm?

A behavioral paradigm defines:
- The type of behavioral task or protocol (e.g., spatial memory, anxiety, locomotion)
- The required environment type (must match the setup's environment type)
- Key parameters or variables (e.g., trial structure, cues, reward schedules)

## How Behavioral Paradigms Relate to Setups

- Each behavioral paradigm is associated with a specific environment type (e.g., T-maze, Open field)
- Only setups with a matching environment type can be used for a given paradigm
- This ensures that experimental sessions are created with the correct physical and procedural context

## Creating a Behavioral Paradigm

1. Go to *Personal Attributes* → *Behavioral Paradigms*
2. Click *Add behavioral paradigm*
3. Fill in the required fields:
    - **Name**: Descriptive name (e.g., "T-maze Alternation Task")
    - **Setup Type**: Select the matching setup type (e.g., T-maze)
    - **Description**: Briefly describe the protocol, goals, and any special requirements
4. Save the paradigm. It will now be available when creating sessions in compatible setups.

### Example: Defining a T-maze Alternation Paradigm
```json
{
  "name": "T-maze Alternation Task",
  "setup_type": "T-maze",
  "description": "A spatial working memory task where the subject must alternate between left and right arms for reward."
}
```

## Best Practices
- Use clear, standardized names for paradigms
- Include enough detail in the description for reproducibility
- Link paradigms to the correct environment type to avoid confusion
- Update paradigms as protocols evolve, but keep a record of changes

{: .note }
> Behavioral paradigms are critical for organizing and analyzing behavioral data. Defining them up front ensures your lab's experiments are well-documented and comparable across projects.

## Next Steps

Now that you have behavioral paradigms defined, you can begin documenting complete experiments:

- **Document complete experiments**: Follow either the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) tutorials to see how behavioral paradigms integrate with full experimental documentation
- **Set up your infrastructure**: Configure the physical setups and equipment using [Setting Up Lab Infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure) to create the experimental environments where your behavioral paradigms will be executed
- **Set up data storage**: Configure [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to link your behavioral sessions to actual data files for analysis
- **Expand your resources**: Visit [Submit Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies) to contribute new behavioral equipment or paradigm types to the BrainSTEM platform
- **Enable data sharing**: Make your behavioral paradigms publicly available through [Sharing Project Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) to promote reproducible research protocols
