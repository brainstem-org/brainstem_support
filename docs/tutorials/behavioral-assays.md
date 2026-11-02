---
layout: default
title: Behavioral Assays
parent: Tutorials
nav_order: 5
---
# Behavioral Assays
{: .no_toc}

This tutorial creates a behavioral assay, the description of a task your subjects perform (a T-maze alternation, an open field exploration, a Morris water maze), and shows how a session's **Behavior** refers to it. At the end you have one assay that can be selected in every session recorded on a setup of the same type.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Prerequisites

- An account that belongs to a group (see [Get started!]({{site.baseurl}}/tutorials/get_started)).
- At least one **setup** with the setup type the task is run in, for example a T-maze (see [Setting Up Lab Infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure)).

## How assays, setups and sessions fit together

A behavioral assay belongs to a **setup type** (T-maze, Open field arena, Head-fixed disc, ...). A setup belongs to a setup type too. When you add a **Behavior** to a session, you pick a setup and an assay, and the form requires both to have the same setup type. One assay therefore serves every setup of that type in your lab, and a session records which physical setup was used on that day.

The assay also names a **behavioral paradigm** from the shared taxonomy, so that tasks are comparable across labs. Field definitions are on the [Behavioral assay data model page]({{site.baseurl}}/datamodel/personal_attributes/behavioralassay/).

## Step 1: Open the form

1. Go to **Personal attributes** → **Behavioral assays** in the left menu.
2. Click **Add behavioral assay**.

![A behavioral assay's form: setup category and type, behavioral category and paradigm, licenses, visibility and description.]({{site.baseurl}}/assets/images/screenshots/behavioral-assay-form.png)
{: .screenshot }
*A behavioral assay's form: setup category and type, behavioral category and paradigm, licenses, visibility and description.*

## Step 2: Fill in the assay

| Field | Value |
|-------|-------|
| **Behavioral assay name** * | T-maze Alternation Task |
| **Setup category** | Freely Moving Awake (narrows the setup type list) |
| **Setup type** * | T-maze |
| **Behavioral category** | The category that narrows the paradigm list |
| **Behavioral paradigm** * | Alternation task (select the paradigm that matches your task) |
| **Authenticated groups** * | Select your lab group |
| **Licenses** | The licenses that cover the task, if you keep them in BrainSTEM |
| **Description** | A spatial working memory task. The subject alternates between the left and right arm for a reward. Include the trial structure, cues, rewards, light conditions and room temperature. |
| **Behavioral assay visibility** | Leave on **Private** |

{: .note }
> Setup types and behavioral paradigms are shared taxonomies. If the paradigm or setup type you need is missing, add it under **Taxonomies** → **Behavioral paradigms** or **Setup types**; your pending entry can be used right away while it is reviewed. See [Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies).

## Step 3: Save

Click **Save**. The assay now appears in the **Behavioral assay** dropdown of the **Behavior** tab of a session whenever the selected setup has the setup type T-maze.

{: .important }
> The **Behavior** form shows the notice "The Behavioral assay must belong to the same setup type as the selected setup." If your assay is missing from the dropdown, check the setup type of the setup you picked.

## Step 4: Use the assay in a session

1. Open a session and go to its **Behavior** tab (or add a behavior from **Sessions** → **Behaviors**).
2. Select the **Subjects**, the **Setup** (for example "T-maze Behavior Room") and the **Behavioral assay** "T-maze Alternation Task".
3. Save. The [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) shows a complete session with a behavior, data acquisitions and epochs.

## Sharing an assay

Assays have their own **Behavioral assay visibility** switch and are not published with a project. Make the assay public when you publish a project whose sessions use it, so that readers can see the task; see [Share data publicly]({{site.baseurl}}/tutorials/sharing-project-publicly).

## Next steps

- **Data model**: [Behavioral assays]({{site.baseurl}}/datamodel/personal_attributes/behavioralassay/), [Setups]({{site.baseurl}}/datamodel/personal_attributes/setup/) and [Behaviors]({{site.baseurl}}/datamodel/modules/behavior/).
- **Lab infrastructure**: create the setups and equipment the assays run on in [Setting Up Lab Infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure).
- **Complete workflows**: the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) and the [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) use assays in sessions.
- **Data storage**: link the behavioral sessions to their files with [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage).
