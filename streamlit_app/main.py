import streamlit as st
from src.utils import readJson
from collections import Counter

st.markdown("# DataProduct de [Satellite-Work](https://github.com/mklaudia06/Satellite-Work)")

satelliteucs = readJson("./json/satelliteucs.json")

sucs_data = []

for data in satelliteucs.iterrows():
    sucs_data.append({
        "sat_name": data[1]["sat_name"],
        "owner_country":data[1]["owner_country"],
        "owner":data[1]["owner"],
        "users":data[1]["users"],
        "purpose":data[1]["purpose"],
        "orbit_class":data[1]["orbit_class"],
        "orbit_kind":data[1]["orbit_kind"],
        "inclination_degrees":data[1]["inclination_degrees"],
        "date_launch":data[1]["date_launch"],
        "expected_lifetime_years":data[1]["expected_lifetime_years"],
        "launch_site":data[1]["launch_site"]
    })

orbit_class = []
for i in range(len(sucs_data)):
    orbit_class.append(sucs_data[i]["orbit_class"])
    
counted_orbit_class = Counter(orbit_class)

st.bar_chart(
    data=counted_orbit_class,
    x_label="Tipo de Orbita",
    y_label="Cantidad",
)