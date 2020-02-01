import pandas as pd
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
root_path = f"{dir_path}/.."

df_account = pd.read_csv(f"{root_path}/public/account_data.csv")
meter_uids = df_account["Meter_UID"].to_list()

for index, row in df_account.iterrows():
    json_data = row.to_json(
        f"{root_path}/public/mock/api_data/{row['Meter_UID']}/account.json"
    )
