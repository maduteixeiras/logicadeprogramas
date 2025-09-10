import streamlit as st
import time 

st.title("Laço de Repetição = FOR ")

st.header("Mostrar 10x o número na tela")
num = st.number_input("Digite um número: ", step= 1)

if st.button("Iniciar ação"):
    for i in range(1,11):
        st.write(num)
        time.sleep(1)
    
    st.header("FIM")