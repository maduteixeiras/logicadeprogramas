import streamlit as st
import time 

st.title("Mostrar números pares")

for i in range(100, 121, +2):
    st.write(i)
    time.sleep(0.5)