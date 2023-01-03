---
layout: default
title: API endpoints and commands
parent: REST API
nav_order: 2
---
# API endpoints
The API endpoints' URLs are defined by the portal, the app and the model: 
```
https://www.BrainSTEM.org/rest/*portal*/*app*/*model*/
```
{: .note }
> __portal__: `private` or `public`
> 
> __app__: `stem`, `modules`, `personal_attributes`, `resources`, `taxonomies`, `attributes`, `auth`, `users`
> 
> __model__: e.g. `dataset` and `action`. Please see the [data model](https://petersenpeter.github.io/brainstem_support/datamodel/data-model/) for an overview of the models. 


__dataset endpoint:__ 
```
https://www.BrainSTEM.org/rest/private/stem/dataset/
```
__action endpoint:__ 
```
https://www.BrainSTEM.org/rest/private/modules/action/
```

### Portals
The private and public portals have separate authentication systems. Please see the dedicated page on 
Public datasets: 
```
https://www.BrainSTEM.org/rest/public/stem/dataset/
```

{: .no_toc}

## Query parameters
When querying an endpoints, extra parameters can be set, including field-specific filters, change the sorting, and define relationships to include in the query. 

### Filters
```

/?filter{name}=project1
/?filter{description.icontains}=hippo
```
### Sorting
```
/?sort[]=-name
/?sort[]=description
```

### Include relationships
Relational fields will by default only include the id, but relationships can also be included when querying one model. The
```
/?include[]=behaviors
/?include[]=experiment_data
```

### Combine query parameters
The query parameters can be combined:
```
/?filter{name}=project1&sort[]=-name&include[]=behaviors
```
