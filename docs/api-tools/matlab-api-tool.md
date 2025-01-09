---
layout: default
title: Matlab API tool
parent: API tools
nav_order: 1
---
# Matlab API tool
{: .no_toc}

You can download the BrainSTEM Matlab API tools repository from GitHub at [github.com/brainstem-org/brainstem_matlab_api_tools](https://github.com/brainstem-org/brainstem_matlab_api_tools) and add it to your Matlab setpath.

Please see the dedicated [tutorial]({{"/tutorials/matlab-api-tool/"|absolute_url}}) with examples on usage. The main functions are described below.

| Function        | Description  |
|:-------------|:-------------|
| `get_token` | Get and save authentication token |
| `load_model` | Load data from any model |
| `save_model` | Save data to any model |
| `load_settings` | Local settings: API token, url to the server, and local storage. |
| `load_project` | Load project(s). Convenience function for handling projects. Extra parameters: `id`,`name`,`description`,`sessions`,`subjects`,`tags`,`is_public`. Included relational data: `sessions`,`subjects`,`collections`. |
| `load_subject` | Load subject(s). Convenience function for handling subjects. Extra parameters: `id`,`name`,`description`,`projects`,`strain`,`sex`,`tags`. Included relational data: `procedures`,`subjectlogs`. |
| `load_session` | Load session(s). Convenience function for handling sessions. Extra parameters: `id`,`name`,`description`,`projects`,`datastorage`,`tags`. Included relational data: `dataacquisition`,`behaviors`,`manipulations`,`epochs`. |
| `brainstem_api_tutorial` | Tutorial script. |

### Filters
You can use filters, using fields and relationships by providing cell array with paired filters. Below example will just load the session with the id:

```m
output = load_session('filter', {'id', 'ee57e766-fc0c-42e1-9277-7d40d6e9353a'});
```

### Change sorting
Loaded models can be sorted by different criteria applying to their fields. In below example, sessions will be sorted in descending order according to their name.

```m
output = load_model('model', 'session', 'sort', {'-name'});
```

### Include related models

In some cases models contain relations with other models, and they can be also loaded with the models if requested. 

In below example, all the projects, data acquisition, behaviors and manipulations related to each session will be included.

```m
output = load_model('model', 'session', 'include', {'projects', 'dataacquisition', 'behaviors', 'manipulations'});
```

### Convenience functions
For the three primary data models (projects, subjects and sessions), you can use convenience functions to ease commonly performed tasks. The convenience functions have the  fields of the models accessible as input parameters providing convenient filters and the calls include relational data as well:

__load_session__
```m
output = load_session('name','mysession');
```
Performs the same API call as:
```m
output = load_model('app', 'stem', 'model', 'session', 'filter', {'name', 'mysession'}, 'include', {'dataacquisition', 'behaviors', 'manipulations', 'epochs'});
```

__load_project__

```m
output = load_project('name','myproject');
```
Performs the same API call as:
```m
output = load_model('app', 'stem', 'model', 'project', 'filter', {'name', 'myproject'}, 'include', {'sessions', 'subjects', 'collections'});
```

__load_subject__

```m
output = load_subject('name','mysubject');
```
Performs the same API call as:
```m
output = load_model('app', 'stem', 'model', 'subject', 'filter', {'name','mysubject'}, 'include', {'procedures', 'subjectlogs'});
```
