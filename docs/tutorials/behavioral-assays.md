---
layout: default
title: Behavioral Assays
parent: Tutorials
nav_order: 4
---
# Behavioral Assays
{: .no_toc}

This tutorial creates a behavioral assay, the description of a task your subjects perform, and shows how a session's behavior refers to it. The example is the theta-maze alternation task of the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow). At the end you have one assay that can be selected in every session recorded on a setup of the setup type Theta maze.

**Prerequisites**: the setup **Theta Maze Rig** with the setup type Theta maze (see [Setting Up Lab Infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure)).

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## How assays, setups and sessions fit together

[![The behavioral track and the setup track: behavioral categories group paradigms, and an assay is your lab's version of a paradigm on a setup type; a setup is your rig of a setup type, with its equipment. A behavior in a session runs one assay on one setup with its subjects.]({{site.baseurl}}/assets/images/diagrams/behavior-tracks-behavioralassay.svg)]({{site.baseurl}}/assets/images/diagrams/behavior-tracks-behavioralassay.svg)
*The behavioral track and the setup track: behavioral categories group paradigms, and an assay is your lab's version of a paradigm on a setup type; a setup is your rig of a setup type, with its equipment. A behavior in a session runs one assay on one setup with its subjects.*

A behavioral assay belongs to a **setup type** (Theta maze, Open field arena, Head-fixed disc, ...). A setup belongs to a setup type too. When you add a behavior to a session, you pick a setup and an assay, and the form requires both to have the same setup type. One assay therefore serves every setup of that type in your lab, and each session records which physical setup was used on that day.

The assay also names a **behavioral paradigm** from the shared taxonomy, so that tasks are comparable across labs.

## Step 1: Open the form

1. Go to **Personal attributes** → **Behavioral assays** in the left menu.
2. Click **Add behavioral assay**.

![A behavioral assay's form: setup category and type, behavioral category and paradigm, licenses, visibility and description.]({{site.baseurl}}/assets/images/screenshots/behavioral-assay-form.png)
{: .screenshot }
*A behavioral assay's form: setup category and type, behavioral category and paradigm, licenses, visibility and description.*

## Step 2: Fill in the assay

1. Enter the **Name of behavioral assay** "Theta Maze Alternation Task". Once the assay is saved, its edit page (shown above) labels the field **Behavioral assay name**.
2. Select the **Setup category** "Freely Moving Awake", then the **Setup type** "Theta maze". The category narrows the setup type list.
3. Select the **Behavioral category** "Working Memory", then the **Behavioral paradigm** "Delayed Alternation".
4. In **Authenticated groups**, select your lab group. The groups you select get Contributor access to the assay.
5. Click **Save**. The assay's edit page opens.
6. Write a **Description** of the task: trial structure, cues, rewards, light conditions. For example: "Forced alternation in the theta maze. The rat alternates between the left and right arm for a food reward. Trial duration 180 s, inter-trial interval 45 s, 40 trials per session." Leave **Behavioral assay visibility** on **Private** and click **Save**.

All fields, including **Licenses**, are described on the [Behavioral assays]({{site.baseurl}}/datamodel/personal_attributes/behavioralassay/) page.

Setup types and behavioral paradigms are shared taxonomies. If the one you need is missing, add it under **Taxonomies** → **Setup types** or **Behavioral paradigms**; your pending entry can be used right away while it is reviewed. See [Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies).

## Step 3: Use the assay in a session

1. Open a session's edit page and go to its **Behaviors** tab (or add a behavior under **Sessions** → **Behaviors**).
2. Select the **Subjects**, the **Setup** "Theta Maze Rig" and the **Behavioral Assay** "Theta Maze Alternation Task".
3. Click **Save**.

{: .important }
> The behavior form shows the notice "The Behavioral assay must belong to the same setup type as the selected setup." If your assay is missing from the list, check the setup type of the setup you picked.

## End state

The assay "Theta Maze Alternation Task" is offered in the **Behaviors** tab of every session whose behavior uses a setup of the setup type Theta maze. The [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) shows a complete session with a behavior, data acquisitions and epochs.

## Sharing an assay

An assay has its own **Behavioral assay visibility** and is not published with a project. Make it public when you publish a project whose sessions use it, so that readers can see the task; see [Share data publicly]({{site.baseurl}}/tutorials/sharing-project-publicly).

## Next steps

- **Next:** [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage): describe where the recordings of these sessions are stored.
- Data model: [Behavioral assays]({{site.baseurl}}/datamodel/personal_attributes/behavioralassay/), [Setups]({{site.baseurl}}/datamodel/personal_attributes/setup/), [Behaviors]({{site.baseurl}}/datamodel/modules/behavior/) and [Behavioral paradigms]({{site.baseurl}}/datamodel/taxonomies/behavioralparadigm/).
- [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow): another workflow that uses assays in sessions.
