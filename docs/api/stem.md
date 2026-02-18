---
layout: default
title: STEM
parent: API
has_children: true
nav_order: 1
has_toc: false
---
# STEM API Endpoints

The STEM app provides the core data model to track your experiments. This section documents the primary endpoints for managing projects, sessions, subjects, and related data structures.

## Available Endpoints

The STEM module includes the following key endpoints:

- **[Projects](/api/stem/project/)** - Research project organization
- **[Subjects](/api/stem/subject/)** - Research subjects
- **[Sessions](/api/stem/session/)** - Experimental sessions
- **[Cohorts](/api/stem/cohort/)** - Subject cohorts for studies
- **[Collections](/api/stem/collection/)** - Data collections and groupings of sessions
- **[Project Group Membership Invitations](/api/stem/project_group_membership_invitation/)** - Group invitation management
- **[Project Membership Invitations](/api/stem/project_membership_invitation/)** - User invitation management
- **`SessionDataStorage`** (`/api/private/stem/sessiondatastorage/`) - Session-to-data storage relations and ordering
- **`CollectionSession`** (`/api/private/stem/collectionsession/`) - Collection-to-session relations and ordering
- **`CohortSubject`** (`/api/private/stem/cohortsubject/`) - Cohort-to-subject relations and ordering

Each endpoint supports standard CRUD operations (Create, Read, Update, Delete) with consistent authentication and query parameter support.

## Common Use Cases

- Organize experimental sessions by project and subject
- Group subjects into cohorts for comparative studies
- Manage data collections across multiple sessions
- Control project access through membership invitations
- Track collaborative research projects with multiple users
- Export session and subject metadata for analysis workflows
