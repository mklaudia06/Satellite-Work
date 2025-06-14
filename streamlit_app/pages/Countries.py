import streamlit as st, folium, pandas as pd, plotly.express as px
from collections import Counter
from main import data
from src.utils import showMapDetails
from src.schemas import Texts, Countries

st.html(Texts.h1_country_map)
m = folium.Map(location=[0, 0], zoom_start=-5, min_zoom=2, width=1000, height=550)

columns = st.columns([1, 2, 1])

toggle = st.toggle("Mostrar mapa")

if toggle:
    showMapDetails(m, columns[1])
    
countries = []

for i in range(len(data)):
    if "/" not in data[i]["owner_country"] and "Multinational" not in data[i]["owner_country"] \
        and "ESA" not in data[i]["owner_country"]:
        countries.append(data[i]["owner_country"])

countries.sort()
counted_countries = Counter(countries)
countries_box = st.selectbox("Selecciona uno o varios Países:", Countries.countries.keys())

sat_list = []

df = pd.read_json("./json/satellite_list.json")

for index, satellites in df.iterrows():
    sat_list.append({
        "name": satellites["name"],
        "country": satellites["country"],
        "year_launch": satellites["launch_date"].split("/")[-1],
        "month_launch": satellites["launch_date"].split("/")[1],
        "day_launch": satellites["launch_date"].split("/")[0],
        "status":satellites["status"],
        "function": satellites["function"]
    })
    
selected_country = []

for sel in sat_list:
    if sel["country"] == Countries.countries[countries_box]:
        selected_country.append(sel)

country_df = pd.DataFrame(selected_country)
if len(selected_country) == 1:
    if selected_country[0]["status"] == "in orbit":
        status = "se encuentra orbitando normalmente"
    elif selected_country[0]["status"] == "in GSO":
        status = "se encuentra en la órbita geostacionaria (GSO)"
    elif selected_country[0]["status"] == "deorbited":
        status = "se encuentra desorbitado"
    elif selected_country[0]["status"] == "recovered":
        status = "fue recuperado"
    else:
        status = "decaído"

    st.html(Texts.satellite.format(selected_country[0]["name"], selected_country[0]["year_launch"], status))
else:
    st.title(f"Cantidad de Sátelites lanzados durante años en {countries_box if countries_box != "URSS" else "la Unión Soviética"}")
    
    st.bar_chart(country_df,
                 y="year_launch",
                 y_label="Años",
                 x_label="Cantidad de satélites")
    
    # df2 = pd.DataFrame(sat_list)
    # day = df2["day_launch"].mode()
    # month = df2["month_launch"].mode()
    # year = df2["year_launch"].mode()
    # print(day)
    # print(month)
    # print(year)
    st.html(f"<h3>Total de sátelites lanzados: {len(selected_country)}</h3>")