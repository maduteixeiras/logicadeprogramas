import streamlit as st
st.title("Calculos")

# elobore um algoritmo que solicita 2 numeros e apos mostre no final a media, soma, produto, o menor e o maior valor 

num1 = st.number_input("Digite o primeiro valor:")
num2 = st.number_input("Digite o segundo valor: ")

soma = num1 + num2 
produto = num1 * num2 
media = (num1 + num2) / 2 
maiornum = max(num1, num2)
menornum = min(num1, num2)

if st.button("Confirmar valores desejados"):
    if num1 and num2:
        st.success(f"Média: {media}")
        st.info(f"Produto: {produto}")
        st.success(f"Soma: {soma}")
        st.info(f"Menor valor: {menornum}")
        st.success(f"Maior Valor: {maiornum}")
else:
    st.warning("Informe  os valores")

