import streamlit as st
import time

st.set_page_config(page_title="Status y Feedback", page_icon="🚦")

st.markdown("# Status y Feedback")
st.sidebar.header("Status")

st.write("Es importante comunicar al usuario qué está pasando en la aplicación. Streamlit tiene varias formas de hacerlo.")

st.header("1. Mensajes de Estado")

st.success("¡Operación exitosa! (`st.success`)")
st.info("Esto es información puramente informativa (`st.info`)")
st.warning("Advertencia: ten cuidado con esto (`st.warning`)")
st.error("Error: algo salió mal (`st.error`)")
st.exception(RuntimeError("Esto es una excepción simulada (`st.exception`)"))

st.divider()

st.header("2. Notificaciones Toast")
if st.button("Mostrar Toast"):
    st.toast("¡Soy una notificación flotante!", icon="🍞")
    time.sleep(0.5)
    st.toast("¡Puedo aparecer varias veces!", icon="🥓")

st.divider()

st.header("3. Progreso y Spinners")
st.write("Útil para operaciones largas.")

if st.button("Simular proceso largo"):
    with st.status("Descargando datos...", expanded=True) as status:
        st.write("Buscando datos...")
        time.sleep(1)
        st.write("Descargando imágenes...")
        time.sleep(1)
        st.write("Procesando información...")
        time.sleep(1)
        status.update(label="¡Descarga completa!", state="complete", expanded=False)
    
    st.button("Reiniciar")

st.subheader("Barra de progreso")
if st.button("Iniciar barra de progreso"):
    barra = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        barra.progress(i + 1)
    st.success("Terminado!")

st.divider()

st.header("4. Efectos divertidos")
col1, col2 = st.columns(2)
with col1:
    if st.button("Globos"):
        st.balloons()
with col2:
    if st.button("Nieve"):
        st.snow()
