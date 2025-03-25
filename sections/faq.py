import streamlit as st

def show_faq():
    st.markdown('<h1 class="section-title">❓ Preguntas Frecuentes</h1>', unsafe_allow_html=True)
    

    
    # Preguntas sobre herramientas y tecnología
    st.markdown('<h2 class="subsection-title">Herramientas y Tecnología</h2>', unsafe_allow_html=True)
    
    tech_faqs = [
        {
            "q": "¿Puedo usar otras herramientas además de Python para el análisis?",
            "a": """
                El proyecto está diseñado principalmente para Python, pero puedes complementarlo con otras herramientas si lo consideras necesario. Por ejemplo:
                
                - **Python** debe ser tu herramienta principal para la limpieza y análisis
                - **Power BI/Tableau** podrían usarse para visualizaciones adicionales
                - **Excel** podría usarse para análisis complementarios
                
                Asegúrate de que tu trabajo principal esté en Python y bien documentado en Jupyter Notebooks o scripts.
            """
        },
        {
            "q": "¿Qué bibliotecas de Python se recomienda utilizar?",
            "a": """
                Se recomiendan las siguientes bibliotecas:
                
                - **pandas** para manipulación y análisis de datos
                - **numpy** para operaciones numéricas
                - **matplotlib** y **seaborn** para visualizaciones estáticas
                - **plotly** para visualizaciones interactivas
                - **scikit-learn** si deseas implementar algún modelo predictivo simple
                
                No es necesario utilizar todas, pero pandas será esencial para la limpieza y preparación de datos.
            """
        },
        {
            "q": "¿Necesito experiencia previa con GitHub para este proyecto?",
            "a": """
                No es necesario ser un experto en Git/GitHub, pero se espera un conocimiento básico para:
                
                - Crear un repositorio
                - Hacer commits y push de tu código
                - Organizar archivos y carpetas
                - Escribir un README en Markdown
                
                Si eres principiante en GitHub, hay muchos tutoriales online que pueden ayudarte a preparar tu repositorio correctamente. Lo más importante es mantener una organización clara y lógica.
            """
        },
        {
            "q": "¿Puedo usar ChatGPT u otras herramientas de IA para ayudarme?",
            "a": """
                Sí, puedes utilizar herramientas de IA como asistentes para:
                
                - Generar ideas o enfoques
                - Depurar código con errores
                - Mejorar la redacción de informes
                
                Sin embargo, recuerda que:
                
                1. **Debes entender completamente** cualquier código o análisis que incluyas
                2. **El trabajo principal debe ser tuyo**
                3. **Menciona en tu documentación** si usaste estas herramientas y cómo
                
                El objetivo es desarrollar tus habilidades, por lo que deberías hacer el trabajo analítico por ti mismo.
            """
        }
    ]
    
    for faq in tech_faqs:
        with st.expander(faq["q"]):
            st.markdown(faq["a"])
    
    # Preguntas sobre el dataset y el análisis
    st.markdown('<h2 class="subsection-title">Dataset y Análisis</h2>', unsafe_allow_html=True)
    
    data_faqs = [
        {
            "q": "¿Qué hago si no puedo corregir algún valor en el dataset?",
            "a": """
                Parte del desafío es tomar decisiones sobre datos problemáticos. Si encuentras valores que no puedes corregir con certeza:
                
                1. **Documenta el problema** específico y por qué es difícil de corregir
                2. **Justifica tu enfoque** (eliminar, imputar, marcar como especial, etc.)
                3. **Evalúa el impacto** de tu decisión en el análisis posterior
                
                Lo importante es demostrar pensamiento crítico y documentar tu razonamiento, no necesariamente encontrar la solución "perfecta".
            """
        },
        {
            "q": "¿Debo responder todas las preguntas de análisis o puedo centrarme en algunas?",
            "a": """
                Se espera que intentes responder todas las preguntas principales del desafío. Sin embargo:
                
                - Puedes priorizar algunas preguntas si ofrecen insights más valiosos
                - Es mejor responder menos preguntas con análisis profundo que todas superficialmente
                - Si omites alguna pregunta, explica por qué (limitaciones de los datos, relevancia, etc.)
                
                En tu presentación final, probablemente solo tendrás tiempo para centrarte en 3-4 insights principales, pero tu repositorio debe mostrar un análisis más completo.
            """
        },
        {
            "q": "¿Qué pasa si encuentro patrones diferentes a los esperados en las preguntas de análisis?",
            "a": """
                ¡Esto es normal y bienvenido! El propósito del análisis de datos es descubrir la realidad, no confirmar suposiciones.
                
                - Si encuentras resultados inesperados, documéntalos con claridad
                - Proporciona evidencia sólida para respaldar hallazgos sorprendentes
                - Sugiere posibles explicaciones para estos patrones
                - Considera si podrían representar oportunidades o riesgos para la empresa
                
                Los descubrimientos inesperados a menudo proporcionan los insights más valiosos, siempre que estén respaldados por datos sólidos.
            """
        },
        {
            "q": "¿Cuántas visualizaciones debo incluir en mi análisis?",
            "a": """
                La calidad es más importante que la cantidad. Como guía general:
                
                - Tu repositorio debería incluir al menos 7-10 visualizaciones significativas
                - Tu presentación debería incluir 3-5 de las visualizaciones más impactantes
                
                Cada visualización debe:
                - Tener un propósito claro relacionado con una pregunta o insight
                - Incluir títulos, etiquetas y leyendas apropiados
                - Usar el tipo de gráfico más adecuado para los datos y el mensaje
                - Estar acompañada de una interpretación clara
                
                Evita crear visualizaciones solo por hacerlas; cada una debe aportar valor al análisis.
            """
        },
        {
            "q": "¿Hay algún enfoque específico que deba tomar para la limpieza de datos?",
            "a": """
                No hay un enfoque único "correcto", pero deberías seguir estos principios:
                
                1. **Sé sistemático**: Aborda los problemas en un orden lógico
                2. **Documenta tus decisiones**: Explica por qué elegiste cada enfoque
                3. **Valida tus resultados**: Verifica que tus transformaciones funcionaron como esperabas
                4. **Considera el contexto**: Las decisiones de limpieza deben tomar en cuenta el objetivo del análisis
                
                Lo más importante es demostrar un proceso de pensamiento claro y mantener la integridad de los datos mientras los haces utilizables para el análisis.
            """
        }
    ]
    
    for faq in data_faqs:
        with st.expander(faq["q"]):
            st.markdown(faq["a"])
    
    # Preguntas sobre la entrega y evaluación
    st.markdown('<h2 class="subsection-title">Entrega y Evaluación</h2>', unsafe_allow_html=True)
    
    delivery_faqs = [
        {
            "q": "¿Puedo colaborar con otros estudiantes en este proyecto?",
            "a": """
                Este es un proyecto individual, diseñado para evaluar tus habilidades personales. Sin embargo:
                
                - Puedes **discutir enfoques generales** con compañeros
                - Está bien **compartir recursos útiles** (artículos, tutoriales)
                - **No compartas código específico** ni soluciones detalladas
                
                Todo el trabajo que entregues debe ser principalmente tuyo. La colaboración excesiva será evidente en la presentación, donde deberás demostrar comprensión profunda de todo tu trabajo.
            """
        },
        {
            "q": "¿Hay alguna extensión o prórroga para la entrega?",
            "a": """
                La fecha de entrega es el 1 de abril de 2025. Recomendamos encarecidamente cumplir con esta fecha por las siguientes razones:
                
                - Las presentaciones están programadas según esta fecha
                - Es una práctica profesional importante cumplir con los plazos
                - La gestión del tiempo es una habilidad clave en el análisis de datos
                
                Si enfrentas circunstancias excepcionales, comunícate lo antes posible con demetrio.esteban@bootcamp-upgrade.com para discutir tu situación específica.
            """
        },
        {
            "q": "¿Cómo debo prepararme para las preguntas después de la presentación?",
            "a": """
                Las preguntas suelen centrarse en:
                
                1. **Decisiones metodológicas**: Por qué elegiste ciertos enfoques de limpieza o análisis
                2. **Interpretación de resultados**: El significado de tus hallazgos para el negocio
                3. **Limitaciones**: Qué advertencias deberían considerarse al interpretar tus conclusiones
                4. **Recomendaciones**: Cómo implementarías tus sugerencias en la práctica
                
                La mejor preparación es:
                - Comprender profundamente tu propio trabajo
                - Anticipar preguntas críticas sobre tus decisiones y conclusiones
                - Revisar toda tu metodología y estar listo para justificar cada paso
                - Practicar explicaciones claras y concisas
            """
        },
        {
            "q": "¿Qué pasa si mi repositorio o presentación no está completamente terminado para la fecha límite?",
            "a": """
                Es mejor entregar un proyecto parcial pero bien ejecutado que nada en absoluto. Si no puedes completar todo:
                
                1. **Prioriza**: Enfócate en tener al menos la limpieza de datos y algunas preguntas bien analizadas
                2. **Documenta**: Explica claramente qué completaste y qué queda pendiente
                3. **Entrega lo que tengas**: Un proyecto parcial todavía puede demostrar tus habilidades
                
                Recuerda que en situaciones profesionales reales, a veces es necesario entregar análisis preliminares antes de completar todo el trabajo planificado.
            """
        }
    ]
    
    for faq in delivery_faqs:
        with st.expander(faq["q"]):
            st.markdown(faq["a"])
    
    # Soporte y ayuda
    st.markdown('<h2 class="subsection-title">¿Necesitas más ayuda?</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    Si tienes preguntas adicionales o necesitas apoyo durante el desafío:
    
    - **Email**: demetrio.esteban@bootcamp-upgrade.com
    - **Sesiones grupales**: Participa en las sesiones de preguntas y respuestas programadas
    
    Recuerda que enfrentar desafíos y superarlos es parte del proceso de aprendizaje. No dudes en pedir ayuda cuando la necesites.
    """)