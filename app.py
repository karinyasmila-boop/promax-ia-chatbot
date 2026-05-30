import streamlit as st
import requests

st.title("PROMAX IA Compensaciones")

employee_id = st.text_input("Ingresa tu código de empleado")

consulta = st.selectbox(
    "¿Qué deseas consultar?",
    [
        "Bandas salariales",
        "Plan de carrera",
        "Diagnóstico"
    ]
)

pregunta = st.text_area("Describe tu consulta")

if st.button("Consultar"):

    webhook_url = "https://hook.us2.make.com/9m7ly3yx7tbtn27ldm63jtg4ljcs52kj"

    datos = {
        "employee_id": employee_id,
        "selected_option": consulta,
        "text": pregunta
    }

    respuesta = requests.post(webhook_url, json=datos)

    if respuesta.status_code == 200:
        st.success("Consulta procesada correctamente")

        try:
            resultado = respuesta.json()["respuesta"]
            st.success(resultado)

        except:
            st.error("No se pudo leer la respuesta")

    else:
        st.error("Error conectando con Make")
