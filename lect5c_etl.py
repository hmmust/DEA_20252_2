import json
import pandas as pd
import glob

conn_uri = "postgresql://admin:admin@localhost:5433/fitdb"

schema = json.load(open("artists_db/schemas.json"))
print(schema['artists'][0]['column_name'])
artists_schema = schema['artists']
artists_schema = sorted(artists_schema,
                        key= lambda a:a['column_position'])
cols = [col['column_name'] for col in artists_schema]
files = glob.glob("artists_db/artists/*")
for file in files:
    print("loading artists:",file)
    file1 = pd.read_csv(file,
                        header=None,names=cols)
    file1.to_sql("artists",conn_uri,index=False,
                 if_exists="append")


