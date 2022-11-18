---
layout: default
title: Home
nav_order: 1
has_children: false
---
# A collaborative electronic lab notebook for FAIR experimental neuroscience
{: .no_toc}
{: .fs-9 }

BrainSTEM has a customizable web interface built on a flexible data model and functions as an electronic lab notebook that allows for the organization of experiments and raw data. Granular access control enables collaboration within or across labs. The database of metadata can be accessed through either a web interface or REST API. A prototype of this tool has been deployed in the Buzsáki Lab, and a beta version for broad distribution is currently under development.
{: .fs-6 .fw-300}

[Get started now](#getting-started){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2} [Matlab API tool](https://github.com/petersenpeter/brainstem_matlab_api_tools){: .btn .fs-5 .mb-4 .mb-md-0} [Python API tool](https://github.com/petersenpeter/brainstem_python_api_tools){: .btn .fs-5 .mb-4 .mb-md-0}

## Introduction
{: .no_toc}
BrainSTEM (Brain STructured Experimental Metadata) is a centralized, collaborative electronic lab notebook for experimental neuroscience that facilitates compliance with NIH and other data sharing requirements. BrainSTEM was designed with ease of adoption and use as a primary consideration.

It is a web-based tool, so no technical know how is needed to use it, and the interface can be customized for the data, materials, and personnel of a particular lab or group to streamline the process of collecting metadata. It is designed to capture a range of electrophysiology, imaging, and behavioral data collection, and is built on a flexible data model so it can be extended to capture other types of data as well. Granular permissions allow access control to enable private collaboration within and across labs, and one click public sharing of datasets.

Available taxonomies (e.g. species, brain atlases) are integrated with BrainSTEM and, when none are available, controlled vocabularies are used to ensure standardization across users for general attributes (behavioral paradigms, data repositories, journals, and publications) and resources (e.g. consumables, hardware devices, and suppliers), as well as local standardization for personnel (people, groups, and labs). These standards ensure that data will be understandable and interoperable.

The data model supports sophisticated querying through both a public web interface. A REST API is currently under development and will allow querying programmatically through the REST API. More advanced users can use the API to interact with BrainSTEM in either Matlab or Python to allow for programmable access from other toolsets. It will also allow BrainSTEM to interface with the rest of the FAIR ecosystem e.g. Dandi Archive & NWB, including allowing integration with data repositories via their APIs to facilitate the export of data to repositories and mapping and transfer of BrainSTEM metadata to repositories
The large diversity of cell-types of the brain, provides the means by which circuits perform complex operations. Understanding such diversity is one of the key challenges of modern neuroscience. Neurons have many unique electrophysiological and behavioral features from which parallel cell-type classification can be inferred.

[Data model]({{"/datamodel/"|absolute_url}}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-4} [Web interface]({{"/pipeline/"|absolute_url}}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-4} [REST API]({{"/webinterface/"|absolute_url}}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-4}

## Getting started
1. Create a user account
2. Create or join a group
3. Create or join a project

That's it! Now you can use the web interface and API tools to describe your experimental data. We recommend exploring some of the tutorials to help you get acqueinted with BrainSTEM.

[View tutorials]({{ "/tutorials/"|absolute_url}}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2}

## Support
Please use the [GitHub issues system](https://github.com/petersenpeter/brainstem_support/issues) and [GitHub Discussions](https://github.com/petersenpeter/brainstem_support/discussions) for reporting bugs, enhancement requests or general questions.

## Funding
BrainSTEM is funded through the [Oxytocin U19 BRAIN Initiative Grant](https://med.nyu.edu/departments-institutes/neuroscience/research/shared-research-resources/oxytocin-u19-brain-initiative-grant).

<p align="center">
	<img src="https://raw.githubusercontent.com/petersenpeter/common_resources/main/images/brain_initiative.png" width="19%">&emsp;&emsp;&emsp;&emsp;
</p>
