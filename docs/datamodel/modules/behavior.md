---
layout: default
title: Behaviors
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

The behaviors model is a module in sessions used to describe the behaviors occurring in a session. The behaviors are characterized by the involved subjects, the setups, and behavioral paradigms. Both the setups and the behavioral paradigms are private attributes that must be defined separately before filling in the behavior form. These private attributes belong to group(s) that must be shared with one of the session's associated projects.

## Fields

| Field | Description |
|:------|:------------|
| `Sessions` | Sessions of the behavior (**required**). Must reference an existing [sessions]({{"datamodel/stem/session/"|absolute_url}}). Example: "Training session #5" |
| `Subjects` | Subjects taking part in the behavior (**required**). Can include multiple subjects. Example: "Mouse_01", "Mouse_02" |
| `Setup` | Setup of the behavior (**required**). Must reference an existing [setups]({{"datamodel/personal_attributes/setup/"|absolute_url}}). Example: "Linear track A" |
| `Behavioral paradigms` | Behavioral paradigms of the behavior (**required**). Must reference an existing [behavioral paradigms]({{"datamodel/personal_attributes/behavioralparadigm/"|absolute_url}}). Example: "Spatial alternation task" |
| `Notes` | Notes about the behavior (string). Example: "Subject performed normally with 85% accuracy" |

## Permissions

Behaviors inherit permissions through their associated session.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Behaviors API access

The API allows for programmable access to behaviors. Learn more about the behaviors' fields and data structure on the [Behaviors API page]({{"api/modules/behavior/"|absolute_url}}).
