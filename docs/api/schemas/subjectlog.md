---
layout: default
title: Subject log
parent: Schemas
grand_parent: API
nav_order: 7
---

# Subject log schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## FoodConsumption
```
{
    "type": "object",
    "title": "Food Consumption log",
    "options": {
        "compact": "true"
    },
    "additionalProperties": false,
    "properties": {
        "foodAmount": {
            "title": "Food amount (grams)",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "Food amount in grams."
            }
        }
    },
    "required": [
        "foodAmount"
    ]
}
```

## FoodDeprivation
```
{
    "type": "object",
    "title": "Food deprivation log",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
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
    "required": [
        "responsiblePerson"
    ]
}
```

## GenericObservation
```
{
    "type": "object",
    "title": "Generic Observation",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false
    },
    "properties": {
        "observationType": {
            "title": "Observation type",
            "brief": "type",
            "type": "string",
            "enum": [
                "Pain score",
                "Grooming",
                "Exploration",
                "Freezing",
                "Facial expression",
                "Unusual behavior",
                "Other"
            ],
            "options": {
                "infoText": "The category or behavioral domain of the observation."
            }
        },
        "observation": {
            "title": "Observation",
            "brief": "value",
            "type": "string",
            "options": {
                "infoText": "Description of the observed behavior."
            }
        },
        "repetitions": {
            "title": "Repetitions",
            "brief": "repetitions",
            "type": "integer",
            "minimum": 1,
            "default": 1,
            "options": {
                "infoText": "How many times this observation was recorded under the same condition."
            }
        }
    },
    "required": [
        "observationType",
        "observation"
    ]
}
```

## Habituation
```
{
    "type": "object",
    "title": "Habituation log",
    "options": {
        "compact": "true"
    },
    "additionalProperties": false,
    "properties": {
        "habituationMethod": {
            "title": "Method of habituation",
            "type": "string",
            "options": {
                "infoText": "E.g., tail lift, cupping, glove."
            }
        }
    },
    "required": []
}
```

## Handling
```
{
    "type": "object",
    "title": "Handling log",
    "options": {
        "compact": "true"
    },
    "additionalProperties": false,
    "properties": {
        "handlingMethod": {
            "title": "Method of handling",
            "type": "string",
            "options": {
                "infoText": "E.g., tail lift, cupping, glove."
            }
        }
    },
    "required": []
}
```

## HargreavesTest
```
{
    "type": "object",
    "title": "Hargreaves Thermal sensitivity test",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false
    },
    "properties": {
        "stimulusLocation": {
            "title": "Stimulus location",
            "brief": "location",
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
            ],
            "options": {
                "infoText": "Anatomical location where the thermal stimulus was applied using the Hargreaves test."
            }
        },
        "latency": {
            "title": "Withdrawal latency (s)",
            "brief": "latency",
            "type": "number",
            "minimum": 0,
            "units": "s",
            "options": {
                "infoText": "Time from stimulus onset to paw withdrawal, measured in seconds."
            }
        },
        "cutoffLatency": {
            "title": "Cutoff latency (s)",
            "brief": "cutoff",
            "type": "number",
            "minimum": 0,
            "units": "s",
            "default": 20,
            "options": {
                "infoText": "Maximum allowable latency before automatic termination to prevent tissue damage."
            }
        },
        "responseScore": {
            "title": "Response score (0\u20133)",
            "brief": "score",
            "type": "integer",
            "minimum": 0,
            "maximum": 3,
            "enum": [
                0,
                1,
                2,
                3
            ],
            "descriptions": {
                "0": "No response",
                "1": "Delayed or uncertain movement",
                "2": "Clear paw withdrawal",
                "3": "Exaggerated withdrawal or escape behavior"
            },
            "options": {
                "infoText": "Categorical assessment of behavioral response. 0: No response, 1: Delayed movement, 2: Normal withdrawal, 3: Exaggerated or escape behavior"
            }
        },
        "repetitions": {
            "title": "Repetitions",
            "brief": "repetitions",
            "type": "integer",
            "minimum": 1,
            "default": 3,
            "options": {
                "infoText": "Number of repeated Hargreaves trials at the given location."
            }
        }
    },
    "required": [
        "stimulusLocation",
        "latency",
        "responseScore"
    ]
}
```

## Housing
```
{
    "type": "object",
    "title": "Housing log",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "location": {
            "title": "Location",
            "type": "string",
            "options": {
                "infoText": "The location the subject is housed, e.g. an animal housing unit with a specific status.",
                "inputAttributes": {
                    "placeholder": "e.g., Unit A, Room 101"
                }
            }
        },
        "cageId": {
            "title": "Cage ID",
            "type": "string",
            "options": {
                "infoText": "The ID of the cage where the subject is housed.",
                "inputAttributes": {
                    "placeholder": "e.g., Cage-12345"
                }
            }
        },
        "cageType": {
            "title": "Cage type",
            "type": "string",
            "options": {
                "infoText": "The type of cage, e.g. an IVC cage with a specific model number, NexGen500 or NexGen1800.",
                "inputAttributes": {
                    "placeholder": "e.g., IVC cage, NexGen1800"
                }
            }
        },
        "lightCycle": {
            "title": "Light cycle",
            "type": "string",
            "options": {
                "infoText": "The light cycle of the housing unit, e.g. normal or reversed, or specific time points",
                "inputAttributes": {
                    "placeholder": "e.g. normal or reversed"
                }
            }
        },
        "enrichment": {
            "title": "Enrichment",
            "type": "string",
            "options": {
                "infoText": "Enrichment items in the cage such as nesting material, shelter, or something to gnaw.",
                "inputAttributes": {
                    "placeholder": "e.g., nesting material, shelter"
                }
            }
        }
    }
}
```

## TrainingSession
```
{
    "type": "object",
    "title": "Training session log",
    "options": {
        "compact": "true"
    },
    "additionalProperties": false,
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
            "type": "string",
            "options": {
                "infoText": "The reinforcement type used during training (e.g. food, water, open-loop/closed loop."
            }
        },
        "performance": {
            "title": "The performance level",
            "type": "string",
            "options": {
                "infoText": "The performance level of the training. How well the subject performs the task"
            }
        }
    },
    "required": []
}
```

## VonFreyTest
```
{
    "type": "object",
    "title": "Von Frey Mechanical sensitivity test",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false
    },
    "properties": {
        "stimulusLocation": {
            "title": "Stimulus location",
            "brief": "location",
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
            ],
            "options": {
                "infoText": "Anatomical location where the Von Frey filament was applied."
            }
        },
        "stimulusForce": {
            "title": "Stimulus force (g)",
            "brief": "force",
            "type": "number",
            "minimum": 0,
            "units": "g",
            "options": {
                "infoText": "Force of the Von Frey filament used for mechanical stimulation, in grams."
            }
        },
        "responseScore": {
            "title": "Response score (0\u20133)",
            "brief": "score",
            "type": "integer",
            "minimum": 0,
            "maximum": 3,
            "enum": [
                0,
                1,
                2,
                3
            ],
            "descriptions": {
                "0": "No response",
                "1": "Slight movement",
                "2": "Strong withdrawal",
                "3": "Flinching or escape"
            },
            "options": {
                "infoText": "Categorical assessment of behavioral response to stimulation.  0: No response, 1: Slight movement, 2: Strong withdrawal, 3: Flinching or escape"
            }
        },
        "repetitions": {
            "title": "Repetitions",
            "brief": "repetitions",
            "type": "integer",
            "minimum": 1,
            "default": 10,
            "options": {
                "infoText": "Number of repetitions of Von Frey stimulation at the given location."
            }
        }
    },
    "required": [
        "stimulusLocation",
        "stimulusForce",
        "responseScore"
    ]
}
```

## WaterConsumption
```
{
    "type": "object",
    "title": "Water consumption log",
    "options": {
        "compact": "true"
    },
    "additionalProperties": false,
    "properties": {
        "waterAmount": {
            "title": "Water amount (mL)",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "Water amount in milliliters."
            }
        }
    },
    "required": [
        "waterAmount"
    ]
}
```

## WaterDeprivation
```
{
    "type": "object",
    "title": "Water deprivation log",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
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
    "required": [
        "responsiblePerson"
    ]
}
```

## Weighing
```
{
    "type": "object",
    "title": "Weighing log",
    "options": {
        "compact": "true"
    },
    "additionalProperties": false,
    "properties": {
        "weight": {
            "title": "Weight (grams)",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "Weight of subject in grams."
            }
        }
    },
    "required": [
        "weight"
    ]
}
```

## Wellness
```
{
    "type": "object",
    "title": "Wellness log",
    "options": {
        "compact": "true"
    },
    "additionalProperties": false,
    "properties": {
        "wellness": {
            "title": "Wellness",
            "type": "string",
            "options": {
                "infoText": "The current wellness status of the subject, such as good health, fair, or poor.",
                "inputAttributes": {
                    "placeholder": "e.g., good, fair, poor"
                }
            }
        }
    },
    "required": [
        "wellness"
    ]
}
```

