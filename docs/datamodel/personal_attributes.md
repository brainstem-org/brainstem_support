---
layout: default
title: Personal attributes
parent: Data model
has_children: true
nav_order: 7
has_toc: false
---

# Personal attributes

Personal attributes are a lab's own resources. They are shared on their own terms, with individual people or with whole groups, and never through a project: a collaborator on your project does not automatically get your rig, your reagent inventory or your licenses. Each personal attribute has four roles (Member, Contributor, Manager, Owner), a **Public access** switch that publishes it read-only on the public portal, and its own management page where users and groups are invited. People without a BrainSTEM account can be invited by email; the invitation is accepted when they register. The main categories are:

- [**Behavioral assays**]({{site.baseurl}}/datamodel/personal_attributes/behavioralassay): Your lab's implementation of a behavioral paradigm on a setup type, with the licenses that authorize it. Behaviors in sessions point to an assay.

- [**Data storages**]({{site.baseurl}}/datamodel/personal_attributes/datastorage): Where session data live and how they are reached: location, data organization and access protocols. Sessions link to one or more data storages.

- [**Inventories**]({{site.baseurl}}/datamodel/personal_attributes/inventory): The stores that hold [consumable stock]({{site.baseurl}}/datamodel/modules/consumablestock), the lots that material usages are traced to.

- [**Licenses**]({{site.baseurl}}/datamodel/personal_attributes/license): Regulatory authorizations (animal research, biosafety, controlled substances and others) with type, status, issuing authority, validity dates, document and holders. Attached to subjects, procedures, procedure episodes, specimen procedures, behavioral assays and protocols.

- [**Protocols**]({{site.baseurl}}/datamodel/personal_attributes/protocol): Written methods such as SOPs and published protocols, typed for breedings, procedures, specimen procedures, subject logs or specimen logs and optionally restricted to subtypes. Work that followed a protocol references it instead of repeating it.

- [**Setups**]({{site.baseurl}}/datamodel/personal_attributes/setup): The physical rigs and workstations of the lab, each of a shared setup type, with their [equipment]({{site.baseurl}}/datamodel/modules/equipment), image, location and specifications.

## Permissions

| Role | Can |
|:-----|:----|
| Member | See the attribute: it appears in lists and its detail page opens. Cannot use it on an experimental record or change it. |
| Contributor | Use it on experimental records (select the equipment of a setup, the stock of an inventory, an assay, a data storage, a license or a protocol) and, for setups and inventories, add and edit their equipment or stock. |
| Manager | Everything a Contributor can do, plus managing who has access. |
| Owner | Everything a Manager can do, plus editing the attribute's own fields, changing public access and deleting it. |

Groups selected when the attribute is created receive access; afterwards access is managed from the attribute's own page. Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.
