import streamlit as st 
import time, random

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
asunto = st.text_input("Ingresa el asunto:")
mensaje = st.text_area("Ingresa el mensaje:")

if st.button("Enviar"):
    if asunto.strip() and mensaje.strip():
        
        data = {
            "asunto": asunto,
            "mensaje": mensaje
        }
        
        st.json(data)
        st.success("✅")
        
    else:
        st.warning("Algún campo está vacío, por favor completa ambos campos.")

st.write("\n")
st.write("\n")

st.subheader("Ejercicio 6 - Login simulado (Session State)", divider="rainbow")
st.text("Enunciado:")
st.text("Crea dos campos: usuario y contraseña. \n-  Un boton 'Ingresar.' \n- Si el usuario es 'admin' y la contraseña es '1234', guarda en 'st.session_state' que el usuario está logueado y muestra un mensaje de éxito \n- Si ya esta logueado, muestra un boton 'Cerrar Sesion' que limpie el estado.")


if "logueado" not in st.session_state:
    st.session_state.logueado = False


if not st.session_state.logueado:

    user = st.text_input("Usuario:")
    password = st.text_input("Contraseña:", type="password")

    if st.button("Ingresar"):
        if user == "admin" and password == "1234":
            st.session_state.logueado = True
            st.success("Has iniciado sesion")
        else:
            st.error("Usuario o contraseña incorrectos.")

else:
    st.write("Ya estas logueado")
    if st.button("Cerrar Sesión"):
        st.session_state.logueado = False
        st.success("Has cerrado sesion")


    
st.write("\n")
st.write("\n")



st.subheader("Ejercicio 7 - Lista de Compras (Session State)", divider="rainbow")
st.text("Enunciado:")
st.text("- Un 'st.text_input' para ingresar un producto. \n- Dos botones: 'Agregar' y 'Limpiar Lista'. \n- Muestra la lista de productos agregados hasta el momento. La lista debe persistir aunque interactúes con otros widgets.")

if "productos" not in st.session_state:
    st.session_state.productos = []


producto = st.text_input("Ingresa un producto")


if st.button("Agregar"):
    if producto != "":
        st.session_state.productos.append(producto)
        st.success("Producto agregado ✅")
    else:
        st.warning("Escribe un producto primero")


if st.button("Limpiar Lista"):
    st.session_state.productos = []
    st.warning("Lista limpiada")


st.write("### Lista de productos:")
st.write(st.session_state.productos)


st.write("\n")
st.write("\n")



st.subheader("Ejercicio 8 - Grafico interactivo", divider="rainbow")
st.text("Enunciado:")
st.text("- Usa un 'st.slider'  para seleccionar un número `N` entre 10 y 100. \n- Genera una lista de 'N' numeros aleatorios. \n- Muestra un `st.line_chart` con esos datos \n-  Añade un botón para 'Regenerar' los datos (pista: el botón hará rerun, lo que regenerará los aleatorios automáticamente)")

N = st.slider("Selecciona la cantidad de números", 10, 100, 20)

datos = [random.randint(0, 100) for _ in range(N)]

st.line_chart(datos)

if st.button("Regenerar"):
    st.rerun()