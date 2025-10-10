---
layout: default
title: Resources & Taxonomies
parent: Tutorials
nav_order: 7
---

# Resources & Taxonomies
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

BrainSTEM maintains standardized, controlled vocabularies for resources and taxonomies to ensure data consistency across the platform. As a user, you can contribute new entries when you encounter equipment, consumables, or taxonomic classifications that aren't yet in the system. All submissions undergo an administrative review process to maintain data quality and prevent duplicates.

This tutorial guides you through submitting new resources and taxonomies, tracking their approval status, and using approved entries in your research documentation.

## Available Resources & Taxonomies

### Resources
{: .no_toc}

Laboratory materials and equipment that can be submitted:

| Resource Type | Description | Examples |
|--------------|-------------|----------|
| **[Consumables]({{"datamodel/resources/consumable/"|absolute_url}})** | Materials used in experiments | Silicon probes, viral vectors, pharmaceutical agents, electrodes |
| **[Hardware devices]({{"datamodel/resources/hardwaredevice/"|absolute_url}})** | Electronic equipment and instruments | Recording systems, cameras, stimulation devices, microscopes |
| **[Suppliers]({{"datamodel/resources/supplier/"|absolute_url}})** | Vendors and manufacturers | Equipment manufacturers, chemical suppliers, research distributors |

### Taxonomies
{: .no_toc}

Standardized classifications for biological and experimental categories:

| Taxonomy Type | Description | Examples |
|--------------|-------------|----------|
| **[Brain regions]({{"datamodel/taxonomies/brainregion/"|absolute_url}})** | Anatomical brain structures | Hippocampus CA1, Primary visual cortex, Basal ganglia |
| **[Setup types]({{"datamodel/taxonomies/setuptype/"|absolute_url}})** | Experimental environment categories | T-maze, Open field, Head-fixed disc, Surgical table |
| **[Species]({{"datamodel/taxonomies/species/"|absolute_url}})** | Organism species | Mus musculus, Rattus norvegicus, Macaca mulatta |
| **[Strains]({{"datamodel/taxonomies/strain/"|absolute_url}})** | Genetic strains within species | C57BL/6J, Long-Evans, Sprague-Dawley |

## Submission Process

### Before Submitting

**Essential pre-submission checklist:**

1. **Search for existing entries:** Check if the resource or taxonomy already exists to avoid duplicates
2. **Gather complete information:** Collect all necessary details:
   - For consumables: Product name, catalog number, supplier, specifications
   - For hardware devices: Manufacturer, model number, technical specifications, interface details
   - For taxonomies: Scientific names, standard references, descriptions
3. **Verify accuracy:** Double-check names, spellings, and technical specifications
4. **Prepare documentation:** Have links to manufacturer pages, datasheets, or scientific references ready

### Submitting New Entries

**To submit a new resource or taxonomy:**

1. Navigate to the appropriate section:
   - **Resources**: Go to **Resources** → Select type (**Consumables**, **Hardware devices**, or **Suppliers**)
   - **Taxonomies**: Go to **Taxonomies** → Select type (**Brain regions**, **Setup types**, **Species**, or **Strains**)

2. Click the **Add** button for the resource or taxonomy type

3. Fill out the submission form with required information:

| Resource/Taxonomy | Required Fields | Best Practices |
|------------------|----------------|----------------|
| **Consumables** | Product name, consumable type, supplier | Include catalog numbers, specifications, and intended use |
| **Hardware devices** | Manufacturer, model, device type | Provide technical specs, connectivity details, and compatible systems |
| **Suppliers** | Name, website, contact information | Include geographic regions served and product specialties |
| **Setup types** | Environment type name, category | Describe typical experimental use cases |
| **Species** | Scientific name, common name | Follow NCBI Taxonomy database conventions |
| **Strains** | Strain name, species, description | Include genetic background and supplier sources |

4. Add detailed **Description** field content to help other users understand when to use this entry

5. Click **Submit** for admin review

{: .note }
> Detailed descriptions speed up admin review and help other users select the correct entries. Include specifications, use cases, and any relevant technical details.

### Submission Guidelines

**Follow these standards for high-quality submissions:**

- **Use standard nomenclature:** Follow established scientific naming conventions (e.g., NCBI for species)
- **Be specific and descriptive:** 
  - Good: "NeuroNexus A1x32-Poly2 silicon probe, 32-channel, 25μm spacing"
  - Avoid: "Silicon probe"
- **Include references:** Cite manufacturer datasheets, or scientific classifications
- **Check spelling carefully:** Typos can cause rejection or create confusion in the database
- **Avoid abbreviations without context:** Define acronyms and technical terms in descriptions
- **Provide manufacturer links:** Include URLs to product pages or technical documentation where applicable

## Tracking Submissions

### Monitoring Approval Status

**To check the status of your submissions:**

1. Navigate to [www.brainstem.org/private/approvals/](https://www.brainstem.org/private/approvals/)
2. Review your submissions and their current status:

| Status | Description | Action Required |
|--------|-------------|----------------|
| **Pending** | Under administrative review | Wait for admin feedback; no action needed |
| **Approved** | Accepted and now available to all users | Entry is live; you can use it in your experiments |
| **Rejected** | Declined with feedback | Review comments and revise submission |
| **Revision Requested** | Needs modifications before approval | Address feedback and resubmit |

3. Check the **Comments** field for detailed admin feedback or revision requests

### Responding to Feedback

**If your submission requires revisions:**

1. **Read admin comments carefully** to understand specific concerns or needed improvements
2. **Gather additional information** if specifications, references, or details are requested
3. **Make suggested changes** to address each point of feedback
4. **Resubmit** following the same submission process
5. **Add notes** in the submission referencing the original entry and explaining your revisions

**Common reasons for revision requests:**
- Missing technical specifications or catalog numbers
- Unclear or ambiguous naming
- Duplicate entries (similar item already exists)
- Need for additional references or documentation
- Inconsistent formatting or nomenclature

{: .tip }
> Responding promptly to admin feedback speeds up the approval process. Most revisions are simple clarifications that can be addressed quickly.

## After Approval

Once your submission is approved, it becomes part of the BrainSTEM platform:

**Immediate effects:**
- ✅ The entry appears in dropdown menus across BrainSTEM
- ✅ All users can select and reference the approved entry
- ✅ The entry becomes searchable in the resources/taxonomies database
- ✅ You can use it in your experimental documentation (setups, procedures, sessions)

**Long-term impact:**
- Your contribution helps standardize data across the research community
- Other labs can use your submissions, improving data interoperability
- The entry can be referenced in future resource submissions
- It becomes part of the permanent BrainSTEM vocabulary

{: .note }
> Approved entries cannot be deleted but can be marked as deprecated if they become obsolete. Contact administrators if an entry needs updating.

## Next Steps

After successfully contributing resources and taxonomies to BrainSTEM, consider these logical progressions:

- **Set Up Your Lab Infrastructure**: Use your newly approved resources in the [Setting Up Lab Infrastructure tutorial]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure) to configure your own experimental setups with the equipment and suppliers you've contributed
- **Begin Experimental Documentation**: Start documenting your research using the [Get Started tutorial]({{site.baseurl}}/tutorials/get_started) and incorporate your approved resources into real experimental workflows
- **Explore Specific Workflows**: Depending on your research focus, dive into detailed experimental tutorials like [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow)<!-- or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow)--> that will use your contributed resources
- **Organize Your Team**: Use [Managing Projects]({{site.baseurl}}/tutorials/managing-projects) and [Managing Groups]({{site.baseurl}}/tutorials/managing-groups) to organize access to your contributed resources across your research team
- **Continue Contributing**: As you discover new equipment, suppliers, or taxonomic categories in your research, continue expanding the BrainSTEM resource database by submitting additional entries
