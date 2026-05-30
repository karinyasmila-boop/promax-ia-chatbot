import streamlit as st
import requests
from datetime import datetime

# CONFIG
st.set_page_config(
    page_title="ADA PROMAX IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS PREMIUM
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0F172A;
    color: white;
}

/* Fondo principal */
.stApp {
    background: linear-gradient(
        135deg,
        #0F172A 0%,
        #111827 40%,
        #1E293B 100%
    );
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.95);
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Cards */
.metric-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(14px);
    transition: 0.3s;
}

.metric-card:hover {
    transform: translateY(-3px);
    border: 1px solid #3B82F6;
}

/* Chat usuario */
.user-bubble {
    background: linear-gradient(135deg, #2563EB, #1D4ED8);
    padding: 14px;
    border-radius: 16px;
    margin-bottom: 10px;
}

/* Chat IA */
.bot-bubble {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 16px;
    border-radius: 16px;
    margin-bottom: 15px;
    backdrop-filter: blur(12px);
}

/* Título */
.main-title {
    font-size: 42px;
    font-weight: 700;
    background: linear-gradient(90deg, #60A5FA, #A78BFA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Input */
.stChatInput input {
    background-color: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: white !important;
    border-radius: 14px !important;
}

/* Botones */
.stButton button {
    background: linear-gradient(135deg, #3B82F6, #8B5CF6);
    border: none;
    border-radius: 12px;
    color: white;
    font-weight: 600;
}

/* Ocultar footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:

    st.markdown("## 🤖 ADA PROMAX IA")

    st.markdown("---")

    st.markdown("""
    ### 🧠 Módulos IA

    - 💰 Compensaciones
    - 📈 Bandas Salariales
    - 🚀 Plan Carrera
    - 📊 Analítica RRHH
    - 🎯 Diagnóstico Inteligente
    """)

    st.markdown("---")

    st.markdown("### ⚡ Estado")
    st.success("Sistema Operativo")

# HEADER
st.markdown("""
<div class="main-title">
ADA PROMAX IA
</div>
""", unsafe_allow_html=True)

st.caption("Asistente Inteligente de Recursos Humanos")

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h4>📊 Consultas</h4>
        <h2>1,284</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h4>⚡ Tiempo Respuesta</h4>
        <h2>1.2s</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h4>😊 Satisfacción</h4>
        <h2>98%</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# HISTORIAL
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes
for msg in st.session_state.messages:

    if msg["role"] == "user":
        st.markdown(f"""
        <div class="user-bubble">
        👤 {msg["content"]}
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div class="bot-bubble">
        🤖 {msg["content"]}
        </div>
        """, unsafe_allow_html=True)

# INPUT CHAT
prompt = st.chat_input("Escribe tu consulta...")

if prompt:

    # Guardar usuario
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    webhook_url = "https://hook.us2.make.com/9m7ly3yx7tbtn27ldm63jtg4ljcs52kj"

    datos = {
        "employee_id": "PE0000012",
        "selected_option": "Consulta General",
        "text": prompt,
        "timestamp": str(datetime.now())
    }

    with st.spinner("ADA está analizando tu consulta..."):

        try:

            respuesta = requests.post(
                webhook_url,
                json=datos
            )

            if respuesta.status_code == 200:

                resultado = respuesta.text

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": resultado
                })

                st.rerun()

            else:
                st.error("Error conectando con Make")

        except Exception as e:
            st.error(f"Error: {e}")
