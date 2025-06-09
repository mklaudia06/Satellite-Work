import pandas as pd
import streamlit as st
import json


def readJson(path: str, pandas: bool = False) -> pd.DataFrame:
    
    if pandas:
        json_pandas = pd.read_json(path)
        
        return json_pandas
    else:
        with open(path, "r", encoding="utf-8") as file:
            json_norm = json.load(file)

        return json_norm