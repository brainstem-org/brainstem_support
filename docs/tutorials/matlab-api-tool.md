---
layout: default
title: Matlab API tool
parent: Tutorials
nav_order: 5
---
# Tutorial for the Matlab API tool
{: .no_toc}

### Installation

Download the BrainSTEM Matlab API tools repository from GitHub at [github.com/brainstem-org/brainstem_matlab_api_tools](https://github.com/brainstem-org/brainstem_matlab_api_tools) and add it to your Matlab setpath.

### Setup credentials/token: 

Email and password will be requested

```m
get_token
```

The token is saved to a mat file (`brainstem_authentication.mat`) in the Matlab API tool folder.

### Loading sessions

`load_model` can be used to load any model: We just need to set the name of the model.

```m
output1 = load_model('model','session');
```

We can fetch a single session entry from the loaded models.

```m
session = output1.sessions(1);
```

We can also filter the models by providing cell array with paired filters In this example, it will just load sessions whose name is "yeah".

```m
output1_1 = load_model('model','session','filter',{'name','yeah'});
```

Loaded models can be sorted by different criteria applying to their fields. In this example, sessions will be sorted in descending ording according to their name.

```m
output1_2 = load_model('model','session','sort',{'-name'});
```

In some cases models contain relations with other models, and they can be also loaded with the models if requested. In this example, all the projects, data acquisition, behaviors and  manipulations related to each session will be included.

```m
output1_3 = load_model('model','session','include',{'projects','dataacquisition','behaviors','manipulations'});
```

The list of related data acquisition can be retrieved from the returned dictionary.

```m
dataacquisition = output1_3.dataacquisition;
```

Get all subjects with related procedures and subject state changes

```m
output1_4 = load_model('model','subject','include',{'procedures'});
```

Get all projects with related subjects and sessions

```m
output1_5 = load_model('model','project','include',{'sessions','subjects'});
```

All these options can be combined to suit the requirements of the users. For example, we can get only the session that contain the word "Rat" in their name, sorted in descending order by their name and including the related projects.

```m
output1_6 = load_model('model','session', 'filter',{'name.icontains', 'Rat'}, 'sort',{'-name'}, 'include',{'projects'});
```

### Updating a session

We can make changes to a model and update it in the database. In this case, we change the description of one of the previously loaded sessions.

```m
session = output1.sessions(1);
session.description = 'new description';
output2 = save_model('data',session,'model','session');
```

### Creating a new session

We can submit a new entry by defining a struct with the required fields.

```m
session = {};
session.name = 'New session85';
session.description = 'new session description';
session.projects = {'0c894095-2d16-4bde-ad50-c33b7680417d'};
```

Submitting session

```m
output3 = save_model('data',session,'model','session');
```

### Load public projects

Request the public data by defining the portal to be public

```m
output4 = load_model('model','project','portal','public');
```

This tutorial in also available in the [Matlab API tool Github repository](https://github.com/brainstem-org/brainstem_matlab_api_tools).

