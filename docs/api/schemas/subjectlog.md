---
layout: default
title: Subject log
parent: Schemas
grand_parent: API
nav_order: 1
---

# Subject log schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Food consumption log
```
{
    "type": "object",
    "title": "Food Consumption log",
    "properties": {
        "foodAmount": {
            "title": "Food amount (grams)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": ["foodAmount"]
}
```

*Food amount* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "foodAmount": 32.4
}
```


## Water consumption log
```
{
    "type": "object",
    "title": "Water consumption log",
    "properties": {
        "waterAmount": {
            "title": "Water Amount (mL)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": ["waterAmount"]
}
```

*Water amount* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "waterAmount": 53.9
}
```


## Weighing log
```
{
    "type": "object",
    "title": "Weighing log",
    "properties": {
        "weight": {
            "title": "Weight (grams)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": ["weight"]
}
```

*Weight* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "weight": 2.5
}
```


## Food deprivation log
```
{
    "type": "object",
    "title": "Food deprivation log",
    "properties": {
        "responsiblePerson": {
            "title": "Responsible person (name and phone number)",
            "type": "string"
        },
        "protocol": {
            "title": "Protocol",
            "type": "string"
        }
    },
    "required": ["responsiblePerson"]
}
```

*Responsible person* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "responsiblePerson": "Dr. Smith (555-0123)",
    "protocol": "Standard 24-hour food deprivation protocol"
}
```


## Water deprivation log
```
{
    "type": "object",
    "title": "Water deprivation log",
    "properties": {
        "responsiblePerson": {
            "title": "Responsible person (name and phone number)",
            "type": "string"
        },
        "protocol": {
            "title": "Protocol",
            "type": "string"
        }
    },
    "required": ["responsiblePerson"]
}
```

*Responsible person* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "responsiblePerson": "Dr. Johnson (555-0456)",
    "protocol": "Standard 16-hour water deprivation protocol"
}
```


## Wellness log
```
{
    "type": "object",
    "title": "Wellness log",
    "properties": {
        "wellness": {
            "title": "Wellness",
            "type": "string"
        }
    },
    "required": ["wellness"]
}
```

*Wellness* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "wellness": "good"
}
```


## Housing log
```
{
    "type": "object",
    "title": "Housing log",
    "properties": {
        "location": {
            "title": "Location",
            "type": "string"
        },
        "cageId": {
            "title": "Cage ID",
            "type": "string"
        },
        "cageType": {
            "title": "Cage type",
            "type": "string"
        },
        "lightCycle": {
            "title": "Light cycle",
            "type": "string"
        },
        "enrichment": {
            "title": "Enrichment",
            "type": "string"
        }
    }
}
```

All fields are optional.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "location": "Unit A, Room 101",
    "cageId": "Cage-12345",
    "cageType": "IVC cage, NexGen1800",
    "lightCycle": "normal",
    "enrichment": "nesting material, shelter"
}
```


## Training session log
```
{
    "type": "object",
    "title": "Training session log",
    "properties": {
        "task": {
            "title": "Task of the training",
            "type": "string"
        },
        "setup": {
            "title": "Setup of the training",
            "type": "string"
        },
        "reinforcementType": {
            "title": "Reinforcement type",
            "type": "string"
        },
        "performance": {
            "title": "The performance level",
            "type": "string"
        }
    },
    "required": []
}
```

All fields are optional.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "task": "Lever pressing task",
    "setup": "Operant chamber with two levers",
    "reinforcementType": "food reward",
    "performance": "85% accuracy"
}
```


## Hargreaves test log
```
{
    "type": "object",
    "title": "Hargreaves Thermal sensitivity test",
    "properties": {
        "stimulusLocation": {
            "title": "Stimulus location",
            "type": "string",
            "enum": [
                "Left hind paw",
                "Right hind paw",
                "Left forepaw",
                "Right forepaw",
                "Face (left)",
                "Face (right)",
                "Tail",
                "Other"
            ]
        },
        "latency": {
            "title": "Withdrawal latency (s)",
            "type": "number",
            "minimum": 0
        },
        "cutoffLatency": {
            "title": "Cutoff latency (s)",
            "type": "number",
            "minimum": 0,
            "default": 20
        },
        "responseScore": {
            "title": "Response score (0–3)",
            "type": "integer",
            "minimum": 0,
            "maximum": 3,
            "enum": [0, 1, 2, 3]
        },
        "repetitions": {
            "title": "Repetitions",
            "type": "integer",
            "minimum": 1,
            "default": 3
        }
    },
    "required": [
        "stimulusLocation",
        "latency",
        "responseScore"
    ]
}
```

*Stimulus location*, *latency*, and *response score* are **required** fields.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "stimulusLocation": "Left hind paw",
    "latency": 12.5,
    "responseScore": 2,
    "cutoffLatency": 20,
    "repetitions": 3
}
```


## Von Frey test log
```
{
    "type": "object",
    "title": "Von Frey Mechanical sensitivity test",
    "properties": {
        "stimulusLocation": {
            "title": "Stimulus location",
            "type": "string",
            "enum": [
                "Left hind paw",
                "Right hind paw",
                "Left forepaw",
                "Right forepaw",
                "Face (left)",
                "Face (right)",
                "Tail",
                "Other"
            ]
        },
        "stimulusForce": {
            "title": "Stimulus force (g)",
            "type": "number",
            "minimum": 0
        },
        "responseScore": {
            "title": "Response score (0–3)",
            "type": "integer",
            "minimum": 0,
            "maximum": 3,
            "enum": [0, 1, 2, 3]
        },
        "repetitions": {
            "title": "Repetitions",
            "type": "integer",
            "minimum": 1,
            "default": 10
        }
    },
    "required": [
        "stimulusLocation",
        "stimulusForce",
        "responseScore"
    ]
}
```

*Stimulus location*, *stimulus force*, and *response score* are **required** fields.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "stimulusLocation": "Right hind paw",
    "stimulusForce": 4.0,
    "responseScore": 2,
    "repetitions": 10
}
```


## Generic observation log
```
{
    "type": "object",
    "title": "Generic Observation",
    "properties": {
        "observationType": {
            "title": "Observation type",
            "type": "string",
            "enum": [
                "Pain score",
                "Grooming",
                "Exploration",
                "Freezing",
                "Facial expression",
                "Unusual behavior",
                "Other"
            ]
        },
        "observation": {
            "title": "Observation",
            "type": "string"
        },
        "repetitions": {
            "title": "Repetitions",
            "type": "integer",
            "minimum": 1,
            "default": 1
        }
    },
    "required": [
        "observationType",
        "observation"
    ]
}
```

*Observation type* and *observation* are **required** fields.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "observationType": "Grooming",
    "observation": "Subject engaged in normal grooming behavior for 5 minutes",
    "repetitions": 3
}
```


## Habituation log
```
{
    "type": "object",
    "title": "Habituation log",
    "properties": {
        "habituationMethod": {
            "title": "Method of habituation",
            "type": "string"
        }
    },
    "required": []
}
```

All fields are optional.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "habituationMethod": "tail lift"
}
```


## Handling log
```
{
    "type": "object",
    "title": "Handling log",
    "properties": {
        "handlingMethod": {
            "title": "Method of handling",
            "type": "string"
        }
    },
    "required": []
}
```

All fields are optional.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "handlingMethod": "cupping"
}
```