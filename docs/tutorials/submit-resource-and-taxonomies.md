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

BrainSTEM maintains standardized, controlled vocabularies for resources, taxonomies and publications to ensure data consistency across the platform. As a user, you can contribute new entries when you encounter equipment, consumables, strains or papers that aren't yet in the system. All submissions go through a review by the BrainSTEM team to maintain data quality and prevent duplicates. You can use your own submission right away while it is pending.

This tutorial guides you through submitting new entries with the **Lookup RRID** and **Lookup DOI** helpers, tracking their approval status, and using approved entries in your research documentation.

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
| **[Anatomical regions]({{"datamodel/taxonomies/anatomicalregion/"|absolute_url}})** | Anatomical structures defined by an atlas (system-loaded, no submission) | Hippocampus CA1, Primary visual cortex, Basal ganglia |
| **[Setup types]({{"datamodel/taxonomies/setuptype/"|absolute_url}})** | Experimental environment categories | T-maze, Open field, Head-fixed disc, Surgical table |
| **[Species]({{"datamodel/taxonomies/species/"|absolute_url}})** | Organism species | Mus musculus, Rattus norvegicus, Macaca mulatta |
| **[Strains]({{"datamodel/taxonomies/strain/"|absolute_url}})** | Genetic strains within species | C57BL/6J, Long-Evans, Sprague-Dawley |
| **[Behavioral categories and paradigms]({{"datamodel/taxonomies/behavioralparadigm/"|absolute_url}})** | Standardized behavioral tasks | Alternation task, Open field exploration |
| **[Regulatory authorities]({{"datamodel/taxonomies/regulatoryauthority/"|absolute_url}})** | Bodies that issue licenses | National and institutional authorities |

Anatomical regions are loaded from reference atlases (Allen CCF, Waxholm Space and others) and cannot be submitted; choose the atlas on the form and search its regions instead.

### Dissemination
{: .no_toc}

| Type | Description |
|------|-------------|
| **[Publications]({{"datamodel/dissemination/publication/"|absolute_url}})** | Papers linked to projects; filled in from a DOI |
| **[Journals]({{"datamodel/dissemination/journal/"|absolute_url}})** | Journals of those publications |

### Silicon probe and ECoG array designs
{: .no_toc}

Probe designs are consumables of type **Silicon probe design** and **ECoG array design**. They are imported from vendor catalogs (NeuroNexus, ATLAS Neuroengineering, Cambridge Neurotech, IMEC Neuropixels; Blackrock Neurotech and PMT Corporation for ECoG) and come with a probe schematic drawn from their geometry. Search the catalog before creating one. If your design is missing, submit it as a consumable of the matching type with the geometry fields filled in; it goes through the same review.

## Submission Process

### Before Submitting

**Essential pre-submission checklist:**

1. **Search for existing entries:** Check if the resource or taxonomy already exists to avoid duplicates
2. **Find the identifier:** An RRID (for antibodies, viral vectors, chemicals, instruments, species and strains) or a DOI (for publications) lets BrainSTEM fill in most fields for you
3. **Gather the rest:** Supplier, catalog number and specifications for consumables; manufacturer and model for hardware devices
4. **Verify accuracy:** Double-check names, spellings, and technical specifications

### Submitting New Entries

**To submit a new resource or taxonomy:**

1. Navigate to the appropriate section:
   - **Resources**: Go to **Resources** → Select type (**Consumables**, **Hardware devices**, or **Suppliers**)
   - **Taxonomies**: Go to **Taxonomies** → Select type (**Setup types**, **Species**, **Strains**, **Behavioral paradigms**, ...)
   - **Dissemination**: Go to **Dissemination** → **Publications** or **Journals**

2. Click the **Add** button for the resource or taxonomy type

3. Prefill from an identifier where available:
   - **Consumables, hardware devices, species and strains**: enter the RRID (for example `RRID:AB_123456` for an antibody, `RRID:SCR_001622` for an instrument, `RRID:NCBI_txid9606` for a species, `RRID:IMSR_JAX:000664` for a strain) and click **Lookup RRID**. BrainSTEM fetches the SciCrunch record and fills name, description and external identifiers; for consumables it also sets the type (antibody, viral vector, chemical, drug, dye) and the supplier when the name matches, and for strains it selects the species. Nothing is saved until you submit the form.
   - **Publications**: enter the DOI and click **Lookup DOI**. BrainSTEM fetches the Crossref record and fills title, authors, abstract, volume, URL and date. The journal is selected when its name matches an existing journal; otherwise add the journal first.
   - **Suggest details with AI**: when your administrators have enabled it, a second button next to the lookup fills remaining empty fields with suggestions you can review and undo. It never writes to a record by itself.

4. Fill in or check the remaining fields:

| Resource/Taxonomy | Required Fields | Best Practices |
|------------------|----------------|----------------|
| **Consumables** | Name, consumable type, supplier | Include catalog numbers, specifications, and intended use |
| **Hardware devices** | Name, device type | Provide manufacturer, technical specs, connectivity details |
| **Suppliers** | Name | Include website and product specialties |
| **Setup types** | Name, category | Describe typical experimental use cases |
| **Species** | Scientific name | Add the popular name and follow NCBI Taxonomy conventions |
| **Strains** | Name, species | Include genetic background and supplier sources |
| **Publications** | Title, DOI | Check the authors and journal filled in from Crossref |

5. Add a **Description** to help other users understand when to use this entry

6. Click **Save**. The message "Your submission will now go through an approval process - The admin team has been notified." confirms the submission.

{: .note }
> Detailed descriptions speed up review and help other users select the correct entries. Include specifications, use cases, and any relevant technical details.

### Submission Guidelines

**Follow these standards for high-quality submissions:**

- **Use standard nomenclature:** Follow established scientific naming conventions (e.g., NCBI for species)
- **Be specific and descriptive:** 
  - Good: "NeuroNexus A1x32-Poly2 silicon probe, 32-channel, 25μm spacing"
  - Avoid: "Silicon probe"
- **Include identifiers:** An RRID or DOI makes the entry findable and feeds the STAR Methods report and NWB export
- **Include references:** Cite manufacturer datasheets, or scientific classifications
- **Check spelling carefully:** Typos can cause rejection or create confusion in the database
- **Avoid abbreviations without context:** Define acronyms and technical terms in descriptions
- **Provide manufacturer links:** Include URLs to product pages or technical documentation where applicable

## Tracking Submissions

### Monitoring Approval Status

**To check the status of your submissions:**

1. Open **Tools** → **Pending approvals**, or go to [www.brainstem.org/private/approvals/](https://www.brainstem.org/private/approvals/). The page lists submissions awaiting review, grouped by Resources, Taxonomies and Dissemination. The **Pending approvals** dashboard widget shows the same counts.
2. Review your submissions and their current status:

| Status | Description | Action Required |
|--------|-------------|----------------|
| **Pending** | Under review. The entry is visible only to you and can already be used in your own records. | Wait for feedback; no action needed |
| **Accepted** | Now available to all users | Entry is live |
| **Changes Required** | Needs modifications before approval | Address the feedback; unaddressed requests are rejected after 30 days |
| **Hold for Merge** / **Merged** | A matching entry already exists; your submission is merged into it after 30 days (or sooner) | Use the existing entry |
| **Hold for Rejection** / **Rejected** | Declined, with the reason | Review the feedback and submit a corrected entry |
| **Cancelled** | Withdrawn by you | None |

3. You are emailed on every status change. In dropdowns, your pending entries carry a status badge such as "Pending" or "Changes Required (!)" next to their name.

### Responding to Feedback

**If your submission requires revisions:**

1. **Read the reviewer's comments carefully** to understand specific concerns or needed improvements
2. **Gather additional information** if specifications, references, or details are requested
3. **Edit your pending entry** to address each point of feedback; a change to an existing accepted entry creates a new change request for review
4. **Add a note** explaining your revisions

**Common reasons for revision requests:**
- Missing technical specifications or catalog numbers
- Unclear or ambiguous naming
- Duplicate entries (similar item already exists)
- Need for additional references or documentation
- Inconsistent formatting or nomenclature

{: .note }
> Responding promptly to feedback speeds up the approval process. Most revisions are simple clarifications that can be addressed quickly. Reviewers are users with the Taxonomies, Resources or Dissemination admin role; their own submissions are accepted directly.

## After Approval

Once your submission is approved, it becomes part of the BrainSTEM platform:

**Immediate effects:**
- The entry appears in dropdown menus across BrainSTEM for all users, without the pending badge
- The entry is listed on the public portal; shared catalogs are always public
- Records you already created with the pending entry keep pointing to it

**Long-term impact:**
- Your contribution helps standardize data across the research community
- Other labs can use your submissions, improving data interoperability
- The entry can be referenced in future resource submissions
- It becomes part of the permanent BrainSTEM vocabulary

{: .note }
> Approved entries can only be deleted by the catalog administrators. To correct one, edit it; the change is submitted for review in the same way.

## Next Steps

After successfully contributing resources and taxonomies to BrainSTEM, consider these logical progressions:

- **Set Up Your Lab Infrastructure**: Use your newly approved resources in the [Setting Up Lab Infrastructure tutorial]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure) to configure your own experimental setups with the equipment and suppliers you've contributed
- **Begin Experimental Documentation**: Start documenting your research using the [Get Started tutorial]({{site.baseurl}}/tutorials/get_started) and incorporate your approved resources into real experimental workflows
- **Explore Specific Workflows**: Depending on your research focus, dive into detailed experimental tutorials like [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) that will use your contributed resources
- **Organize Your Team**: Use [Managing Projects]({{site.baseurl}}/tutorials/managing-projects) and [Managing Groups]({{site.baseurl}}/tutorials/managing-groups) to organize access to your contributed resources across your research team
- **Continue Contributing**: As you discover new equipment, suppliers, or taxonomic categories in your research, continue expanding the BrainSTEM resource database by submitting additional entries
