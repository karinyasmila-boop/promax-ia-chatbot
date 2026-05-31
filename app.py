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
# CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* BACKGROUND */

.stApp {

    background:
    radial-gradient(circle at top left, rgba(124,58,237,0.20), transparent 30%),
    radial-gradient(circle at bottom right, rgba(6,182,212,0.20), transparent 30%),
    #020617;

    color: white;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #050816,
        #091224
    );

    border-right:
    1px solid rgba(255,255,255,0.05);
}

/* LOGO */

.logo {

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
}

.logo-sub {

    color: #CBD5E1;

    margin-bottom: 25px;
}

/* ONLINE */

.online {

    display: inline-block;

    padding: 10px 18px;

    border-radius: 999px;

    background:
    rgba(255,255,255,0.05);

    border:
    1px solid rgba(255,255,255,0.06);

    margin-bottom: 25px;

    color: #22C55E;

    font-weight: 600;
}

/* HERO */

.hero-card {

    background:
    linear-gradient(
        145deg,
        rgba(15,23,42,0.95),
        rgba(17,24,39,0.95)
    );

    border:
    1px solid rgba(255,255,255,0.05);

    border-radius: 28px;

    padding: 45px;

    min-height: 520px;

    box-shadow:
        0 0 50px rgba(59,130,246,0.10);
}

.hero-title {

    font-size: 68px;

    font-weight: 800;

    line-height: 1.1;

    margin-bottom: 10px;
}

.hero-gradient {

    background: linear-gradient(
        90deg,
        #60A5FA,
        #A78BFA
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {

    font-size: 24px;

    font-weight: 700;

    color: #A78BFA;

    margin-bottom: 30px;
}

.hero-desc {

    color: #CBD5E1;

    font-size: 18px;

    line-height: 1.8;

    margin-bottom: 30px;
}

/* MESSAGE BOX */

.message-box {

    background:
    linear-gradient(
        90deg,
        rgba(124,58,237,0.22),
        rgba(59,130,246,0.10)
    );

    border:
    1px solid rgba(139,92,246,0.35);

    border-radius: 22px;

    padding: 22px;

    color: white;

    font-size: 17px;
}

/* FEATURE CARD */

.feature-card {

    background:
    rgba(255,255,255,0.03);

    border:
    1px solid rgba(255,255,255,0.05);

    border-radius: 22px;

    padding: 28px;

    min-height: 190px;

    transition: 0.3s;
}

.feature-card:hover {

    transform: translateY(-5px);

    border:
    1px solid #8B5CF6;

    box-shadow:
        0 0 25px rgba(139,92,246,0.30);
}

.feature-title {

    font-size: 22px;

    font-weight: 700;

    margin-top: 16px;

    margin-bottom: 10px;
}

.feature-desc {

    color: #94A3B8;

    line-height: 1.7;
}

/* SIDE PANEL */

.side-panel {

    background:
    rgba(255,255,255,0.03);

    border:
    1px solid rgba(255,255,255,0.05);

    border-radius: 24px;

    padding: 28px;

    margin-bottom: 20px;
}

.side-title {

    font-size: 22px;

    font-weight: 700;

    margin-bottom: 20px;
}

.side-item {

    margin-bottom: 18px;

    color: #CBD5E1;
}

/* CHAT */

.user-msg {

    background:
    linear-gradient(
        135deg,
        #2563EB,
        #7C3AED
    );

    padding: 18px;

    border-radius: 18px;

    margin-left: 30%;

    margin-bottom: 15px;
}

.bot-msg {

    background:
    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.05);

    padding: 18px;

    border-radius: 18px;

    margin-right: 30%;

    margin-bottom: 15px;
}

/* INPUT */

.stChatInput input {

    background:
    rgba(15,23,42,0.92) !important;

    border:
    1px solid rgba(139,92,246,0.35) !important;

    border-radius: 20px !important;

    color: white !important;

    height: 65px !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("""
    <div class='logo'>
        ADA PROMAX IA
    </div>

    <div class='logo-sub'>
        Asistente Inteligente RRHH
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='online'>
        ● En línea
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
# MAIN
# =====================================================

left, right = st.columns([3,1])

# =====================================================
# HERO
# =====================================================

with left:

    st.markdown("<div class='hero-card'>", unsafe_allow_html=True)

    c1, c2 = st.columns([1,1.4])

    with c1:

        st.image(
            "https://images.unsplash.com/photo-1677442136019-21780ecad995",
            width=340
        )

    with c2:

        st.markdown("""
        <div class='hero-title'>
            Hola, soy
            <span class='hero-gradient'>
                ADA PROMAX IA
            </span>
            👋
        </div>

        <div class='hero-sub'>
            Tu asistente inteligente en Recursos Humanos
        </div>

        <div class='hero-desc'>
            Estoy aquí para ayudarte con información
            especializada en compensaciones,
            desarrollo profesional y análisis
            estratégico del talento.
        </div>

        <div class='message-box'>
            Puedes preguntarme sobre bandas salariales,
            planes de carrera, análisis de compensación
            y mucho más...
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("## ⚡ Sugerencias rápidas")

    f1, f2, f3 = st.columns(3)

    with f1:

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

    with f2:

        st.markdown("""
        <div class='feature-card'>

            <div style='font-size:32px;'>📈</div>

            <div class='feature-title'>
                Plan de Carrera
            </div>

            <div class='feature-desc'>
                Desarrollo profesional y crecimiento.
            </div>

        </div>
        """, unsafe_allow_html=True)

    with f3:

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

# =====================================================
# RIGHT PANEL
# =====================================================

with right:

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

# =====================================================
# CHAT
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    if msg["role"] == "user":

        st.markdown(f"""
        <div class='user-msg'>
            👤 {msg["content"]}
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class='bot-msg'>
            🤖 {msg["content"]}
        </div>
        """, unsafe_allow_html=True)

# =====================================================
# INPUT
# =====================================================

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
