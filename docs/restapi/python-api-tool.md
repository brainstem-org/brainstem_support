---
layout: default
title: Python API tool
parent: REST API
nav_order: 3
---
# Python API tool
{: .no_toc}

# 0. Setup credentials: 
# Email and password will be requested
settings = StemSettings()

# 1. Loading datasets
output1 = stem_load_model(settings, 'dataset')

# 2. Updating a dataset

dataset = output1["datasets"][0]
dataset["description"] = 'new description'
output2 = stem_save_model(settings, "dataset", data=dataset)

# 3. Creating a new dataset
dataset = {}
dataset["name"] = 'New dataset88'
dataset["description"] = 'new dataset description'
dataset["projects"] = ['e7475834-7733-48cf-9e3b-f4f2d2d0305a']

output3 = stem_save_model(settings, "dataset", data=dataset)

# 4. Load public projects
output4 = stem_load_model(settings, "project", portal="public")

See the full tutorial in the Python Github repository.
