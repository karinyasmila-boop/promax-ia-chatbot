import streamlit as st
import requests
from streamlit_option_menu import option_menu

# =====================================================
# CONFIGURACIÓN GENERAL
# =====================================================
st.set_page_config(
    page_title="ADA PROMAX IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CARGAR CSS FUTURISTA
# =====================================================
with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =====================================================
# SIDEBAR — PANEL HOLOGRÁFICO
# =====================================================
with st.sidebar:

    st.markdown("""
    <div class='logo-title'>ADA PROMAX IA</div>
    <div class='logo-sub'>Asistente Inteligente RRHH</div>

    <div class='online-badge'>
        <div class='online-dot'></div>
        <span>En línea</span>
    </div>
    """, unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None,
        options=[
            "Inicio",
            "Bandas Salariales",
            "Plan de Carrera",
            "Diagnóstico IA",
            "Historial",
            "Configuración"
        ],
        icons=[
            "house",
            "cash-stack",
            "graph-up-arrow",
            "cpu",
            "clock-history",
            "gear"
        ],
        default_index=0
    )

# =====================================================
# LAYOUT PRINCIPAL
# =====================================================
left, right = st.columns([3.2, 1])

# =====================================================
# HERO FUTURISTA
# =====================================================
with left:

    hero_html = """
    <div class='hero-card'>

        <div class='hero-label'>
            AI Powered HR Intelligence
        </div>

        <div class='hero-title'>
            <span>ADA PROMAX IA</span>
        </div>

        <div class='hero-subtitle'>
            Tu copiloto inteligente de Recursos Humanos
        </div>

        <div class='hero-description'>
            Plataforma IA especializada en compensaciones,
            bandas salariales, planes de carrera y analítica
            estratégica del talento.
        </div>

        <div class='message-box'>
            Pregúntame sobre compensaciones,
            carrera o RRHH...
        </div>

    </div>
    """

    st.markdown(hero_html, unsafe_allow_html=True)
    st.image(
        "assets/Copilot_20260530_202650.png",
        width=380
    )
    # =====================================================
    # SUGERENCIAS RÁPIDAS — TARJETAS NEO
    # =====================================================
    st.markdown("## ⚡ Sugerencias rápidas")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown("""
        <div class='feature-card'>
            <div style='font-size:32px;'>💰</div>
            <div class='feature-title'>Bandas Salariales</div>
            <div class='feature-desc'>
                Consulta estructuras salariales y rangos competitivos.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class='feature-card'>
            <div style='font-size:32px;'>📈</div>
            <div class='feature-title'>Plan de Carrera</div>
            <div class='feature-desc'>
                Diseña rutas de crecimiento profesional.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class='feature-card'>
            <div style='font-size:32px;'>🧠</div>
            <div class='feature-title'>Diagnóstico IA</div>
            <div class='feature-desc'>
                Análisis inteligente de compensaciones.
            </div>
        </div>
        """, unsafe_allow_html=True)

# =====================================================
# PANEL DERECHO — MÓDULOS HOLOGRÁFICOS
# =====================================================
with right:

    st.markdown("""
    <div class='side-panel'>
        <div class='side-title'>Capacidades ADA IA</div>
        <div class='side-item'>📊 Análisis inteligente de datos</div>
        <div class='side-item'>🎯 Recomendaciones personalizadas</div>
        <div class='side-item'>🌐 Información actualizada</div>
        <div class='side-item'>⏰ Soporte 24/7</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='side-panel'>
        <div class='side-title'>Estadísticas</div>
        <div class='side-item'>📈 Consultas: 12,840 ↑12%</div>
        <div class='side-item'>🎯 Precisión: 98% ↑3%</div>
        <div class='side-item'>⚡ Tiempo promedio: 1.2s ↓15%</div>
        <div class='side-item'>😊 Satisfacción: 99% ↑5%</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# CHAT — BURBUJAS NEON
# =====================================================
st.markdown("<br>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-message'>👤 {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='assistant-message'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

# =====================================================
# INPUT DEL CHAT
# =====================================================
prompt = st.chat_input("Escribe tu consulta para ADA...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    webhook_url = "https://hook.us2.make.com/9m7ly3yx7tbtn27ldm63jtg4ljcs52kj"

    payload = {
        "employee_id": "PE0000012",
        "selected_option": "Consulta General",
        "text": prompt
    }

    with st.spinner("ADA está analizando tu consulta..."):

        try:
            response = requests.post(webhook_url, json=payload)

            if response.status_code == 200:
                result = response.text
                st.session_state.messages.append({"role": "assistant", "content": result})
                st.rerun()
            else:
                st.error("Error conectando con Make")

        except Exception as e:
            st.error(f"Error: {e}")
