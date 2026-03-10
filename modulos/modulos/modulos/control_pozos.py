import streamlit as st

def control_pozos():

    st.subheader("Control de pozos")

    pit_gain = st.slider("Pit gain bbl",0,50,3)

    flow_out = st.slider("Flow out %",0,150,100)

    spp = st.slider("SPP psi",0,5000,3200)

    if pit_gain > 10:

        st.error("Posible ingreso de formación")

    if flow_out > 110:

        st.error("Flujo anormal")
