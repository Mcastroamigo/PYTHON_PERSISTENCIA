import streamlit as st
libros=[]
tab_nuevo,tab_todos,tab_buscar,tab_precios=st.tabs(["Nuevo libro","Mostrar todos","Buscar por título","Libros por precio máximo"])
with tab_nuevo:
    titulo=st.text_input("Introduce título:")
    autor=st.text_input("Introduce autor:")
    precio=st.number_input("Introduce precio:")
    if st.button("Guardar libro"):
        libros.append({"titulo": titulo, "autor": autor, "precio": precio})
with tab_buscar:
    titulo=st.text_input("Introduce el título del libro a buscar: ")
    if st.button("Buscar"):
        libs=list(filter(lambda lib:lib["titulo"].lower()==titulo.lower(),libros))
        if libs:
            st.success(f"Titulo: {libs[0]["titulo"]}, Autor: {libs[0]["autor"]}, Precio: {libs[0]["precio"]}")
        else:
            st.error("Libro no encontrado")
with tab_todos:
    st.title("Listado de libros")
    st.table(libros)