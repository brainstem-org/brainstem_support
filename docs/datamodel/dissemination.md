---
layout: default
title: Dissemination
parent: Data model
has_children: true
nav_order: 10
has_toc: false
---

# Dissemination

The Dissemination model captures information related to the publication and sharing of research findings. Both components are shared across all BrainSTEM users and go through the same approval queue as the taxonomies and resources. Publications are linked from the project side: a [project]({{site.baseurl}}/datamodel/stem/project) names the publications its data support, which is what connects a paper to the subjects, sessions and procedures behind it.

- [**Journals**]({{site.baseurl}}/datamodel/dissemination/journal): Scientific journals, preprint servers and conference proceedings where research findings are published, with name, description and website.

- [**Publications**]({{site.baseurl}}/datamodel/dissemination/publication): Specific papers, articles or preprints, with title, authors, journal, abstract, DOI, volume, publication date and URLs for the publication and any publicly accessible PDF. The web form can prefill a publication from its DOI.
