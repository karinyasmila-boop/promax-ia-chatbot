import streamlit as st
import requests
from streamlit_option_menu import option_menu

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="ADA PROMAX IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# LOAD CSS
# =====================================================

with open("styles/main.css", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("""
    <div class="logo-title">
        ADA PROMAX IA
    </div>

    <div class="logo-sub">
        Asistente Inteligente RRHH
    </div>

    <br>

    <div class="online-badge">
        <div class="online-dot"></div>
        En línea
    </div>

    <br>
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
            "graph-up",
            "cpu",
            "clock-history",
            "gear"
        ],
        default_index=0
    )

# =====================================================
# MAIN LAYOUT
# =====================================================

main_left, main_right = st.columns([4, 1.3])

# =====================================================
# HERO SECTION
# =====================================================

with main_left:

    st.markdown("<div class='hero-card'>", unsafe_allow_html=True)

    hero_left, hero_right = st.columns([1, 2])

    # =================================================
    # ROBOT
    # =================================================

    with hero_left:

        st.image(
            "assets/Copilot_20260530_200709.png",
            width=240
        )

    # =================================================
    # TEXT
    # =================================================

    with hero_right:

        st.markdown("""
        <div class="hero-label">
            AI Powered HR Intelligence
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="hero-title">
            <span>ADA PROMAX IA</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="hero-subtitle">
            Tu copiloto inteligente de Recursos Humanos
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="hero-description">
            Plataforma IA especializada en compensaciones,
            bandas salariales, planes de carrera y analítica
            estratégica del talento.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="message-box">
            Pregúntame sobre compensaciones,
            carrera o RRHH...
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =================================================
    # FEATURE CARDS
    # =================================================

    st.markdown("""
    <h2 style="margin-bottom:25px;">
        ⚡ Sugerencias rápidas
    </h2>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="feature-card">

            <div class="feature-title">
                💰 Bandas Salariales
            </div>

            <div class="feature-desc">
                Información sobre estructura salarial
                y compensaciones.
            </div>

        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="feature-card">

            <div class="feature-title">
                📈 Plan de Carrera
            </div>

            <div class="feature-desc">
                Rutas de crecimiento y desarrollo profesional.
            </div>

        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class="feature-card">

            <div class="feature-title">
                🤖 Diagnóstico IA
            </div>

            <div class="feature-desc">
                Análisis inteligente de compensaciones.
            </div>

        </div>
        """, unsafe_allow_html=True)

# =====================================================
# RIGHT PANEL
# =====================================================

with main_right:

    st.markdown("""
    <div class="side-panel">

        <div class="side-title">
            Capacidades ADA IA
        </div>

        <div class="side-item">
            📊 Análisis inteligente de datos
        </div>

        <div class="side-item">
            🎯 Recomendaciones personalizadas
        </div>

        <div class="side-item">
            🌐 Información actualizada
        </div>

        <div class="side-item">
            🛟 Soporte 24/7
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="side-panel">

        <div class="side-title">
            Estadísticas
        </div>

        <div class="side-item">
            📈 Consultas: 12,840
        </div>

        <div class="side-item">
            🎯 Precisión: 98%
        </div>

        <div class="side-item">
            ⚡ Tiempo promedio: 1.2s
        </div>

        <div class="side-item">
            😊 Satisfacción: 99%
        </div>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# CHAT
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    if msg["role"] == "user":

        st.markdown(f"""
        <div class="user-message">
            👤 {msg["content"]}
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class="assistant-message">
            🤖 {msg["content"]}
        </div>
        """, unsafe_allow_html=True)

# =====================================================
# INPUT
# =====================================================

prompt = st.chat_input(
    "Escribe tu consulta para ADA..."
)

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    webhook_url = "https://hook.us2.make.com/9m7ly3yx7tbtn27ldm63jtg4ljcs52kj"

    payload = {
        "employee_id": "PE0000012",
        "text": prompt
    }

    with st.spinner("ADA está analizando..."):

        try:

            response = requests.post(
                webhook_url,
                json=payload
            )

            result = response.text

            st.session_state.messages.append({
                "role": "assistant",
                "content": result
            })

            st.rerun()

        except Exception as e:

            st.error(str(e))
