---
layout: default
title: Matlab API tool
parent: REST API
nav_order: 3
---
# Matlab API tool
{: .no_toc}

### 0. Setup credentials: 
```m
% Email and password will be requested
stem_set_basic_authorization
```

### 1. Loading datasets
```m
output1 = stem_load_model('model','dataset');
```

### 2. Updating a dataset
```m
dataset = output1.datasets(1);
dataset.description = 'new description';
output2 = stem_save_model('data',dataset,'model','dataset');
```

### 3. Creating a new dataset
```m
dataset = {};
dataset.name = 'New dataset85';
dataset.description = 'new dataset description';
dataset.projects = {'0c894095-2d16-4bde-ad50-c33b7680417d'};

output3 = stem_save_model('data',dataset,'model','dataset');
```

### 4. Load public projects
```m
output4 = stem_load_model('model','project','portal','public');
```

See the full tutorial in the Matlab Github repository

