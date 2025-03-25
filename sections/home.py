import streamlit as st

def show_home():
    st.markdown('<h1 class="main-title">🚀 ¡Tu Primer Desafío en Upgrade Hub!</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="subtitle">Análisis de Campañas de Marketing: </h2>', unsafe_allow_html=True)
    

    
    # Introducción con mejor diseño
    st.markdown("""
    <div style="background-color:#f0f0f0; padding:1.5rem; border-radius:10px; border-left:5px solid #FF5A5F; margin:1rem 0; box-shadow:0 2px 5px rgba(0,0,0,0.1);">
        <h3 style="color:#333; margin-bottom:1rem;">Bienvenido a tu primer reto como Analista de Datos</h3>
        <p style="color:#333;">Una multinacional tecnológica nos ha proporcionado un dataset sobre sus campañas de marketing de los últimos dos años. Tu misión es <strong>limpiar, analizar y extraer insights valiosos</strong> para guiar sus futuras estrategias.</p>
        <div style="display:flex; flex-wrap:wrap; margin-top:1rem;">
            <div style="background-color:#fff; padding:0.5rem 1rem; border-radius:5px; margin-right:1rem; margin-bottom:0.5rem; display:inline-block;">
                <span style="color:#333; font-weight:600;">Dataset:</span> 
                <code style="background-color:#eee; padding:0.1rem 0.3rem; border-radius:3px; color:#333;">marketingcampaigns.csv</code>
            </div>
            <div style="background-color:#fff; padding:0.5rem 1rem; border-radius:5px; display:inline-block;">
                <span style="color:#333; font-weight:600;">Fecha de entrega:</span> 
                <span style="color:#FF5A5F; font-weight:700;">1 de abril de 2025</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Vistazo rápido al desafío
    st.markdown('<h2 style="font-size:1.8rem; font-weight:600; color:#FF5A5F; margin:1.5rem 0 1rem 0; padding-bottom:0.5rem; border-bottom:2px solid #FF5A5F;">¿En qué consiste?</h2>', unsafe_allow_html=True)
    

    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background-color:#f0f0f0; padding:1.2rem; border-radius:10px; height:100%; border-top:3px solid #FF5A5F;">
            <div style="font-size:2.2rem; text-align:center; margin-bottom:0.8rem;">🧹</div>
            <h3 style="color:#333; text-align:center; font-size:1.3rem; margin-bottom:0.8rem;">Limpia</h3>
            <p style="color:#555; text-align:center;">Transforma un dataset desordenado con problemas de fechas, valores faltantes y errores.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color:#f0f0f0; padding:1.2rem; border-radius:10px; height:100%; border-top:3px solid #FF5A5F;">
            <div style="font-size:2.2rem; text-align:center; margin-bottom:0.8rem;">🔍</div>
            <h3 style="color:#333; text-align:center; font-size:1.3rem; margin-bottom:0.8rem;">Analiza</h3>
            <p style="color:#555; text-align:center;">Descubre patrones e insights valiosos sobre canales, tipos de campaña y rendimiento.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background-color:#f0f0f0; padding:1.2rem; border-radius:10px; height:100%; border-top:3px solid #FF5A5F;">
            <div style="font-size:2.2rem; text-align:center; margin-bottom:0.8rem;">📈</div>
            <h3 style="color:#333; text-align:center; font-size:1.3rem; margin-bottom:0.8rem;">Presenta</h3>
            <p style="color:#555; text-align:center;">Comunica tus hallazgos y recomendaciones en una presentación impactante de 10 minutos.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Cierre del contenedor principal
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Habilidades que desarrollarás
    st.markdown('<h2 style="font-size:1.8rem; font-weight:600; color:#FF5A5F; margin:1.5rem 0 1rem 0; padding-bottom:0.5rem; border-bottom:2px solid #FF5A5F;">Habilidades que desarrollarás</h2>', unsafe_allow_html=True)
    
    skills_col1, skills_col2 = st.columns(2)
    
    with skills_col1:
        st.markdown("""
        <div style="background-color:#f0f0f0; padding:1.2rem; border-radius:10px; margin-bottom:1rem;">
            <h3 style="color:#333; font-size:1.2rem; border-bottom:1px solid #ddd; padding-bottom:0.5rem; margin-bottom:1rem;">💻 Habilidades técnicas</h3>
            <ul style="color:#333; padding-left:1.5rem;">
                <li>Limpieza y preparación de datos con Python</li>
                <li>Análisis exploratorio y visualización</li>
                <li>Manejo de valores faltantes y outliers</li>
                <li>Documentación de código y hallazgos</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with skills_col2:
        st.markdown("""
        <div style="background-color:#f0f0f0; padding:1.2rem; border-radius:10px; margin-bottom:1rem;">
            <h3 style="color:#333; font-size:1.2rem; border-bottom:1px solid #ddd; padding-bottom:0.5rem; margin-bottom:1rem;">💼 Habilidades profesionales</h3>
            <ul style="color:#333; padding-left:1.5rem;">
                <li>Comunicación efectiva de datos</li>
                <li>Resolución de problemas con datos reales</li>
                <li>Presentación de insights accionables</li>
                <li>Gestión de proyectos de datos</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
   
    
    
    # Mensaje final motivador
    st.markdown("""
    <div style="text-align:center; margin-top:3rem; background-color:#f0f0f0; padding:2rem; border-radius:10px; border-top:4px solid #FF5A5F;">
        <h2 style="color:#FF5A5F; margin-bottom:1rem;">¿Estás listo para el desafío?</h2>
        <p style="color:#333; font-size:1.1rem;">Este proyecto es tu oportunidad para demostrar tus habilidades y destacar como analista de datos.</p>
        <p style="color:#333; font-size:1.1rem; margin-top:0.5rem;"><strong>¡Convierte el caos en claridad y muestra tu potencial!</strong></p>
    </div>
    """, unsafe_allow_html=True)