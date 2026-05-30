import streamlit as st
import requests

st.set_page_config(page_title="ADA PROMAX IA", layout="centered")

st.title("ADA PROMAX IA 🤖 Asistente RRHH - Compensaciones")

# Inicializar historial
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Caja de texto del chat
prompt = st.chat_input("Escribe tu consulta...")

if prompt:

    # Mostrar mensaje usuario
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # URL WEBHOOK MAKE
    webhook_url = "https://hook.us2.make.com/9m7ly3yx7tbtn27ldm63jtg4ljcs52kj"

    datos = {
        "employee_id": "PE0000012",
        "selected_option": "Consulta General",
        "text": prompt
    }

    try:
        respuesta = requests.post(webhook_url, json=datos)

        if respuesta.status_code == 200:

            resultado = respuesta.text

            st.session_state.messages.append(
                {"role": "assistant", "content": resultado}
            )

            with st.chat_message("assistant"):
                st.markdown(resultado)

        else:
            st.error("Error conectando con Make")

    except Exception as e:
        st.error(f"Error: {e}")
