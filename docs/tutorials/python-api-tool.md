---
layout: default
title: Python API tool
parent: Tutorials
nav_order: 6
---
# Tutorial for the Python API tool
{: .no_toc}

### Installation

Download the BrainSTEM Python API tools repository from GitHub at [github.com/brainstem-org/brainstem_python_api_tools](https://github.com/brainstem-org/brainstem_python_api_tools).

You can also install the package using `pip`:

	pip install brainstem_python_api_tools

### Load the client. User email and password will be requested.
```python
from brainstem_api_client import BrainstemClient

client = BrainstemClient()
```

{: .note }
> The client will prompt for your email and password. Your credentials are used to generate an authentication token that's stored locally for future use.

### Troubleshooting Authentication

If you encounter authentication issues:
- Ensure your email and password are correct
- Check that your account is active
- Try regenerating your authentication token

### Loading sessions.

load_model can be used to load any model: We just need to pass our settings and the name of the model.

```python
output1 = client.load_model('session').json()
```

{: .important }
> Always check the response status before accessing data. If the request fails, the response will contain error information instead of your expected data.

We can fetch a single session entry from the loaded models.

```
session = output1["sessions"][0]
```

We can also filter the models by providing a dictionary where the keys are the fields and the values the possible contents. In this example, it will just load sessions whose name is "yeah".

```python
output1 = client.load_model('session', filters={'name': 'yeah'}).json()
```

{: .note }
> Filtering helps reduce data transfer and processing time. You can filter by any field available in the model.

Loaded models can be sorted by different criteria applying to their fields. In this example, sessions will be sorted in descending ordering according to their name.

```
```python
output1 = client.load_model('session', sort=['-name']).json()
```

```python
output1 = client.load_model('session', include=['projects', 'dataacquisition', 'behaviors', 'manipulations']).json()
```

```python
dataacquisition = output1["sessions"][0]["dataacquisition"]
```

```python
output1 = client.load_model('session', filters={'name.icontains': 'Rat'}, sort=["-name"], include=['projects']).json()
```

### Error Handling Best Practices

Always check if your requests were successful:

```python
response = client.load_model('session')
if response.status_code == 200:
    data = response.json()
    sessions = data.get('sessions', [])
else:
    print(f"Error: {response.status_code} - {response.text}")
```
```

In some cases models contain relations with other models, and they can be also loaded with the models if requested. In this example, all the projects, data acquisition, behaviors and manipulations related to each session will be included.

```
output1 = client.load_model('session', include=['projects', 'dataacquisition', 'behaviors', 'manipulations']).json()
```

The list of related data acquisition can be retrieved from the returned dictionary.

```
dataacquisition = output1["sessions"][0]["dataacquisition"]
```

All these options can be combined to suit the requirements of the users. For example, we can get only the session that contain the word "Rat" in their name, sorted in descending order by their name and including the related projects.

```
output1 = client.load_model('session', filters={'name.icontains': 'Rat'}, sort=["-name"], include=['projects']).json()
```

### Updating a session

We can make changes to a model and update it in the database. In this case, we changed the description of one of the previously loaded sessions.

```python
session = {}
session["description"] = 'new description'
output2 = client.save_model("session", id="0e39c1fd-f413-4142-95f7-f50185e81fa4", data=session).json()
```

{: .warning }
> Be careful when updating data. Always verify the ID is correct and consider the impact of your changes on related data.

### Creating a new session

We can submit a new entry by defining a dictionary with the required fields.

```python
session = {}
session["name"] = "New Session"
session["projects"] = ['e7475834-7733-48cf-9e3b-f4f2d2d0305a']
session["description"] = 'description'
```

Submitting session
```python
output3 = client.save_model("session", data=session).json()
```

{: .note }
> When creating new entries, ensure all required fields are included. Check the [data model documentation](/datamodel/) for field requirements.

### Load public projects

Request the public data by defining the portal to be public
```python
output4 = client.load_model("project", portal="public").json()
```

{: .tip }
> Public data doesn't require authentication but has the same filtering and sorting capabilities as private data.

### Complete Example Workflow

Here's a complete example that demonstrates loading, filtering, and creating data:

```python
from brainstem_api_client import BrainstemClient

# Initialize client
client = BrainstemClient()

try:
    # Load projects to get a valid project ID
    projects_response = client.load_model('project')
    if projects_response.status_code == 200:
        projects = projects_response.json()['projects']
        if projects:
            project_id = projects[0]['id']
            
            # Create a new session
            new_session = {
                "name": "Example Session",
                "projects": [project_id],
                "description": "Created via API tutorial"
            }
            
            session_response = client.save_model("session", data=new_session)
            if session_response.status_code == 201:
                print("Session created successfully!")
                session_data = session_response.json()
                print(f"New session ID: {session_data['session']['id']}")
            else:
                print(f"Failed to create session: {session_response.text}")
        else:
            print("No projects available")
    else:
        print(f"Failed to load projects: {projects_response.text}")
        
except Exception as e:
    print(f"An error occurred: {e}")
```

See the tutorial in the Python Github repository.

## Next Steps

After mastering the Python API basics, consider these logical progressions:

- **Complete Experimental Workflows**: Review the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) tutorials to see how API data fits into complete experimental documentation
- **Data Storage Integration**: Learn about [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to optimize your API-based analysis workflows with proper data organization
- **MATLAB Integration**: If you work in mixed programming environments, check out the [MATLAB API tool tutorial]({{site.baseurl}}/tutorials/matlab-api-tool) for cross-platform data access patterns