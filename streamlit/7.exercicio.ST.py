import streamlit as st 
import time 
st.title("Tabuada")

num = st.number_input("Digite o número: \n", step=1 )

if st.button("calcular"):
    for i in range(1, 11):
        st.success (f"{num} x {i} = {num*i}")
        time.sleep(0.1)

    st.header("fim")