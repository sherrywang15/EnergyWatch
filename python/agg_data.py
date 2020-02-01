import os
import json
import pandas as pd


dir_path = os.path.dirname(os.path.realpath(__file__))
root_path = f"{dir_path}/.."

df_account = pd.read_csv(f"{root_path}/public/account_data.csv")
meter_uids = df_account["Meter_UID"].to_list()

df_concat = []
for uid in meter_uids:
    with open(f"{root_path}/public/mock/api_data/{uid}/intervals.json") as file:
        intervals = json.load(file)
        df_readings = pd.DataFrame(intervals["intervals"][-1]["readings"])
        df_concat.append(df_readings.set_index("start")["kwh"])

df_concat = pd.concat(df_concat)
df_means = df_concat.groupby(df_concat.index).mean().reset_index()

with open(f"{root_path}/public/mock/group_average.json", "w") as outfile:
    json.dump(df_means.to_dict(orient="records"), outfile, indent=2)
