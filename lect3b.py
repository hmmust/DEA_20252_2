import json

nouf_str = '{"name": "Nouf", "age": 22, "courses": ["DEA", "ML"]}'
nouf = json.loads(nouf_str)
print(nouf['name'],nouf.get('age'))