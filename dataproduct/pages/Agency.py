import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly_express as px

st.title("Análisis por agencias")
st.markdown("Descubre cuántos satélites orbitan actualmente la Tierra, " \
"qué países y agencias los operan, y con qué propósito fueron lanzados. " \
"Desde misiones científicas hasta satélites de comunicaciones y observación terrestre, " \
"esta herramienta te ofrece una visión clara y actualizada del panorama espacial global. " \
"Explora cómo se distribuyen los satélites por nación, agencia espacial y función, y comprende mejor el impacto y el alcance de la actividad satelital en el mundo moderno.")

ruta = "./json/satelliteucs.json"
data = pd.read_json(ruta)
list_country = []
for i in data['owner_country']:
    if '/' in i:
        continue
    list_country.append(i)

country_select = st.selectbox('Elige una país',options = set(list_country))

filter_row = []
for _,fila in data.iterrows():
    country = fila['owner_country']
    if country == country_select:
        filter_row.append(fila)

filter_data = pd.DataFrame(filter_row)    
agency_count = {}
for _,filas in filter_data.iterrows():
    agencies = filas['owner'] 
    if agencies in agency_count:
        agency_count[agencies] += 1
    else:
        agency_count[agencies] = 1
    
agency_count_df = pd.DataFrame(list(agency_count.items()), columns=['Agencies', 'Number'])

st.title(f"Cantidad de satélites lanzados por agencias de {country_select}")

fig = px.bar(
    agency_count_df,
    x='Agencies',
    y='Number',
    labels={'Number': 'Number of satellites', 'Agencies': 'Agencies'},
    title=f'Number of satellites per agency in {country_select}',
    color_discrete_sequence=px.colors.qualitative.Safe
)
fig.update_layout(
    width=1000,       
    height=800,         
    showlegend=False   
)
st.plotly_chart(fig)


select_agency = st.selectbox("Seleccione una agencia que pertence a ese país",options = agency_count_df['Agencies'])

filter_agencia =[]
for _, fila in filter_data.iterrows():
    new_agencia = fila['owner']
    if new_agencia == select_agency:
        filter_agencia.append(fila)

filter_row_agency = pd.DataFrame(filter_agencia)

purpose_sat = {}
for _,filas in filter_row_agency.iterrows():
    purpose = filas['purpose'] 
    if purpose in purpose_sat:
        purpose_sat[purpose] += 1
    else:
        purpose_sat[purpose] = 1

proposito_df = pd.DataFrame(list(purpose_sat.items()),columns=['Purpose','Count'])
total_satellites = sum(proposito_df['Count'])
proposito_df['Percent'] = (proposito_df['Count'] / total_satellites) * 100 


st.subheader(f"Distribución de propósitos de {select_agency}")
fig = px.pie(
    proposito_df,
    names='Purpose',
    values='Percent',
    title=f'Purposes of the satellites of {select_agency} (%)',
    color_discrete_sequence=px.colors.qualitative.Pastel,
)
fig.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig)