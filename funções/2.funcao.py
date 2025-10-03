import os 
os.system("cls")

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso "))

def boasvindas(nome, idade, altura, peso): 
    print(f"\nOlá {nome}. Seja Bem-Vindo(a) !")
    print(f"Sua idade é {idade} anos")
    print(f"Seu peso é {peso} kg")
    print(f"Sua altura é {altura}")

boasvindas(nome, idade, altura, peso)