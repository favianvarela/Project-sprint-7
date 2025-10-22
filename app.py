import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Análisis de Anuncios de Venta de Coches",
    page_icon="🚗",
    layout="wide"
)

st.header('Análisis de Anuncios de Venta de Coches Usados')
st.markdown('Esta aplicación interactiva permite explorar la distribución de precios, el kilometraje y la relación entre ambos, utilizando datos de anuncios de coches en EE. UU.')

@st.cache_data
def load_data():
    data = pd.read_csv('vehicles_us.csv')
    return data

car_data = load_data()

st.subheader('Selecciona las Visualizaciones:')

build_histogram = st.checkbox('Construir un Histograma de Kilometraje')
build_scatter = st.checkbox('Construir un Gráfico de Dispersión (Precio vs. Kilometraje)')


if build_histogram:
    st.markdown('### Distribución de Kilometraje')
    st.write('El histograma a continuación muestra la distribución del kilometraje ("odometer") de los vehículos anunciados.')

    fig_hist = px.histogram(
        car_data, 
        x="odometer", 
        title="Histograma de Kilometraje",
        labels={"odometer": "Kilometraje (millas)"}
    )

    st.plotly_chart(fig_hist, use_container_width=True)


if build_scatter:
    st.markdown('### Relación entre Precio y Kilometraje')
    st.write('El gráfico de dispersión muestra cómo el precio de un coche se relaciona con su kilometraje ("odometer").')
    
    fig_scatter = px.scatter(
        car_data, 
        x="odometer", 
        y="price", 
        title="Precio vs. Kilometraje",
        labels={"odometer": "Kilometraje (millas)", "price": "Precio ($)"},
        color="condition"
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

if st.checkbox('Mostrar los datos brutos'):
    st.subheader('Datos Brutos (Primeras 500 filas)')
    st.dataframe(car_data.head(500))