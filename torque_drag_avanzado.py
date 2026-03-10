import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def torque_drag():

    st.subheader("Modelo Torque y Drag")

    md = st.slider("Profundidad ft",1000,20000,9000)

    friccion = st.slider("Coeficiente fricción",0.1,0.45,0.25)

    peso = st.slider("Peso sarta klb",20,200,100)

    torque = peso * friccion * md/120

    st.metric("Torque estimado",int(torque))

    profundidad = np.linspace(0,md,100)
    torque_modelo = profundidad * friccion

    fig,ax = plt.subplots()

    ax.plot(profundidad,torque_modelo)

    ax.set_xlabel("Profundidad")
    ax.set_ylabel("Torque relativo")

    st.pyplot(fig)

    if torque > 25000:
        st.error("ALERTA: posible pega diferencial")
