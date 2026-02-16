import streamlit as st

st.set_page_config(page_title="Texto y Visualización", page_icon="📜")

st.markdown("# Texto y Visualización")
st.sidebar.header("Texto y Visualización")

st.write(
    """
    En Streamlit, mostrar texto y datos es muy sencillo.
    Aquí tienes algunos ejemplos de las funciones más comunes.
    """
)

st.header("1. Títulos y Encabezados")
st.code("""
st.title("Este es un título")
st.header("Este es un encabezado")
st.subheader("Este es un sub-encabezado")
""", language="python")

st.subheader("Resultado:")
st.title("Este es un título")
st.header("Este es un encabezado")
st.subheader("Este es un sub-encabezado")

st.divider()

st.header("2. Texto con formato")
st.write("`st.write()` es la navaja suiza de Streamlit. Puede escribir casi cualquier cosa.")
st.markdown("`st.markdown()` permite usar **negrita**, *cursiva*, y más.")
st.caption("Esto es un `st.caption` para texto pequeño.")

st.divider()

st.header("3. Código y LaTeX")
st.write("Puedes mostrar código formateado:")
st.code("print('Hola Mundo')", language="python")

st.write("Y también fórmulas matemáticas con LaTeX:")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.divider()

st.header("4. Métricas")
st.metric(label="Temperatura", value="70 °F", delta="1.2 °F")
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "70 °F", "1.2 °F")
col2.metric("Viento", "9 mph", "-8%")
col3.metric("Humedad", "86%", "4%")
