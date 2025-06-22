import streamlit as st
from datetime import datetime as dt
import pandas as pd

st.title("Buscador de satélites según su fecha de lanzamiento")
st.subheader("🛰️ Descubre qué satélites fueron lanzados en la fecha que elijas y que países fueron los responsables.")
st.markdown("Cada día, el cielo se llena un poco más y más. Satélites de todo el mundo son enviados al espacio para explorar, comunicar, observar o proteger." \
" ¿Cuál es el tuyo? Descubre si se lanzaron satélites el día que naciste o que comenzaron su viaje en una fecha especial para ti." \
" El espacio guarda historias todos los días, el cielo siempre tiene algo que contar.")


df = pd.read_json("./json/satelliteucs.json")
min_date = dt(1957,1,1)
max_date = dt(2024,12,31) 
date = st.date_input("📅 Elige una fecha y comienza a explorar el espacio por día",min_value=min_date, max_value=max_date) 
formatted_date = f'{date.month}/{date.day}/{date.year}'
columnas_a_mostrar = ['sat_name', 'owner_country', 'owner','purpose','orbit_class','launch_site']

fila_filtrada = []
for _,fila in df.iterrows():
    date_lauch = fila['date_launch']
    if date_lauch == formatted_date:
        fila_filtrada.append(fila[columnas_a_mostrar])

if fila_filtrada:
    resultado = pd.DataFrame(fila_filtrada)
    country_select = st.selectbox('Elige un país', options=set(resultado['owner_country']))
    new_filter = []
    for _,fila in resultado.iterrows():
        country =  fila['owner_country']
        if country == country_select:
            new_columnas_a_mostrar = ['sat_name', 'owner','purpose','orbit_class','launch_site']
            new_filter.append(fila[new_columnas_a_mostrar])
    if new_filter:
        st.dataframe(new_filter,
                    hide_index=True, width=1000,
                    column_config={
                        'sat_name':'Name of the satellites',
                        'owner_country':'Country',
                        'owner':'Owner',
                        'purpose':'Objective',
                        'orbit_class':'Orbit',
                        'launch_site': 'Launch Site'
                    })
else:
    st.write("🚫 No se lanzaron satélites en esa fecha 🚫 ")