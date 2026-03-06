import streamlit as st
import requests

# 1. Pegá acá el link RAW de tu portal_cliente.py en el repo privado
URL_PRIVADA = "https://raw.githubusercontent.com/Gdicampli22/soporteerpia/refs/heads/main/app/portal_cliente.py?token=GHSAT0AAAAAADWY2ETHQUK7DD4XKXXQ5KXU2NLC7BQ"

try:
    github_token = st.secrets["GITHUB_TOKEN"]
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3.raw"
    }
    respuesta = requests.get(URL_PRIVADA, headers=headers)
    
    if respuesta.status_code == 200:
        # Ejecuta el portal en memoria
        exec(respuesta.text)
    else:
        st.error("⚠️ Acceso denegado a la bóveda privada. Revisá el Token o la URL.")
        st.stop()
except Exception as e:
    st.error(f"⚠️ Error de conexión: {e}")
    st.stop()