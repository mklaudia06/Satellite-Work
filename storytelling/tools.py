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
    with open (route,"r",encoding='utf8') as f:
        data = json.load(f)
        years = [i for i in range(1957,2025)]
        satellites_usa = []
        satellites_rus = []
        for i in data['Russia']:
            satellites_rus.append(i['launches'])
        for i in data['United_States']:
            satellites_usa.append(i['launches'])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = years,y=satellites_rus,mode="lines+markers", name = "Russian Launches"))
        fig.add_trace(go.Scatter(x = years,y =satellites_usa,mode= "lines+markers",name="United Stated Launches"))
        fig.update_layout(title="Launches by year and country (Russia and the United States)",xaxis_title="Years",yaxis_title="Number of launches",legend_title="Country")
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
        rusia_orbits.append(count)

    usa_orbits = []
    for orbit in all_orbits:
        if orbit in usa_count:
            count = usa_count[orbit]
        usa_orbits.append(count)
    
    countries = ["Russia", "United States"]
    satellite_counts = [rusia_orbits, usa_orbits]
    fig = go.Figure(data=go.Heatmap(z=satellite_counts,
    x=all_orbits,
    y=countries,
    colorscale='Viridis',
    zmin=0,
    zmax=max(max(element) for element in satellite_counts),
    colorbar=dict(title='Number of satellites'))
    )
    fig.update_layout(
    title="🛰️ Distribution of satellites by type of orbit and by country ",
    xaxis_title="Type of Orbit",
    yaxis_title="Country")
    return fig


    