---
layout: default
title: Python API tool
parent: API tools
nav_order: 2
---
# Python API tool
{: .no_toc}

Python toolset for interacting with the BrainSTEM API. You can get it from GitHub at [github.com/brainstem-org/brainstem_python_api_tools](https://github.com/brainstem-org/brainstem_python_api_tools).

Please see the dedicated [tutorial]({{"/tutorials/python-api-tool/"|absolute_url}}) with examples on usage. The main functions are described below.

| Function        | Description  |
|:-------------|:-------------|
| `authentication` | Get and save authentication token |
| `load_model` | Load data from any model |
| `save_model` | Save data to any model |
| `load_settings` | Local settings: API token, url to the server, and local storage. |
| `brainstem_api_tutorial` | Tutorial script. |


### Filters
You can use filters, using fields and relationships by providing cell array with paired filters. Below example will just load the dataset with the id:

```
output = load_model(settings, 'dataset', filters={'id': 'ee57e766-fc0c-42e1-9277-7d40d6e9353a'})
```

### Change sorting
Loaded models can be sorted by different criteria applying to their fields. In below example, datasets will be sorted in descending order according to their name.

```
output = load_model(settings, 'dataset', sort=["-name"])
```

### Include related models

In some cases models contain relations with other models, and they can be also loaded with the models if requested. 

In below example, all the projects, experiment data, behaviors and manipulations related to each dataset will be included.

```
output = load_model(settings, 'dataset', include=['projects','experimentdata','behaviors','manipulations'])
```
