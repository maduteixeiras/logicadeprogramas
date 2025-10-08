import os 
os.system("cls")
import calendar
from datetime import date
#Escreva um programa que solicite ao usuário o ano de
#nascimento e, utilizando uma função, retorne com a idade do
#usuário.

while True:
    data = int(input("digite data de nascimento: "))
    if data >= 1 and data <= 31: 
        break

while True: 
    mes = int(input("Digite o número correspondente ao seu mês de nascimento: "))
    if mes >= 1 and mes <= 12: 
        break 

while True: 
    ano = int(input("Digite seu ano de nascimento: "))
    if ano <= date.today().year:
        break

def calcular_idade(data_nascimento):
    hoje = date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

data_nasc = date(ano, mes, data)
idade = calcular_idade(data_nasc)
print(f"\nSua idade é: {idade} anos.")