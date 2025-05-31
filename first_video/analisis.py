import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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
        
df = pd.DataFrame(array)

# grouped = df.groupby(["country", "status"]).size().unstack(fill_value=0)
# grouped["total"] = grouped.sum(axis=1)
# grouped = grouped.drop("ESA", errors="ignore")
# top10 = grouped.sort_values(ascending=False, by="deorbited").head(10)

# ax = top10[["total", "deorbited"]].plot(kind="bar", color=["#64E2B7", "#CB0404"], figsize=(8, 5))
# plt.xlabel("País")
# plt.ylabel("Cantidad de satélites")
# plt.xticks(rotation=45)
# plt.grid(axis="y", linestyle="solid", alpha=1)
# plt.tight_layout()
# plt.show()

# total = len(df)

# decayed = (df["status"] == "decayed").sum()
# deorbit = (df["status"] == "deorbited").sum()

# values = [total - deorbit - decayed, deorbit]

# plt.bar(["Total Lanzados", "Desorbitados"], values, color=["#0E2148", "#CD5656"])
# plt.grid(axis="y", linestyle="-", alpha=1)
# plt.show()

df_filtered = df[df["status"] != "decayed"]
df_filtered["status_group"] = df_filtered["status"].apply(lambda x: "in orbit" if x != "deorbited" else "deorbited")

status_count = df_filtered["status_group"].value_counts().reset_index()
status_count.columns = ["status", "count"]

# print(status_count.columns)

fig = px.pie(status_count,
             values='count',
             names='status',
             title='Distribucion de satelites orbitantes y desorbitados',
             color='status',
             color_discrete_map={'in orbit': 'lightblue', 'deorbited': 'lightcoral'})

fig.add_pie(customdata=status_count)
fig.show()