---
layout: default
title: Schemas
parent: API
has_children: true
nav_order: 8
has_toc: false
---
# JSON Schemas

JSON schemas provide formal validation and documentation for complex data structures used throughout the BrainSTEM API. These schemas ensure data consistency, enable validation, and provide clear documentation for developers working with structured data fields.

## Available Schema Documentation

The following pages describe the JSON schema specifications used across BrainSTEM:

### Core Schemas
- **[Coordinates](/api/schemas/coordinates/)** - Spatial coordinate system schemas for anatomical positioning

### Module Schemas
- **[Data Acquisition](/api/schemas/dataacquisition/)** - Data acquisition configuration and metadata schemas
- **[Equipment](/api/schemas/equipment/)** - Laboratory equipment specification schemas
- **[Procedures](/api/schemas/procedure/)** - Experimental procedure definition schemas
- **[Manipulations](/api/schemas/manipulation/)** - Experimental manipulation specification schemas
- **[Procedure Logs](/api/schemas/procedurelog/)** - Procedure logging schemas
- **[Subject Logs](/api/schemas/subjectlog/)** - Subject observation and activity logging schemas
- **[Consumable Stock](/api/schemas/consumablestock/)** - Inventory management schemas

## Common Use Cases

- Validate structured data before submission to the API
- Understand expected data formats for complex fields
- Generate client-side validation for data entry forms
- Ensure consistency across different data acquisition systems
- Document equipment specifications and configurations
- Standardize experimental procedure definitions
- Enable automated data processing and validation workflows
