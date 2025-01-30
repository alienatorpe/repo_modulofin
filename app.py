import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Cargar el modelo entrenado
with open('modelo_rfr.pkl', 'rb') as file:
    modelo = pickle.load(file)

# Definir la interfaz de usuario en Streamlit
st.title('Predicción de Precios de Laptops')

# Controles de entrada para las características
inches = st.number_input('Tamaño de Pantalla (pulgadas)', min_value=10.0, max_value=19.0, value=10.1)
ram = st.number_input('Memoria RAM (GB)', min_value=1, max_value=64, value=8)
screen_width = st.number_input('Ancho de Pantalla (pixeles)', min_value=800, max_value=4000, value=1920)
screen_height = st.number_input('Alto de Pantalla (pixeles)', min_value=600, max_value=3000, value=1080)
ghz = st.number_input('GHz del CPU', min_value=0.1, max_value=5.0, value=2.5)
hdd = st.number_input('HDD (GB)', min_value=0, max_value=2000, value=0)
ssd = st.number_input('SSD (GB)', min_value=0, max_value=2000, value=256)
flashstorage = st.number_input('FlashStorage (GB)', min_value=0, max_value=2000, value=0)
hddextra = st.number_input('HDD extra (GB)', min_value=0, max_value=2000, value=0)
peso = st.number_input('Peso (Kg)', min_value=1.0, max_value=10.0, value=1.5)

type_2en1 = st.selectbox('¿Es 2 en 1 Convertible?', ['No', 'Sí'])
type_gaming = st.selectbox('¿Es Gaming?', ['No', 'Sí'])
type_netbook = st.selectbox('¿Es Netbook?', ['No', 'Sí'])
type_notebook = st.selectbox('¿Es Notebook?', ['No', 'Sí'])
type_ultrab = st.selectbox('¿Es Ultrabook?', ['No', 'Sí'])
type_workst = st.selectbox('¿Es Workstation?', ['No', 'Sí'])

# Convertir entradas a formato numérico
type_2en1 = 1 if type_2en1 == 'Sí' else 0
type_gaming = 1 if type_gaming == 'Sí' else 0
type_netbook = 1 if type_netbook == 'Sí' else 0
type_notebook = 1 if type_notebook == 'Sí' else 0
type_ultrab = 1 if type_ultrab == 'Sí' else 0
type_workst = 1 if type_workst == 'Sí' else 0

# Botón para realizar predicción
if st.button('Predecir el precio'):

    # Crear DataFrame con las entradas
    input_data = pd.DataFrame([[inches,ghz,ram,peso,screen_width, screen_height, type_2en1, type_gaming, type_netbook, type_notebook, type_ultrab, type_workst, hdd, ssd, flashstorage, hddextra]],
                    columns=['Inches','Cpu','Ram', 'Weight','Screen_width', 'Screen_height','TypeName_2 in 1 Convertible','TypeName_Gaming', 'TypeName_Netbook', 'TypeName_Notebook', 'TypeName_Ultrabook', 'TypeName_Workstation','HDD', 'SSD','FlashStorage', 'HDDExtra'])

    # Realizar predicción
    prediction = modelo.predict(input_data)

    # Mostrar predicción
    st.write(f'Precio predecido: {prediction[0]:.2f} euros')
