import os 
os.system("cls")

nota = int(input("Digite um numero menor que 10 e maior que 100 \n"))

if nota < 10 or nota > 100:
    print("válido!")
else:
    print("inválido!")

