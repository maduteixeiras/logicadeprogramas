import os 
os.system("cls")

soma = 0 

for i in range(3): 
    nota = float(input(f"Digite sua {i+1}° nota: \n"))
    soma += nota 

print (f"Soam das notas = {soma}")

