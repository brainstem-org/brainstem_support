---
layout: default
title: Web API tool
parent: API tools
nav_order: 3
---
# Web API Tool
{: .no_toc}

The Web API Tool provides a browser-based interface for exploring, testing, and debugging BrainSTEM API endpoints without writing any code. This interactive tool is perfect for data exploration, API testing, and generating code snippets for your applications. There are links to the API pages on the list and entry pages of the regular interface. 

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Getting Started

Access the Web API Tool by navigating to any BrainSTEM API endpoint in your web browser. You'll need to be logged into your BrainSTEM account to access private data.

### Basic Usage
{: .no_toc}
Simply navigate to any API endpoint URL in your browser:

```
https://www.brainstem.org/api/private/stem/session/
```

This will display the interactive Web API interface where you can:
- Browse available data
- Test different query parameters
- View response formats
- Generate code examples

## Interface Modes

### Interactive API Browser
{: .no_toc}
The default view provides a clean interface that displays:
- **Endpoint information**: Shows the HTTP method and URL
- **Response headers**: Displays allowed methods and content type
- **JSON response**: Formatted API response data with proper syntax highlighting
- **Navigation links**: Quick access to related endpoints across all BrainSTEM modules

Access the interactive interface by visiting any endpoint:
```
https://www.brainstem.org/api/private/stem/session/
```

The interface shows the actual API response structure, including:
- **Data arrays**: Your actual data (e.g., `"sessions": []`)
- **Metadata**: Pagination information (`"meta"` object with page details)
- **HTTP status**: Response codes and headers

![web_api_screenshot_v2](/assets/images/web_api_screenshot_v2.png)

### Raw JSON Output
{: .no_toc}
For direct API responses suitable for development and debugging, use the `json` format:
```
https://www.brainstem.org/api/private/stem/session/?format=json
```

This returns the raw JSON response without the web interface wrapper.

## Key Features

### Data Exploration
{: .no_toc}
- **Browse your data**: View actual API responses in a clean, formatted interface
- **Navigation menu**: Quick access to all BrainSTEM endpoints from any page
- **Response structure**: See the exact JSON structure your applications will receive
- **Pagination metadata**: View pagination information including total results and pages

### API Testing
{: .no_toc}
- **Direct endpoint access**: Test any endpoint by navigating to its URL
- **Query parameter testing**: Add parameters to URLs to test different queries
- **Response validation**: Verify API responses and data formats
- **HTTP method display**: See which methods (GET, POST, etc.) are available for each endpoint

### Development Support
{: .no_toc}
- **JSON formatting**: Properly formatted and syntax-highlighted JSON responses
- **HTTP headers**: View response headers including allowed methods and content types
- **URL examples**: Direct URLs you can use in your applications
- **Response structure**: Understand the exact format for programmatic access

## Next Steps

Once you've explored your data with the Web API Tool:

1. **For Python development**: Use the [Python API Tool](/api-tools/python-api-tool/) for full functionality
2. **For MATLAB development**: Try the [MATLAB API Tool](/api-tools/matlab-api-tool/) for native integration
3. **For advanced queries**: Reference the full [API documentation](/api/) for all available parameters

The Web API Tool is an excellent starting point for understanding your data and testing queries before implementing them in your research workflows.
