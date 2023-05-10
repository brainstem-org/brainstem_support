---
layout: default
title: Matlab API tool
parent: API tools
nav_order: 1
---
# Matlab API tool
{: .no_toc}

Matlab toolset for interacting with the BrainSTEM API. You can get it from GitHub at [github.com/brainstem-org/brainstem_matlab_api_tools](https://github.com/brainstem-org/brainstem_matlab_api_tools).

Please see the dedicated [tutorial]({{"/tutorials/matlab-api-tool/"|absolute_url}}) with examples on usage. The main functions are described below.

| Function        | Description  |
|:-------------|:-------------|
| `get_token` | Get and save authentication token |
| `load_model` | Load data from any model |
| `save_model` | Save data to any model |
| `load_settings` | Local settings: API token, url to the server, and local repositories. |
| `load_project` | Load project(s). Convenience function for handling projects. Extra parameters: `id`,`name`,`description`,`datasets`,`subjects`,`tags`,`is_public`. Included relational data: `datasets`,`subjects`,`collections`. |
| `load_subject` | Load subject(s). Convenience function for handling subjects. Extra parameters: `id`,`name`,`description`,`projects`,`strain`,`sex`,`tags`. Included relational data: `actions`,`subjectstatechanges`,`subjectlogs`. |
| `load_dataset` | Load dataset(s). Convenience function for handling datasets. Extra parameters: `id`,`name`,`description`,`projects`,`datarepositories`,`tags`. Included relational data: `experimentdata`,`behaviors`,`manipulations`,`epochs`. |
| `brainstem_api_tutorial` | Tutorial script. |

### Filters
You can use filters, using fields and relationships by providing cell array with paired filters. Below example will just load the dataset with the id:

```m
output = load_dataset('filter', {'id', 'ee57e766-fc0c-42e1-9277-7d40d6e9353a'});
```

### Change sorting
Loaded models can be sorted by different criteria applying to their fields. In below example, datasets will be sorted in descending order according to their name.

```m
output = load_model('model', 'dataset', 'sort', {'-name'});
```

### Include related models

In some cases models contain relations with other models, and they can be also loaded with the models if requested. 

In below example, all the projects, experiment data, behaviors and manipulations related to each dataset will be included.

```m
output = load_model('model', 'dataset', 'include', {'projects', 'experimentdata', 'behaviors', 'manipulations'});
```

### Convenience functions
For the three primary data models (projects, subjects and datasets), you can use convenience functions to ease commonly performed tasks. The convenience functions have the  fields of the models accessible as input parameters providing convenient filters and the calls include relational data as well:

__load_dataset__
```m
output = load_dataset('name','mydataset');
```
Performs the same API call as:
```m
output = load_model('app', 'stem', 'model', 'dataset', 'filter', {'name', 'mydataset'}, 'include', {'experimentdata', 'behaviors', 'manipulations', 'epochs'});
```

__load_project__

```m
output = load_project('name','myproject');
```
Performs the same API call as:
```m
output = load_model('app', 'stem', 'model', 'project', 'filter', {'name', 'myproject'}, 'include', {'datasets', 'subjects', 'collections'});
```

__load_subject__

```m
output = load_subject('name','mysubject');
```
Performs the same API call as:
```m
output = load_model('app', 'stem', 'model', 'subject', 'filter', {'name','mysubject'}, 'include', {'actions', 'subjectstatechanges', 'subjectlogs'});
```
