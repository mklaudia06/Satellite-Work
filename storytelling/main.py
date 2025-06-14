import streamlit as st
import tools as tls
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title= "Story about satellites", page_icon="imagen.png")
tls.for_titles_centered("La competencia espacial entre dos superpotencias", level="h1",color="#1E90FF")
tls.for_titles_centered("Desde la antigua Unión Soviética hasta la actual Rusia VS Estados Unidos", level="h3", color="	#1E90FF")
st.divider()
st.subheader("Competencia de lanzamientos")

st.markdown("Cada lanzamiento era una demostración de poder, una victoria ideológica y un hito tecnológico que repercutía en todo el mundo. La competencia no era solo por quién llegaba primero, sino por quién demostraba tener la tecnología y la ciencia superiores.El espacio, un lugar donde una nación podía demostrar su superioridad tecnológica y su visión del futuro.Antes de 1957, la órbita terrestre estaba vacía, un lienzo en blanco esperando ser reclamado.")
st.markdown("**4 de octubre de 1957**, un simple pitido resonó desde el cielo. La Unión Soviética lanzó el Sputnik 1, el primer satélite artificial de la historia. El sonido del **Sputnik 1**fue el llamado de atención que Estados Unidos necesitaba. La nación se movilizó con urgencia, impulsando la creación de la NASA. Estados Unidos lanzó su propia respuesta el **Explore 1**, y desde 1957 estas dos superpotencias se han visto en una competencia constante con el lanzamiento de satélites artificiales.")

fig = tls.graph_per_year()
st.plotly_chart(fig)

st.divider()
st.subheader("Batalla por la superioridad espacial")

st.markdown("Ambos países se esforzaron por demostrar su dominio tecnológico y la capacidad de " \
"usar el espacio para fines estratégicos." \
"Cada tipo de órbita representa una táctica en la batalla por el dominio espacial. " \
"Ambas naciones posicionan sus satélites en los distintos tipos órbitas segun sus objetivos y pueden llegar a dominar alguna de ellas por su predominio de satélites lanzados a estas  " \
"—en órbitas bajas (LEO), medias (MEO), geoestacionarias (GEO), y más allá— según sus objetivos:" \
" vigilancia, comunicación, navegación o defensa. La densidad orbital no es casualidad: " \
"es geopolítica codificada en trayectorias.")

fig = tls.orbit_map()
st.plotly_chart(fig)
