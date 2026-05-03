import json

schema = json.load(open("artists_db/schemas.json"))
print(schema['artists'])
cols= [i['column_name'] for i in schema['artists']]
print(cols)