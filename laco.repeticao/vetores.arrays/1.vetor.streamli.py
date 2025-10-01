import streamlit as st


st.title("Calculadora de Média de Notas")



quantidade_notas = st.number_input(
    "Quantas notas você deseja inserir?",
    min_value=2,
    max_value=5,
    value=2,
    step=1 )


lista_notas = []
for i in range(int(quantidade_notas)):
    nota = st.number_input(
        f"Digite a {i+1}ª nota:",
        min_value=0.0,
        max_value=10.0,
        step=0.1 )
    lista_notas.append(nota)

if st.button("Calcular Média"):
    if not lista_notas or len(lista_notas) < 2:
        st.warning("Por favor, insira pelo menos 2 notas para calcular a média.")
    else:
        soma = sum(lista_notas)
        media = soma / len(lista_notas)
        menor_nota = min(lista_notas)
        maior_nota = max(lista_notas)
        
       
        st.info(f"Soma das notas: **{soma:.2f}**")
        st.info(f"Menor nota: **{menor_nota:.2f}**")
        st.info(f"Maior nota: **{maior_nota:.2f}**")

    
        if media >= 7:
            st.success("Parabéns! Você foi **aprovado**!")
        elif media >= 5:
            st.warning("Você foi para a **recuperação**!")
        else:
            st.error("Infelizmente você está **reprovado**.")