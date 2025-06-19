import streamlit as st
import plotly.express as px
import pandas as pd
from main import data
from collections import Counter
from src.schemas import Satellites

orbit_class = []
for i in range(len(data)):
    orbit_class.append(data[i]["orbit_class"])
    
counted_orbit_class = Counter(orbit_class)

st.html("<h1 style='text-align: center; padding-top: 20px;'>Cantidad de satélites por tipo de órbita</h1>")
fig = px.pie(names=counted_orbit_class.keys(), values=counted_orbit_class.values())
st.plotly_chart(fig)

df = pd.DataFrame(data)
df = df.drop(columns=["orbit_kind", "users", "purpose", "inclination_degrees", "launch_site"])

st.html("<h3>Descubre cuales son los satélites con mas estimación de vida útil según su órbita</h3>")
sat_box = st.selectbox(label="Selecciona la órbita que desees",
                       options=["GEO", "LEO", "MEO", "Elliptical"])

st.html(f"<h5 style='color: #FFE3BB;'>{sat_box}: {Satellites.orbit_kind_info[sat_box]}</h5>")

filtered_df = df[df["orbit_class"] == sat_box]
filtered_df = filtered_df.sort_values(by="expected_lifetime_years", ascending=False)

st.dataframe(filtered_df.head(10), hide_index=True)