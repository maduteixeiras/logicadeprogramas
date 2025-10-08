import os 
os.system("cls")

#Fazer um programa que solicita um valor em metros 
# e por meio de uma função,
# retorna o correspondente em centímetros.

valor_m = float(input("Digite um valor em metros: "))

def m_for_cm(valor_m): 
    cm = valor_m * 100
    return cm 

print(f"\nResultado : {m_for_cm(valor_m)}cm")