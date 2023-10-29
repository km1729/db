`jsonschema` is a Python library used for validating JSON data against a JSON schema. It ensures that the structure and data within a JSON document adher to a specified schema or structure defined in a separate JSON file.  

Key features:  
- **Schema Vailidation**: define a JSON schema that describes the structure of a JSON document. This schema specifies that types, formats, constraints, and relationships between various elements in the JSON data. JOSN 형태로 스키마를 정의하고 문서의 구조를 서ퟝ명한다. 이것은 컬럼, 타입, 포맷, 제약, 관계성 등 여러가지를 포함한다.    
- **Validation Process**: with the defined schema, `jsonschema` validates the actual JSON data, ensuring it conforms to the provided schema. It checks for things like data types, required fields, and any custon constraints outlined in the schema. 앞서 정의한 스키마와 json 데이터가 유효성성을 검사한다. 데이터 형식, 필수 필드 및 스키마에서 지정된 사용자 저의 제약 사항을 확인한다.    
- **python library**: It's a python library, available through PyPi, used to parse and validate JSON data against a JSON schema. pypi를 통해 제공되며, json데이터를 스키마에 파싱하고 유효성을 검사한다.   

The error you're encountering is due to the structure of the JSON data not matching the defined schema.  The schema you've defined expects an object but the JSOn data seems to be an array of objects. 내가 제공한 데애터는 리스트이면서 오브젝트를 포함하는것. 그럼 for를 써야지

## object  
objects are the mapping type in JSON. They map "keys" to "values". In Json, the "keys" must always be strings. Each of these pairs is conventionally reffered to as a "property".  


# References  
https://json-schema.org/  