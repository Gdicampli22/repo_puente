import streamlit as st

# 1. Configuración de la página (Debe ser la primera línea)
st.set_page_config(
    page_title="Portfolio | Gastón Di Campli",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Lógica del Botón de Tema (Claro / Oscuro)
if 'tema' not in st.session_state:
    st.session_state.tema = 'oscuro'

def cambiar_tema():
    if st.session_state.tema == 'claro':
        st.session_state.tema = 'oscuro'
    else:
        st.session_state.tema = 'claro'

# Definimos las paletas de colores según el tema elegido
if st.session_state.tema == 'claro':
    bg_app = "#ffffff"
    text_main = "#333333"
    text_muted = "#666666"
    bg_card = "#ffffff"
    bg_secondary = "#f8f9fa"
    border_color = "#e0e0e0"
    accent_color = "#2e86c1"
    btn_label = "🌙 Modo Oscuro"
else:
    bg_app = "#0e1117"
    text_main = "#fafafa"
    text_muted = "#a0a0a0"
    bg_card = "#1e1e27"
    bg_secondary = "#12141b"
    border_color = "#333333"
    accent_color = "#4eb3f0"
    btn_label = "☀️ Modo Claro"

# 3. Inyección de CSS Dinámico
# Usamos un f-string para inyectar nuestras variables de color de Python directamente al CSS
st.markdown(f"""
<style>
    /* Ocultar el menú superior y footer por defecto de Streamlit */
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}

    /* Forzar el color de fondo de toda la aplicación */
    .stApp {{
        background-color: {bg_app};
    }}

    /* Estilos del Encabezado (Hero) */
    .hero-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 1rem 1rem 4rem 1rem;
        animation: fadeIn 1.5s ease-in-out;
    }}
    .hero-title {{
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        background: -webkit-linear-gradient(45deg, {accent_color}, #8e44ad);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .hero-subtitle {{
        font-size: 1.5rem;
        color: {text_main};
        font-weight: 500;
        margin-bottom: 1.5rem;
    }}
    .hero-text {{
        font-size: 1.1rem;
        color: {text_muted};
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.8;
        text-align: center;
    }}

    /* Separador personalizado */
    .custom-divider {{
        height: 1px;
        background-color: {border_color};
        margin: 2rem 0;
        border: none;
    }}

    /* Estilos de las Tarjetas de Proyectos (Cards) */
    .card-grid {{
        display: flex;
        gap: 2rem;
        justify-content: center;
        flex-wrap: wrap;
        padding: 1rem;
    }}
    .project-card {{
        background-color: {bg_card};
        border-radius: 15px;
        padding: 2.5rem 2rem;
        width: 100%;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
        border: 1px solid {border_color};
        text-decoration: none;
        display: block;
        color: {text_main} !important;
        cursor: pointer;
    }}
    .project-card:hover {{
        transform: translateY(-12px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.2);
        border-color: {accent_color};
    }}
    .card-icon {{
        font-size: 3rem;
        margin-bottom: 1.5rem;
    }}
    .card-title {{
        font-size: 1.6rem;
        font-weight: 700;
        color: {text_main};
        margin-bottom: 0.8rem;
    }}
    .card-desc {{
        color: {text_muted};
        font-size: 1rem;
        margin-bottom: 2rem;
        line-height: 1.6;
    }}
    .card-button {{
        display: inline-block;
        padding: 0.7rem 1.4rem;
        background-color: {bg_secondary};
        color: {accent_color};
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.95rem;
        border: 1px solid {border_color};
        transition: all 0.2s ease;
    }}
    .project-card:hover .card-button {{
        background-color: {accent_color};
        color: white;
        border-color: {accent_color};
    }}
    
    /* Estilos para la sección de Tecnologías */
    .skills-section {{
        margin-top: 5rem;
        padding: 4rem 1rem;
        background-color: {bg_secondary};
        border-radius: 15px;
        text-align: center;
    }}
    .skills-title {{
        color: {text_main};
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }}
    .skills-subtitle {{
        color: {text_muted};
        font-size: 1.1rem;
        margin-bottom: 3rem;
    }}
    .skills-container {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1rem;
        max-width: 900px;
        margin: 0 auto;
    }}
    .skill-badge {{
        background-color: {bg_card};
        color: {accent_color};
        padding: 0.7rem 1.6rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.95rem;
        border: 1px solid {border_color};
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }}
    .skill-badge:hover {{
        background-color: {accent_color};
        color: white;
        border-color: {accent_color};
        transform: translateY(-4px);
        box-shadow: 0 6px 14px rgba(0,0,0,0.2);
    }}
    
    /* Animación de entrada */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
</style>
""", unsafe_allow_html=True)

# 4. Botón superior para cambiar el tema
col_vacia, col_boton = st.columns([8, 1])
with col_boton:
    st.button(btn_label, on_click=cambiar_tema)

# 5. Sección Hero
st.markdown(f"""
<div class="hero-container">
<h1 class="hero-title">Gastón Di Campli</h1>
<h2 class="hero-subtitle">Especialista Funcional de Soporte ERP</h2>
<p class="hero-text">Optimizando procesos y resolviendo desafíos operativos mediante automatizaciones ágiles y soluciones impulsadas por Inteligencia Artificial. Explora el ecosistema Nexus a continuación.</p>
</div>
<hr class="custom-divider">
""", unsafe_allow_html=True)

# 6. Sección de Proyectos
st.markdown(f"<h3 style='text-align: center; color: {text_main}; margin-top: 2rem; margin-bottom: 3rem; font-size: 2rem; font-weight: 700;'>Ecosistema Nexus</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<a href="https://nexusos.streamlit.app/" target="_blank" class="project-card">
<div class="card-icon">🧠</div>
<div class="card-title">Nexus OS</div>
<div class="card-desc">Consultoría Funcional potenciada por Inteligencia Artificial. Análisis y estrategia de implementación.</div>
<div class="card-button">Acceder al Sistema →</div>
</a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
<a href="https://nexuscli.streamlit.app/" target="_blank" class="project-card">
<div class="card-icon">⚙️</div>
<div class="card-title">Nexus ERP</div>
<div class="card-desc">Dashboard integral para la gestión de soporte funcional. Monitoreo de procesos, seguimiento de métricas y resolución ágil de incidencias."</div>
<div class="card-button">Acceder al Panel →</div>
</a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
<a href="https://nexuscli.streamlit.app/" target="_blank" class="project-card">
<div class="card-icon">🏢</div>
<div class="card-title">Portal Clientes</div>
<div class="card-desc">Autogestión de soporte del ecosistema Nexus ERP. Resolución rápida y seguimiento de tickets.</div>
<div class="card-button">Área de Clientes →</div>
</a>
    """, unsafe_allow_html=True)

# 7. Sección de Tecnologías 
st.markdown("""
<div class="skills-section">
<h3 class="skills-title">Stack Tecnológico</h3>
<p class="skills-subtitle">Herramientas que utilizo para desarrollar, automatizar y desplegar soluciones.</p>
<div class="skills-container">
<div class="skill-badge">Soporte Funcional ERP</div>
<div class="skill-badge">Python (Automatizaciones con IA)</div>
<div class="skill-badge">Streamlit</div>
<div class="skill-badge">Supabase</div>
<div class="skill-badge">n8n</div>
<div class="skill-badge">Google Gemini (AI Studio)</div>
<div class="skill-badge">Docker</div>
<div class="skill-badge">Railway</div>
</div>
</div>
""", unsafe_allow_html=True)

# 8. Footer
st.markdown(f"""
<div style="text-align: center; margin-top: 6rem; padding: 3rem 2rem; color: {text_muted}; border-top: 1px solid {border_color}; background-color: {bg_card}; border-radius: 15px;">
<p style="font-size: 1rem; margin-bottom: 0.5rem;">© 2026 Gastón Di Campli. Todos los derechos reservados.</p>
<p style="font-size: 0.9rem;">Desarrollado profesionalmente con Python y Streamlit.</p>
</div>
""", unsafe_allow_html=True)