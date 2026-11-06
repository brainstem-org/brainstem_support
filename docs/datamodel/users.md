---
layout: default
title: Users
parent: Data model
has_children: false
nav_order: 11
has_toc: false
---

# Users
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

The users part of the data model covers accounts, the groups that share a lab's resources, and the laboratories that describe those groups. Permissions throughout BrainSTEM are built on users and groups.

{% include datamodel_embed.html model="users.user" %}

## Components

### Users

A user is one person's account, identified by an email address. The account itself grants almost nothing: access arrives through membership of [projects]({{"datamodel/stem/project/"|absolute_url}}) (the research entries), and membership of groups (the lab's setups, inventories, protocols, licenses, assays and data storages). A user has a first and last name, a profile (image, bio, institution, department, city, country, website, ORCID and Google Scholar) and two working preferences: the preferred atlas, which pre-selects the Atlas filter on region selectors, and the active-projects filter, which narrows selectors to the projects the person is currently working on. User names and public profile links are visible to other users; email addresses are not shown on the public portal.

### Groups

A group is a set of people who work together, usually a lab. A group holds no entries of its own: it is a name you can grant access to, so that everyone in it gets that access at once. Projects and personal attributes can both be shared with a group or with individual people. Access does not travel between the two kinds: adding a collaborator to your project does not let them select your equipment unless the setup is shared with them too.

Group membership is managed from the group's management page by its managers and owners. A member holds one of three permission roles: Member, Manager (manages membership) or Owner. People are added by **invitation**, which grants one of these roles, and accept or reject it. A user can also send a **join request** to a group, which its managers accept or reject, and can leave a group. Group names are unique across BrainSTEM, and the public portal shows only a group's id and name.

### Laboratories

A laboratory describes the lab a group represents, in a one-to-one relationship with the group. It records the institution (required), the principal investigators (required; BrainSTEM users), department, city, country, website and a description. Filling it in turns a bare group name into something identifiable to people outside the lab.

### Invitations

Projects, groups and personal attributes invite users through invitations that the invitee accepts or rejects and that the inviter can cancel. An invitation to a project or a personal attribute names the permission role to grant: Member, Contributor, Manager or Owner. People who do not yet have a BrainSTEM account can be invited by email; the **pending invitation** holds the email, the target entry and the role, expires after a time, can be resent, and is accepted when the person registers.

## Permissions

Users and groups hold the permission roles of projects and personal attributes; the entries of a study inherit from their project and a lab's resources from the groups they are shared with. For the roles and what they allow, visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}).

## API access

The API provides programmatic access to users, groups, laboratories, invitations and join requests. Learn more about the available endpoints and data structures on the [Users API page]({{site.baseurl}}/api/users).
