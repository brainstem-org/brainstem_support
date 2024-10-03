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
| `brainstem_api_client` | main function |
| `brainstem_api_tutorial` | Tutorial script |


### Filters
You can use filters, using fields and relationships by providing cell array with paired filters. Below example will just load the dataset with the name:

```
from brainstem_api_client import BrainstemClient

client = BrainstemClient()

output1 = client.load_model('dataset', filters={'name': 'yeah'}).json()
```

### Change sorting
Loaded models can be sorted by different criteria applying to their fields. In below example, datasets will be sorted in descending order according to their name.

```
output1 = client.load_model('dataset', sort=['-name']).json()
```

### Include related models

In some cases models contain relations with other models, and they can be also loaded with the models if requested. 

In below example, all the projects, experiment data, behaviors and manipulations related to each dataset will be included.

```
output1 = client.load_model('dataset', include=['projects', 'experimentdata', 'behaviors', 'manipulations']).json()

```
