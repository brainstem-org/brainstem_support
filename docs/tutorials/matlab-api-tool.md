---
layout: default
title: Matlab API tool
parent: Tutorials
nav_order: 5
---
# Tutorial for the Matlab API tool
{: .no_toc}

### 0. Setup credentials/token: 

Email and password will be requested

```m
get_token
```

The token is saved to a mat file (`brainstem_authentication.mat`) in the Matlab API tool folder.

### 1. Loading datasets

`load_model` can be used to load any model: We just need to set the name of the model.

```m
output1 = load_model('model','dataset');
```

We can fetch a single dataset entry from the loaded models.

```m
dataset = output1.datasets(1);
```

We can also filter the models by providing cell array with paired filters In this example, it will just load datasets whose name is "yeah".

```m
output1_1 = load_model('model','dataset','filter',{'name','yeah'});
```

Loaded models can be sorted by different criteria applying to their fields. In this example, datasets will be sorted in descending ording according to their name.

```m
output1_2 = load_model('model','dataset','sort',{'-name'});
```

In some cases models contain relations with other models, and they can be also loaded with the models if requested. In this example, all the projects, experiment data, behaviors and  manipulations related to each dataset will be included.

```m
output1_3 = load_model('model','dataset','include',{'projects','experimentdata','behaviors','manipulations'});
```

The list of related experiment data can be retrieved from the returned dictionary.

```m
experimentdata = output1_3.experimentdata;
```

Get all subjects with related procedures and subject state changes

```m
output1_4 = load_model('model','subject','include',{'procedures'});
```

Get all projects with related subjects and datasets

```m
output1_5 = load_model('model','project','include',{'datasets','subjects'});
```

All these options can be combined to suit the requirements of the users. For example, we can get only the dataset that contain the word "Rat" in their name, sorted in descending order by their name and including the related projects.

```m
output1_6 = load_model('model','dataset', 'filter',{'name.icontains', 'Rat'}, 'sort',{'-name'}, 'include',{'projects'});
```

### 2. Updating a dataset

We can make changes to a model and update it in the database. In this case, we change the description of one of the previously loaded datasets.

```m
dataset = output1.datasets(1);
dataset.description = 'new description';
output2 = save_model('data',dataset,'model','dataset');
```

### 3. Creating a new dataset

We can submit a new entry by defining a struct with the required fields.

```m
dataset = {};
dataset.name = 'New dataset85';
dataset.description = 'new dataset description';
dataset.projects = {'0c894095-2d16-4bde-ad50-c33b7680417d'};
```

Submitting dataset

```m
output3 = save_model('data',dataset,'model','dataset');
```

### 4. Load public projects

Request the public data by defining the portal to be public

```m
output4 = load_model('model','project','portal','public');
```

This tutorial in also available in the [Matlab API tool Github repository](https://github.com/brainstem-org/brainstem_matlab_api_tools).

