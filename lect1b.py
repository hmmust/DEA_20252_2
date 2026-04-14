import pandas as pd
import pyarrow.csv as pa_csv

customers_table = pa_csv.read_csv("customers.csv")
customers_df= customers_table.to_pandas()

customers_df['customer_fullname']= customers_df['customer_fname']+ " " + customers_df['customer_lname']
del customers_df['customer_fname']
del customers_df['customer_lname']
print(customers_df)
customers_df.to_csv("customers2.csv",index=False,
                    columns=['customer_id','customer_fullname'])