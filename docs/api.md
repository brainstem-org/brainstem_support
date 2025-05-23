---
layout: default
title: API
nav_order: 4
has_children: true
---
# API
{: .no_toc}
The API allows for programmable access to the full data model. [API tools](/api-tools/) have been built for Matlab and Python and a Web API tool allows for browsing the API endpoints in a browser. 

## The API endpoints
The API endpoints' URLs are defined by the portal, the app and the model: 
```
https://www.BrainSTEM.org/api/*portal*/*app*/*model*/*id*/
```
{: .note }
> __portal__: `private` or `public`
> 
> __app__: `stem`, `modules`, `personal_attributes`, `resources`, `taxonomies`, `dissemination`, `auth`, `users`
> 
> __model__: e.g. `session` and `procedure`. Please see the [data model](/datamodel/) for an overview of the models. 


__session endpoint:__ 
```
https://www.BrainSTEM.org/api/private/stem/session/
```
__procedure endpoint:__ 
```
https://www.BrainSTEM.org/api/private/modules/procedure/
```

### Portals
The private and public portals have separate authentication systems. Please see the dedicated page on 
Public sessions: 
```
https://www.BrainSTEM.org/api/public/stem/session/
```

{: .no_toc}

## Query parameters
When querying an endpoints, extra parameters can be set, including field-specific filters, the sorting of the output of a query can be set, and define relationships to include in the query. 

### Filters
Filter entries by defining a specific value, e.g. name="project1":
```
/?filter{name}=project1
```
or search for a specific string, e.g. description.icontains=hippo, where icontains, defines that the string description should contain the string "hippo":
```
/?filter{description.icontains}=hippo
```

### Sorting
To alter the default sorting of the output of a query, define which field to use and which order, ascending or descending. A minus-sign will sort descending. E.g. to sort descending by the name field:
```
/?sort[]=-name
```

Or simply sort by the description field:
```
/?sort[]=description
```

### Include relationships
Relational fields will by default only include the id (UUID), but relationships can also be included when querying a model. To include the relational field `behaviors` or `dataacquisition`: 
```
/?include[]=behaviors
/?include[]=dataacquisition
```

### Combine query parameters
Finally query parameters can be combined:
```
/?filter{name}=project1&sort[]=-name&include[]=behaviors
```

# API endpoints
Below pages describes the API endpoints.
