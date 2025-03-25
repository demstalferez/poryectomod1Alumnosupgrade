import streamlit as st

def show_deliverables():
    st.markdown('<h1 class="section-title">📅 Entregables</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
        <p>Para el <span class="date-highlight">1 de abril de 2025</span>, necesitas:</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="subsection-title">1. Repositorio de GitHub</h2>', unsafe_allow_html=True)
    st.markdown("""
    Un repositorio de GitHub con:
    
    - **Portada**: Un archivo README.md con el nombre del proyecto, tu nombre, un resumen corto y el logo de Upgrade Hub (si lo tienes).
    
    - **Código**: Un notebook o archivos de Python bien organizados, con comentarios que expliquen qué haces.
    
    - **Datos limpios**: El archivo marketing_campaigns_clean.csv con todo arreglado y net_profit.
    
    - **Informe**: Un apartado (en el notebook o un archivo .md) con:
      - Cuántas filas quitaste (repetidas o raras).
      - Respuestas a las 7 preguntas, con al menos 3 gráficos.
    
    - **Organización**: Usa carpetas como /data, /code, /docs si quieres.
    """)
    
    st.markdown('<h2 class="subsection-title">2. Presentación de 10 Minutos</h2>', unsafe_allow_html=True)
    st.markdown("""
    Una charla de 10 minutos lista para presentar lo que hiciste y sorprender al equipo de Upgrade Hub:
    
    - Explica rápido cómo estaba el dataset y qué hiciste para limpiarlo.
    - Muestra tus respuestas a las 7 preguntas, usando los gráficos para que se entienda.
    - Termina con una idea para el cliente basada en lo que encontraste (ej. qué canal usar más).
    - Practica para que te salga clara y no pases de los 10 minutos.
    """)
    
    st.markdown("""
    <div style="background-color: white; color: black;">
      <h3>¡Tú Puedes con Esto!</h3>
      <p>El 1 de abril de 2025, vas a enseñar lo que lograste con este dataset. No es solo limpiar números: es demostrar que puedes tomar algo desordenado y convertirlo en respuestas útiles. Tu repositorio y tu presentación van a mostrar que estás listo para ser parte del equipo de Upgrade Hub. ¡Dale caña y haz que todos digan "guau" con tu trabajo!</p>
    </div>
    """, unsafe_allow_html=True)