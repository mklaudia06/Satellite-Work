import streamlit as st
import tools as tls

st.set_page_config(layout="wide", page_title= "Story about satellites", page_icon="imagen.png")
tls.for_titles_centered("La competencia espacial entre dos superpotencias", level="h1",color="#1E90FF")
tls.for_titles_centered("Desde la antigua Unión Soviética hasta la actual Rusia VS Estados Unidos", level="h3", color="	#1E90FF")
st.divider()
st.subheader("Competencia de lanzamientos")

st.markdown("Cada lanzamiento era una demostración de poder, una victoria ideológica y un hito tecnológico que repercutía en todo el mundo. La competencia no era solo por quién llegaba primero, sino por quién demostraba tener la tecnología y la ciencia superiores.El espacio, un lugar donde una nación podía demostrar su superioridad tecnológica y su visión del futuro.Antes de 1957, la órbita terrestre estaba vacía, un lienzo en blanco esperando ser reclamado.")
st.markdown("**4 de octubre de 1957**, un simple pitido resonó desde el cielo. La Unión Soviética lanzó el Sputnik 1, el primer satélite artificial de la historia. El sonido del **Sputnik  1** fue el llamado de atención que Estados Unidos necesitaba. La nación se movilizó con urgencia, impulsando la creación de la NASA. Estados Unidos lanzó su propia respuesta el **Explore 1**, y desde 1957 estas dos superpotencias se han visto en una competencia constante con el lanzamiento de satélites artificiales.")

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

st.markdown("Tanto Estados Unidos como Rusia tienen la mayoría de los satélites en la órbita Low Earth Orbit (LEO) a pesar de que la cantidad de satélites de Estados Unidos sobre pasa muchísimo la cantidad de satélites de Rusia en esa órbita. " \
"Esto se debe a que es la órbita con mayor acceso por sus bajos costos por lo que facilita los lanzamientos masivos y frecuentes," \
" presenta baja latencia lo que mejora las comunicaciones modernas, es ideal para observaciones terrestres y permite el monitoreo frecuente y amplia cobertura. " \
"Pero también tiene una desventaja importante que al llenarse  rápidamente, aumenta el riesgo de colisiones y genera más basura espacial. ")
st.markdown("Si te interesa conocer más sobre el tema de la basura espacial puedes pulsar el siguiente botón para ver nuestro video sobre ello.")
st.link_button("Ver video", "https://www.youtube.com/@mk_data_sciece_beginner")

st.divider()
st.subheader("Carrera espacial moderna: Principales agencias lanzadoras de satélites en Rusia y EE. UU.")
st.markdown("En la actual era espacial, tanto Rusia como Estados Unidos mantienen una presencia activa en el lanzamiento de satélites, \
pero lo hacen a través de estructuras muy diferentes.\
 Mientras que Rusia depende casi exclusivamente de su agencia estatal Roscosmos, Estados Unidos cuenta con un ecosistema más diverso que incluye tanto agencias gubernamentales como empresas privadas.\
 La siguiente gráfica compara a las principales agencias lanzadoras de satélites de ambos países, destacando su nivel de actividad y su participación en misiones espaciales. Esta comparación permite observar las diferencias en el modelo espacial de cada nación,\
así como el creciente protagonismo del sector privado en EE. UU.")

fig = tls.graph_agency()
st.plotly_chart(fig)

st.markdown("SpaceX (EE.UU.) domina el número de satélites lanzados, ha lanzado con mucha diferencia más satélites que cualquier otra agencia, superando los 3900 lanzamientos." \
"Roscosmos y las Fuerzas Espaciales Militares (VKS) de Rusia tienen un número de lanzamientos muy pequeño en comparación." \
"Esto indica que Rusia tiene una participación mucho menor en términos de volumen total de satélites lanzados en los últimos años." \
"Aunque la NASA es una agencia muy influyente, su número de satélites lanzados es bajo en comparación con SpaceX." \
"Esto probablemente se deba a que la NASA no se enfoca en lanzamientos masivos de satélites comerciales (como los de Starlink), sino en misiones científicas y exploratorias." \
"SpaceX ha lanzado miles de satélites para su constelación Starlink, lo que explica su ventaja masiva." \
"El enfoque de agencias gubernamentales (como Roscosmos y NASA) no es la cantidad, sino la calidad y la finalidad de sus misiones." \
"La diferencia también refleja el liderazgo del sector privado estadounidense en la nueva era espacial comercial.")
st.divider()