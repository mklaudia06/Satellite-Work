import streamlit as st, folium
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
countries_box = st.selectbox("Selecciona uno o varios Paises:", Countries.countries.keys())
print(Countries.countries[countries_box])