import streamlit as st 
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def for_titles_centered (text, level="h1", color="blue"):
    st.markdown(
        f"<{level} style='text-align: center; color: {color};'>{text}</{level}>",
        unsafe_allow_html=True
    )

def open_json(route):
    with open (route,'r',encoding='utf8') as f:
        return json.load(f)


def graph_per_year ():
    route = "./json/total_launches_by_country_and_year.json"
    with open (route,"r",encoding='utf-8') as f:
        data = json.load(f)
        years = [i for i in range(1957,2025)]
        satellites_usa = []
        satellites_rus = []
        for i in data['Russia']:
            satellites_rus.append(i['launches'])
        for i in data['United_States']:
            satellites_usa.append(i['launches'])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = years,y=satellites_rus,mode="lines+markers", name = "Lanzamientos rusos"))
        fig.add_trace(go.Scatter(x = years,y =satellites_usa,mode= "lines+markers",name="Lanzamientos estadounidenses"))
        fig.update_layout(title="Lanzamientos por año y pais (Rusia y Estados Unidos)",xaxis_title="Años",yaxis_title="Numero de lanzamientos",legend_title="Pais")
    return fig

def orbit_map():
    data = open_json("./json/satelliteucs.json")
    rusia_count = {}
    usa_count = {}
    for i in data:
        orbit_type = i["orbit_class"]
        if i["owner_country"] == "Russia":
            if orbit_type in rusia_count:
                rusia_count[orbit_type] +=1
            else:
                rusia_count[orbit_type] = 1
        elif i["owner_country"] == "USA":
            if orbit_type in usa_count:
                usa_count[orbit_type] += 1
            else:
                usa_count[orbit_type] = 1

    all_orbits = sorted(set(rusia_count.keys()).union(usa_count.keys()))

    rusia_orbits = []
    for orbit in all_orbits:
        if orbit in rusia_count:
            count = rusia_count[orbit]
        else:
            count = 0
        rusia_orbits.append(count)

    usa_orbits = []
    for orbit in all_orbits:
        if orbit in usa_count:
            count = usa_count[orbit]
        else:
            count = 0
        usa_orbits.append(count)
    
    countries = ["Rusia", "Estados Unidos"]
    satellite_counts = [rusia_orbits, usa_orbits]
    fig = go.Figure(go.Heatmap(z=satellite_counts,
    x=all_orbits,
    y=countries,
    colorscale='Viridis',
    zmin=0,
    zmax=max(max(element) for element in satellite_counts),
    colorbar=dict(title='Cantidad de satelites'))
    )
    fig.update_layout(
    title="🛰️ Distribucion de satelites por tipo de orbita y por pais",
    xaxis_title="Tipo de Orbita",
    yaxis_title="Pais")
    return fig

data = open_json("./json/satelliteucs.json")
agencias_rusia = set()
agencias_usa = set()
for i in data:
    agency = i.get("owner")
    if i['owner_country'] == "Russia":
        if agency:  
            agencias_rusia.add(agency)
    elif i['owner_country'] == "USA":
        if agency :
            agencias_usa.add(agency)
# print(f"Agencias de Rusia: {agencias_rusia}")
# print(f"Agencias de USA: {agencias_usa}")


def graph_agency ():
    data = open_json("./json/satelliteucs.json")
    agency_rusia_count = {}
    agency_usa_count = {}
    for i in data:
        agency = i['owner']
        country = i['owner_country']
        if country == 'Russia' and agency in ['Military Space Forces (VKS)','Roscosmos State Corporation']: 
            if agency in agency_rusia_count:
                agency_rusia_count[agency] += 1
            else:
                agency_rusia_count[agency] = 1
        elif country == 'USA':
            if agency == 'SpaceX':
                if agency in agency_usa_count:
                    agency_usa_count[agency] += 1
                else:
                    agency_usa_count[agency] = 1
            if 'NASA' in agency:
                if 'NASA' in agency_usa_count:
                    agency_usa_count['NASA'] += 1
                else:
                    agency_usa_count['NASA'] = 1
    agency_usa = []
    agency_rusia = []
    value_usa = []
    value_rusia = []
    for agency,number in agency_usa_count.items():
        agency_usa.append(agency)
        value_usa.append(number)
    for agency, number in agency_rusia_count.items():
        agency_rusia.append(agency)
        value_rusia.append(number)
    
    fig = go.Figure([
    go.Bar(name='Rusia', x = agency_rusia, y=value_rusia, marker_color='green'),
    go.Bar(name='Estados Unidos', x=agency_usa, y=value_usa, marker_color='blue')
    ])

    fig.update_layout(
        barmode='group',
        title='Comparacion de las principales agencias de lanzamiento de satelites: Rusia vs Estados Unidos',
        xaxis_title='Agencias',
        yaxis_title='Satelites lanzados',
        legend_title='Pais'
    )
    return fig







                



    