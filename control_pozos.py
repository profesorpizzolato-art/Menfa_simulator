import streamlit as st

def control_pozos():

    st.subheader("Monitoreo de Control de Pozos")

    pit_gain = st.slider("Ganancia de piletas bbl",0,50,3)

    flow_out = st.slider("Flow Out %",0,150,100)

    presion = st.slider("SPP psi",0,5000,3200)

    if pit_gain > 10:
        st.error("Alerta: posible ingreso de formación")

    if flow_out > 110:
        st.error("Flujo anormal detectado")
