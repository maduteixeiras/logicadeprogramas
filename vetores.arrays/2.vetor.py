import os 
os.system("cls")
#Crie um programa que leia 6 números, armazenando em um vetor e informe quantos são pares
# e quantos são ímpares.
#Mostre os números informados pelo usuário.

QUANT_NUMERO = 6
vetor_numeros = []
pares = 0 
impares = 0 

for i in range(QUANT_NUMERO):
    numero = int(input(f"Digite o {i+1}° número:\n"))
    vetor_numeros.append(numero)

    if numero%2 == 0: 
        pares += 1
    else: 
        impares += 1

print("\n==== INFORMAÇÕES ====")
print(f"Quantidade de números pares = {pares}")
print(f"Quantidade de números pares = {impares}")