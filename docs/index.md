---
layout: default
title: Home
nav_order: 1
has_children: false
has_toc: false
---

# BrainSTEM Documentation & Support
{: .no_toc}
{: .fs-9 }

Documentation, tutorials, and support resources for BrainSTEM.
{: .fs-6 .fw-300}

[Get started now]({{ "/tutorials/get_started/"|absolute_url}}){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2} [Visit BrainSTEM.org](https://www.brainstem.org/){: .btn .fs-5 .mb-4 .mb-md-0}

## About BrainSTEM
{: .no_toc}

This site provides documentation and support for BrainSTEM, a collaborative electronic lab notebook designed for experimental neuroscience. BrainSTEM captures and organizes the metadata of in-vivo and ex-vivo experiments, from subjects, surgeries and implants to recordings, imaging and behavior, and from tissue preparations to staining and slice physiology, through a modular, standardized data model that grows with new methods.

Whether you run a small lab or manage large collaborative projects, BrainSTEM provides the infrastructure to organize, share and access your experimental metadata with controlled vocabularies, versioned schemas and reproducible workflows.

### Key features
{: .no_toc}

{% include tour.html %}

- **Complete experimental records**: projects, subjects and specimen sets, procedures with their materials and the interfaces they implant, sessions with data acquisition, manipulations, behavior and epochs, all with type-specific, validated fields.
- **Collaboration and compliance**: object-level permissions through projects and groups, procedure episodes with severity classifications, licenses and protocols, and planned records.
- **Shared resources and taxonomies**: a catalog of consumables (including hundreds of silicon probe and ECoG array designs), hardware devices and suppliers; species, strains, atlases with brain-region trees and coordinate previews; new entries can be submitted with an RRID or DOI.
- **Open science**: one-click public sharing of projects, a public portal and API, versioned JSON exports, STAR Methods reports, and conversion to NWB files for DANDI.
- **Programmable and AI ready**: a REST API with Python and MATLAB tools, permanent URLs for every schema version and a machine-readable reference generated from the server; an in-app assistant that searches your records, an MCP server for Claude, Cursor and other assistants, and agent skills for coding agents, all bound by your permissions.
- **Integrations**: SoftMouse colony import, CSV and batch import, and an interactive data model to explore how everything connects.
{: .tour-features }

### How BrainSTEM structures an experiment
{: .no_toc}

A project holds the subjects, and each session records one occasion with a subject. Around them, BrainSTEM records what was done, what was recorded, with what, where in the brain, under which rules and where the data lives. Colours follow the apps of the [data model]({{ "/datamodel/"|absolute_url}}).

![How BrainSTEM structures an experiment: a project holds subjects and sessions; procedures, interfaces, epochs, behavior, data acquisition and manipulations answer what was done and recorded; species, data storage, protocols, atlases, materials and setups answer which animal, where the data lives, under which rules, where in the brain, which products and with what.]({{site.baseurl}}/assets/images/diagrams/what-brainstem-records.svg)

[Data model]({{"/datamodel/"|absolute_url}}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-4} [Web interface]({{"/webinterface/"|absolute_url}}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-4} [API]({{"/api/"|absolute_url}}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-4} [Tools]({{"/tools/"|absolute_url}}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-4}

## Getting started

New to BrainSTEM? The tutorials guide you from account creation to complete experimental workflows.

### For new users
{: .no_toc}
- [Setting up your first project, subjects and sessions]({{ "/tutorials/get_started/"|absolute_url}})
- [Creating or joining research groups]({{ "/tutorials/managing-groups/"|absolute_url}})
- [Understanding the BrainSTEM data model]({{ "/datamodel/"|absolute_url}})
- [Forms, lists and entry pages of the web interface]({{ "/webinterface/"|absolute_url}})

### For advanced users
{: .no_toc}
- [Ex vivo workflows with specimen sets, specimen procedures and slice sessions]({{ "/tutorials/specimen-workflow/"|absolute_url}})
- [Public data sharing]({{ "/tutorials/sharing-project-publicly/"|absolute_url}}), [exports and NWB conversion]({{ "/tutorials/exporting-to-nwb/"|absolute_url}})
- [Submitting resources and taxonomies]({{ "/tutorials/submit-resource-and-taxonomies/"|absolute_url}})
- [Working with the AI assistant, the MCP server and agent skills]({{ "/tutorials/working-with-ai/"|absolute_url}})

[Get started tutorial]({{ "/tutorials/get_started/"|absolute_url}}){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2}
[View all tutorials]({{ "/tutorials/"|absolute_url}}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2}

## Support and community

### Get help
{: .no_toc}

- **[FAQ]({{ "/faq/"|absolute_url}})**: answers to the questions new users ask most
- **[GitHub Issues](https://github.com/brainstem-org/brainstem_support/issues)**: report bugs and technical problems
- **[GitHub Discussions](https://github.com/brainstem-org/brainstem_support/discussions)**: ask questions, request features, and engage with the community
- **[Contact form](https://brainstem.org/#Get-in-touch)**: account-specific issues and direct support

### Contributing
{: .no_toc}
BrainSTEM thrives on community input. Whether you report bugs, suggest enhancements or take part in discussions, your contribution helps improve the platform for everyone.

## Acknowledgments

BrainSTEM is supported by the [Oxytocin U19 BRAIN Initiative Grant](https://med.nyu.edu/departments-institutes/neuroscience/research/shared-research-resources/oxytocin-u19-brain-initiative-grant), enabling advances in collaborative neuroscience research infrastructure.

<p style="text-align: center;"><img src="{{site.baseurl}}/assets/images/brain_initiative.png" alt="BRAIN Initiative" width="160"></p>
