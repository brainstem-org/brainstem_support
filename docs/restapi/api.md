---
layout: default
title: API endpoints and commands
parent: Public data
nav_order: 2
---
# API
API endpoints
https://www.BrainSTEM.org/rest/*portal*/*app*/*model*/

datasets: 
https://www.BrainSTEM.org/rest/private/stem/dataset/

actions: 
https://www.BrainSTEM.org/rest/private/modules/action/

Private and public portals have separate authentication systems
Public datasets: 
https://www.BrainSTEM.org/rest/public/stem/dataset/

{: .no_toc}

### Filters
/?filter{name}=project1
/?filter{description.icontains}=hippo

### Sorting
/?sort[]=-name
/?sort[]=description

### Include relationships
/?include[]=behaviors
/?include[]=experiment_data

### Combine query parameters
/?filter{name}=project1&sort[]=-name&include[]=behaviors
