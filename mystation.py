import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Configuración de la página
st.set_page_config(page_title="Mi Proyecto", page_icon="📌", layout="wide")

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
st.write("Aquí puedes conocer más sobre lo que hacemos, nuestras redes sociales y ubicación.")

# Sección de redes sociales
st.subheader("📢 Conéctate con nosotros")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[Facebook](https://www.facebook.com)")
with col2:
    st.markdown("[Twitter](https://www.twitter.com)")
with col3:
    st.markdown("[Instagram](https://www.instagram.com)")

# Sección de ubicación
st.subheader("📍 Nuestra Ubicación")
mapa = folium.Map(location=[12.1364, -86.2519], zoom_start=15)  # Ubicación de Managua, Nicaragua
folium.Marker([12.1364, -86.2519], popup="Ubicación de Mi Proyecto").add_to(mapa)
st_folium(mapa, width=700, height=500)

# Sección de publicaciones
st.subheader("📝 Últimas Publicaciones")
if "posts" not in st.session_state:
    st.session_state.posts = []

new_post = st.text_area("Escribe una nueva publicación:")
if st.button("Publicar"):
    if new_post:
        st.session_state.posts.append(new_post)
        st.success("Publicación agregada con éxito!")
    else:
        st.warning("Por favor, escribe algo antes de publicar.")

# Mostrar publicaciones
for post in reversed(st.session_state.posts):
    st.write(f"💬 {post}")
