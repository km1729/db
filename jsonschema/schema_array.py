from jsonschema import validate

schema = {
    "$id": "https://example.com/arrays.schema.json",
    "$schema": "https://json-schema.org/draft/2020-12/schema",

    "description": "A presentation of a person, company, organization, or place",
    "type": "object",
    "properties": {
        "fruites": { "type": "array", "items":{"type":"string"}},
        "vegetables": {"type": "array", "items": {"$ref": "#/$defs/veggie"}}
    },
    "$defs":{
        "veggie": {
            "type": "object",
            "required": ["veggieName", "veggieLike"],
            "properties": {
                "veggiName" : {"type": "string"},
                "veggieLike" : {"type": "string"}
            }
        }
    }
}

data = {
    "fruites": ['apple', 'orange', 'pear'],
    "vegetables" :[
        {
            "veggieName": "potato",
            "veggieLike": "true"
        }, 
        {
            "veggieName": "broccolie",
            "veggieLike": "false"
        } 
    ]
}

try:
    validate(instance=data, schema=schema)
    print("JSON data is valid!")
except Exception as e:
    print(f"Validation error: {e}")