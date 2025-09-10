import streamlit as st
import time 

st.title("Laço de Repetição = FOR ")

st.header("Contagem")
num = st.number_input("Até qual número deseja fazer a contagem? ", step= 1)

if st.button("Iniciar ação"):
    for i in range(1,num+1):
        st.write(i)
        time.sleep(1)
    
    st.header("FIM")