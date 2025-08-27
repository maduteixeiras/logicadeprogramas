import os 
os.system("cls")

nome = str(input("Qual seu nome? \n"))
print(f"Ola {nome} !")
idade = int(input("Qual sua idade? \n"))

if idade < 16: 
    print("Você não pode votar!")
elif idade >= 65:
    print("Voto opcional!")
elif idade >= 18: 
    print("Voto obrigatorio!")
else:
    print("Voto opcional!")