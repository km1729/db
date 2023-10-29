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

# same JSON data
with open("../json_2_sql/employee.json") as file:
    data = json.load(file)

try:
    for item in data:
        print(type(item))
        validate(instance=item, schema=schema)
    print("JSON 데이터가 스키마와 일치합니다")
except Exception as e:
    print("유효성 검사 실패: ", e)