#Escrever um algoritmo que solicite ao usuário um
#número e faça a contagem regressiva a partir do
#número informado até o número 1, aguardando um
#segundo para exibir cada número.

import streamlit as st 
import time 
st.title("Contagem Regressiva")

num = st.number_input("Digite o número")

if st.button("Iniciar contagem"):
    

