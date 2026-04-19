import requests
import pandas as pd
customers_url = "https://raw.githubusercontent.com/hmmust/DEA_50251/refs/heads/master/customers_filtered.json"
response= requests.get(customers_url)
print(response.status_code)
if response:
    customers = response.json()
    #customers = json.loads(response.text)
    customers_df = pd.DataFrame(customers)
    print(customers_df)


