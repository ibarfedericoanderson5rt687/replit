
import streamlit as st
import sys
import os

# Agregar el directorio actual al path para importar módulos
sys.path.append(os.path.dirname(__file__))

# Importar la aplicación de Streamlit
from static.app_qrgb_streamlit import main

# Ejecutar la aplicación Streamlit
if __name__ == "__main__":
    main()
