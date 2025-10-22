Proyecto Sprint 7: Análisis de Anuncios de Venta de Coches Usados

Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación web interactiva utilizando la librería Streamlit para el análisis exploratorio de datos (EDA) sobre anuncios de venta de coches en Estados Unidos (vehicles_us.csv).

La aplicación está diseñada para ser una herramienta de visualización de datos simple y efectiva, permitiendo a los usuarios generar gráficos clave con solo seleccionar una casilla de verificación.

Funcionalidad de la Aplicación

La aplicación proporciona las siguientes visualizaciones clave, generadas interactivamente:

1. Histograma de Kilometraje: Muestra la distribución de la columna odometer (kilometraje), permitiendo entender cuántos vehículos se encuentran en diferentes rangos de millas recorridas.

2. Gráfico de Dispersión (Precio vs. Kilometraje): Visualiza la relación directa entre el price (precio) y el odometer (kilometraje), con puntos de color según la condition (condición) del vehículo, lo cual es útil para identificar patrones de precios.

3. Datos Brutos: Opción para mostrar una vista previa de los datos brutos.

Requisitos de Ejecución

Para ejecutar esta aplicación localmente, se requiere tener instalado Python y las siguientes librerías, listadas en requirements.txt:

- pandas

- streamlit

- plotly_express

- nbformat