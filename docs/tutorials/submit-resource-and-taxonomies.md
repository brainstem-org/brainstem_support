---
layout: default
title: Submit Resources & Taxonomies
parent: Tutorials
nav_order: 8
---

# Submitting Resources & Taxonomies
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

BrainSTEM maintains controlled lists of resources and taxonomies that can be expanded through user submissions. All submissions go through an approval process to maintain data quality and consistency.

## Available Resources & Taxonomies

Resources that can be submitted:
- [Consumables]({{"datamodel/resources/consumable/"|absolute_url}})
- [Hardware devices]({{"datamodel/resources/hardwaredevice/"|absolute_url}}) 
- [Suppliers]({{"datamodel/resources/supplier/"|absolute_url}})

Taxonomies that can be submitted:
- [Brain regions]({{"datamodel/taxonomies/brainregion/"|absolute_url}})
- [Setup types]({{"datamodel/taxonomies/setuptype/"|absolute_url}})
- [Species]({{"datamodel/taxonomies/species/"|absolute_url}})
- [Strains]({{"datamodel/taxonomies/strain/"|absolute_url}})

## Submission Process

### Before Submitting

1. **Check for existing entries:** Search the current lists to avoid duplicating existing resources or taxonomies
2. **Gather complete information:** Ensure you have all necessary details like specifications, supplier information, or scientific classifications
3. **Verify accuracy:** Double-check names, spellings, and technical details

### Submitting New Entries

1. Navigate to the appropriate section in BrainSTEM:
   - For resources: Go to *Resources* → select the type (Consumables, Hardware devices, or Suppliers)
   - For taxonomies: Go to *Taxonomies* → select the type (Setup types, Species, or Strains)

2. Click the *Add* button for the resource or taxonomy type

3. Fill out the submission form with all required fields:
   - **For consumables:** Include product name, supplier, specifications
   - **For hardware devices:** Provide manufacturer, model, specifications, interface details
   - **For species/strains:** Include scientific names, common names, description

4. Add detailed descriptions to help other users understand when to use this entry

5. Submit the form for admin review

{: .note }
> Provide as much detail as possible in descriptions. This helps admins review submissions faster and helps other users select the correct entries.

### Common Submission Guidelines

- **Use standard nomenclature:** Follow established scientific naming conventions
- **Include references:** Add citations for taxonomies based on published atlases or classifications  
- **Be specific:** "Silicon probe, 32-channel, A1x32-Poly2" is better than just "Silicon probe"
- **Check spelling:** Typos can lead to rejection or confusion

## Tracking Submissions

### Monitoring Status

1. Go to [https://www.brainstem.org/private/approvals/](https://www.brainstem.org/private/approvals/)
2. View the status of your submissions:
   - **Pending:** Under admin review
   - **Approved:** Accepted and available to all users
   - **Rejected:** Declined with feedback for revision
3. Check the "Comments" field for admin feedback or revision requests

### Responding to Feedback

If your submission needs revision:
1. Read the admin comments carefully
2. Make the suggested changes
3. Resubmit following the same process
4. Reference the original submission in your revision notes

{: .tip }
> Admins may request clarification on specifications, ask for additional references, or suggest naming improvements. Addressing feedback promptly helps speed up the approval process.

## After Approval

Once approved:
- The entry becomes available in dropdown menus across BrainSTEM
- All users can select and use the approved entry
- The entry can be referenced in new submissions

## Next Steps

After successfully contributing resources and taxonomies to BrainSTEM, consider these logical progressions:

- **Set Up Your Lab Infrastructure**: Use your newly approved resources in the [Setting Up Lab Infrastructure tutorial]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure) to configure your own experimental setups with the equipment and suppliers you've contributed
- **Begin Experimental Documentation**: Start documenting your research using the [Get Started tutorial]({{site.baseurl}}/tutorials/get_started) and incorporate your approved resources into real experimental workflows
- **Explore Specific Workflows**: Depending on your research focus, dive into detailed experimental tutorials like [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) that will use your contributed resources
- **Organize Your Team**: Use [Managing Projects]({{site.baseurl}}/tutorials/managing-projects) and [Managing Groups]({{site.baseurl}}/tutorials/managing-groups) to organize access to your contributed resources across your research team
- **Continue Contributing**: As you discover new equipment, suppliers, or taxonomic categories in your research, continue expanding the BrainSTEM resource database by submitting additional entries
