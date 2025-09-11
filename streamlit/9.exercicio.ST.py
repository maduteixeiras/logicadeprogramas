
#Escrever um programa de computador que solicite do usuário 5 números inteiros e, 
# ao final, apresente a soma de todos os números lidos

import os 
os.system("cls")

import streamlit as st 
st.title("Somar")

num1 = st.number_input(f"Digite o 1° valor : ", step=1)
num2  = st.number_input(f"Digite o 2° valor : ", step=1)
num3  = st.number_input(f"Digite o 3° valor : ", step=1)
num4 = st.number_input(f"Digite o 4° valor : ", step=1)
num5 = st.number_input(f"Digite o 5° valor : ", step=1)

resultado = num1 + num2 + num3 + num4 + num5

if st.button("somar valores"):
    st.success(f"Soma dos valores = {somas}" )
