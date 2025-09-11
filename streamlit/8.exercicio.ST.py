#Escrever um algoritmo que solicite ao usuário um
#número e faça a contagem regressiva a partir do
#número informado até o número 1, aguardando um
#segundo para exibir cada número.
import os
os.system("cls")

import streamlit as st 
st.title("Contagem Regressiva")

import time 

num = st.number_input("Digite o número: \n" , step=1)

if st.button("Iniciar contagem"):
    for i in range(num, 0, -1): 
        st.success(i) 
        time.sleep(0.3)
    st.header("fim da contagem")