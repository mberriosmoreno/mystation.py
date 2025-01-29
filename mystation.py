import streamlit as st

# Configuración de la página
st.set_page_config(page_title="My Station", page_icon="📌", layout="wide")

# Estilos personalizados
st.markdown("""
    <style>
        .main {background-color: #f5f5f5;}
        h1, h2, h3 {color: #0070C0;}
        .stButton>button {background-color: #FFD700; color: #000; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# Encabezado
st.title("Bienvenido a Mi Proyecto 🚀")
st.write("Explora nuestras diferentes secciones en el menú lateral.")
