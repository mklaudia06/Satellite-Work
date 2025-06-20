import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Análisis por agencias")
#aqui va el texto

ruta = "./json/satelliteucs.json"
data = pd.read_json(ruta)

country_select = st.selectbox('Elige una opción',options= set(data['owner_country']))
for _,fila in data.iterrows():
    country = fila['owner_country']
    if country == country_select:
        st.title(f"Number of satellites by agency of {country}")
        agency_count = {}
        agencies = fila['owner'] 
        if agencies in agency_count:
            agency_count[agencies] += 1
        else:
            agency_count[agencies] = 1
        name_agencias = []
        cantidad = []
        for clave,valor in agency_count.items():
            pass
        fig = go.Figure(
        go.Bar(name =country, x = name_agencias, y=cantidad, marker_color='green')
        )
            

        

    