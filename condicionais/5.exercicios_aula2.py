import os 
os.system("cls")

nome = str(input("Qual seu nome? \n"))
print(f"Olá {nome}! Iremos te ajudar a calcular sua média:")

nota1 = float(input("digite sua primeira nota: \n"))
nota2 = float(input("digite sua segunda nota: \n"))
nota3 = float(input("digite sua terceira nota: \n"))

media = (nota1 + nota2 + nota3) / 3
print(f"sua media é: {media:.2f}")

if media >= 7:
        print("Parabénss {nome}!! Você foi aprovado(a).")
else:
    print("Infelizmente, você foi reprovado(a).")