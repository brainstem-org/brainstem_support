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
The behavior model is a module in datasets that is used to describe the behavior occuring in a dataset. The behavior is described by the involved subjects, the experimental setup, and a behavioral paradigm. Both the experimental setup and the behavioral paradigm are private attributes and must be defined separately. You must create both before filling in the behavior form. The private attributes belong to group(s) that must be shared with one of a dataset's associated projects.

## Fields

| Field       | Description  |
|:------------|:-------------|
| Dataset     | Dataset of the behavior (**required**) |
| Subjects    | Subjects taking part in the behavior (**required**) |
| Experimental setup | Experimental setup of the behavior (**required**) |
| Behavioral paradigm  | Behavioral paradigm of the behavior (**required**) |
| Description | Description of the action (max length: 500) |

## Permissions
Behavior inherit permissions through the dataset associated with it.

Visit the [permissions page] to learn more. 

## Behavior API access
The API allows for programmable access to behaviors. Learn more about the behaviors' fields and data structure on the [Behavior API page]({{"api/modules/behavior/"|absolute_url}}). 
