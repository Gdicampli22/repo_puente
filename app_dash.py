import streamlit as st
import requests

# 1. Acá pegás la URL RAW de tu archivo app.py que está en el repo PRIVADO
URL_PRIVADA = "https://raw.githubusercontent.com/Gdicampli22/soporteerpia/refs/heads/main/app/dashboard_v2.py?token=GHSAT0AAAAAADWY2ETHQFAVPSIVSRR4YFWC2NKDOZQ"

try:
    # 2. Llamamos al token secreto que configuraremos en la nube
    github_token = st.secrets["GITHUB_TOKEN"]
    
    # 3. Nos hacemos pasar por vos para abrir la bóveda
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3.raw"
    }
    
    # 4. Descargamos el código en memoria (no se guarda en ningún archivo visible)
    respuesta = requests.get(URL_PRIVADA, headers=headers)
    
    if respuesta.status_code == 200:
        # 5. Ejecutamos tu Nexus OS directamente desde la memoria
        codigo_secreto = respuesta.text
        exec(codigo_secreto)
    else:
        st.error("⚠️ Acceso denegado a la bóveda privada. Revisá el Token o la URL.")
        st.stop()

except Exception as e:
    st.error(f"⚠️ Error detallado para Gastón: {e}")
    st.stop()