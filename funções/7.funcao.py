#Crie funções que recebam 2 números e retorne a soma,
#subtração, divisão e a multiplicação destes dois números
#informados.
#Obs.: Crie uma função para cada operação.

import os 
os.system("cls")
# criando funções das operações 
def soma(n1,n2): 
    return n1 + n2 
def sub (n1,n2):
    return n1 - n2 
def div(n1,n2):
    return n1 / n2 if n2 != 0 else "Divisão por 0"
def mult(n1,n2): 
    return n1*n2 

#solicitando os valores 
n1 = int(input("Digite o 1° valor: "))
n2 = int(input("Digite o 2° valor: "))

#exibindo os valores
print(f"""
Resultados: 
Soma -> {soma(n1,n2)}
Subtração -> {sub(n1,n2)}
Multiplição -> {mult(n1,n2)}
Divisão -> {div(n1,n2)}
""")


