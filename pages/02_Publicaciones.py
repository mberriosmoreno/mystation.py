import streamlit as st

st.title("📝 Últimas Publicaciones")

if "posts" not in st.session_state:
    st.session_state.posts = []

new_post = st.text_area("Escribe una nueva publicación:")
if st.button("Publicar"):
    if new_post:
        st.session_state.posts.append(new_post)
        st.success("Publicación agregada con éxito!")
    else:
        st.warning("Por favor, escribe algo antes de publicar.")

for post in reversed(st.session_state.posts):
    st.write(f"💬 {post}")
