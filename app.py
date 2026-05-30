import streamlit as st

st.title("PROMAX IA Compensaciones")

employee_id = st.text_input("Ingresa tu código de empleado")

consulta = st.selectbox(
    "¿Qué deseas consultar?",
    [
        "Bandas salariales",
        "Plan de carrera",
        "Diagnóstico"
    ]
)

pregunta = st.text_area("Describe tu consulta")

if st.button("Consultar"):
    st.success("Consulta enviada correctamente")

    st.write("Empleado:", employee_id)
    st.write("Opción:", consulta)
    st.write("Consulta:", pregunta)

    respuesta = f"""
    Hola. Tu consulta sobre {consulta} fue registrada correctamente.

    Próximamente el sistema responderá con información personalizada.
    """

    st.info(respuesta)
