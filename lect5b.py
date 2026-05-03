import pandas as pd

conn_uri = "postgresql://admin:admin@localhost:5433/fitdb"
customers = pd.read_sql("customers",con=conn_uri)
print(customers)
order_status = pd.read_sql_query(
    "select distinct order_status from orders order by 1",
    con=conn_uri)
print(order_status)