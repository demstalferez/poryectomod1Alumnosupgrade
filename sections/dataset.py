import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO
import base64

# Definir funciones localmente para evitar problemas de importación
def load_dataset(file_path, sample_data=None):
    """Carga el dataset o usa datos de ejemplo si falla."""
    try:
        # Intentar cargar el archivo CSV, omitiendo líneas problemáticas
        df = pd.read_csv(file_path, encoding='utf-8', on_bad_lines='warn')
        st.success(f"Dataset '{file_path}' cargado correctamente.")
        return df
    except FileNotFoundError:
        st.error(f"⚠️ El archivo '{file_path}' no se encuentra.")
        if sample_data:
            st.warning("Mostrando datos de ejemplo.")
            return pd.read_csv(StringIO(sample_data))
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error al cargar el dataset: {str(e)}")
        st.info("Intentando cargar el archivo ignorando líneas problemáticas...")
        try:
            # Segundo intento: omitir líneas malas
            df = pd.read_csv(file_path, encoding='utf-8', on_bad_lines='skip')
            st.warning(f"Se omitieron líneas problemáticas en '{file_path}'. Revisa el archivo para corregir inconsistencias.")
            return df
        except Exception as e2:
            st.error(f"No se pudo cargar el archivo incluso omitiendo errores: {str(e2)}")
            if sample_data:
                st.warning("Mostrando datos de ejemplo.")
                return pd.read_csv(StringIO(sample_data))
            return pd.DataFrame()

def get_download_link(file_path, file_name):
    """Genera un enlace de descarga para un archivo."""
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        return f'<a href="data:file/csv;base64,{b64}" download="{file_name}" class="btn-primary">📥 Descargar {file_name}</a>'
    except FileNotFoundError:
        return "⚠️ Archivo no disponible."

def show_dataset():
    st.markdown('<h1 class="section-title">📊 Dataset del Proyecto</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight" style="color: black;">
        <h3>marketing_campaigns_messy.csv</h3>
        <p>Este dataset contiene información sobre campañas de marketing de los últimos dos años, como nombres de campañas, fechas, presupuestos, ROI, tipos de campaña, audiencias, canales, tasas de conversión e ingresos.</p>
        <p>El archivo está intencionalmente desordenado con fechas que no tienen sentido, números que faltan, valores raros, etc.</p>
    </div>
    """, unsafe_allow_html=True)
    # Enlace de descarga
    st.markdown(get_download_link("data/marketingcampaigns.csv", "marketingcampaigns.csv"), unsafe_allow_html=True)
    
    # Datos de ejemplo
    sample_data = """campaign_name,date,budget,roi,type,target_audience,channel,conversion_rate,revenue
Summer2023_Sale,2023-06-15,75000,0.82,promotional,B2C,social_media,3.2,136500
Tech_Conference,2023-02-28,125000,0.67,event,B2B,email,2.9,208750
Holiday_Special,2023-12-01,95000,.56,seasonal,B2C,display,2.4,148200"""
    
    # Cargar dataset
    df = load_dataset("data/marketingcampaigns.csv", sample_data)
    
    if not df.empty:
        st.markdown('<h2 class="subsection-title">Previsualización</h2>', unsafe_allow_html=True)
        st.dataframe(df.head(10), use_container_width=True)
        
        st.markdown('<h2 class="subsection-title">Resumen</h2>', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Filas", f"{df.shape[0]:,}")
        col2.metric("Columnas", f"{df.shape[1]}")
        col3.metric("Nulos", f"{df.isna().sum().sum():,}")
        col4.metric("Duplicados", f"{df.duplicated().sum():,}")
        
        st.markdown('<h2 class="subsection-title">Problemas Comunes</h2>', unsafe_allow_html=True)
        st.markdown(
            """
            <style>
              /* Estilos para las pestañas: texto negro sobre fondo blanco */
              [data-baseweb="tab"] {
            color: black !important;
            background-color: white !important;
              }
              /* Opcional: efecto hover */
              [data-baseweb="tab"]:hover {
            background-color: #f0f0f0 !important;
              }
            </style>
            """, unsafe_allow_html=True)
        tabs = st.tabs(["Valores Nulos", "Formatos (ejemplo)", "Outliers como curiosidad"])
        
        with tabs[0]:
            fig = px.imshow(df.isnull(), color_continuous_scale=["#000000", "#FF5A5F"], title="Mapa de Nulos")
            st.plotly_chart(fig, use_container_width=True)
        
        with tabs[1]:
            st.markdown("**Ejemplos de formatos inconsistentes:**")
            for col in ['roi', 'date', 'budget']:
                if col in df.columns:
                    ejemplos = df[col].dropna().sample(min(5, len(df))).tolist()
                    st.markdown(f"- **{col}:** {', '.join([f'`{x}`' for x in ejemplos])}")
        
        with tabs[2]:
            numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
            if numeric_cols:
                col_to_plot = st.selectbox("Columna para outliers:", numeric_cols)
                fig = px.box(df, y=col_to_plot, title=f"Outliers en {col_to_plot}")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No hay columnas numéricas.")