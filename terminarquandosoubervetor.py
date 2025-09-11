
#Escrever um programa de computador que solicite do usuário 5 números inteiros e, 
# ao final, apresente a soma de todos os números lidos

import os 
os.system("cls")

import streamlit as st 
st.title("Somar")

for i in range(1,6): 
    num = st.number_input(f"Digite o {i}° valor : ", step=1)
    
if st.button("somar valores"):
    st.success(f)

# TERMINAR QUANDO APRENDER A USAR VETOR NO PYTHON 


    


