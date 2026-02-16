import streamlit as st

st.set_page_config(page_title="Multimedia y Archivos", page_icon="📷")

st.markdown("# Multimedia y Archivos")
st.sidebar.header("Multimedia")

st.write("Streamlit facilita el trabajo con imágenes, audio, video y archivos subidos por el usuario.")

st.header("1. Subir Archivos")
st.write("Usa `st.file_uploader` para permitir que los usuarios carguen archivos.")

uploaded_file = st.file_uploader("Elige un archivo de texto o imagen")

if uploaded_file is not None:
    # Ver detalles del archivo
    st.write("Nombre del archivo:", uploaded_file.name)
    st.write("Tipo de archivo:", uploaded_file.type)
    
    # Si es imagen, mostrarla
    if uploaded_file.type.startswith('image'):
        st.image(uploaded_file, caption='Imagen subida', width=300)
    # Si es texto, leerlo y mostrarlo
    elif uploaded_file.type == "text/plain":
        # Para leer archivo como string
        string_data = uploaded_file.getvalue().decode("utf-8")
        st.text_area("Contenido del archivo:", string_data)

st.divider()

st.header("2. Entrada de Cámara")
st.write("Puedes capturar fotos directamente desde la webcam.")

foto = st.camera_input("Toma una foto")

if foto:
    st.image(foto, caption="Foto capturada")

st.divider()

st.header("3. Audio y Video")

st.subheader("Audio")
st.audio("https://upload.wikimedia.org/wikipedia/commons/c/c4/Murmuration_of_Starlings_at_Otmoor.ogg")

st.subheader("Video")
st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")
