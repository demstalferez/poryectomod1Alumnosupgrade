import streamlit as st

def show_description():
    st.markdown('<h1 class="section-title">📋 Descripción del Desafío</h1>', unsafe_allow_html=True)
    
    # Introducción con diseño mejorado y contraste asegurado
    st.markdown("""
    <div class="highlight">
        <p style="color: #333;">¡Bienvenido a Upgrade Hub! Estás a punto de empezar tu aventura como analista de datos, y tenemos un reto genial para ti. Imagínate esto: una multinacional tecnológica nos ha enviado un dataset con los datos de sus campañas de marketing de los últimos dos años. El archivo (<code>marketingcampaigns.csv</code>) tiene cosas como nombres de campañas, fechas, presupuestos, ROI, tipos de campaña, audiencias, canales, tasas de conversión e ingresos. Suena interesante, ¿verdad? Pero hay un problema: <strong>¡está súper desordenado!</strong> Hay fechas que no tienen sentido, números que faltan, valores raros... un desastre.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Dividir en dos columnas para mejor presentación
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h2 class="subsection-title">Tu Misión</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="color: #ffffff;">Tu misión es clara: <strong>limpiar este lío</strong>, prepararlo para analizarlo y sacar conclusiones útiles que le den valor al cliente. No solo vas a ordenar datos, sino que vas a descubrir qué funciona y qué no en estas campañas.</p>
        
        <p style="color: #ffffff;">El <span class="date-highlight">1 de abril de 2025</span>, vas a presentar todo esto en una charla de 10 minutos, y lo vas a respaldar con un repositorio en GitHub donde pondrás tu código, los datos limpios y tus hallazgos. Es tu oportunidad de mostrar lo que has aprendido y dejar huella en Upgrade Hub.</p>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color:#f0f0f0; padding:1.2rem; border-radius:10px; text-align:center; height:100%; display:flex; flex-direction:column; justify-content:center; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h3 style="margin-bottom:1rem; color:#333;">Objetivo Principal</h3>
            <p style="font-size:1.1rem; color:#333;"><strong>Transformar un dataset desordenado en insights valiosos para el cliente</strong></p>
            <p style="margin-top:1rem; color:#333;"><span style="font-weight:700; color:#FF5A5F;">Fecha de entrega: 1 abril 2025</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Fases del proyecto con visualización mejorada y contraste corregido
    st.markdown('<h2 class="subsection-title">Fases del Proyecto</h2>', unsafe_allow_html=True)
    
    fase_col1, fase_col2, fase_col3 = st.columns(3)
    
    with fase_col1:
        st.markdown("""
        <div style="background-color:#f0f0f0; border-radius:10px; padding:1.2rem; text-align:center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-top: 4px solid #FF5A5F;">
            <div style="font-size:2.5rem; color:#FF5A5F; margin-bottom:1rem;">🧹</div>
            <h3 style="color:#333;">LIMPIAR</h3>
            <p style="color:#333;">Ordenar y corregir los problemas del dataset</p>
        </div>
        """, unsafe_allow_html=True)
    
    with fase_col2:
        st.markdown("""
        <div style="background-color:#f0f0f0; border-radius:10px; padding:1.2rem; text-align:center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-top: 4px solid #FF5A5F;">
            <div style="font-size:2.5rem; color:#FF5A5F; margin-bottom:1rem;">🔧</div>
            <h3 style="color:#333;">PREPARAR</h3>
            <p style="color:#333;">Estructurar los datos para su análisis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with fase_col3:
        st.markdown("""
        <div style="background-color:#f0f0f0; border-radius:10px; padding:1.2rem; text-align:center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-top: 4px solid #FF5A5F;">
            <div style="font-size:2.5rem; color:#FF5A5F; margin-bottom:1rem;">🔍</div>
            <h3 style="color:#333;">EXPLORAR</h3>
            <p style="color:#333;">Analizar y extraer conclusiones valiosas</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Pasos detallados 
    st.markdown('<h2 class="subsection-title">¿Qué Tienes que Hacer?</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <p style="color: #ffffff;">Aquí te dejo los pasos para que completes el desafío. Todo lo que hagas lo guardarás en un repositorio de GitHub para la presentación del 1 de abril de 2025.</p>
    """, unsafe_allow_html=True)
    
    steps = [
        {
            "title": "1. Carga y Mira el Dataset",
            "desc": "Abre el archivo marketingcampaigns.csv y échale un vistazo.",
            "steps": ["Mira las primeras filas para ver cómo está organizado.", 
                     "Comprueba qué tipo de datos tiene cada columna y si hay huecos.", 
                     "Saca algunos números básicos (como promedios o valores máximos) para detectar cosas raras."],
            "icon": "📂"
        },
        {
            "title": "2. Arregla los Valores que Faltan",
            "desc": "Busca dónde faltan datos y decide qué hacer con esos huecos.",
            "steps": ["Cuenta cuántos valores faltan en cada columna.",
                     "Para budget, piensa si pones un valor promedio o quitas esas filas.",
                     "Para type, decide si les das un valor como \"desconocido\" o las eliminas.",
                     "Para conversion_rate, elige cómo llenar los huecos (o si los dejas fuera)."],
            "icon": "🔍"
        },
        {
            "title": "3. Corrige los Formatos Desordenados",
            "desc": "Haz que los números y fechas se vean bien y sean consistentes.",
            "steps": ["Arregla los decimales en roi y conversion_rate (como \"0,74\" o \".37\") para que sean iguales.",
                     "Corrige fechas locas (como \"2023-13-01\" o \"2024-02-30\") para que tengan sentido o las marques como vacías.",
                     "Asegúrate de que budget y revenue sean números claros, sin comas raras."],
            "icon": "🔄"
        },
        {
            "title": "4. Quita las Filas Repetidas",
            "desc": "Encuentra y elimina cualquier fila que esté duplicada.",
            "steps": ["Busca si hay filas idénticas (como copias exactas).",
                     "Quédate solo con una y mira cómo cambia el tamaño del dataset."],
            "icon": "🗑️"
        },
        {
            "title": "5. Encuentra y Maneja Valores Extraños",
            "desc": "Busca números que no tengan lógica y decide qué hacer con ellos.",
            "steps": ["Revisa budget y revenue por valores súper altos o negativos.",
                     "Elige si quitar esas filas, cambiar los valores o dejarlos (y explica por qué)."],
            "icon": "⚠️"
        },
        {
            "title": "6. Arregla Errores de Texto",
            "desc": "Corrige palabras mal escritas o inconsistentes.",
            "steps": ["Busca errores en channel (como \"referal\" en vez de \"referral\") y cámbialos.",
                     "Asegúrate de que target_audience solo diga \"B2B\" o \"B2C\"."],
            "icon": "✏️"
        },
        {
            "title": "7. Añade Algo Nuevo",
            "desc": "Crea una columna extra para hacer el análisis más interesante.",
            "steps": ["Calcula el beneficio neto (net_profit) restando budget a revenue.",
                     "Ten cuidado con los casos donde falten datos y decide cómo manejarlos."],
            "icon": "➕"
        }
    ]
    
    for step in steps:
        with st.expander(f"{step['icon']} {step['title']}"):
            st.markdown(f"**Descripción:** {step['desc']}")
            st.markdown("**Pasos:**")
            for substep in step["steps"]:
                st.markdown(f"- {substep}")
    
    # Preguntas de análisis con diseño mejorado y contraste corregido
    st.markdown('<h2 class="subsection-title">8️⃣ Explora y Responde Preguntas</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
    <p style="color: #333;">Mira los datos limpios y responde estas preguntas para ayudar al cliente. Usa cálculos y gráficos simples.</p>
    </div>
    """, unsafe_allow_html=True)
    
    questions = [
        "¿Qué canal de marketing se usa más?",
        "¿Qué tipo de campaña (type) da más ingresos en promedio?",
        "¿Cómo está repartido el ROI en las campañas?",
        "¿Hay diferencia en la tasa de conversión (conversion_rate) entre B2B y B2C?",
        "¿Qué campaña tiene el mayor beneficio neto (net_profit)?",
        "¿El presupuesto (budget) tiene relación con los ingresos (revenue)?",
        "¿Qué campañas tienen un ROI mayor a 0.5 y ingresos encima de 500,000?"
    ]
    
    quest_col1, quest_col2 = st.columns(2)
    
    for i, question in enumerate(questions):
        if i < 4:  # Primeras 4 preguntas en la columna 1
            with quest_col1:
                st.markdown(f"""
                <div style="background-color:#f0f0f0; padding:1rem; border-radius:10px; margin-bottom:1rem; border-left: 3px solid #FF5A5F;">
                    <span style="background-color:#FF5A5F; color:white; padding:0.2rem 0.5rem; border-radius:5px; margin-right:0.5rem; font-size:0.8rem;">Q{i+1}</span> 
                    <span style="color:#333;">{question}</span>
                </div>
                """, unsafe_allow_html=True)
        else:  # Resto en la columna 2
            with quest_col2:
                st.markdown(f"""
                <div style="background-color:#f0f0f0; padding:1rem; border-radius:10px; margin-bottom:1rem; border-left: 3px solid #FF5A5F;">
                    <span style="background-color:#FF5A5F; color:white; padding:0.2rem 0.5rem; border-radius:5px; margin-right:0.5rem; font-size:0.8rem;">Q{i+1}</span> 
                    <span style="color:#333;">{question}</span>
                </div>
                """, unsafe_allow_html=True)
    
    # Pasos finales en formato simplificado para evitar problemas de contraste
    st.markdown('<h2 class="subsection-title">Pasos Finales</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color:#f0f0f0; padding:1.5rem; border-radius:10px; margin-bottom:1.5rem;">
        <h3 style="color:#333; border-bottom:1px solid #ddd; padding-bottom:0.5rem;">9. Arma tu Repositorio en GitHub</h3>
        <p style="color:#333;">Crea un repositorio (puedes llamarlo upgrade-hub-marketing-analysis o algo así).</p>
        <p style="color:#333;">Incluye README.md, código bien comentado, datos limpios e informe con tus hallazgos.</p>
    </div>
    
    <div style="background-color:#f0f0f0; padding:1.5rem; border-radius:10px; margin-bottom:1.5rem;">
        <h3 style="color:#333; border-bottom:1px solid #ddd; padding-bottom:0.5rem;">10. Prepara tu Charla de 10 Minutos</h3>
        <p style="color:#333;">Explica rápido cómo estaba el dataset y qué hiciste para limpiarlo.</p>
        <p style="color:#333;">Muestra tus respuestas a las 7 preguntas, usando los gráficos para que se entienda.</p>
        <p style="color:#333;">Termina con una idea para el cliente basada en lo que encontraste.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Mensaje motivacional final con contraste corregido
    st.markdown("""
    <div style="text-align:center; margin-top:2rem; padding:1.5rem; background-color:#f0f0f0; border-radius:10px; border-top:4px solid #FF5A5F;">
        <h2 style="color:#FF5A5F;">¡Tú Puedes con Esto!</h2>
        <p style="font-size:1.1rem; color:#333;">Este desafío es tu oportunidad para demostrar tus habilidades de análisis de datos y dejar huella en Upgrade Hub.</p>
        <p style="font-style:italic; color:#333;">"No es solo limpiar números: es convertir caos en respuestas útiles."</p>
    </div>
    """, unsafe_allow_html=True)