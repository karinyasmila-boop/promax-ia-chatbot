import streamlit as st
import requests

st.title("PROMAX IA 🤖 Compensaciones")

employee_id = st.text_input("Ingresa tu código de empleado")
[Ejm: PEXXXXXXXX]

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

    webhook_url = "https://hook.us2.make.com/x0obbhw96ggsb0oqcjodrqlgyhmfaav2"

    datos = {
        "employee_id": employee_id,
        "selected_option": consulta,
        "text": pregunta
    }

    respuesta = requests.post(webhook_url, json=datos)

    if respuesta.status_code == 200:
        st.success("Consulta procesada correctamente")

         try:
            resultado = respuesta.text
            st.info(resultado)

        except:
            st.error("No se pudo leer la respuesta")

    else:
        st.error("Error conectando con Make")
