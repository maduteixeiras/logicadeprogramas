import os 
os.system("cls")

#Crie um algoritmo que preencha um vetor com 5 números,
#  mostre a quantidade de números negativos 
# e a soma dos números positivos desse vetor.

QUANTIDADE_VETOR = 5
vetor_numeros= []
negativo = 0 
positivo = 0 
zero = 0 
soma_positivos = 0 

for i in range(QUANTIDADE_VETOR):
    numero = float(input(f"Digite o {i+1}° número:\n"))
    vetor_numeros.append(numero)
    
    if numero > 0 :
        positivo = positivo + 1
        soma_positivos = soma_positivos + numero
    elif numero == 0 : 
        zero = zero + 1
    else: 
        negativo = negativo + 1

print("\n=============================================")
print(f"Todos os números digitados : {vetor_numeros}")
print(f"Números Positivos = {positivo}")
print(f"Números Negativos = {negativo}")
print(f"Soma dos números Positivos: {soma_positivos}")
print(f"Números neutros = {zero}")
