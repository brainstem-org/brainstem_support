---
layout: default
title: Web API tool
parent: API Tools
nav_order: 3
---
# Web API tool
{: .no_toc}
The web API can be used for troubleshooting, and pulling out data without a third-party tool. You can query your data directly in your browser, by going to any of the endpoints. E.g., to query the datasets go to:
```
https://www.brainstem.org/api/private/stem/dataset
```
This is the same as specifying `api` as format:
```
https://www.brainstem.org/api/private/stem/dataset?format=api
```

![web_api_screenshot](https://brainstem-org.github.io/brainstem_support/assets/images/web_api_screenshot.png)

### Query as a json string
To query the result as regular json string, you must specify `json` as the format:
```
https://www.brainstem.org/api/private/stem/dataset?format=json
```
