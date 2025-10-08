import calendar
from datetime import date
import streamlit as st 

st.title("Calculando idade")


data = st.number_input("Digite o dia de nascimento:", min_value=1, max_value=31)
mes = st.number_input("Digite o mês de nascimento:", min_value=1, max_value=12)
ano = st.number_input("Digite o ano de nascimento:", max_value=date.today().year)

def calcular_idade(data_nascimento):
    hoje = date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

if st.button("Exibir idade"):
    data_nasc = date(int(ano), int(mes), int(data))
    idade = calcular_idade(data_nasc)
    st.success(f"Sua idade é: {idade} anos.")
