import streamlit as st

st.set_page_config(page_title="Caso Plastiflex", page_icon="⚖️", layout="centered")

# Estado inicial
if "monto_prestamo" not in st.session_state:
    st.session_state.monto_prestamo = 90000
    st.session_state.deuda_pendiente = True
    st.session_state.cobro_extrajudicial_intentos = 0
    st.session_state.reputacion = 80
    st.session_state.gastos_legales = 0
    st.session_state.recuperado = 0
    st.session_state.terminado = False
    st.session_state.pagado_parcial = False

bienes = [
    "USD 20,000 en el Banco del Pichincha",
    "Marca de fábrica registrada",
    "Nombre comercial registrado en el SENADI"
]

# Título
st.title("⚖️ Caso Plastiflex - Asistente Legal Interactivo")
st.write("La empresa Plastiflex Cía. Ltda. prestó USD 90,000 a Bonilla Asociados, respaldado con una letra de cambio. No se pagó al vencimiento.")
st.write("Puedes consultar estado, negociar, ofrecer pago parcial, demandar, ejecutar letra, preguntar por bienes, preguntar ubicación de oficinas, preguntar estado de la empresa o abandonar.")

# Entrada de usuario
user_input = st.text_input("👤 Tú:", "")

if user_input:
    mensaje = user_input.lower()

    if "estado" in mensaje and "empresa" in mensaje:
        st.markdown("🤖 **Asistente:** La empresa deudora se encuentra en proceso de liquidación.")
    elif "estado" in mensaje or "ver" in mensaje or "consultar" in mensaje:
        st.markdown(
            f"🤖 **Asistente:**\n"
            f"- Monto adeudado: ${st.session_state.monto_prestamo}\n"
            f"- Intentos de cobro extrajudicial: {st.session_state.cobro_extrajudicial_intentos}\n"
            f"- Reputación: {st.session_state.reputacion}/100\n"
            f"- Gastos legales acumulados: ${st.session_state.gastos_legales}\n"
            f"- Monto recuperado: ${st.session_state.recuperado}\n"
            f"- ¿Deuda pendiente?: {'Sí' if st.session_state.deuda_pendiente else 'No'}"
        )
    elif "bienes" in mensaje:
        st.markdown("🤖 **Asistente:** La empresa Bonilla Asociados tiene los siguientes bienes:")
        for bien in bienes:
            st.markdown(f"- {bien}")
    elif "ubicación" in mensaje or ("dónde" in mensaje and "oficina" in mensaje):
        st.markdown("🤖 **Asistente:** Las oficinas están ubicadas en la República del Salvador y Moscú, en Quito.")
    elif "negociar" in mensaje or "extrajudicial" in mensaje:
        st.session_state.cobro_extrajudicial_intentos += 1
        if st.session_state.cobro_extrajudicial_intentos < 3:
            st.markdown("🤖 **Asistente:** Se intenta negociar de nuevo, pero Bonilla Asociados sigue sin pagar. Puedes seguir insistiendo, ofrecer pago parcial o pasar a vía legal.")
        else:
            st.markdown("🤖 **Asistente:** Después de varios intentos fallidos, se recomienda considerar acciones legales.")
    elif "ofrecer" in mensaje and "parcial" in mensaje:
        st.session_state.recuperado = st.session_state.monto_prestamo * 0.10
        st.session_state.deuda_pendiente = False
        st.session_state.pagado_parcial = True
        st.markdown(f"🤖 **Asistente:** El deudor acepta pagar solo el 10% (${st.session_state.recuperado}) porque no tiene dinero.")
    elif "ejecutar" in mensaje or "letra" in mensaje:
        st.session_state.gastos_legales += 5000
        st.session_state.recuperado = st.session_state.monto_prestamo * 0.8
        st.session_state.reputacion -= 10
        st.session_state.deuda_pendiente = False
        st.markdown(f"🤖 **Asistente:** Se ejecutó la letra de cambio. Se recuperó el 80% (${st.session_state.recuperado}). La reputación empresarial baja un poco por el litigio.")
    elif "demandar" in mensaje or "juicio" in mensaje:
        st.session_state.gastos_legales += 10000
        st.session_state.recuperado = st.session_state.monto_prestamo * 0.9
        st.session_state.reputacion -= 15
        st.session_state.deuda_pendiente = False
        st.markdown(f"🤖 **Asistente:** Se demandó judicialmente y se recuperó el 90% (${st.session_state.recuperado}). Gastos legales suben y la reputación disminuye.")
    elif "abandonar" in mensaje or "salir" in mensaje:
        st.session_state.reputacion -= 5
        st.session_state.deuda_pendiente = True
        st.session_state.terminado = True
        st.markdown("🤖 **Asistente:** Has decidido abandonar el cobro. La reputación empresarial se afecta ligeramente por no recuperar el dinero.")
    elif "terminar" in mensaje or "finalizar" in mensaje:
        if not st.session_state.deuda_pendiente:
            st.markdown(
                f"🎉 **Asistente:** Caso concluido exitosamente.\n"
                f"- Saldo recuperado: ${st.session_state.recuperado}\n"
                f"- Gastos legales: ${st.session_state.gastos_legales}\n"
                f"- Reputación final: {st.session_state.reputacion}/100"
            )
            st.session_state.terminado = True
        else:
            st.markdown("🤖 **Asistente:** Aún no se ha recuperado la deuda. Considera ejecutar, demandar, ofrecer pago parcial o abandonar.")
    else:
        st.markdown("🤖 **Asistente:** No entendí tu mensaje. Puedes decirme: 'consultar estado', 'estado de la empresa', 'negociar', 'ofrecer pago parcial', 'ejecutar letra', 'demandar', 'bienes', 'dónde están las oficinas', 'abandonar' o 'terminar'.")
