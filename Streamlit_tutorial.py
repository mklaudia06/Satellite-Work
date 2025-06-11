import streamlit as st
 #page_icon =
st.title("Mi proyecto")
st.header("MiniProyecto de Streamlit")
st.subheader("Klaudia ")
st.caption("insertar caption")
st.text("esto es un parrafo grande")
st.button("Si no presionas, eres gay")
st.text_input("Caja de texto")

#Concatenar 
nombre = 'klaudia'
edad = 18

st.text(f'hola, mi nombre es {nombre} y tengo {str(edad)} años ')

#Markdown
st.subheader("markdown")
st.markdown("# soy un titulo H1")
st.markdown("## soy un titulo H2")
st.markdown("### soy un titulo H3")
st.markdown("parrafo comun y corriente")

st.markdown("este texto tiene **negritas**")
st.markdown("este texto es *cursiva*")
st.markdown("y este es ***cursivas con negritas***")
st.markdown("[Google](https://google.com)")
st.markdown("---")
st.divider()
#pagina markdown guide.org tutorial de como funciona

#Latex
#Json/Codes

#Write
st.subheader("write")
st.write("# Soy un titulo con write")
json = {"nombre":"klaudia", "edad":18}
st.write(json,nombre,edad)
st.write("""
- **Negritas**
- _cursiva_
- [Enlace a Google](https://google.com)
""")

#Metric 
st.subheader("metric")
st.metric(label = "ventas del mes",value = "$1500", delta = "35%")
st.metric(label = "Dolar",value = "$360",delta = "-5%")