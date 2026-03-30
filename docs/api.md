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

BrainSTEM uses **Personal Access Tokens** for API authentication. Because BrainSTEM enforces two-factor authentication (2FA), tokens must be obtained through a browser-based flow — your password is never sent to a script or CLI tool.

| Token Type | Lifetime | How to obtain | Best for |
|------------|----------|---------------|----------|
| **Personal Access Token** | 1 year (sliding, auto-refresh) | Web UI form or CLI device auth flow | Scripts, integrations, CLI tools, automation |

### Option 1: Create a Token in the Web UI
{: .no_toc}

Visit your [API Token Management page](https://www.brainstem.org/private/users/tokens/), enter a descriptive token name (e.g., "My API Integration", "Data Export Script"), and click **Create**. Copy the token immediately — it is only shown once.

**Use your token in requests:**
```bash
curl -H "Authorization: Bearer YOUR_PERSONAL_TOKEN" \
     https://www.brainstem.org/api/private/stem/project/
```

{: .important }
> Personal access tokens are shown only once when created. Save them immediately in a secure location.

### Option 2: CLI Device Authorization Flow
{: .no_toc}

CLI tools (e.g. the BrainSTEM Python and MATLAB API tools) use a browser-based sign-in flow so that 2FA is always enforced. Your password is never sent to the CLI.

**Browser-redirect mode (default)**

The CLI opens a browser window automatically. If you are already logged in, just click **Approve**.

```
# Step 1 — CLI initiates a device session
POST /api/auth/device/
→ {"session_id": "...", "verification_uri_complete": "https://www.brainstem.org/account/authorize/?session=...", ...}

# Step 2 — CLI opens that URL in your browser; you approve (with 2FA if needed)

# Step 3 — CLI polls until approved
POST /api/auth/device/token/   body: {"device_code": "..."}
→ {"status": "authorization_pending"}  ← keep polling every 5 s
→ {"status": "success", "token": "YOUR_PAT"}  ← done
```

**Headless / no-browser mode**

For servers or Docker environments where no browser is available, the CLI prints a short code instead:

```
Open https://www.brainstem.org/account/authorize/ in a browser
and enter the code: WXYZ-1234

Waiting for authorization...
```

Navigate to that URL on any device, enter the code, and approve — the CLI receives the token automatically.

**Poll response reference**

All `POST /api/auth/device/token/` responses return HTTP 200. Check the JSON body:

```json
{"status": "authorization_pending"}   // keep polling (every 5 s)
{"status": "success", "token": "..."}  // done — save the token
{"error": "access_denied"}            // user clicked Deny — abort
{"error": "expired_token"}            // 15-minute window elapsed — restart
{"error": "already_used"}             // token already collected
```

### Authentication in API Tools
{: .no_toc}

The device authorization flow is built into the official API tools:
- **Python API tool**: `BrainstemClient()` opens a browser automatically; `BrainstemClient(headless=True)` for headless environments. See the [Python API tool docs](/api-tools/python-api-tool/).
- **MATLAB API tool**: `BrainstemClient()` opens a browser automatically; pass `'token', getenv('BRAINSTEM_TOKEN')` for scripts. See the [MATLAB API tool docs](/api-tools/matlab-api-tool/).
- **Web API tool**: Uses your existing browser session — no token required for basic exploration.

### Security Best Practices
{: .no_toc}

- **Never send your password to scripts**: Use the device auth flow or create a token in the web UI
- **Keep tokens secure**: Never commit tokens to version control or share them in logs
- **Save immediately**: Personal access tokens are shown only once when created
- **Clean up regularly**: Delete unused tokens via your [token management page](https://www.brainstem.org/private/users/tokens/)

## Available API Endpoints

The following pages provide detailed documentation for each API endpoint, including available fields, relationships, and specific examples:

### Core Data Management
{: .no_toc}
- **[STEM](/api/stem/)** - Core experimental data model including projects, sessions, subjects, cohorts, and collections
- **[Modules](/api/modules/)** - procedures, behaviors, data acquisition, manipulations, subject logs, consumable stocks and equipment
- **[Personal Attributes](/api/personal_attributes/)** - User-specific configurations of  behavioral assays, data storage, inventories and setups

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
