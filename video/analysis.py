import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from collections import defaultdict, Counter

json_route = "./json/satellite_list.json"

json = pd.read_json(json_route)

df = pd.DataFrame(json)

data = []

for index, row in df.iterrows():
    data.append({
        "name": row["name"],
        "country": row["country"],
        "function": row["function"],
        "status": row["status"],
        "launch_day": int(row["launch_date"].split("/")[0]),
        "launch_month": int(row["launch_date"].split("/")[1]),
        "launch_year": int(row["launch_date"].split("/")[-1]),
    })

################# Cantidad de satelites lanzados por decadas ##########################

# # Obtener decadas
# def get_decade(year: int):
#     return (year // 10) * 10

# decade_counts = defaultdict(int)

# # Obtener decada de ese año y agregar al diccionario gradualmente
# for sat in data:
#     decade = get_decade(sat["launch_year"])
#     decade_counts[decade] += 1
    
# sorted_decades = sorted(decade_counts.items())

# decades = []
# counts = []

# for dec, count in sorted_decades:
#     decades.append(f"{dec}s")
#     counts.append(count)

# plt.figure(figsize=(10, 6)) 
# plt.bar(decades, counts)
# plt.title("Lanzamientos de satélites por década", fontsize=14, pad=20)
# plt.xlabel("Década", fontsize=12)
# plt.ylabel("Número de satélites lanzados", fontsize=12)
# plt.grid(axis="y", linestyle="--", alpha=0.7)
# plt.tight_layout()
# plt.show()


################### Pie de satelites en orbita, desorbitados, caidos y recuperados ########################

# status = []

# for sat in data:
#     if sat["status"] in ["in orbit", "deorbited", "decayed", "recovered"]:
#         status.append(sat["status"])

# counted_status = Counter(status)

# px.pie(names=["orbitando", "caidos", "recuperados", "fuera de orbita"], values=counted_status.values()).show()

################## Satelites fuera de orbita y caidos vs recuperados ##########################

# sats = []

# for sat in data:
#     if sat["status"] in ["deorbited", "recovered", "decayed"]:
#         sats.append(sat["status"])
    
# counted_sats = Counter(sats)

# total_out = [(counted_sats["deorbited"] + counted_sats["decayed"]), counted_sats["recovered"]]

# fig = px.bar(total_out, ["fuera de orbita y caidos", "recuperados"], y=total_out, labels={'x': 'Satelites', 'y': 'Cantidad'})
# fig.show()