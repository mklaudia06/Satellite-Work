import pandas as pd
import matplotlib.pyplot as plt

json_route = "./json/satellite_list.json"

json = pd.read_json(json_route)

array = []

for json_cols in json.iterrows():
    array.append({
        "name": json_cols[1]["name"],
        "country": json_cols[1]["country"],
        "lauch_date": json_cols[1]["launch_date"],
        "status": json_cols[1]["status"],
        "function": json_cols[1]["function"]
    })
        
arr_df = pd.DataFrame(array)

grouped = arr_df.groupby(["country", "status"]).size().unstack(fill_value=0)
grouped["total"] = grouped.sum(axis=1)
top10 = grouped.sort_values(ascending=False, by="deorbited").head(10)

ax = top10[["total", "deorbited"]].plot(kind="bar", color=["#64E2B7", "#CB0404"], figsize=(8, 5))
plt.xlabel("País")
plt.ylabel("Cantidad de satélites")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="solid", alpha=1)
plt.tight_layout()
plt.show()