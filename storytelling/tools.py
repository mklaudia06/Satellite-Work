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

