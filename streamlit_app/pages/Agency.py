import streamlit as st
import pandas as pd

st.title("Análisis por agencias")
#aqui va el texto

ruta = "./json/satelliteucs.json"
data = pd.read_json(ruta)

country_select = st.selectbox('Elige un País',options= set(data['owner_country']))
for _,fila in data.iterrows():
   pass
    # country = fila['owner_country'] 
    