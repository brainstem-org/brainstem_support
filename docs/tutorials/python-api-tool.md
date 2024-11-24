---
layout: default
title: Python API tool
parent: Tutorials
nav_order: 6
---
# Tutorial for the Python API tool
{: .no_toc}


###  0. Load the client. User email and password will be requested.
```
from brainstem_api_client import BrainstemClient

client = BrainstemClient()
```

###  1. Loading datasets.

load_model can be used to load any model: We just need to pass our settings and the name of the model.

```
output1 = client.load_model('dataset').json()
```

We can fetch a single dataset entry from the loaded models.

```
dataset = output1["datasets"][0]
```

We can also filter the models by providing a dictionary where the keys are the fields and the values the possible contents. In this example, it will just load datasets whose name is "yeah".

```
output1 = client.load_model('dataset', filters={'name': 'yeah'}).json()
```

Loaded models can be sorted by different criteria applying to their fields. In this example, datasets will be sorted in descending ording according to their name.

```
output1 = client.load_model('dataset', sort=['-name']).json()
```

In some cases models contain relations with other models, and they can be also loaded with the models if requested. In this example, all the projects, experiment data, behaviors and manipulations related to each dataset will be included.

```
output1 = client.load_model('dataset', include=['projects', 'experimentdata', 'behaviors', 'manipulations']).json()
```

The list of related experiment data can be retrived from the returned dictionary.

```
experiment_data = output1["datasets"][0]["experimentdata"]
```

All these options can be combined to suit the requirements of the users. For example, we can get only the dataset that contain the word "Rat" in their name, sorted in descending order by their name and including the related projects.

```
output1 = client.load_model('dataset', filters={'name.icontains': 'Rat'}, sort=["-name"], include=['projects']).json()
```

###  2. Updating a dataset

We can make changes to a model and update it in the database. In this case, we changed the description of one of the previously loaded datasets.

```
dataset = {}
dataset["description"] = 'new description'
output2 = client.save_model("dataset", id="0e39c1fd-f413-4142-95f7-f50185e81fa4", data=dataset).json()
```

###  3. Creating a new dataset

We can submit a new entry by defining a dictionary with the required fields.

```
dataset = {}
dataset["name"] = "New Dataset"
dataset["projects"] = ['e7475834-7733-48cf-9e3b-f4f2d2d0305a']
dataset["description"] = 'description'
```

Submitting dataset
```
output3 = client.save_model("dataset", data=dataset).json()
```

###  4. Load public projects

Request the public data by defining the portal to be public
```
output4 = client.load_model("project", portal="public").json()
```

See the tutorial in the Python Github repository.
