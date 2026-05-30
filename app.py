import streamlit as st
import requests

st.title("PROMAX IA 🤖 Compensaciones")

employee_id = st.text_input("Ingresa tu código de empleado")

consulta = st.selectbox(
    "¿Qué deseas consultar?",
    [
        "1.- Bandas salariales",
        "2.- Plan de carrera",
        "3.- Diagnóstico Salarial"
    ]
)

pregunta = st.text_area("Describe tu consulta")

if st.button("Enviar Consulta"):

    webhook_url = "https://hook.us2.make.com/9m7ly3yx7tbtn27ldm63jtg4ljcs52kj"

    datos = {
        "employee_id": employee_id,
        "selected_option": consulta,
        "text": pregunta
    }

    try:

        respuesta = requests.post(webhook_url, json=datos)

        if respuesta.status_code == 200:

            st.success("Consulta procesada correctamente")

            data = respuesta.json()

            resultado = data["respuesta"]

            st.info(resultado)

        else:
            st.error("Error conectando con Make")

    except Exception as e:
        st.error(f"Error: {e}")
