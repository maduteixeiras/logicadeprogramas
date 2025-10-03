import os 
os.system("cls")

# faça um programa que imprime a tabuada de uma número informado pelo usuario
# de 1 a 10 
# ultilizando uma funcao para exibir o resultado 
QUANT = 10

while True: 
    numero = int(input("Qual número deseja saber a tabuada? (1 a 10) \n"))
    if numero >= 1 and numero <= 10: 
        break
    else: 
        print("\nInforme uma tabuada que consta no sistema!")

def tabuada(numero): 
    for i in range(1,11):
        print(f"{i} x {numero} = {numero * i}")


print("\nTabuada:")
tabuada(numero)