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

## API Token Management

BrainSTEM supports multiple token types for secure API access. Choose the authentication method that best fits your use case - from long-lived tokens for scripts to short-lived tokens for web applications.

### Token Types Overview
{: .no_toc}

| Token Type | Duration | Renewal | Best For |
|------------|----------|---------|----------|
| **Personal Access Token** | 1 year (auto-refresh) | Automatic when used | Scripts, integrations, automation |
| **Access Token** | 1 hour (fixed expiry) | Refresh token required | Web applications, temporary access |
| **Refresh Token** | 30 days (fixed expiry) | Re-authenticate with credentials | Renewing access tokens |

### 1. Personal Access Tokens (Recommended)
{: .no_toc}

Personal access tokens are sliding tokens that automatically refresh themselves and last for 1 year. They're perfect for scripts and integrations since they don't require manual renewal.

**Creating Personal Access Tokens:**
1. Visit your [API Token Management page](https://www.brainstem.org/private/users/tokens/)
2. Enter a descriptive name (e.g., "My API Integration", "Data Export Script")
3. Click "Create Personal Access"
4. Save the token immediately - it's only shown once when created

**Using Personal Access Tokens:**
```bash
curl -H "Authorization: Bearer YOUR_PERSONAL_TOKEN" \
     https://www.brainstem.org/api/private/stem/project/
```

{: .important }
> Personal access tokens are shown only once when created. Save them immediately in a secure location.

### 2. Short-lived Access Tokens
{: .no_toc}

For temporary access or when you need fresh tokens regularly. These tokens expire after 1 hour (3600 seconds) and must be renewed using a refresh token which can be used for 30 days.

**Get Access + Refresh Token Pair:**
```bash
curl -X POST https://www.brainstem.org/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"email": "your-email", "password": "your-password"}'
```

**Response:**
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", 
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "expires_in": 3600
}
```

**Renew Access Token (before it expires):**
```bash
curl -X POST https://www.brainstem.org/api/auth/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "YOUR_REFRESH_TOKEN"}'
```

{: .important }
> When renewing the access token, a new refresh token will also be provided and the previous refresh token becomes invalid.

**Use Access Token:**
```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     https://www.brainstem.org/api/private/stem/project/
```

### 3. Backward Compatible Method
{: .no_toc}

Direct username/password authentication that returns a long-lived sliding token (equivalent to a Personal Access Token):

```bash
curl -X POST https://www.brainstem.org/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your-email", "password": "your-password"}'
```

**Response:**
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_id": 1,
    "message": "Token created successfully"
}
```

{: .note }
> The created token will be listed in your Personal Access Token management page and can be deleted manually.

### Authentication in API Tools
{: .no_toc}
The token acquisition process is built into the official API tools:
- **MATLAB and Python tools**: Automatically handle token requests and management
- **Web API tool**: Uses your regular credentials (email and password) for browser-based access

### Security Best Practices
{: .no_toc}

- **Keep tokens secure**: Never share them in public repositories or logs
- **Save immediately**: Personal access tokens are shown only once when created  
- **Monitor expiration**: Access tokens (1 hour) and refresh tokens (30 days) have fixed lifetimes
- **Clean up regularly**: Delete unused tokens and monitor usage in your [token management page](https://www.brainstem.org/private/users/tokens/)

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

## Error Handling

The API returns standard HTTP status codes:

- **200**: Success
- **201**: Created successfully
- **400**: Bad Request (invalid parameters)
- **401**: Unauthorized (invalid or missing token)
- **403**: Forbidden (insufficient permissions)
- **404**: Not Found
- **500**: Internal Server Error
