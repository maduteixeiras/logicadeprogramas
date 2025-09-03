 # condicionais compostas 
import os 
os.system("cls")

idade = int(input("digite sua idade:"))


if idade >= 60: 
    print("você é idoso")
elif idade >= 18 :
    print("você é adulto")
elif idade >=12: 
    print("você é adolescente")
else:
    print("você é criança")
