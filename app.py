import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json

# CONFIG
st.set_page_config(
    page_title="ADA PROMAX IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# LOAD CSS
with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:

        
    selected = option_menu(
        menu_title=None,
        options=[
            "Inicio",
            "Compensaciones",
            "Bandas",
            "Plan Carrera",
            "Diagnóstico IA",
            "Analytics"
        ],
        icons=[
            "house",
            "cash-stack",
            "graph-up",
            "rocket",
            "cpu",
            "bar-chart"
        ],
        default_index=0,
    )

# HERO SECTION
col1, col2 = st.columns([2.2, 1])

with col1:

    st.markdown(
        "<div class='hero-label'>🤖 AI Powered HR Intelligence</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1 class='hero-title'>ADA PROMAX IA</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='hero-subtitle'>Tu copiloto inteligente de Recursos Humanos</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p class='hero-description'>
        Plataforma IA especializada en compensaciones,
        bandas salariales, planes de carrera y analítica
        estratégica del talento.
        </p>
        """,
        unsafe_allow_html=True
    )

    badge1, badge2, badge3 = st.columns(3)

    with badge1:
        st.markdown(
            "<div class='hero-badge'>⚡ IA Enterprise</div>",
            unsafe_allow_html=True
        )

    with badge2:
        st.markdown(
            "<div class='hero-badge'>📊 HR Analytics</div>",
            unsafe_allow_html=True
        )

    with badge3:
        st.markdown(
            "<div class='hero-badge'>💰 Compensation AI</div>",
            unsafe_allow_html=True
        )

with col2:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
        width=280
    )

# KPI ROW
k1,k2,k3,k4 = st.columns(4)

metrics = [
    ("Consultas", "12,840"),
    ("Precisión", "98%"),
    ("Tiempo", "1.2s"),
    ("Satisfacción", "99%")
]

for col, metric in zip([k1,k2,k3,k4], metrics):

    with col:
        st.markdown(f"""
        <div class='metric-card'>
            <h4>{metric[0]}</h4>
            <h2>{metric[1]}</h2>
        </div>
        """, unsafe_allow_html=True)

# CHAT
st.markdown("## 💬 Conversación Inteligente")

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_container = st.container()

with chat_container:

    for msg in st.session_state.messages:

        if msg["role"] == "user":

            st.markdown(f"""
            <div class='user-message'>
            👤 {msg["content"]}
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class='assistant-message'>
            🤖 {msg["content"]}
            </div>
            """, unsafe_allow_html=True)

# INPUT
prompt = st.chat_input(
    "Pregúntale a ADA sobre compensaciones, carrera o RRHH..."
)

if prompt:

    st.session_state.messages.append({
        "role":"user",
        "content":prompt
    })

    webhook_url = "https://hook.us2.make.com/9m7ly3yx7tbtn27ldm63jtg4ljcs52kj"

    payload = {
        "employee_id":"PE0000012",
        "text":prompt
    }

    with st.spinner("ADA está analizando..."):

        try:

            response = requests.post(
                webhook_url,
                json=payload
            )

            result = response.text

            st.session_state.messages.append({
                "role":"assistant",
                "content":result
            })

            st.rerun()

        except Exception as e:
            st.error(str(e))
