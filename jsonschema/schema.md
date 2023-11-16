$schema, $id, $ref  are the keywords used to define the schema itself, set an identifier for the schema, and reference other parts of the schema, respectively.  

# $schmea
- is used to declare the version of the JSOn schemea tht current schema is written in. It specifies the URI of the JSON Schema standard that the schema adheres to. The follwoing schema is written according to the JSON schema Draft 7
"""json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "integer" }
  }
}
"""

# $id
- is used to assign a unique identifier to the schema. It is often used to give the schema a URL or URL-like identifier. 
"""json
{
  "$id": "https://example.com/schemas/person-schema",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "integer" }
  }
}


"""