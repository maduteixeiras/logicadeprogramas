# Verifique a idade de uma pessoa 
# se for menor que 18, mostre : menor de idade 
# caso contrario, mostre: maior de idade 
# usando streamlit 

import streamlit as st
st.title("Autorização de Acesso")

idade = st.number_input("Digite sua idade: ", min_value= 0, max_value= 140, step=1)

if st.button ("Confirmar"):
    if idade >= 18:
        st.write("Maior de Idade. Autorizado!!!")
    else:
        st.write("Menor de idade. Não Autorizado!! ")
else: 
    st.write("Por favor digite sua idade!")