import os 
os.system("cls")

#Crie um algoritmo que receba do usuário valores e armazene em um vetor 5 números, 
# caso seja informado um valor negativo, atribua o valor 0.  Liste os valores do vetor.

QUANTIDADE_VALORES = 5 
vetor_valores = []

print("=== Solicitando os valores ===")
for i in range(QUANTIDADE_VALORES):
    valor = int(input(f"Digite o {i + 1}° valor: "))
    if valor < 0: 
        valor = 0 

    vetor_valores.append(valor)

print("=== Exibindo os valores ===")
for i, valor in enumerate(vetor_valores, start=1): 
    print(f"{i}° número = {valor}")