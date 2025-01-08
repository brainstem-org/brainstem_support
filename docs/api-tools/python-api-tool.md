---
layout: default
title: Python API tool
parent: API tools
nav_order: 2
---
# Python API tool
{: .no_toc}

### Installation

Python toolset for interacting with the BrainSTEM API. You can get it from GitHub at [github.com/brainstem-org/brainstem_python_api_tools](https://github.com/brainstem-org/brainstem_python_api_tools).

You can also install the package using `pip`:

	pip install brainstem_python_api_tools

### Tutorial
Please see the dedicated [tutorial]({{"/tutorials/python-api-tool/"|absolute_url}}) with examples on usage. The main functions are described below.

| Function        | Description  |
|:-------------|:-------------|
| `BrainstemClient` | The Brainstem API client |
| `brainstem_api_tutorial` | Tutorial script |


### Filters
You can use filters, using fields and relationships by providing cell array with paired filters. Below example will just load the session with the name:

```
from brainstem_api_client import BrainstemClient

client = BrainstemClient()

output1 = client.load_model('session', filters={'name': 'yeah'}).json()
```

### Change sorting
Loaded models can be sorted by different criteria applying to their fields. In below example, sessions will be sorted in descending order according to their name.

```
output1 = client.load_model('session', sort=['-name']).json()
```

### Include related models

In some cases models contain relations with other models, and they can be also loaded with the models if requested. 

In below example, all the projects, data acquisition, behaviors and manipulations related to each session will be included.

```
output1 = client.load_model('session', include=['projects', 'dataacquisition', 'behaviors', 'manipulations']).json()

```
