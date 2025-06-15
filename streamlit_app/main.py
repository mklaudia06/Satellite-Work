import streamlit as st
from src.utils import readJson, loadSatUCSData

satelliteucs = readJson("./json/satelliteucs.json", pandas=True)
data = loadSatUCSData(satelliteucs)

pg = st.navigation([
    st.Page("pages/Start.py", title="Inicio", icon=":material/home:"),
    st.Page("pages/Countries.py", title="Países", icon=":material/flag:"),
    st.Page("pages/Search_satellites_by_date.py", title="Satélites por fechas", icon=":material/calendar_month:"),
    st.Page("pages/Agency.py", title="Agencias", icon=":material/real_estate_agent:"),
    st.Page("pages/Orbit_kind.py", title="Tipo de Órbita", icon=":material/category:")
])

pg.run()