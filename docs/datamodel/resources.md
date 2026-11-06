---
layout: default
title: Resources
parent: Data model
has_children: true
nav_order: 8
has_toc: false
---

# Resources

Resources are the shared catalog used by every lab: the product identities of consumables and hardware devices, and the suppliers that provide them. One list is used by everyone on BrainSTEM, which is what makes work comparable between labs. Entries carry a Research Resource Identifier (RRID) and external identifiers where they exist, and the catalog is expandable through user submissions that go through an approval queue.

- [**Consumables**]({{site.baseurl}}/datamodel/resources/consumable): Products that are used up or dedicated to one subject: reagents, solutions, virus constructs, silicon probe and ECoG array designs, optic fibers, electrodes, surgical consumables. A lab's own lot of a consumable is a [consumable stock]({{site.baseurl}}/datamodel/modules/consumablestock) in an inventory.

- [**Hardware devices**]({{site.baseurl}}/datamodel/resources/hardwaredevice): Durable instrument products such as amplifiers, cameras, acquisition systems and stereotaxic frames. A lab's own unit is an [equipment]({{site.baseurl}}/datamodel/modules/equipment) entry in a setup.

- [**Suppliers**]({{site.baseurl}}/datamodel/resources/supplier): Companies, organizations or individuals that provide consumables or hardware devices. Both require a supplier, and subjects can name their supplier too.

## Submission and approval

Anyone can submit a new entry or propose a change to an existing one. A submission enters the approval queue and is usable immediately in your own records; a pending entry is visible only to you until it is accepted. Approval statuses are Pending, Accepted, Changes required, Hold for rejection, Rejected and Cancelled. A rejected entry is replaced with "Other" wherever it was used, so check the existing list for near-duplicates before submitting. Resources admins review submissions and can edit or delete accepted entries.

## RRID lookup

Consumable and hardware device forms have a **Lookup RRID** button beside the RRID field. It fetches the entry from the SciCrunch registry and fills in the name, description and external identifiers, and suggests or matches the supplier. Everything it fills stays editable. You can paste either `RRID:Addgene_176754` or `Addgene_176754`.
