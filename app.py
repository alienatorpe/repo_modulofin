import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Cargar el modelo entrenado
with open('modelo_ia.pkl', 'rb') as file:
    modelo = pickle.load(file)

# Definir la interfaz de usuario en Streamlit
st.title('Predicción de Tickets de Soporte de TI')

# Controles de entrada para las características
subject = st.text_input('Título:','Escriba el título')
body = st.text_area('Mensaje', height=275)
type = st.selectbox('Tipo', ['Change', 'Incident', 'Problem', 'Request'])
department = st.selectbox('Departamento', ['Billing and Payments', 'Returns and Exchanges', 'Technical Support', 'Product Support', 'Customer Service', 'General Inquiry', 'Human Resources', 'Sales and Pre-Sales', 'Service Outages and Maintenance'])

# Botón para realizar predicción
if st.button('Predecir la prioridad'):

    # Crear DataFrame con las entradas
    input_data = pd.DataFrame([[subject, body, type, department]],
                    columns=['subject','body','type', 'department'])

    # Realizar predicción
    prediction = modelo.predict(input_data)

    # Mostrar predicción
    st.write(f'Prioridad predecida: {prediction[0]}')
