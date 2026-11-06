---
layout: default
title: Resources & Taxonomies
parent: Tutorials
nav_order: 12
---

# Resources & Taxonomies
{: .no_toc}

BrainSTEM keeps shared catalogs of resources (consumables, hardware devices, suppliers), taxonomies (species, strains, setup types, behavioral paradigms, ...) and publications, so that every lab describes the same thing the same way. This tutorial adds a missing entry with the **Lookup RRID** or **Lookup DOI** helper, follows its review and uses it in your own entries. At the end, your entry is in the catalog for everyone, and you could use it from the moment you submitted it.

**Prerequisites**: a BrainSTEM account (see [Get started!]({{site.baseurl}}/tutorials/get_started)).

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## What you can submit

### Resources
{: .no_toc}

| Resource | What it is | Examples |
|----------|------------|----------|
| **[Consumables]({{"datamodel/resources/consumable/"|absolute_url}})** | Materials and device designs used in experiments | Silicon probe designs, viral vectors, drugs, antibodies |
| **[Hardware devices]({{"datamodel/resources/hardwaredevice/"|absolute_url}})** | Instruments | Recording systems, cameras, stimulators, microscopes |
| **[Suppliers]({{"datamodel/resources/supplier/"|absolute_url}})** | Vendors and manufacturers | Equipment manufacturers, chemical suppliers |

### Taxonomies
{: .no_toc}

| Taxonomy | What it is | Examples |
|----------|------------|----------|
| **[Setup types]({{"datamodel/taxonomies/setuptype/"|absolute_url}})** | Kinds of experimental setup, grouped by category | Theta maze, Open field arena, Head-fixed disc, Surgical table |
| **[Species]({{"datamodel/taxonomies/species/"|absolute_url}})** | Organism species | Mus musculus, Rattus norvegicus |
| **[Strains]({{"datamodel/taxonomies/strain/"|absolute_url}})** | Genetic strains within a species | C57BL/6J, Long-Evans |
| **[Behavioral categories and paradigms]({{"datamodel/taxonomies/behavioralparadigm/"|absolute_url}})** | Standardized behavioral tasks | Delayed Alternation, Spontaneous Alternation |
| **[Regulatory authorities]({{"datamodel/taxonomies/regulatoryauthority/"|absolute_url}})** | Bodies that issue licenses | National and institutional authorities |

[Anatomical regions]({{"datamodel/taxonomies/anatomicalregion/"|absolute_url}}) are loaded from reference atlases (Allen CCF, Waxholm Space and others) and cannot be submitted; choose the atlas on the form and search its regions instead.

### Dissemination
{: .no_toc}

| Type | What it is |
|------|------------|
| **[Publications]({{"datamodel/dissemination/publication/"|absolute_url}})** | Papers linked to projects; filled in from a DOI |
| **[Journals]({{"datamodel/dissemination/journal/"|absolute_url}})** | Journals of those publications |

Silicon probe and ECoG array designs are consumables imported from vendor catalogs; search the [Probe catalog]({{site.baseurl}}/webinterface/probe-catalog/) before submitting one.

## Step 1: Search before you submit

Open the catalog (for example **Resources** → **Consumables**) and search for the item. If a matching entry exists, use it. Then find the item's identifier: an RRID (antibodies, viral vectors, chemicals, instruments, species, strains) or a DOI (publications) lets BrainSTEM fill in most fields for you.

## Step 2: Submit a new entry

1. Open the catalog: **Resources** → **Consumables**, **Hardware devices** or **Suppliers**; **Taxonomies** → **Setup types**, **Species**, **Strains**, **Behavioral paradigms**, ...; or **Dissemination** → **Publications** or **Journals**.
2. Click the **Add** button of that catalog.
3. Fill in the form from the identifier:
   - **Consumables, hardware devices, species and strains**: enter the RRID (for example `RRID:AB_123456` for an antibody, `RRID:SCR_001622` for an instrument, `RRID:NCBI_txid9606` for a species, `RRID:IMSR_JAX:000664` for a strain) and click **Lookup RRID**. BrainSTEM fetches the SciCrunch record and fills in the name, description and external identifiers. For consumables it also sets the type (antibody, viral vector, chemical, drug, dye) and the supplier when the name matches; for strains it selects the species.
   - **Publications**: enter the DOI and click **Lookup DOI**. BrainSTEM fetches the Crossref record and fills in the title, authors, abstract, volume, URL and date. The journal is selected when it matches an existing journal; otherwise add the journal first.
   - Where **Suggest details with AI** is offered next to the lookup, it fills the remaining empty fields with suggestions you can review and undo.
4. Check the filled-in fields and complete the required ones. Write a **Description** that tells other users when to use this entry. The fields of each catalog are described on its data model page, linked in the tables above.
5. Click **Save**. Nothing is saved before this. The message "Your submission will now go through an approval process - The admin team has been notified." confirms the submission.

Be specific: "NeuroNexus A1x32-Poly2 silicon probe, 32 channels, 25 μm spacing" rather than "Silicon probe". Follow established nomenclature (NCBI Taxonomy for species), define abbreviations and link the manufacturer's page. An RRID or DOI also feeds the STAR Methods report and the NWB export.

## Step 3: Use your entry right away

You can select your pending entry in your own entries at once.

{: .important }
> A pending entry is visible only to you until it is accepted. Your lab mates cannot see or select it, so an entry they need to fill in themselves has to wait for the review.

In dropdowns it carries a status badge such as "Pending" or "Changes Required (!)". Entries you create with it keep pointing to it after it is accepted.

## Step 4: Follow the review

BrainSTEM curators review every submission. Open **Tools** → **Pending approvals**, or go to [www.brainstem.org/private/approvals/](https://www.brainstem.org/private/approvals/), to see your submissions grouped by Resources, Taxonomies and Dissemination. The **Pending approvals** dashboard widget shows the same counts. You are emailed on every status change.

| Status | Meaning | What to do |
|--------|---------|------------|
| **Pending** | Under review; visible only to you, already usable in your own entries | Nothing |
| **Accepted** | Available to all users | Nothing |
| **Changes Required** | The curators ask for changes | Edit the entry and add a note; requests left unanswered are rejected after 30 days |
| **Hold for Merge** / **Merged** | A matching entry already exists; your submission is merged into it after 30 days (or sooner) | Use the existing entry |
| **Hold for Rejection** / **Rejected** | Declined, with the reason | Read the reason and submit a corrected entry |
| **Cancelled** | Withdrawn by you | Nothing |

Common reasons for a change request are a missing catalog number or specification, an ambiguous name, a duplicate, or nomenclature that does not follow the convention.

## End state

Once accepted, the entry appears in the dropdowns of all users without a badge and on the public portal; shared catalogs are always public. You cannot delete an accepted entry. To correct one, edit it: the change is submitted for review in the same way.

## Next steps

- **Next:** [Setting Up Lab Infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure): link your equipment and stock to catalog entries.
- [Behavioral Assays]({{site.baseurl}}/tutorials/behavioral-assays): use a setup type and a behavioral paradigm in an assay.
- [Manage Projects]({{site.baseurl}}/tutorials/managing-projects): link a publication to a project.
- Data model: [Resources]({{site.baseurl}}/datamodel/resources/), [Taxonomies]({{site.baseurl}}/datamodel/taxonomies/) and [Dissemination]({{site.baseurl}}/datamodel/dissemination/).
