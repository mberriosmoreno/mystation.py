import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("📍 Nuestra Ubicación")

mapa = folium.Map(location=[12.1364, -86.2519], zoom_start=15)
folium.Marker([12.1364, -86.2519], popup="Ubicación de Mi Proyecto").add_to(mapa)

st_folium(mapa, width=700, height=500)
