import streamlit as st
import time
st.success("todo correcto")
mensaje_error=st.error("se ha producido un error")
time.sleep(3)
mensaje_error.empty()
st.toast("Mensaje flotante",duration="long")
