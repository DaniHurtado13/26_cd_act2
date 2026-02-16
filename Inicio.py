import streamlit as st

st.set_page_config(
    page_title="Tutorial Streamlit",
    page_icon="👋",
)

st.write("# ¡Bienvenido al Tutorial de Streamlit! 👋")

st.sidebar.success("Selecciona una demostración arriba.")

st.markdown(
    """
    Streamlit es un framework de código abierto creado específicamente para
    ingenieros de Machine Learning y científicos de datos.
    
    **👈 ¡Selecciona una demostración en la barra lateral** para ver algunos ejemplos
    de lo que Streamlit puede hacer!
    
    ### ¿Qué aprenderemos?
    - Visualización de datos y texto básico
    - Widgets interactivos (botones, sliders, inputs)
    - Diseño y layout (columnas, pestañas)
    - Manejo de estado de la sesión (Session State)
    
    ### ¿Cómo usar este tutorial?
    Navega por las páginas en orden y lee las explicaciones y el código.
    Intenta modificar el código tú mismo para ver qué pasa.
    """
)
