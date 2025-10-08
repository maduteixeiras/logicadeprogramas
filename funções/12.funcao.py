#Escreva um programa que permita ler 2 notas de um aluno einforme
#por meio de funções:
 #A média;
 # Com base na média, se o aluno está aprovado ou reprovado.
# Critério para aprovação: média 7,0.

QUANTIDADE_NOTAS = 2 
vetornotas = []


for i in range(QUANTIDADE_NOTAS): 
    notas = float(input(f"Digite sua {i+1}° nota: "))
    vetornotas.append(notas)
        
def media(notas):
    soma = sum(vetornotas) / QUANTIDADE_NOTAS
    return soma 

print(f"\nSua média foi de: {media(notas)}")
if media(notas) >= 7 :
    print("Aprovado!")
else: 
    print("Reprovado! ")