import json

nouf = {"name":'Nouf',"age":22,"courses":["DEA","ML"]}
nouf_json_str= json.dumps(nouf)
print(nouf_json_str,type(nouf_json_str))
#students = []