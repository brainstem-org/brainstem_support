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
| `Session` | Session of the behavior (**required**) |
| `Subjects` | Subjects taking part in the behavior (**required**) |
| `Experimental setup` | Experimental setup of the behavior (**required**) |
| `Behavioral paradigm` | Behavioral paradigm of the behavior (**required**) |
| `Notes` | Notes about the behavior (max length: 500 characters) |

## Permissions

Behaviors inherit permissions through their associated session.

Visit the [permissions page]({{"datamodel/permission/"|absolute_url}}) to learn more. 

## Behavior API access

The API allows for programmable access to behaviors. Learn more about the behaviors' fields and data structure on the [Behavior API page]({{"api/modules/behavior/"|absolute_url}}).
