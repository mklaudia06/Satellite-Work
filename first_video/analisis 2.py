import json
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"


ruta_archivo = "./json/per_year.json"
year = []
satellite = []

with open (ruta_archivo,"r",encoding='utf8') as f:
    data = json.load(f)
    for i in data:
        year.append(i['year'])
        satellite.append(i['launchs'])

import pandas as pd
df = pd.DataFrame({"Year": year, "Launches": satellite})
fig = px.line(df, x="Year", y="Launches", title="Release by year")
fig.show()


