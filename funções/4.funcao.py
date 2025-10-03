import os 
os.system("cls")

# afaca uma funcao que recebe um valor inteiro
#  e verifica se ele é negatico ou positivo 

valor = int(input("Digite um valor: "))

def verificando(valor): 
    os.system("cls")
    if valor < 0: 
        print("Valor negativo")
    elif valor > 0: 
        print("valor positivo!")
    else: 
        print("valor igual a zero!")

verificando(valor)