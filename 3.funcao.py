import os 
os.system("cls")
import math

numero = int(input("Digite um número: "))

def aoquadrado(numero): 
    quadrado = numero*numero
    print(f"Resultado de {numero}^2 : {quadrado}")

def raizq(numero): 
    raiz2 = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é: {raiz2}")


def soma2nums(numero): 
    somas = numero + numero
    print(f"Adição desse número: {somas}")

print("\n")
raizq(numero)
aoquadrado(numero)
soma2nums(numero)