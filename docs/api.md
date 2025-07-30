---
layout: default
title: API
nav_order: 4
has_children: true
has_toc: false
---
# API
{: .no_toc}
The BrainSTEM API provides programmatic access to the complete data model, enabling developers to interact with neuroscience data and metadata through RESTful endpoints. [API tools](/api-tools/) have been developed for MATLAB and Python, and a Web API tool allows for browsing and testing API endpoints directly in your browser.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Token-based API Authentication
To access the API, you must authenticate using a token. The API token can be obtained from the endpoint `https://www.brainstem.org/api/token/` by sending a POST request with your username and password. Once acquired, the token does not expire and can be reused for all subsequent API requests.

### Getting Your API Token
{: .no_toc}
**Example cURL request to get an API token:**

```bash
curl \
  -X POST https://www.brainstem.org/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "user@email.com", "password": "password"}'
```

**Example response:**

```json
{"token":"38d541204dc8c932c563ee472511e6afdcacaa71"}
```

### Using Your Token
{: .no_toc}
Once you have your token, include it in the Authorization header for all API requests:

```bash
curl \
  -H "Authorization: Token 38d541204dc8c932c563ee472511e6afdcacaa71" \
  https://www.brainstem.org/api/private/stem/session/
```

### Authentication in API Tools
{: .no_toc}
The token acquisition process is built into the official API tools:
- **MATLAB and Python tools**: Automatically handle token requests and management
- **Web API tool**: Uses your regular credentials (email and password) for browser-based access

## Available API Endpoints

The following pages provide detailed documentation for each API endpoint, including available fields, relationships, and specific examples:

### Core Data Management
{: .no_toc}
- **[STEM](/api/stem/)** - Core experimental data model including projects, sessions, subjects, cohorts, and collections
- **[Modules](/api/modules/)** - procedures, behaviors, data acquisition, manipulations, subject logs, consumable stocks and equipment
- **[Personal Attributes](/api/personal_attributes/)** - User-specific configurations of  behavioral paradigms, data storage, inventories and setups

### Shared resources, taxonomies and dissemination
{: .no_toc}
- **[Resources](/api/resources/)** - consumable, hardware devices, and supplier information
- **[Taxonomies](/api/taxonomies/)** - Standardized classifications for species, strains, brain regions, and setup types
- **[Dissemination](/api/dissemination/)** - research output tracking though publications and journals

### Collaboration
{: .no_toc}
- **[Users](/api/users/)** - User accounts, groups, laboratories, and membership management

### Technical Documentation
{: .no_toc}
- **[Schemas](/api/schemas/)** - JSON schema specifications for complex data structures and validation

## API Endpoint Structure

The BrainSTEM API follows a RESTful design pattern. All API endpoints follow a consistent URL structure:

```
https://www.BrainSTEM.org/api/{portal}/{app}/{model}/{id}/
```

### URL Components
{: .no_toc}
{: .note }
> **portal**: `private` or `public` - Determines access permissions and authentication requirements
> 
> **app**: The application apps - `stem`, `modules`, `personal_attributes`, `resources`, `taxonomies`, `dissemination`, `auth`, `users`
> 
> **model**: The specific data model (e.g., `session`, `procedure`, `project`). See the [data model](/datamodel/) for a complete overview
> 
> **id**: (Optional) Specific record identifier (UUID) for individual resource access

### Example Endpoints
{: .no_toc}
**Session endpoint (all sessions):**
```
https://www.BrainSTEM.org/api/private/stem/session/
```

**Specific session by ID:**
```
https://www.BrainSTEM.org/api/private/stem/session/12345678-1234-1234-1234-123456789abc/
```

**Procedure endpoint:**
```
https://www.BrainSTEM.org/api/private/modules/procedure/
```

## Public vs Private Portals

BrainSTEM provides two distinct portals with separate authentication systems:

### Private Portal
{: .no_toc}
- **Access**: Requires user authentication with API token
- **Content**: Your private data and projects
- **URL Pattern**: `https://www.BrainSTEM.org/api/private/...`

### Public Portal  
{: .no_toc}
- **Access**: Open access to publicly shared data
- **Content**: Data that has been explicitly made public by researchers
- **URL Pattern**: `https://www.BrainSTEM.org/api/public/...`

**Example - Public sessions:**
```
https://www.BrainSTEM.org/api/public/stem/session/
```

## HTTP Methods

The BrainSTEM API supports standard HTTP methods:

- **GET**: Retrieve data (list of records or specific record)
- **POST**: Create new records
- **PUT**: Update existing records (complete replacement)
- **PATCH**: Partial update of existing records
- **DELETE**: Remove records

## Query Parameters

When querying endpoints, you can use various parameters to filter, sort, and customize the response data. 

### Filtering Data
{: .no_toc}
You can filter results by specifying field values or search criteria:

**Exact match filter:**
Filter records where a field equals a specific value:
```
/?filter{name}=project1
```

**Text search filter:**
Search for records containing specific text using case-insensitive matching:
```
/?filter{description.icontains}=hippocampus
```

**Other filter operators:**
- `icontains`: Case-insensitive text search
- `startswith`: Field value starts with specified text
- `endswith`: Field value ends with specified text
- `gt`, `gte`: Greater than, greater than or equal
- `lt`, `lte`: Less than, less than or equal

### Sorting Results
{: .no_toc}
Control the order of returned results by specifying sort fields and direction:

**Descending sort (newest/highest first):**
Use a minus sign (-) prefix for descending order:
```
/?sort[]=-name
/?sort[]=-created_date
```

**Ascending sort (oldest/lowest first):**
Default behavior, no prefix needed:
```
/?sort[]=description
/?sort[]=name
```

**Multiple sort fields:**
```
/?sort[]=-created_date&sort[]=name
```

### Including Related Data
{: .no_toc}
By default, relational fields return only the ID (UUID) of related records. You can include full related data in the response:

**Include single relationship:**
```
/?include[]=behaviors
/?include[]=dataacquisition
```

**Include multiple relationships:**
```
/?include[]=behaviors&include[]=subjects&include[]=procedures
```

This reduces the number of API calls needed to get complete data by fetching related records in a single request.

### Combining Query Parameters
{: .no_toc}
Multiple query parameters can be combined using the `&` operator:

**Complex query example:**
```
/?filter{name}=project1&sort[]=-created_date&include[]=behaviors&include[]=subjects
```

This query will:
1. Filter for records where name equals "project1"
2. Sort by creation date (newest first)
3. Include full behavior data
4. Include full subject data

### Pagination
{: .no_toc}
For large datasets, the API automatically paginates results:

- **Default page size**: 20 records
- **Custom page size**: `/?limit=50` (maximum 100)
- **Navigate pages**: `/?offset=20` (skip first 20 records)

**Example pagination:**
```
/?limit=10&offset=30  # Get records 31-40
```

## Response Format

All API responses return JSON data with a consistent structure:

```json
{
  "count": 150,
  "next": "https://www.brainstem.org/api/private/stem/session/?offset=20",
  "previous": null,
  "results": [
    {
      "id": "12345678-1234-1234-1234-123456789abc",
      "name": "Experiment Session 1",
      "description": "Description of the session...",
      "created_date": "2024-01-15T10:30:00Z"
    }
  ]
}
```

## Error Handling

The API returns standard HTTP status codes:

- **200**: Success
- **201**: Created successfully
- **400**: Bad Request (invalid parameters)
- **401**: Unauthorized (invalid or missing token)
- **403**: Forbidden (insufficient permissions)
- **404**: Not Found
- **500**: Internal Server Error

Error responses include detailed messages:

```json
{
  "error": "Invalid filter parameter",
  "detail": "Field 'invalid_field' does not exist on model 'Session'"
}
```
