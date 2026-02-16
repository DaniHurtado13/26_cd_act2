import streamlit as st 
import time

st.sidebar.header("Ejercicios")

st.subheader("Ejercicio 1 - Saludo Simple", divider="rainbow")
st.text("Enunciado:")
st.text("Crea un campo de entrada de texto para que el usuario escriba su nombre. \nSi el nombre no está vacío, muestra un mensaje de bienvenida: '¡Hola, [Nombre]!'. ")

nombre = st.text_input("Escribe tu nombre: ")
st.write("¡Hola, ", nombre + "!")

st.write("\n")
st.write("\n")


st.subheader("Ejercicio 2 - Calculadora de producto", divider="rainbow")
st.text("Enunciado:")
st.text("Pide al usuario dos números \n- Muestra el resultado de su multiplicación.\n- Si alguno de los números es mayor a 100, muestra un warning indicando 'Números grandes.' ")

num1 = st.number_input("Ingresa un número: ",  value=0)
num2 = st.number_input("Ingresa otro número: ",  value=0)

if num1 > 100 or num2 > 100:
    st.warning("Numeros grandes")
else:
    st.write("EL resultado es: ", num1 * num2)
    
    
    

st.write("\n")
st.write("\n")

st.subheader("Ejercicio 3 - Convertidor de temperatura", divider="rainbow")
st.text("Enunciado:")
st.text("Usa un 'st.radio' para elegir la direcciòn de la conversión: 'Celsius a Fahrenheit' o 'Fahrenheit a Celsius'. \n- Usa un `st.number_input` para ingresar la temperatura.\n- Muestra el resultado calculado.")

temperaturaInicial = st.radio(
    "Ingresa la temperatura inicial", 
    ["Celsius", "Fahrenheit"]
    )

valor = st.number_input(
    "Ingresa la temperatura: ", 
    value=0.0
    )


if temperaturaInicial == "Celsius":
    resultado = (valor * 9 / 5) + 32
    unidad_destino = "Fahrenheit"
else:
    resultado = (valor - 32) * 5 / 9
    unidad_destino = "Celsius"

st.success(f"{valor:.2f}° {temperaturaInicial} = {resultado:.2f}° {unidad_destino}")


st.write("\n")
st.write("\n")

st.subheader("Ejercicio 4 - Galería de Mascotas", divider="rainbow")
st.text("Enunciado:")
st.text("Crea 3 pestañas:  'Gatos',  'Perros',  'Aves'.\n- En cada pestaña muestra una imagen diferente y un botón de 'Me gusta' que, al ser presionado, muestre un 'st.toast' diciendo 'te gusta esta mascota.'")


tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Monos"])

with tab1:
    st.header("Un gato")
    st.image("https://i.pinimg.com/originals/1d/40/0e/1d400e79e924b844848049f3e52172b2.jpg", width=300)
with tab2:
    st.header("Un perro")
    st.image("https://i.pinimg.com/736x/30/d2/06/30d206c9b157d8c7493f96e9074fab58.jpg", width=300)
with tab3:
    st.header("Un mono narigudo")
    st.image("https://www.anipedia.net/imagenes/monos-narigudos.jpg", width=400)
    


def like():
    msg = st.toast("Guardando tu like...")
    time.sleep(1)
    time.sleep(1)
    msg.toast("Te gusta esta mascota!", icon="✅")

if st.button("Me gusta"):
    like()
    
    
    


st.write("\n")
st.write("\n")

st.subheader("Ejercicio 5 - Caja de comentarios (Formulario)", divider="rainbow")
st.text("Enunciado:")
st.text("Crea un formulario con: \n- Un campo de texto para el asunto. \n- Un área de texto para el mensaje. \n- Un botón de envío. \n- Al enviar, muestra los datos ingresados en un 'st.json' o 'st.write' solo si el mensaje no está vacío.")

st.write("\n")
asunto = st.text_input("Ingresa el asunto: ")
mensaje = st.text_area("Ingresa el mensaje: ")

if st.button("Enviar"):

    code = '''{
        f{asunto}
        f{mensaje}
        
    }'''
    
    st.code(code, language="python")