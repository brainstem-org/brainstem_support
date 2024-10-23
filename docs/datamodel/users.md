---
layout: default
title: Users
parent: Data model
has_children: true
nav_order: 7
---

# User

The User model in BrainSTEM manages the authentication, authorization, and organizational aspects of the platform. It consists of three main components:

### Permissions and ownership

- __Users__: Individual accounts on the BrainSTEM platform. All user profiles are public within the system.

- __Groups__: Collections of users that can be used for organizing teams or labs. All groups are public within BrainSTEM.

- __Laboratories__: Organizational units that are tied to groups in a one-to-one relationship. Linking a group to a lab allows for additional information to be associated with the group.