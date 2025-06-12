import streamlit as st
import plotly.express as px
from main import data
from collections import Counter

orbit_class = []
for i in range(len(data)):
    orbit_class.append(data[i]["orbit_class"])
    
counted_orbit_class = Counter(orbit_class)

st.html("<h1 style='text-align: center; padding-top: 20px;'>Cantidad de satélites por tipo de órbita</h1>")
fig = px.pie(names=counted_orbit_class.keys(), values=counted_orbit_class.values())
st.plotly_chart(fig)