import os
os.system("cls")

print("Ola! Iremos verificar se você está ou não apto a receber aposentadoria! \n")

matricula = int(input("Dígite sua matricula de empregado (código) : \n"))
anonascimento = int(input("Digite o ano de seu nascimento:\n"))
anostrabalhados = int(input("Por quantos anos você trabalhou ? \n "))
anoatual = 2025
idade = anoatual - anonascimento

print("\n")
print(f"Seu código de empregado é {matricula} ")
print(f"Sua idade é {idade} anos")
print(f"Seu tempo trabalhado é de {anostrabalhados} anos")

if idade >= 65:
    if anostrabalhados >= 30: 
        print("Requer aposentaria! \n")
else:
        print("Não requer aposentadoria \n")