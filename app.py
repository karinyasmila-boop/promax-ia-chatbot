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
# CARGA DE ESTILOS (CSS)
# =====================================================
with open("styles/main.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =====================================================
# ESTADO DE SESIÓN
# =====================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:

    st.markdown("""
    <div class="logo-title">ADA PROMAX IA</div>
    <div class="logo-sub">Asistente Inteligente RRHH</div>
    <br>
    <div class="online-badge">
        <div class="online-dot"></div> En línea
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
# LAYOUT PRINCIPAL
# =====================================================
main_left, main_right = st.columns([4, 1.3])

# =====================================================
# HERO SECTION
# =====================================================
with main_left:

    st.markdown('<div class="hero-card">', unsafe_allow_html=True)

    hero_left, hero_right = st.columns([1, 2])

    # Imagen del robot
    with hero_left:
        st.image("assets/Copilot_20260530_200709.png", width=240)

    # Textos del hero
    with hero_right:
        st.markdown("""
        <div class="hero-label">AI Powered HR Intelligence</div>
        <div class="hero-title"><span>ADA PROMAX IA</span></div>
        <div class="hero-subtitle">Tu copiloto inteligente de Recursos Humanos</div>
        <div class="hero-description">
            Plataforma IA especializada en compensaciones,
            bandas salariales, planes de carrera y analítica estratégica del talento.
        </div>
        <div class="message-box">
            Pregúntame sobre compensaciones, carrera o RRHH...
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # =================================================
    # SUGERENCIAS RÁPIDAS
    # =================================================
    st.markdown("<h2 class='section-title'>⚡ Sugerencias rápidas</h2>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">💰 Bandas Salariales</div>
            <div class="feature-desc">Información sobre estructura salarial y compensaciones.</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">📈 Plan de Carrera</div>
            <div class="feature-desc">Rutas de crecimiento y desarrollo profesional.</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🤖 Diagnóstico IA</div>
            <div class="feature-desc">Análisis inteligente de compensaciones.</div>
        </div>
        """, unsafe_allow_html=True)

# =====================================================
# PANEL DERECHO
# =====================================================
with main_right:

    st.markdown("""
    <div class="side-panel">
        <div class="side-title">Capacidades ADA IA</div>
        <div class="side-item">📊 Análisis inteligente de datos</div>
        <div class="side-item">🎯 Recomendaciones personalizadas</div>
        <div class="side-item">🌐 Información actualizada</div>
        <div class="side-item">🛟 Soporte 24/7</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="side-panel">
        <div class="side-title">Estadísticas</div>
        <div class="side-item">📈 Consultas: 12,840</div>
        <div class="side-item">🎯 Precisión: 98%</div>
        <div class="side-item">⚡ Tiempo promedio: 1.2s</div>
        <div class="side-item">😊 Satisfacción: 99%</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# CHAT CON FLUJO PERSONALIZADO
# =====================================================
st.markdown("<br><h2 class='section-title'>💬 Conversación Inteligente</h2>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    role_class = "user-message" if msg["role"] == "user" else "assistant-message"
    icon = "👤" if msg["role"] == "user" else "🤖"
    st.markdown(f"<div class='{role_class}'>{icon} {msg['content']}</div>", unsafe_allow_html=True)

prompt = st.chat_input("Escribe tu consulta para ADA...")

# =====================================================
# LÓGICA DE CONVERSACIÓN
# =====================================================
if "employee_id" not in st.session_state:
    st.session_state.employee_id = None
    st.session_state.awaiting_id = True
    st.session_state.messages.append({
        "role": "assistant",
        "content": "👋 ¡Hola! Soy **ADA PROMAX IA**, tu asistente de Recursos Humanos. Por favor, indícame tu **código de empleado** (por ejemplo: PE0000012) para comenzar."
    })

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Si ADA espera el código
    if st.session_state.awaiting_id:
        if prompt.strip().upper().startswith("PE"):
            st.session_state.employee_id = prompt.strip().upper()
            st.session_state.awaiting_id = False
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"Perfecto 👋, tu código de empleado es **{st.session_state.employee_id}**. Estoy consultando tu información..."
            })

            webhook_url = "https://hook.us2.make.com/9m7ly3yx7tbtn27ldm63jtg4ljcs52kj"
            payload = {"employee_id": st.session_state.employee_id}

            with st.spinner("Buscando datos del empleado..."):
                try:
                    response = requests.post(webhook_url, json=payload)
                    result = response.json()  # Make debe devolver JSON estructurado

                    if not result or "nombre" not in result:
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": (
                                "😕 No he podido identificar al colaborador con el código proporcionado. "
                                "Por favor, verifica tu identificador y vuelve a intentarlo. "
                                "Si necesitas orientación, puedo ayudarte con temas como:\n\n"
                                "1️⃣ **Bandas Salariales y Compensación**\n"
                                "2️⃣ **Plan de Carrera y Desarrollo**\n"
                                "3️⃣ **Diagnóstico Inteligente de Compensación**"
                            )
                        })
                    else:
                        nombre = result.get("nombre")
                        puesto = result.get("puesto")
                        area = result.get("area")
                        salario = result.get("salario")
                        experiencia = result.get("experiencia")
                        competencias = result.get("competencias")

                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": (
                                f"✨ ¡Encantada de conocerte, **{nombre}**! Actualmente ocupas el puesto de **{puesto}** "
                                f"en el área de **{area}**. Con base en tu perfil y experiencia, puedo ayudarte con:\n\n"
                                "1️⃣ **Bandas Salariales y Compensación** — para conocer tu rango salarial y oportunidades de ajuste.\n"
                                "2️⃣ **Plan de Carrera y Desarrollo** — para explorar tus rutas de crecimiento profesional.\n"
                                "3️⃣ **Diagnóstico Inteligente de Compensación** — para analizar tu desempeño y proyección.\n\n"
                                "¿Sobre cuál tema te gustaría que te ayude hoy?"
                            )
                        })
                    st.rerun()

                except Exception as e:
                    st.error(f"Error: {str(e)}")

        else:
            st.session_state.messages.append({
                "role": "assistant",
                "content": (
                    "😊 Gracias por tu saludo. Para comenzar, necesito tu **código de empleado** "
                    "(por ejemplo: PE0000012). Una vez lo ingreses, podré mostrarte tu información personalizada."
                )
            })
            st.rerun()

    else:
        # Si ya tiene employee_id, continuar con consultas normales
        webhook_url = "https://hook.us2.make.com/9m7ly3yx7tbtn27ldm63jtg4ljcs52kj"
        payload = {"employee_id": st.session_state.employee_id, "text": prompt}

        with st.spinner("ADA está analizando..."):
            try:
                response = requests.post(webhook_url, json=payload)
                result = response.text

                # Validación de seguridad para salario
                if "salario" in prompt.lower() and "otro" in prompt.lower():
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": (
                            "🚫 Por motivos de confidencialidad, no puedo mostrar información salarial de otros puestos o colaboradores. "
                            "Solo puedo ofrecerte datos relacionados con tu propio rol o área."
                        )
                    })
                else:
                    st.session_state.messages.append({"role": "assistant", "content": result})
                st.rerun()

            except Exception as e:
                st.error(f"Error: {str(e)}")
