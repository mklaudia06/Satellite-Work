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
              
        name_agencias = list(agency_count.keys())
        cantidad = list(agency_count.values())
        fig = go.Figure(
            go.Bar(name =country, x = name_agencias, y=cantidad, marker_color='green')
            )
        fig.update_layout(
            title='',
            xaxis_title='',
            yaxis_title='',
            legend_title=''
        )
st.plotly_chart(fig)
            

        

    