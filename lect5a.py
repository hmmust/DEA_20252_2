import pandas as pd

conn_uri = "postgresql://admin:admin@localhost:5433/fitdb"
new_orders = [{"order_id":99999,
              "order_date":"2026-05-03 00:00:00",
              "order_customer_id":1,
              "order_status":"COMPLETE"}]
new_df = pd.DataFrame(new_orders)
new_df.to_sql("orders2",conn_uri,index=False)
