---
layout: default
title: FAQ
nav_order: 8
---

# Frequently asked questions
{: .no_toc}

Short answers to the questions new users ask most, each with a link to the page that explains it in full.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Access and sharing

### How do I give a colleague access to my project?

Open the project, click **Manage** and use **Invite user** or **Invite group**. Inviting your lab's group is usually best: everyone in the group gets the level you choose, including people who join later. See [Sharing and memberships]({{site.baseurl}}/webinterface/sharing-and-memberships/).

### A colleague cannot see my subject or session. Why?

Subjects and sessions are visible to the people of their projects. Check that the entry lists the right project under **Projects**, and that your colleague (or their group) has access to that project. See [Permissions]({{site.baseurl}}/datamodel/permissions/).

### Why can't I select a setup, inventory, assay or data storage in a form?

Using a lab resource on an entry needs the Contributor level on that resource; Members can see it but not use it. Ask an owner or manager of the resource to raise your level, or to give it to your group. For behavioral assays, the assay's setup type must also match the setup of the behavior. See [Personal attributes]({{site.baseurl}}/datamodel/personal_attributes/) and [Behavioral assays]({{site.baseurl}}/tutorials/behavioral-assays/).

### What is the difference between a project, a cohort and a collection?

A project holds subjects and sessions and decides who can see them. A cohort is an ordered subgroup of subjects within one project, for example an experimental group. A collection is an ordered subgroup of sessions within one project, for example the sessions of one figure. See [Cohorts]({{site.baseurl}}/datamodel/stem/cohort/) and [Collections]({{site.baseurl}}/datamodel/stem/collection/).

## Entering data

### Can I import my existing spreadsheets?

Yes. The import tool creates subjects, sessions, procedures and other entries from a grid you fill in or a CSV template. See [Import tool]({{site.baseurl}}/webinterface/import-tool/).

### My species, strain, probe or device is missing from the lists.

Submit it to the shared catalog. You can use a submitted entry right away, while it awaits review. See [Submitting resources and taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies/).

### I deleted an entry by mistake. Can I get it back?

Yes. Deleted entries are kept, and the **Recover** button in the list's toolbar restores them. See [Deleted entries]({{site.baseurl}}/webinterface/deleted-entries/).

### Which kind of entry do I use for …?

It depends on what happened: a surgery or injection is a procedure, a weight or health check a subject log, an implanted device an experimental interface, tissue taken out a specimen set, and what was recorded, delivered or done in a session a data acquisition, manipulation or behavior. See [Where do I record it?]({{site.baseurl}}/datamodel/#where-do-i-record-it).

### Where do my planned sessions go?

Planned entries carry an orange **Planned** pill and stay out of counts, the public portal and API listings until they are marked as performed. See [Planning]({{site.baseurl}}/webinterface/planning/).

### Where do I find an entry's id?

See [Finding an ID]({{site.baseurl}}/webinterface/import-tool/#finding-an-id).

## Sharing and export

### How do I make my data public?

Set the project's **Project visibility** to **Public**. Lab resources the project uses, such as setups and protocols, are shared separately, and planned entries are never public. See [Share data publicly]({{site.baseurl}}/tutorials/sharing-project-publicly/).

### Does BrainSTEM store my data files?

No. BrainSTEM holds the metadata; a data storage entry records where the files live and how to reach them. See [Managing data storage]({{site.baseurl}}/tutorials/managing-data-storage/).

### Can I export to NWB?

Yes: download a project or session export and convert it with brainstem-nwb. See [Exporting to NWB]({{site.baseurl}}/tutorials/exporting-to-nwb/).

## Account and API

### I lost my phone with my authenticator app.

Sign in with a backup token or email code, then set up the app again. See [Two-factor authentication: Recovery]({{site.baseurl}}/webinterface/two-factor-authentication/#recovery).

### How long does an API token last?

One year from when it was created; using it does not extend it. Create a new token before it expires. See [API authentication]({{site.baseurl}}/api/#authentication).

### Can the AI assistant change my data?

The in-app assistant only reads, and only what you may read. The MCP server and agent skills act with your token's permissions, so read [Working with AI]({{site.baseurl}}/tutorials/working-with-ai/) before connecting them.

## Still stuck?

Ask in [GitHub Discussions](https://github.com/brainstem-org/brainstem_support/discussions), report a problem in [GitHub Issues](https://github.com/brainstem-org/brainstem_support/issues), or use the [contact form](https://brainstem.org/#Get-in-touch) for account-specific questions.
