import pandas as pd
customers = pd.read_csv("customers.csv")
customers.to_parquet("customers2.parquet",index=False,
                     compression="snappy")



