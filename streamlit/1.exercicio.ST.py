# verificando a media 
# solicite o usuario a media do aluno 
# se maior ou igual a 7 mostre aprovado 
# caso contrario reprovado

import streamlit as st 
st.title("Verificando Média")

nota1 = st.number_input("Digite sua primeira nota:")
nota2 = st.number_input("Digite sua segunda nota:")

if st.button ("Confirmar notas "):
    media = (nota1 + nota2) / 2

    if media >= 7: 
        st.success(f"Sua média é {media}. Você foi aprovado!")
    else: 
        st.error(f"Sua média é {media}. Você foi reprovado!")
else:
    st.warning("Informe as notas")

# st.sucess = verde 
# st.error = vermelho 
# st.warning = amarelo 
# st.info = azul