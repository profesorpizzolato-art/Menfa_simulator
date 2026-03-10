import streamlit as st

from modulos.panel_cabina import panel_cabina
from modulos.torque_drag_avanzado import torque_drag
from modulos.sistema_circulacion import sistema_circulacion
from modulos.geonavegacion import geonavegacion
from modulos.control_pozos import control_pozos
from modulos.deteccion_kick import deteccion_kick
from modulos.graficas_tiempo_real import graficas_rt

from evaluacion.examen import modulo_examen

st.set_page_config(page_title="Simulador MENFA",layout="wide")

st.title("Centro de Entrenamiento MENFA - Simulador de Perforación")

menu = st.sidebar.selectbox(
"Menú del simulador",
[
"Cabina del Perforador",
"Torque y Drag",
"Sistema de Circulación",
"Geonavegación",
"Control de Pozos",
"Detección de Kick",
"Gráficas en Tiempo Real",
"Evaluación MENFA"
]
)

if menu == "Cabina del Perforador":
    panel_cabina()

if menu == "Torque y Drag":
    torque_drag()

if menu == "Sistema de Circulación":
    sistema_circulacion()

if menu == "Geonavegación":
    geonavegacion()

if menu == "Control de Pozos":
    control_pozos()

if menu == "Detección de Kick":
    deteccion_kick()

if menu == "Gráficas en Tiempo Real":
    graficas_rt()

if menu == "Evaluación MENFA":
    modulo_examen()
