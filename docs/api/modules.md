---
layout: default
title: Modules
parent: API
has_children: true
nav_order: 2
has_toc: false
---
# Modules API Endpoints

The Modules app provides specialized endpoints for managing experimental protocols, procedures, equipment, and detailed logging of experimental activities. These modules extend the core STEM functionality with detailed tracking capabilities for complex experimental workflows.

## Available Endpoints

The Modules app includes the following specialized endpoints:

- **[Procedures](/api/modules/procedure/)** - Experimental procedures and protocols
- **[Behaviors](/api/modules/behavior/)** - Behavioral paradigms and tasks
- **[Data Acquisition](/api/modules/dataacquisition/)** - Data collection configuration and metadata
- **[Manipulations](/api/modules/manipulation/)** - Experimental manipulations and interventions
- **[Equipment](/api/modules/equipment/)** - Laboratory equipment and instrumentation
- **[Procedure Logs](/api/modules/procedurelog/)** - Detailed logs of procedure execution
- **[Subject Logs](/api/modules/subjectlog/)** - Subject-specific activity and observation logs
- **[Consumable Stock](/api/modules/consumablestock/)** - Laboratory consumables inventory management

Each endpoint supports standard CRUD operations with comprehensive filtering, sorting, and relationship inclusion capabilities.

## Common Use Cases

- Define and standardize experimental procedures across projects
- Track behavioral paradigms and experimental manipulations
- Log detailed procedure execution and subject observations
- Manage laboratory equipment and consumable inventory
- Configure data acquisition systems and parameters
- Maintain audit trails for experimental activities
- Link procedures to specific sessions and subjects
