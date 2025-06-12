import streamlit as st
from src.utils import readJson, loadData

satelliteucs = readJson("./json/satelliteucs.json", pandas=True)
data = loadData(satelliteucs)

pg = st.navigation([
    st.Page("pages/Start.py", title="Inicio"),
    st.Page("pages/Countries.py", title="Paises"),
    st.Page("pages/Satellites.py", title="Satelites"),
    st.Page("pages/Agency.py", title="Agencias"),
    st.Page("pages/Orbit_kind.py", title="Tipo de Orbita")
])

pg.run()