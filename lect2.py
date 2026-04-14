import pandas as pd

customers_df = pd.read_json("customers.json")
del customers_df['customer_street']
print(customers_df.sample(5))
customers_df.to_json("customers2.json",index=False,
                     orient="records")