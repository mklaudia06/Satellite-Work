import matplotlib.pyplot as plt
import json

ruta_archivo = "./json/per_year.json"
year = []
satellite = []

with open (ruta_archivo,"r",encoding='utf8') as f:
    data = json.load(f)
    for i in data:
        year.append(i['year'])
        satellite.append(i['launchs'])

plt.plot(year,satellite,marker='o', linestyle='-', color='orange')
plt.xlabel('Years')
plt.ylabel('Launches')
plt.title('Releases by year')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()


    
