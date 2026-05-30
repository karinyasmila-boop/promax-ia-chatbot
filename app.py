import streamlit as st
import requests

st.set_page_config(page_title="ADA PROMAX IA", page_icon="🤖")

st.title("ADA PROMAX IA 🤖 Asistente RRHH - Compensaciones")

# Historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
prompt = st.chat_input("Escribe tu consulta...")

if prompt:

    # Mostrar mensaje usuario
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    webhook_url = "https://hook.us2.make.com/9m7ly3yx7tbtn27ldm63jtg4ljcs52kj"

    datos = {
        "employee_id": "PE0000012",
        "selected_option": "Consulta general",
        "text": prompt
    }

    try:

        respuesta = requests.post(webhook_url, json=datos)

        if respuesta.status_code == 200:

            resultado = respuesta.text

            with st.chat_message("assistant"):
                st.markdown(resultado)

            st.session_state.messages.append({
                "role": "assistant",
                "content": resultado
            })

        else:
            st.error("Error conectando con Make")

    except Exception as e:
        st.error(f"Error: {e}")
