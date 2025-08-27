import os
os.system("cls")

nome = str(input("Qual seu nome? \n"))
nota1 = float(input("Qual sua primeira nota? \n"))
nota2 = float(input("Qual sua segunda nota? \n"))

media = (nota1 + nota2) / 2

print(f"Oi {nome}, sua média é: {media} \n")
if media >= 9: 
    print("APROVADO! Entrou no conceito A")
elif media >= 7.5:
    print("APROVADO! Entrou no conceito B")
elif media >= 6:
    print("APROVADO! Entrou no conceito C")
elif media >= 4:
    print("REPROVADO! Entrou no conceito D")
else:
    print(f"REPROVADO! Entrou no conceito E ")
    