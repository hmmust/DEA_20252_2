
import pandas as pd
customers = pd.read_parquet("customers.parquet",
                            columns=['customer_fullname'])
print(customers)
customers = pd.read_parquet("customers.parquet",
                           filters=[["customer_state","==","CA"]])
print(customers)


