from jsonschema import validate
import json

# sample JSON schema
# 스키마 정보를 나타내는 메타데이터(metadata)
schema = {
    "title": "employee", #스키마 제목
    "description": "직원",
    "type": "object",
    "properties": {   #컬럼
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "department" : {"type": "string"},
        "position" : {"type": "string"},
        "salary": {"type": "number"}
    },
    "required": ['name']
}

schema2 = {
    "type":"object",
    "properties":{
        "employee" : {
            "type": "array", # list
            "items":{ # items are following by list
                "type":"object",
                "properties": {
                     "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "department" : {"type": "string"},
                    "position" : {"type": "string"},
                    "salary": {"type": "number"}
                }
               
          },
        "required":['name', 'id']

        }
        
    }
}

schema = {
    "type": "object",
    "properties": {
        "employees": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "position": {"type": "string"},
                    "salary": {"type": "number"}
                },
                "required": ["id", "name", "position", "salary"]
            }
        }
    },
    "required": ["employees"]
}


# same JSON data
with open("../data/employee.json") as file:
    data = json.load(file)

with open("../data/employee-array.json") as file:
    data2 = json.load(file)

try:
    for item in data2:
        print(type(item))
        validate(instance=item, schema=schema2)
    print("JSON data is valid")
except Exception as e:
    print("Validation error: ", e)