import os 
os.system("cls")

idade = int(input("Qual sua idade? \n"))

if idade >= 18 and idade < 65:
    print("voto obrigatório !")
elif idade == 16 or idade == 17 or idade >= 65:
    print("voto opcional !")
else:
    print("Não pode votar !")