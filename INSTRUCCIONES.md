# Guía de Actividad: Instrucciones Generales

Esta guía detalla cómo preparar tu entorno y entregar la actividad práctica de Streamlit.

## 1. Instrucciones de Configuración (Fork & Clone)

Antes de empezar a codificar, prepara tu entorno de trabajo:

1.  **Fork**: Ve a la página del repositorio original en GitHub y haz clic en el botón **"Fork"** (arriba a la derecha) para crear una copia en tu propia cuenta.
2.  **Clonar**: Clona **tu** repositorio (el fork) en tu máquina local:
    ```bash
    git clone https://github.com/TU_USUARIO/nombre-del-repo.git
    cd nombre-del-repo
    ```
3.  **Entorno Virtual**: Crea y activa un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv .venv
    # En Windows:
    .venv\Scripts\activate
    # En Mac/Linux:
    source .venv/bin/activate
    ```
4.  **Instalar Dependencias**: Instala las librerías necesarias desde el archivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## 2. Instrucciones de Desarrollo

1.  Dentro de la carpeta `pages`, crea un nuevo archivo llamado: `09_Ejercicios.py`.
2.  Importa streamlit (`import streamlit as st`) y configura la página.
3.  Resuelve los ejercicios descritos en el archivo `EJERCICIOS.md`.
4.  Separa visualmente cada ejercicio usando `st.subheader` y `st.divider`.

## 3. Entrega

1.  Asegúrate de que tu código corra sin errores (`streamlit run Inicio.py`).
2.  Haz commit y push de tus cambios a tu repositorio en GitHub:
    ```bash
    git add .
    git commit -m "Solución de ejercicios Streamlit"
    git push origin main
    ```
3.  Envía la URL de tu repositorio.
