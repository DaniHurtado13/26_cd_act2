import streamlit as st
import time

st.set_page_config(page_title="Diseño y Columnas", page_icon="📐")

st.markdown("# Diseño y Layout")
st.sidebar.header("Diseño y Columnas")

st.write(
    """
    Streamlit permite organizar tu aplicación con columnas, pestañas, barras laterales y contenedores expandibles.
    """
)

st.header("1. Columnas")
st.write("Usa `st.columns` para colocar elementos lado a lado.")

col1, col2 = st.columns(2)

with col1:
    st.header("Columna 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("Columna 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

st.divider()

st.header("2. Pestañas (Tabs)")
st.write("Las pestañas son excelentes para organizar contenido relacionado pero separado.")

tab1, tab2, tab3 = st.tabs(["Gato", "Perro", "Búho"])

with tab1:
    st.header("Un gato")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("Un perro")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("Un búho")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

st.divider()

st.header("3. Expander")
st.write("`st.expander` permite ocultar contenido que no es esencial ver de inmediato.")

with st.expander("Ver más detalles"):
    st.write("""
        Las gráficas y la visualización de datos son muy importantes.
        Aquí podrías poner una explicación detallada o una tabla de datos muy larga.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")

st.divider()

st.header("4. Contenedores vacíos")
st.write("Puedes usar `st.empty` para crear un contenedor que puedes actualizar o reemplazar más tarde.")

with st.empty():
    for seconds in range(5):
        st.write(f"⏳ {seconds} segundos han pasado")
        time.sleep(1)
    st.write("✔️ ¡Tiempo terminado!")
