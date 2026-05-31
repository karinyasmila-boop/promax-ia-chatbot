import streamlit as st
import requests
from streamlit_option_menu import option_menu

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ADA PROMAX IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
FONTS
========================================================= */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {

    font-family: 'Inter', sans-serif;

    scroll-behavior: smooth;
}

/* =========================================================
GLOBAL
========================================================= */

.stApp {

    background:
    radial-gradient(circle at top left, rgba(124,58,237,0.22), transparent 28%),
    radial-gradient(circle at bottom right, rgba(6,182,212,0.22), transparent 28%),
    #020617;

    color: white;

    overflow-x: hidden;
}

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* =========================================================
SCROLLBAR
========================================================= */

::-webkit-scrollbar {

    width: 10px;
}

::-webkit-scrollbar-track {

    background: #020617;
}

::-webkit-scrollbar-thumb {

    background:
    linear-gradient(
        #7C3AED,
        #3B82F6
    );

    border-radius: 999px;
}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #050816,
        #091224
    );

    border-right:
    1px solid rgba(255,255,255,0.06);
}

section[data-testid="stSidebar"] > div {

    padding-top: 24px;
}

/* =========================================================
SIDEBAR MENU
========================================================= */

.nav-link {

    border-radius: 18px !important;

    margin-bottom: 10px !important;

    transition: all 0.3s ease !important;

    padding: 10px 14px !important;
}

.nav-link:hover {

    background:
    rgba(139,92,246,0.14) !important;

    transform: translateX(4px);
}

.nav-link-selected {

    background:
    linear-gradient(
        135deg,
        #7C3AED,
        #3B82F6
    ) !important;

    border-radius: 18px !important;

    box-shadow:
        0 0 25px rgba(124,58,237,0.35);
}

/* =========================================================
LOGO
========================================================= */

.logo-title {

    font-size: 34px;

    font-weight: 800;

    margin-bottom: 5px;

    background: linear-gradient(
        90deg,
        #60A5FA,
        #A78BFA
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    text-shadow:
        0 0 25px rgba(96,165,250,0.18);
}

.logo-sub {

    color: #CBD5E1;

    font-size: 15px;

    margin-bottom: 25px;
}

/* =========================================================
ONLINE BADGE
========================================================= */

.online-badge {

    display: flex;

    align-items: center;

    gap: 10px;

    width: fit-content;

    padding: 12px 18px;

    border-radius: 999px;

    background:
    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.08);

    margin-bottom: 28px;

    backdrop-filter: blur(14px);
}

.online-dot {

    width: 10px;

    height: 10px;

    border-radius: 50%;

    background: #22C55E;

    box-shadow:
        0 0 14px #22C55E;
}

/* =========================================================
HERO CARD
========================================================= */

.hero-card {

    position: relative;

    background:
    linear-gradient(
        145deg,
        rgba(10,15,35,0.94),
        rgba(20,25,55,0.94)
    );

    border:
    1px solid rgba(255,255,255,0.06);

    border-radius: 32px;

    padding: 50px;

    overflow: hidden;

    min-height: 580px;

    box-shadow:
        0 0 70px rgba(59,130,246,0.10);

    backdrop-filter: blur(18px);
}

.hero-card::before {

    content: "";

    position: absolute;

    inset: 0;

    background-image:
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);

    background-size: 40px 40px;

    opacity: 0.20;

    pointer-events: none;
}

.hero-card::after {

    content: "";

    position: absolute;

    width: 450px;

    height: 450px;

    border-radius: 50%;

    background:
    radial-gradient(
        rgba(59,130,246,0.20),
        transparent 70%
    );

    top: -180px;

    left: -180px;

    z-index: 0;
}

/* =========================================================
HERO IMAGE
========================================================= */

.hero-image {

    position: relative;

    z-index: 2;

    display: flex;

    justify-content: center;

    align-items: center;

    height: 100%;
}

/* =========================================================
HERO LABEL
========================================================= */

.hero-label {

    position: relative;

    z-index: 2;

    width: fit-content;

    padding: 10px 18px;

    border-radius: 999px;

    background:
    rgba(124,58,237,0.15);

    border:
    1px solid rgba(124,58,237,0.35);

    color: #C4B5FD;

    font-size: 13px;

    font-weight: 600;

    margin-bottom: 24px;

    backdrop-filter: blur(12px);

    animation: pulseGlow 4s infinite;
}

/* =========================================================
HERO TITLE
========================================================= */

.hero-title {

    position: relative;

    z-index: 2;

    font-size: 76px !important;

    font-weight: 800 !important;

    line-height: 1.05;

    margin-bottom: 18px;

    letter-spacing: -2px;

    color: white;
}

.hero-title span {

    background: linear-gradient(
        90deg,
        #60A5FA,
        #818CF8,
        #A78BFA
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    text-shadow:
        0 0 25px rgba(96,165,250,0.22);
}

/* =========================================================
HERO SUBTITLE
========================================================= */

.hero-subtitle {

    position: relative;

    z-index: 2;

    font-size: 22px;

    font-weight: 700;

    color: #A78BFA;

    margin-bottom: 24px;
}

/* =========================================================
DESCRIPTION
========================================================= */

.hero-description {

    position: relative;

    z-index: 2;

    color: #CBD5E1;

    font-size: 18px;

    line-height: 1.9;

    max-width: 720px;

    margin-bottom: 35px;
}

/* =========================================================
MESSAGE BOX
========================================================= */

.message-box {

    position: relative;

    z-index: 2;

    width: fit-content;

    background:
    linear-gradient(
        90deg,
        rgba(124,58,237,0.25),
        rgba(59,130,246,0.12)
    );

    border:
    1px solid rgba(139,92,246,0.35);

    border-radius: 24px;

    padding: 24px 32px;

    color: white;

    font-size: 18px;

    margin-top: 20px;

    backdrop-filter: blur(18px);

    box-shadow:
        0 0 35px rgba(124,58,237,0.18);
}

/* =========================================================
FEATURE CARDS
========================================================= */

.feature-card {

    background:
    rgba(255,255,255,0.03);

    border:
    1px solid rgba(255,255,255,0.06);

    border-radius: 26px;

    padding: 30px;

    min-height: 190px;

    transition: 0.35s ease;

    cursor: pointer;

    backdrop-filter: blur(16px);
}

.feature-card:hover {

    transform:
    translateY(-6px);

    border:
    1px solid #8B5CF6;

    box-shadow:
        0 0 30px rgba(139,92,246,0.28);
}

.feature-title {

    font-size: 22px;

    font-weight: 700;

    margin-top: 16px;

    margin-bottom: 12px;
}

.feature-desc {

    color: #94A3B8;

    line-height: 1.7;
}

/* =========================================================
SIDE PANEL
========================================================= */

with side_col:

    st.markdown("""
    <div class='side-panel'>

        <div class='side-title'>
            Capacidades ADA IA
        </div>

        <div class='side-item'>
            📊 Análisis inteligente de datos
        </div>

        <div class='side-item'>
            🎯 Recomendaciones personalizadas
        </div>

        <div class='side-item'>
            🌐 Información actualizada
        </div>

        <div class='side-item'>
            ⏰ Soporte 24/7
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='side-panel'>

        <div class='side-title'>
            Estadísticas
        </div>

        <div class='side-item'>
            📈 Precisión: 96%
        </div>

        <div class='side-item'>
            ⚡ Tiempo respuesta: 1.2s
        </div>

        <div class='side-item'>
            😊 Satisfacción: 98%
        </div>

    </div>
    """, unsafe_allow_html=True)
/* =========================================================
CHAT
========================================================= */

.user-message {

    background:
    linear-gradient(
        135deg,
        #2563EB,
        #7C3AED
    );

    padding: 18px 22px;

    border-radius: 20px;

    margin-bottom: 15px;

    margin-left: 30%;

    box-shadow:
        0 0 25px rgba(124,58,237,0.25);
}

.assistant-message {

    background:
    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.06);

    padding: 18px 24px;

    border-radius: 20px;

    margin-bottom: 15px;

    margin-right: 30%;

    backdrop-filter: blur(16px);
}

/* =========================================================
INPUT
========================================================= */

.stChatInput input {

    background:
    rgba(15,23,42,0.92) !important;

    border:
    1px solid rgba(139,92,246,0.35) !important;

    border-radius: 20px !important;

    color: white !important;

    padding-left: 20px !important;

    height: 65px !important;

    font-size: 16px !important;

    box-shadow:
        0 0 25px rgba(139,92,246,0.15);
}

/* =========================================================
ANIMATION
========================================================= */

@keyframes pulseGlow {

    0% {
        box-shadow:
        0 0 10px rgba(124,58,237,0.15);
    }

    50% {
        box-shadow:
        0 0 30px rgba(124,58,237,0.40);
    }

    100% {
        box-shadow:
        0 0 10px rgba(124,58,237,0.15);
    }
}

/* =========================================================
RESPONSIVE
========================================================= */

@media (max-width: 900px) {

    .hero-title {

        font-size: 46px !important;
    }

    .hero-card {

        padding: 28px;
    }

    .user-message {

        margin-left: 5%;
    }

    .assistant-message {

        margin-right: 5%;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class='logo-title'>
        ADA PROMAX IA
    </div>

    <div class='logo-sub'>
        Asistente Inteligente RRHH
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='online-badge'>
        <div class='online-dot'></div>
        En línea
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

# =========================================================
# MAIN LAYOUT
# =========================================================

main_col, side_col = st.columns([3, 1])

```python
# =========================================================
# HERO SECTION
# =========================================================

with main_col:

    hero_left, hero_right = st.columns([1, 1.4])

    # =====================================================
    # LEFT IMAGE
    # =====================================================

    with hero_left:

        st.markdown("""
        <div class='hero-card'>
        """, unsafe_allow_html=True)

        st.image(
            "https://images.unsplash.com/photo-1677442136019-21780ecad995",
            width=340
        )

        st.markdown("""
        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # RIGHT CONTENT
    # =====================================================

    with hero_right:

        st.markdown("""
        <div class='hero-card'>

            <div class='hero-label'>
                🤖 AI Powered HR Intelligence
            </div>

            <div class='hero-title'>
                Hola, soy <span>ADA PROMAX IA</span> 👋
            </div>

            <div class='hero-subtitle'>
                Tu asistente inteligente en Recursos Humanos
            </div>

            <div class='hero-description'>
                Estoy aquí para ayudarte con información
                especializada en compensaciones, desarrollo
                profesional y análisis estratégico del talento.
            </div>

            <div class='message-box'>
                Puedes preguntarme sobre bandas salariales,
                planes de carrera, análisis de compensación
                y mucho más...
            </div>

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# QUICK ACTIONS
# =========================================================

st.markdown("## ⚡ Sugerencias rápidas")

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
    <div class='feature-card'>

        <div style='font-size:32px;'>💰</div>

        <div class='feature-title'>
            Bandas Salariales
        </div>

        <div class='feature-desc'>
            Información sobre estructura salarial
            y compensaciones.
        </div>

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class='feature-card'>

        <div style='font-size:32px;'>📈</div>

        <div class='feature-title'>
            Plan de Carrera
        </div>

        <div class='feature-desc'>
            Rutas de crecimiento y desarrollo profesional.
        </div>

    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown("""
    <div class='feature-card'>

        <div style='font-size:32px;'>🧠</div>

        <div class='feature-title'>
            Diagnóstico IA
        </div>

        <div class='feature-desc'>
            Análisis inteligente de compensaciones.
        </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# RIGHT PANEL
# =========================================================

with side_col:

    st.markdown("""
    <div class='side-panel'>

        <div class='side-title'>
            Capacidades ADA IA
        </div>

        <div class='side-item'>
            📊 Análisis inteligente de datos
        </div>

        <div class='side-item'>
            🎯 Recomendaciones personalizadas
        </div>

        <div class='side-item'>
            🌐 Información actualizada
        </div>

        <div class='side-item'>
            ⏰ Soporte 24/7
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='side-panel'>

        <div class='side-title'>
            Estadísticas
        </div>

        <div class='side-item'>
            📈 Precisión: 96%
        </div>

        <div class='side-item'>
            ⚡ Tiempo respuesta: 1.2s
        </div>

        <div class='side-item'>
            😊 Satisfacción: 98%
        </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# CHAT
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

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

# =========================================================
# CHAT INPUT
# =========================================================

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
        "selected_option":"Consulta General",
        "text":prompt
    }

    with st.spinner("ADA está analizando..."):

        try:

            response = requests.post(
                webhook_url,
                json=payload
            )

            if response.status_code == 200:

                result = response.text

                st.session_state.messages.append({
                    "role":"assistant",
                    "content":result
                })

                st.rerun()

            else:

                st.error("Error conectando con Make")

        except Exception as e:

            st.error(f"Error: {e}")
