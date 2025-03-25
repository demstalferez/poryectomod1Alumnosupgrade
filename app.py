import streamlit as st
from datetime import datetime

# Importaciones correctamente ajustadas
from sections.home import show_home
from sections.description import show_description
from sections.dataset import show_dataset
from sections.tasks import show_tasks
from sections.deliverables import show_deliverables
from sections.faq import show_faq

# Configuración de la página
st.set_page_config(
    page_title="Desafío de Marketing - Upgrade Hub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-title { font-size: 2.8rem; font-weight: 700; color: #FF5A5F; margin-bottom: 0.5rem; text-align: center; }
    .subtitle { font-size: 1.4rem; font-weight: 500; color: #484848; margin-bottom: 2rem; text-align: center; }
    .section-title { font-size: 1.8rem; font-weight: 600; color: #FF5A5F; margin: 1.5rem 0 1rem 0; padding-bottom: 0.5rem; border-bottom: 2px solid #FF5A5F; }
    .subsection-title { font-size: 1.3rem; font-weight: 600; color: #484848; margin: 1rem 0; }
    .highlight { background-color: #f9f9f9; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #FF5A5F; margin: 1rem 0; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    .date-highlight { font-weight: 700; color: #FF5A5F; }
    .step-container { background-color: #f9f9f9; padding: 1rem; border-radius: 10px; margin-bottom: 1rem; border-left: 3px solid #FF5A5F; }
    .badge { background-color: #FF5A5F; color: white; padding: 0.2rem 0.5rem; border-radius: 5px; margin-right: 0.5rem; font-size: 0.8rem; }
    .btn-primary { background-color: #FF5A5F; color: white; padding: 0.5rem 1rem; border-radius: 5px; text-decoration: none; font-weight: 600; display: inline-block; }
    .btn-primary:hover { background-color: #e04e53; }
    .sidebar .sidebar-content { background-color: #f5f5f5; }
    
    /* Mejoras visuales adicionales */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f0f0;
        border-radius: 5px 5px 0 0;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FF5A5F;
        color: white;
    }
    
    /* Timeline */
    .timeline-container {
        position: relative;
        padding-left: 50px;
        margin-bottom: 50px;
    }
    .timeline-container::before {
        content: '';
        position: absolute;
        left: 15px;
        top: 0;
        height: 100%;
        width: 4px;
        background: #FF5A5F;
    }
    .timeline-item {
        position: relative;
        margin-bottom: 30px;
    }
    .timeline-dot {
        position: absolute;
        left: -50px;
        top: 0;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background: #FF5A5F;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
    }
    .timeline-content {
        background: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.1);
    }
    
    /* Tarjetas de características */
    .feature-card {
        background-color: white;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        height: 100%;
        border-top: 4px solid #FF5A5F;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    .feature-icon {
        font-size: 2.5rem;
        color: #FF5A5F;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Barra lateral
with st.sidebar:
    # Logo y título
    try:
        st.image("img/logo.svg", width=200)  # Intenta cargar el logo si existe
    except:
        st.markdown("### 📊 Upgrade Hub", unsafe_allow_html=True)  # Fallback si no hay logo
        
    st.markdown("### 📊 Desafío de Marketing", unsafe_allow_html=True)
    st.markdown("---")
    
    # Menú de navegación
    menu = st.radio(
        "",
        ["🏠 Inicio", "📋 Descripción", "📊 Dataset", "📝 Tareas", "📅 Entregables", "❓ FAQ"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Contador de días hasta la fecha límite
    deadline = datetime(2025, 4, 1)
    today = datetime.now()
    days_remaining = (deadline - today).days
    st.markdown(f"""
    <div style="background-color:#FF5A5F; padding:1.2rem; border-radius:10px; color:white; text-align:center;">
        <h3 style="margin:0; padding:0; font-size:1.2rem;">Tiempo restante</h3>
        <h2 style="margin:0.5rem 0; padding:0; font-size:2rem;">{days_remaining} días</h2>
        <p style="margin:0;">Fecha límite: 1 de abril de 2025</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Recursos y soporte
    with st.expander("📚 Recursos"):
        st.markdown("""
        - [Documentación de Pandas](https://pandas.pydata.org/docs/)
        - [Guía de Plotly](https://plotly.com/python/)
        - [Tutorial de GitHub](https://docs.github.com/es)
        - [Curso de Limpieza de Datos](https://www.kaggle.com/learn/data-cleaning)
        - [Visualización de Datos](https://www.kaggle.com/learn/data-visualization)
        """)
        
    with st.expander("📧 Soporte"):
        st.markdown("""
        - Email: demetrio.esteban@bootcamp-upgrade.com  
        - Tutorías: Agenda con tu mentor o si no quieres esperar, participa en las sesiones de clase
        """)
    
    # Pie de página de sidebar
    st.markdown("""
    <div style='position: fixed; bottom: 0; left: 0; padding: 1rem; width: 17%; text-align: center; font-size: 0.8rem; color: #888;'>
        © 2025 Upgrade Hub<br>Todos los derechos reservados
    </div>
    """, unsafe_allow_html=True)

# Renderizar secciones según la selección del menú
if menu == "🏠 Inicio":
    show_home()
elif menu == "📋 Descripción":
    show_description()
elif menu == "📊 Dataset":
    show_dataset()
elif menu == "📝 Tareas":
    show_tasks()
elif menu == "📅 Entregables":
    show_deliverables()
elif menu == "❓ FAQ":
    show_faq()

# Footer principal
st.markdown("""
<div class="footer" style="margin-top:3rem; text-align:center; color:#484848; padding-bottom:20px;">
    <p>© 2025 Upgrade Hub. Todos los derechos reservados.</p>
    <p>Diseñado para el Bootcamp de Data Analytics</p>
</div>
""", unsafe_allow_html=True)