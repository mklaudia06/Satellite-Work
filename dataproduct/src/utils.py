from streamlit_folium import folium_static
from typing import List
from streamlit.delta_generator import DeltaGenerator
import pandas as pd
import json, folium, glob

def readJson(path: str, pandas: bool = False) -> pd.DataFrame:
    
    if pandas:
        json_pandas = pd.read_json(path)
        
        return json_pandas
    else:
        with open(path, "r", encoding="utf-8") as file:
            json_norm = json.load(file)

        return json_norm

def loadSatUCSData(df: pd.DataFrame):
    sucs_data = []

    for data in df.iterrows():
        sucs_data.append({
            "sat_name": data[1]["sat_name"],
            "expected_lifetime_years":data[1]["expected_lifetime_years"],
            "country":data[1]["owner_country"],
            "owner":data[1]["owner"],
            "users":data[1]["users"],
            "purpose":data[1]["purpose"],
            "orbit_class":data[1]["orbit_class"],
            "orbit_kind":data[1]["orbit_kind"],
            "inclination_degrees":data[1]["inclination_degrees"],
            "launch_date":data[1]["date_launch"].split("-")[-1] if data[1]["date_launch"] is not None else None,
            "launch_site":data[1]["launch_site"]
        })

    return sucs_data
    
def showMapDetails(map: folium.Map, column: List[DeltaGenerator]) -> None:
    for route in glob.glob("./json/countries/*"):
        countries_gj = readJson(route, False)
        
        tooltip = folium.GeoJsonTooltip(
            fields=["name_es"],
            aliases=["Pais: "],
            localize=True,
            labels=True,
            style="""
            div {
                height: 20px;
                color: #131D4F;
                font-size: larger;
            }
            """
        )

        folium.GeoJson(countries_gj,
                       style_function=lambda x: {
                           "fillColor": "#EA2F14",
                           "color": "black",
                           "weight": 2,
                           "dashArray": "5, 5"
                       },
                       tooltip=tooltip
                       ).add_to(map)
        
    with column:
        folium_static(map)


