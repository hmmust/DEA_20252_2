import json
import pandas as pd
students = [{"name":'Nouf',"age":22,"courses":["DEA","ML"]},
            {"name":'Duha',"age":20,"courses":["DEA","DL"]}]
file1 = open('dea_students.json',mode='wt')
json.dump(students,file1)
file1.close()
"""with open('dea_students.json',mode='wt') as file1:
    json.dump(students,file1)"""

with open('dea_students.json',mode='rt') as file2:
    students2= json.load(file2)
    print(students2)
    students_df = pd.DataFrame(students2)
    print(students_df)
