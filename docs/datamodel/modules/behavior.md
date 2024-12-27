---
layout: default
title: Behavior
parent: Modules
grand_parent: Data model
nav_order: 1
---

# Behavior model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

The behavior model is a module in sessions used to describe the behavior occurring in a session. The behavior is characterized by the involved subjects, the experimental setup, and a behavioral paradigm. Both the experimental setup and the behavioral paradigm are private attributes that must be defined separately before filling in the behavior form. These private attributes belong to group(s) that must be shared with one of the session's associated projects.

## Fields

| Field | Description |
|:------|:------------|
| `Session` | Session of the behavior (**required**). Must reference an existing [session]({{"datamodel/stem/session/"|absolute_url}}). Example: "Training session #5" |
| `Subjects` | Subjects taking part in the behavior (**required**). Can include multiple subjects. Example: "Mouse_01", "Mouse_02" |
| `Setups` | Setup of the behavior (**required**). Must reference an existing [setup]({{"datamodel/personal_attributes/setup/"|absolute_url}}). Example: "Linear track A" |
| `Behavioral paradigm` | Behavioral paradigm of the behavior (**required**). Must reference an existing [behavioral paradigm]({{"datamodel/personal_attributes/behavioralparadigm/"|absolute_url}}). Example: "Spatial alternation task" |
| `Notes` | Notes about the behavior (string). Example: "Subject performed normally with 85% accuracy" |

## Permissions

Behaviors inherit permissions through their associated session.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Behavior API access

The API allows for programmable access to behaviors. Learn more about the behaviors' fields and data structure on the [Behavior API page]({{"api/modules/behavior/"|absolute_url}}).
