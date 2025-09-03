import os 
os.system("cls")

macas = float(input("Quantas maçãs você deseja? \n"))

maisde12 = macas*1
menosde12 = macas*1.30

if macas >= 12: 
    print(f"Valor a ser pago: {maisde12}$")
else:
    print(f"Valor a ser pago: {menosde12}$")