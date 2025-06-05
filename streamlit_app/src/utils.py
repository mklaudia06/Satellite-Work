import pandas as pd
import streamlit as st

def readJson(path: str) -> pd.DataFrame:
    json = pd.read_json(path)
    
    return json

def selectColor(graph: str):
    color = st.color_picker(f"Selecciona un color para {graph}", value="#FF9B45")

    return color