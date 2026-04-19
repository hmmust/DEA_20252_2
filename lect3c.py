import json
students = [{"name":'Nouf',"age":22,"courses":["DEA","ML"]},
            {"name":'Duha',"age":20,"courses":["DEA","DL"]}]
students_json_str= json.dumps(students)
print(students_json_str,type(students_json_str))
