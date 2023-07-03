---
layout: default
title: Behavior
parent: Modules
grand_parent: Data model
nav_order: 2
---

# Behavior model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction
Behavior is a module in datasets that is used to describe the behavior of subjects. The behavior is described by the physical environment and a behavioral paradigm. Both physical environment and a behavioral paradigm are private attributes and belong to group, and must be defined separately.

## Fields

| Field       | Description  |
|:------------|:-------------|
| Dataset     | Dataset of the behavior (**required**) |
| Subjects    | Subjects taking part in the behavior (**required**) |
| Physical environment | Physical environment of the behavior (**required**) |
| Behavioral paradigm  | Behavioral paradigm of the behavior (**required**) |
| Description | Description of the action (max length: 500) |

## Permissions
Behavior inherit permissions through the dataset associated with it.

Visit the [permissions page] to learn more. 

## Behavior API access
The API allows for programmable access to behaviors. Learn more about the behaviors' fields and data structure on the [Behavior API page]({{"api/modules/behavior/"|absolute_url}}). 
