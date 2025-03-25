import streamlit as st

def show_tasks():
    # Agrega estilos globales
    st.markdown(
        """
        <style>
        /* Cualquier elemento con la clase 'white-bg' o 'highlight' (si es fondo blanco) mostrará texto negro */
        .white-bg, .highlight {
            background-color: white !important;
            color: black !important;
        }
        /* Aseguramos que el texto de la app sea negro por defecto */
        body {
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="section-title">📝 Tareas del Desafío</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
        <p>Este desafío está estructurado en tres fases principales: <strong>Limpieza</strong>, <strong>Análisis</strong> y <strong>Presentación</strong>. Cada fase tiene tareas específicas que te permitirán desarrollar un proyecto completo de análisis de datos.</p>
        <p>Sigue la metodología propuesta para asegurar un enfoque sistemático y profesional.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Cronograma sugerido
    st.markdown('<h2 class="subsection-title">Cronograma Sugerido</h2>', unsafe_allow_html=True)
   
    
    # Fase 1: Limpieza
    st.markdown('<h2 class="subsection-title">Fase 1: Limpieza y Preparación de Datos</h2>', unsafe_allow_html=True)
    
    tasks_cleaning = [
        {
            "title": "1. Exploración Inicial del Dataset",
            "desc": "Realiza una exploración completa del archivo marketingcampaigns.csv para comprender sus características y problemas.",
            "steps": [
                "Examina las primeras y últimas filas para entender la estructura general del dataset",
                "Verifica los tipos de datos de cada columna y su coherencia con los valores esperados",
                "Identifica valores faltantes y su distribución por columna",
                "Calcula estadísticas descriptivas básicas para detectar anomalías y posibles outliers",
                "Analiza la distribución de variables categóricas para detectar errores ortográficos o inconsistencias",
                "Documenta todos los problemas encontrados y prioriza su resolución"
            ]
        },
        {
            "title": "2. Manejo de Valores Faltantes",
            "desc": "Desarrolla una estrategia coherente para manejar valores faltantes en diferentes columnas.",
            "steps": [
                "Cuantifica el porcentaje de valores faltantes por columna para evaluar su impacto",
                "Para 'budget': considera usar la mediana por tipo de campaña o canal",
                "Para 'type': determina si asignar 'unknown' o utilizar técnicas de imputación basadas en otras variables",
                "Para 'conversion_rate': evalúa la correlación con otras variables antes de decidir la estrategia de imputación",
                "Para 'roi' y 'revenue': analiza la relación entre estas variables y 'budget' para una imputación coherente",
                "Documenta y justifica cada decisión de imputación o eliminación"
            ]
        },
        {
            "title": "3. Corrección de Formatos Inconsistentes",
            "desc": "Estandariza los formatos de fechas, números y valores monetarios para permitir un análisis coherente.",
            "steps": [
                "Normaliza los decimales en 'roi' y 'conversion_rate' para usar un formato consistente (punto o coma)",
                "Convierte las fechas a un formato estándar (YYYY-MM-DD) y maneja fechas inválidas",
                "Asegura que 'budget' y 'revenue' sean valores numéricos sin símbolos de moneda o separadores de miles",
                "Verifica la consistencia de unidades (ej: asegúrate que 'conversion_rate' siempre esté en porcentaje o decimal)",
                "Implementa validaciones para confirmar que la conversión de formatos ha sido exitosa"
            ]
        },
        {
            "title": "4. Eliminación de Duplicados",
            "desc": "Identifica y maneja filas duplicadas que pueden distorsionar los resultados del análisis.",
            "steps": [
                "Busca duplicados exactos (todas las columnas idénticas)",
                "Identifica duplicados parciales (misma campaña con ligeras variaciones en los datos)",
                "Desarrolla criterios para decidir qué fila conservar cuando hay duplicados parciales",
                "Documenta cuántas filas se eliminaron y el impacto en el dataset",
                "Verifica que la eliminación de duplicados no ha creado sesgos en los datos"
            ]
        },
        {
            "title": "5. Manejo de Valores Atípicos (Outliers)",
            "desc": "Identifica y trata valores extremos que pueden representar errores o campañas excepcionales.",
            "steps": [
                "Utiliza métodos estadísticos (IQR, Z-score) para detectar outliers en variables numéricas",
                "Analiza 'budget' y 'revenue' para identificar valores inusualmente altos o bajos",
                "Evalúa cada outlier en su contexto para determinar si es un error o un dato válido",
                "Decide si transformar, eliminar o mantener cada outlier basándote en evidencia",
                "Documenta el impacto de tu estrategia de manejo de outliers en el análisis posterior"
            ]
        },
        {
            "title": "6. Corrección de Errores de Texto",
            "desc": "Estandariza y corrige errores ortográficos en las variables categóricas.",
            "steps": [
                "Identifica variaciones ortográficas en 'channel' (como 'referal' vs 'referral')",
                "Normaliza valores en 'target_audience' para usar consistentemente 'B2B' o 'B2C'",
                "Corrige errores en 'type' para unificar categorías",
                "Utiliza técnicas como normalización de texto y distancia de edición para automatizar correcciones",
                "Verifica la consistencia después de las correcciones"
            ]
        },
        {
            "title": "7. Creación de Variables Derivadas",
            "desc": "Enriquece el dataset con nuevas variables que proporcionen insights adicionales.",
            "steps": [
                "Calcula 'net_profit' (beneficio neto) restando 'budget' de 'revenue'",
                "Extrae componentes temporales de la fecha (mes, trimestre, año) para análisis estacional",
                "Crea categorías de rendimiento basadas en ROI y tasa de conversión",
                "Calcula métricas de eficiencia como 'cost_per_conversion'",
                "Considera variables binarias (flags) para características importantes"
            ]
        },
        {
            "title": "8. Validación Final de Datos",
            "desc": "Verifica la calidad e integridad del dataset limpio antes del análisis.",
            "steps": [
                "Comprueba que todas las columnas tienen los tipos de datos correctos",
                "Verifica la consistencia entre variables relacionadas (ej: budget, revenue, roi)",
                "Realiza validaciones cruzadas para detectar inconsistencias lógicas",
                "Asegura que no quedan valores nulos sin justificación",
                "Documenta el proceso completo de limpieza y las transformaciones realizadas"
            ]
        }
    ]
    
    for task in tasks_cleaning:
        with st.expander(f"{task['title']}"):
            st.markdown(f"**Descripción:** {task['desc']}")
            st.markdown("**Pasos:**")
            for step in task["steps"]:
                st.markdown(f"- {step}")
    
    # Fase 2: Análisis
    st.markdown('<h2 class="subsection-title">Fase 2: Análisis Exploratorio</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    Una vez que hayas limpiado y preparado los datos, deberás responder a las siguientes preguntas analíticas utilizando técnicas de análisis exploratorio y visualización de datos:
    """)
    
    questions = [
        {
            "question": "¿Qué canal de marketing se utiliza con mayor frecuencia y cuál genera mejor ROI?",
            "description": "Analiza la distribución de canales y compara su rendimiento en términos de ROI y otros indicadores clave.",
            "approach": "Combina análisis de frecuencia con métricas de rendimiento para identificar no solo los canales más utilizados sino también los más efectivos. Considera segmentar por tipo de campaña o audiencia para un análisis más detallado.",
            "visualization": "Gráfico de barras para frecuencia y diagrama de caja para distribución de ROI por canal"
        },
        {
            "question": "¿Qué tipo de campaña genera más ingresos en promedio y cuál tiene mejor conversión?",
            "description": "Compara los diferentes tipos de campaña para identificar cuáles generan más ingresos y tienen mejor tasa de conversión.",
            "approach": "Analiza el rendimiento financiero (ingresos, beneficio neto) y las métricas de efectividad (tasa de conversión, ROI) por tipo de campaña. Busca si existen relaciones entre estas métricas que puedan explicar el éxito de ciertos tipos.",
            "visualization": "Gráfico de barras para ingresos promedio y tasa de conversión por tipo, diagrama de dispersión para correlación entre estas métricas"
        },
        {
            "question": "¿Cómo se distribuye el ROI entre las campañas? ¿Qué factores están asociados con un ROI alto?",
            "description": "Analiza la distribución del ROI y busca patrones o factores que estén asociados con mejores resultados.",
            "approach": "Estudia la distribución estadística del ROI, identifica segmentos de alto rendimiento y analiza qué características comparten. Busca correlaciones con otras variables como presupuesto, canal, tipo o audiencia.",
            "visualization": "Histograma y boxplot del ROI, heatmap de correlaciones, gráficos de dispersión con ROI como variable objetivo"
        },
        {
            "question": "¿Hay diferencias significativas en la tasa de conversión entre audiencias B2B y B2C?",
            "description": "Compara las tasas de conversión entre los dos tipos de audiencia para determinar si existen diferencias en el comportamiento de compra.",
            "approach": "Realiza análisis comparativos entre ambos segmentos, no solo para tasa de conversión sino también para otras métricas. Considera el análisis por subgrupos combinando audiencia con canal o tipo de campaña.",
            "visualization": "Gráfico de cajas comparativo, gráficos de barras agrupados por audiencia y canal/tipo"
        },
        {
            "question": "¿Qué campaña tiene el mayor beneficio neto (net_profit)? ¿Qué características la hacen exitosa?",
            "description": "Identifica las campañas más rentables y analiza qué factores contribuyen a su éxito.",
            "approach": "Realiza un ranking de campañas según beneficio neto y analiza en profundidad las características de las más exitosas. Busca patrones comunes que puedan replicarse en futuras campañas.",
            "visualization": "Tabla con las top 5-10 campañas por beneficio neto, gráficos comparativos con estas campañas destacadas"
        },
        {
            "question": "¿Existe correlación entre el presupuesto (budget) y los ingresos (revenue)?",
            "description": "Analiza si un mayor presupuesto se traduce en mayores ingresos y si hay un punto óptimo de inversión.",
            "approach": "Estudia la relación entre presupuesto e ingresos mediante análisis de correlación y regresión. Busca si la relación es lineal o si hay rendimientos decrecientes a partir de cierto punto.",
            "visualization": "Gráfico de dispersión con línea de tendencia, posiblemente segmentado por canal o tipo de campaña"
        },
        {
            "question": "¿Qué campañas tienen un ROI mayor a 0.5 y ingresos encima de 500,000?",
            "description": "Identifica las campañas de alto rendimiento que cumplan ambos criterios para posible replicación.",
            "approach": "Filtra las campañas según los criterios establecidos y analiza sus características comunes. Considera crear un sistema de clasificación más completo con múltiples criterios.",
            "visualization": "Tabla filtrada o gráfico de cuadrantes que muestre las campañas de alto rendimiento"
        },
        {
            "question": "¿Existen patrones estacionales o temporales en el rendimiento de las campañas?",
            "description": "Analiza si hay variaciones en el rendimiento según la época del año o tendencias a lo largo del tiempo.",
            "approach": "Utiliza los componentes temporales extraídos de la fecha para agrupar y comparar el rendimiento a lo largo del tiempo. Busca patrones estacionales o tendencias generales.",
            "visualization": "Gráficos de línea temporal, heatmaps por mes y tipo de campaña, análisis de rendimiento por trimestre"
        }
    ]
    
    for i, q in enumerate(questions, 1):
        with st.expander(f"{i}. {q['question']}"):
            st.markdown(f"**Objetivo:** {q['description']}")
            st.markdown(f"**Enfoque sugerido:** {q['approach']}")
            st.markdown(f"**Visualizaciones recomendadas:** {q['visualization']}")
    
    # Fase 3: Presentación
    st.markdown('<h2 class="subsection-title">Fase 3: Documentación y Presentación</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
        <p>La fase final del proyecto consiste en documentar tu trabajo y preparar una presentación efectiva que comunique tus hallazgos y recomendaciones.</p>
    </div>
    """, unsafe_allow_html=True)
    
    documentation_tasks = [
        {
            "title": "1. Documentación en GitHub",
            "desc": "Prepara un repositorio GitHub completo y bien organizado.",
            "steps": [
                "Crea un README.md detallado con título, descripción del proyecto y tu nombre",
                "Organiza el código en notebooks o scripts con secciones claras y comentarios explicativos",
                "Incluye el dataset limpio final (marketingcampaigns_clean.csv)",
                "Documenta todas las decisiones de limpieza y transformación",
                "Añade visualizaciones clave y sus interpretaciones",
                "Considera incluir un documento de insights con recomendaciones"
            ]
        },
        {
            "title": "2. Preparación de la Presentación",
            "desc": "Desarrolla una presentación efectiva de 10 minutos que comunique lo esencial.",
            "steps": [
                "Estructura tu presentación con introducción, métodos, hallazgos y recomendaciones",
                "Selecciona las 3-5 visualizaciones más impactantes que mejor cuenten la historia de los datos",
                "Destaca insights accionables que la empresa pueda implementar",
                "Cuantifica el impacto potencial de tus recomendaciones cuando sea posible",
                "Ensaya tu presentación para asegurarte de que se ajusta al tiempo permitido",
                "Prepárate para posibles preguntas sobre tu metodología y conclusiones"
            ]
        }
    ]
    
    for task in documentation_tasks:
        with st.expander(f"{task['title']}"):
            st.markdown(f"**Descripción:** {task['desc']}")
            st.markdown("**Pasos:**")
            for step in task["steps"]:
                st.markdown(f"- {step}")
    
    # Consejos para un proyecto exitoso
    st.markdown('<h2 class="subsection-title">Consejos para un Proyecto Exitoso</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    - **Enfoque iterativo**: Avanza paso a paso y revisa constantemente tu progreso
    - **Documentación continua**: Documenta decisiones y hallazgos mientras trabajas, no al final
    - **Prioriza la calidad sobre la cantidad**: Enfócate en análisis profundos de alta calidad
    - **Contextualiza tus hallazgos**: Relaciona los insights con el negocio y su impacto potencial
    - **Visualizaciones efectivas**: Diseña gráficos claros con títulos informativos y etiquetas adecuadas
    - **Storytelling con datos**: Construye una narrativa coherente que guíe a través de tus descubrimientos
    - **Pensamiento crítico**: Cuestiona tus propios resultados y busca explicaciones alternativas
    - **Control de versiones**: Usa Git de manera efectiva para gestionar los cambios en tu código
    - **Revisión por pares**: Si es posible, pide a compañeros que revisen tu trabajo
    - **Practica tu presentación**: Ensaya varias veces para lograr una exposición clara y ajustada al tiempo
    """)
    
    # Recursos adicionales
    with st.expander("Recursos Adicionales"):
        st.markdown("""
        **Limpieza de datos:**
        - [Guía de Pandas para limpieza de datos](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)
        - [Artículo: "Tidy Data" por Hadley Wickham](https://www.jstatsoft.org/article/view/v059i10)
        
        **Visualización:**
        - [Guía de Matplotlib](https://matplotlib.org/stable/tutorials/index.html)
        - [Documentación de Seaborn](https://seaborn.pydata.org/tutorial.html)
        - [Plotly para visualizaciones interactivas](https://plotly.com/python/)
        
        **Análisis de datos:**
        - [Data Analysis with Python Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
        - [Técnicas de análisis exploratorio de datos](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15)
        
        **Presentación de datos:**
        - [Storytelling with Data (blog)](http://www.storytellingwithdata.com/)
        - [Mejores prácticas para presentaciones de datos](https://hbr.org/2016/06/visualizations-that-really-work)
        """)