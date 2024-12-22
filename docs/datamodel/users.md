---
layout: default
title: Users
parent: Data model
has_children: false
nav_order: 8
has_toc: false
---

# User

The User model in BrainSTEM manages the authentication, authorization, and organizational aspects of the platform. It consists of three main components:

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Components

### Users

Individual accounts on the BrainSTEM platform. All user profiles are public within the system.

### Groups

Collections of users that can be used for organizing teams or labs. All groups are public within BrainSTEM.
### Laboratories 

Organizational units that are tied to groups in a one-to-one relationship. Linking a group to a lab allows for additional information to be associated with the group.

## Permission Inheritance

For detailed information about permission levels and inheritance, please visit the [permissions documentation]({{site.baseurl}}/datamodel/permissions/).

## User Management API

The API provides programmatic access to user management functions. Learn more about the available endpoints and data structures on the [Users API page]({{site.baseurl}}/api/users).
