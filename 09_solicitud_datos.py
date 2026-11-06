import streamlit as st
import time

nombre=st.text_input("introduce tu nombre")
edad=st.number_input("introduce tu edad")
afiliado=st.checkbox("afiliado")
curso=st.radio("elige un curso: ",["python","C++","Java"])
centro=st.selectbox("Elige centro: ",["Leganes","Getafe","Alcobendas","San blas"])
if st.button("pulsar"):
    st.success(f"te llamas {nombre}, tienes {edad}, años, has elegido el curso {curso}")
    
aula = [ 
    {"id": 1, "nombre": "Juan", "edad": 25}, 
    {"id": 2, "nombre": "Ana", "edad": 30}, 
    {"id": 3, "nombre": "Pedro", "edad": 22} 
] 
st.table(aula) 
