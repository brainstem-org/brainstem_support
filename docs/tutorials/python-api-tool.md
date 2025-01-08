---
layout: default
title: Python API tool
parent: Tutorials
nav_order: 6
---
# Tutorial for the Python API tool
{: .no_toc}

### Installation

Python toolset for interacting with the BrainSTEM API. You can get it from GitHub at [github.com/brainstem-org/brainstem_python_api_tools](https://github.com/brainstem-org/brainstem_python_api_tools).

You can also install the package using `pip`:

	pip install brainstem_python_api_tools

### Load the client. User email and password will be requested.
```
from brainstem_api_client import BrainstemClient

client = BrainstemClient()
```

### Loading sessions.

load_model can be used to load any model: We just need to pass our settings and the name of the model.

```
output1 = client.load_model('session').json()
```

We can fetch a single session entry from the loaded models.

```
session = output1["sessions"][0]
```

We can also filter the models by providing a dictionary where the keys are the fields and the values the possible contents. In this example, it will just load sessions whose name is "yeah".

```
output1 = client.load_model('session', filters={'name': 'yeah'}).json()
```

Loaded models can be sorted by different criteria applying to their fields. In this example, sessions will be sorted in descending ording according to their name.

```
output1 = client.load_model('session', sort=['-name']).json()
```

In some cases models contain relations with other models, and they can be also loaded with the models if requested. In this example, all the projects, data acquisition, behaviors and manipulations related to each session will be included.

```
output1 = client.load_model('session', include=['projects', 'dataacquisition', 'behaviors', 'manipulations']).json()
```

The list of related data acquisition can be retrived from the returned dictionary.

```
dataacquisition = output1["sessions"][0]["dataacquisition"]
```

All these options can be combined to suit the requirements of the users. For example, we can get only the session that contain the word "Rat" in their name, sorted in descending order by their name and including the related projects.

```
output1 = client.load_model('session', filters={'name.icontains': 'Rat'}, sort=["-name"], include=['projects']).json()
```

### Updating a session

We can make changes to a model and update it in the database. In this case, we changed the description of one of the previously loaded sessions.

```
session = {}
session["description"] = 'new description'
output2 = client.save_model("session", id="0e39c1fd-f413-4142-95f7-f50185e81fa4", data=session).json()
```

### Creating a new session

We can submit a new entry by defining a dictionary with the required fields.

```
session = {}
session["name"] = "New Session"
session["projects"] = ['e7475834-7733-48cf-9e3b-f4f2d2d0305a']
session["description"] = 'description'
```

Submitting session
```
output3 = client.save_model("session", data=session).json()
```

### Load public projects

Request the public data by defining the portal to be public
```
output4 = client.load_model("project", portal="public").json()
```

See the tutorial in the Python Github repository.
