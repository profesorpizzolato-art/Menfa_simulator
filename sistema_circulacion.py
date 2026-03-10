import streamlit as st

def sistema_circulacion():

    st.subheader("Sistema de Bombas")

    bombas = 3

    for i in range(1,bombas+1):

        st.write("Bomba",i)

        estado = st.selectbox(
        f"Estado bomba {i}",
        ["OFF","ON"]
        )

        if estado == "ON":

            spm = st.slider(f"SPM bomba {i}",0,200,110)

            presion = st.slider(
            f"Presión psi bomba {i}",
            0,5000,3000
            )

            st.metric("SPM",spm)
            st.metric("Presión",presion)
