import streamlit as st

st.set_page_config(page_title="Formularios", page_icon="📝")

st.markdown("# Formularios")
st.sidebar.header("Formularios")

st.write(
    """
    Los formularios son contenedores que agrupan widgets y detienen la ejecución automática
    de Streamlit hasta que se presiona un botón de envío.
    """
)

st.header("1. ¿Por qué usar formularios?")
st.write(
    """
    Normalmente, *cada vez* que interactúas con un widget, Streamlit recarga toda la página.
    Esto puede ser lento si tienes inputs que dependen entre sí o procesos pesados.
    Los formularios solucionan esto.
    """
)

st.header("2. Ejemplo de Formulario")

with st.form("my_form"):
    st.write("Dentro del formulario")
    
    nombre = st.text_input("Nombre")
    edad = st.slider("Edad", 0, 100, 25)
    
    # Cada formulario debe tener un submit_button
    submitted = st.form_submit_button("Enviar")
    
    if submitted:
        st.write("¡Formulario enviado!")
        st.write(f"Nombre: {nombre}")
        st.write(f"Edad: {edad}")

st.divider()

st.header("3. Formulario en Columnas")

with st.form("column_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        color = st.selectbox("Color favorito", ["Rojo", "Azul", "Verde"])
        
    with col2:
        animal = st.text_input("Animal favorito")
        
    enviar = st.form_submit_button("Guardar preferencias")
    
    if enviar:
        st.success(f"Preferencias guardadas: {color}, {animal}")
