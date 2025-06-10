import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_folium import st_folium
from src.utils import readJson
from src.schemas import Texts
from collections import Counter
import folium
import plotly.express as px
import glob

st.set_page_config(page_title="Our DataProduct", layout="wide")

st.html(Texts.dataproduct_header)
st.html(Texts.satelliteQuiz_header)

satelliteucs = readJson("./json/satelliteucs.json", pandas=True)

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
        "era":data[1]["date_launch"].split("-")[-1] if data[1]["date_launch"] is not None else None,
        "expected_lifetime_years":data[1]["expected_lifetime_years"],
        "launch_site":data[1]["launch_site"]
    })

countries = []

for i in range(len(sucs_data)):
    countries.append(sucs_data[i]["owner_country"])
    
counted_countries = Counter(countries)

# countries_box = st.selectbox("Selecciona uno o varios Paises:", counted_countries.keys(), on_change=print())

selected = option_menu(None, 
                       ["Inicio", "Paises", "Satelites", "Agencia", "Tipo de orbita"],
                       icons=["back", "flag", "rocket", "person-workspace"],
                       menu_icon="cast",
                       orientation="horizontal",
                       key="my_menu")

if selected == "Inicio":
    st.html(Texts.start_text)
elif selected == "Paises":

    st.html("<h1 style='text-align: center;'>Todos los paises que han lanzado satelites desde 1957 hasta 2024</h1>")
    m = folium.Map(location=[0, 0], zoom_start=1.5, min_zoom=2)
    
    
    big_map = folium.Figure(width=1025, height=950)
    big_map.add_child(m)

    col1, col2, col3 = st.columns([1, 2, 1])
    
    for route in glob.glob("./json/countries/*"):
        countries_gj = readJson(route, False)

        folium.GeoJson(countries_gj,
                       style_function=lambda x: {
                           "fillColor": "#EA2F14",
                           "color": "black",
                           "weight": 2,
                           "dashArray": "5, 5"
                       }
                       ).add_to(m)
    
    with col2:
        st_folium(m, width=1025, height=950, key="map")

elif selected == "Satelites":
    st.write("Satellites wiii")
elif selected == "Agencia":
    st.write("Damn dude")
else:
    orbit_class = []
    for i in range(len(sucs_data)):
        orbit_class.append(sucs_data[i]["orbit_class"])
        
    counted_orbit_class = Counter(orbit_class)

    st.html("<h1 style='text-align: center; padding-top: 20px;'>Cantidad de satélites por tipo de órbita</h1>")
    fig = px.pie(names=counted_orbit_class.keys(), values=counted_orbit_class.values())
    st.plotly_chart(fig)