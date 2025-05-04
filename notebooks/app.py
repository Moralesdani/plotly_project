import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la app
st.title('Análisis de autos en venta (US)')

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Histograma del odómetro
st.subheader('Histograma del Odómetro')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches en Estados Unidos')
    fig = px.histogram(car_data, x='odometer', nbins=30, title='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión: Año vs Precio
st.subheader('Gráfico de Dispersión: Año vs Precio')
scatter_button = st.button('Mostrar gráfico de dispersión')

if scatter_button:
    st.write('Gráfico de dispersión que muestra la relación entre el año del modelo y el precio.')
    fig2 = px.scatter(car_data, x='model_year', y='price',
                      title='Relación entre el Año del Modelo y el Precio',
                      labels={'model_year': 'Año del modelo', 'price': 'Precio ($)'},
                      opacity=0.6)
    st.plotly_chart(fig2, use_container_width=True)