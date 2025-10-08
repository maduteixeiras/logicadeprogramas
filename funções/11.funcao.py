#Escreva um programa que permita ler 3 notas de
#um aluno, usando laço de repetição e informe por
#meio de uma função a média;

QUANTIDADE_NOTAS = 3 
vetornotas = []


for i in range(QUANTIDADE_NOTAS): 
    notas = float(input(f"Digite sua {i+1}° nota: "))
    vetornotas.append(notas)
        
def media(notas):
    soma = sum(vetornotas) / QUANTIDADE_NOTAS
    return soma 

print(f"\nSua média foi de: {media(notas)}")