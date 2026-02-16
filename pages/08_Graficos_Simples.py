import streamlit as st
import random

st.set_page_config(page_title="Gráficos Simples", page_icon="📊")

st.markdown("# Gráficos Simples (Sin Pandas)")
st.sidebar.header("Gráficos")

st.write(
    """
    Streamlit soporta gráficos nativos simples que funcionan con listas y diccionarios,
    sin necesidad de instalar librerías complejas como Pandas para casos básicos.
    """
)

st.header("1. Generando Datos de Prueba")
# Generamos algunos datos aleatorios usando listas por comprensión
datos_lista = [random.randint(0, 100) for _ in range(20)]
st.write("Estructura de datos (Lista):", datos_lista[:5], "...")

# Datos en diccionario para múltiples líneas
datos_diccionario = {
    'Línea A': [random.randint(10, 30) for _ in range(10)],
    'Línea B': [random.randint(20, 40) for _ in range(10)],
    'Línea C': [random.randint(0, 50) for _ in range(10)]
}
st.write("Estructura de datos (Diccionario):", datos_diccionario)

st.divider()

st.header("2. Gráfico de Línea (`st.line_chart`)")
st.write("Ideal para series de tiempo o secuencias.")

st.subheader("Desde una lista simple:")
st.line_chart(datos_lista)

st.subheader("Desde un diccionario (Múltiples líneas):")
st.line_chart(datos_diccionario)

st.divider()

st.header("3. Gráfico de Barras (`st.bar_chart`)")
st.write("Para comparar categorías o valores discretos.")

st.bar_chart(datos_diccionario)

st.divider()

st.header("4. Gráfico de Área (`st.area_chart`)")
st.write("Similar al de línea pero con el área rellena.")

st.area_chart(datos_diccionario)

st.divider()

st.header("5. Mapas (`st.map`)")
st.write("Streamlit puede pintar puntos en un mapa si le das latitudes y longitudes.")

# Datos de mapa: Coordenadas aproximadas cerca de Bogotá
datos_mapa = [
    {'lat': 4.6097 + random.uniform(-0.05, 0.05), 'lon': -74.0817 + random.uniform(-0.05, 0.05)}
    for _ in range(10)
]

st.map(datos_mapa)
st.caption("Mapa con puntos aleatorios cerca de Bogotá")
