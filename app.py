import streamlit as st
import requests
import uuid
import time
from datetime import datetime
from streamlit_option_menu import option_menu

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

st.set_page_config(
    page_title="ADA PROMAX IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# VARIABLES / ENDPOINTS
# =========================================================

MAKE_WEBHOOK = "https://hook.us2.make.com/9m7ly3yx7tbtn27ldm63jtg4ljcs52kj"

API_STATUS = "https://hook.us2.make.com/9m7ly3yx7tbtn27ldm63jtg4ljcs52kj"

# =========================================================
# CSS PREMIUM
# =========================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #050816;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#111827,#0B1120);
    border-right: 1px solid rgba(255,255,255,0.05);
}

.logo-title{
    font-size:24px;
    font-weight:700;
    color:white;
}

.logo-sub{
    font-size:13px;
    color:#9CA3AF;
}

.online-badge{
    display:flex;
    align-items:center;
    gap:10px;
    background:#111827;
    padding:12px;
    border-radius:12px;
    border:1px solid rgba(255,255,255,0.05);
}

.online-dot{
    width:12px;
    height:12px;
    background:#22c55e;
    border-radius:50%;
    box-shadow:0 0 10px #22c55e;
}

/* HERO */

.hero-card{
    background: linear-gradient(145deg,#0F172A,#111827);
    padding:35px;
    border-radius:24px;
    border:1px solid rgba(255,255,255,0.05);
}

.hero-title{
    font-size:52px;
    font-weight:800;
    color:white;
}

.hero-subtitle{
    font-size:22px;
    color:#d1d5db;
    margin-top:10px;
}

.hero-description{
    color:#9CA3AF;
    margin-top:15px;
    line-height:1.7;
}

/* FEATURE CARDS */

.feature-card{
    background:#111827;
    border-radius:20px;
    padding:25px;
    transition:0.3s;
    border:1px solid rgba(255,255,255,0.05);
    min-height:180px;
}

.feature-card:hover{
    transform:translateY(-5px);
    border:1px solid #6366F1;
    box-shadow:0 0 25px rgba(99,102,241,0.25);
}

.feature-title{
    font-size:22px;
    font-weight:700;
    margin-bottom:15px;
}

.feature-desc{
    color:#9CA3AF;
    line-height:1.7;
}

/* RIGHT PANEL */

.side-panel{
    background:#111827;
    padding:25px;
    border-radius:20px;
    margin-bottom:20px;
    border:1px solid rgba(255,255,255,0.05);
}

.side-title{
    font-size:20px;
    font-weight:700;
    margin-bottom:15px;
}

/* CHAT */

.user-message{
    background:#312E81;
    padding:16px;
    border-radius:18px;
    margin-bottom:12px;
}

.assistant-message{
    background:#111827;
    padding:16px;
    border-radius:18px;
    margin-bottom:12px;
}

/* KPI */

.kpi-card{
    background:#111827;
    border-radius:18px;
    padding:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.05);
}

.kpi-number{
    font-size:32px;
    font-weight:700;
}

.kpi-label{
    color:#9CA3AF;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "employee_id" not in st.session_state:
    st.session_state.employee_id = None

if "awaiting_id" not in st.session_state:
    st.session_state.awaiting_id = True

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = str(uuid.uuid4())

if "analytics" not in st.session_state:
    st.session_state.analytics = {
        "consultas": 0,
        "tiempo_total": 0,
        "errores": 0
    }

# =========================================================
# FUNCIONES
# =========================================================

def verificar_estado_ada():

    try:
        response = requests.get(API_STATUS, timeout=5)

        if response.status_code == 200:
            return True

        return False

    except:
        return False

def enviar_a_make(payload):

    start = time.time()

    try:

        response = requests.post(
            MAKE_WEBHOOK,
            json=payload,
            timeout=60
        )

        elapsed = round(time.time() - start, 2)

        st.session_state.analytics["consultas"] += 1
        st.session_state.analytics["tiempo_total"] += elapsed

        return response

    except Exception as e:

        st.session_state.analytics["errores"] += 1

        raise e

def generar_payload(prompt, modulo):

    return {
        "employee_id": st.session_state.employee_id,
        "message": prompt,
        "conversation_id": st.session_state.conversation_id,
        "timestamp": str(datetime.now()),
        "module": modulo,
        "history": st.session_state.messages[-10:]
    }

# =========================================================
# ESTADO ADA
# =========================================================

estado_online = verificar_estado_ada()

estado_texto = "En línea" if estado_online else "Desconectado"

estado_color = "#22c55e" if estado_online else "#ef4444"

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(f"""
    <div class="logo-title">ADA PROMAX IA</div>
    <div class="logo-sub">Asistente Inteligente RRHH</div>

    <br>

    <div class="online-badge">
        <div class="online-dot" style="background:{estado_color}; box-shadow:0 0 12px {estado_color};"></div>
        {estado_texto}
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

# =========================================================
# MAIN LAYOUT
# =========================================================

main_left, main_right = st.columns([4,1.3])

# =========================================================
# HERO
# =========================================================

with main_left:

    st.markdown('<div class="hero-card">', unsafe_allow_html=True)

    hero1, hero2 = st.columns([1,2])

    with hero1:
        st.image(
            "assets/Copilot_20260530_200709.png",
            width=250
        )

    with hero2:

        st.markdown("""
        <div class="hero-title">ADA PROMAX IA</div>
        <div class="hero-subtitle">
        Tu copiloto inteligente de Recursos Humanos
        </div>

        <div class="hero-description">
        Plataforma IA especializada en:
        <br><br>
        ✅ Compensaciones<br>
        ✅ Bandas salariales<br>
        ✅ Planes de carrera<br>
        ✅ Diagnóstico IA<br>
        ✅ Analítica avanzada RRHH
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# BOTONES FUNCIONALES
# =========================================================

st.markdown("## ⚡ Acciones Inteligentes")

b1, b2, b3 = st.columns(3)

with b1:

    if st.button("💰 Bandas Salariales", use_container_width=True):

        consulta = "Quiero consultar mi banda salarial"

        st.session_state.messages.append({
            "role":"user",
            "content":consulta
        })

with b2:

    if st.button("📈 Plan de Carrera", use_container_width=True):

        consulta = "Quiero conocer mi plan de carrera"

        st.session_state.messages.append({
            "role":"user",
            "content":consulta
        })

with b3:

    if st.button("🤖 Diagnóstico IA", use_container_width=True):

        consulta = "Quiero un diagnóstico inteligente"

        st.session_state.messages.append({
            "role":"user",
            "content":consulta
        })

# =========================================================
# KPIs REALES
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

k1,k2,k3 = st.columns(3)

consultas = st.session_state.analytics["consultas"]

errores = st.session_state.analytics["errores"]

if consultas > 0:
    promedio = round(
        st.session_state.analytics["tiempo_total"] / consultas,
        2
    )
else:
    promedio = 0

precision = 100

if consultas > 0:
    precision = round(
        ((consultas - errores) / consultas) * 100,
        1
    )

with k1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-number">{consultas}</div>
        <div class="kpi-label">Consultas reales</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-number">{precision}%</div>
        <div class="kpi-label">Precisión</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-number">{promedio}s</div>
        <div class="kpi-label">Tiempo promedio</div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# CHAT
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("## 💬 Conversación Inteligente")

for msg in st.session_state.messages:

    role_class = (
        "user-message"
        if msg["role"] == "user"
        else "assistant-message"
    )

    icon = (
        "👤"
        if msg["role"] == "user"
        else "🤖"
    )

    st.markdown(
        f"<div class='{role_class}'>{icon} {msg['content']}</div>",
        unsafe_allow_html=True
    )

# =========================================================
# MENSAJE INICIAL
# =========================================================

if len(st.session_state.messages) == 0:

    st.session_state.messages.append({
        "role":"assistant",
        "content":"""
👋 Hola, soy ADA PROMAX IA.

Para comenzar necesito tu código de empleado.

Ejemplo:
PE0000012
"""
    })

# =========================================================
# INPUT CHAT
# =========================================================

prompt = st.chat_input(
    "Escribe tu consulta para ADA..."
)

# =========================================================
# PROCESAMIENTO
# =========================================================

if prompt:

    st.session_state.messages.append({
        "role":"user",
        "content":prompt
    })

    # =====================================================
    # VALIDACIÓN EMPLOYEE ID
    # =====================================================

    if st.session_state.awaiting_id:

        if prompt.upper().startswith("PE"):

            st.session_state.employee_id = prompt.upper()

            st.session_state.awaiting_id = False

            with st.spinner("Validando colaborador..."):

                payload = {
                    "employee_id": st.session_state.employee_id,
                    "action":"validate_employee"
                }

                try:

                    response = enviar_a_make(payload)

                    result = response.json()

                    nombre = result.get("nombre","Colaborador")

                    puesto = result.get("puesto","No identificado")

                    area = result.get("area","No identificada")

                    bienvenida = f"""
✨ Bienvenido/a {nombre}

🏢 Área: {area}
💼 Puesto: {puesto}

Ya puedes consultar:

✅ Bandas salariales
✅ Plan de carrera
✅ Diagnóstico IA
✅ Beneficios
✅ Compensaciones
✅ Analítica RRHH
"""

                    st.session_state.messages.append({
                        "role":"assistant",
                        "content":bienvenida
                    })

                    st.rerun()

                except Exception as e:

                    st.error(f"Error conectando con Make: {e}")

        else:

            st.session_state.messages.append({
                "role":"assistant",
                "content":"Necesito un código válido. Ejemplo: PE0000012"
            })

            st.rerun()

    # =====================================================
    # CONSULTAS IA
    # =====================================================

    else:

        payload = generar_payload(prompt, selected)

        with st.spinner("ADA está analizando tu consulta..."):

            try:

                response = enviar_a_make(payload)

                if response.status_code == 200:

                    try:
                        result = response.json()

                        respuesta = result.get(
                            "response",
                            "No se recibió respuesta."
                        )

                    except:
                        respuesta = response.text

                else:

                    respuesta = f"""
❌ Error del servidor

Código:
{response.status_code}
"""

                # SEGURIDAD RRHH

                if (
                    "salario" in prompt.lower()
                    and "otro" in prompt.lower()
                ):

                    respuesta = """
🚫 Acceso restringido.

Por políticas de confidencialidad RRHH,
solo puedes consultar información propia.
"""

                st.session_state.messages.append({
                    "role":"assistant",
                    "content":respuesta
                })

                st.rerun()

            except Exception as e:

                st.session_state.messages.append({
                    "role":"assistant",
                    "content":f"""
❌ Error de conexión con ADA IA

Detalle:
{str(e)}
"""
                })

                st.rerun()

# =========================================================
# HISTORIAL
# =========================================================

if selected == "Historial":

    st.markdown("## 📜 Historial Conversacional")

    for i, msg in enumerate(st.session_state.messages):

        st.markdown(f"""
        **{i+1}. {msg['role'].upper()}**
        <br>
        {msg['content']}
        <br><br>
        """, unsafe_allow_html=True)

# =========================================================
# CONFIG
# =========================================================

if selected == "Configuración":

    st.markdown("## ⚙️ Configuración ADA")

    st.toggle("Modo IA Avanzado", value=True)

    st.toggle("Memoria Conversacional", value=True)

    st.toggle("Analítica RRHH", value=True)

    st.toggle("Logs Empresariales", value=True)
