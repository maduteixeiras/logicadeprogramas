import os 
os.system("cls")
import math
#SEM OS VETORES : 
#soma = 0 
#for i in range(3): 
#    nota = float(input(f"Digite sua {i+1}° nota: \n"))
#    soma += nota 
#print (f"Soma das notas = {soma}")


#             ========= COM OS VETORES =======
lista_notas = []

# usuario pode escolhe quantas notas deseja inserir sendo min de 2 e max de 5, senão retorna a pergunta 
while True: 
    quantidade_notas = int(input("Quantas notas deseja inserir? (máx de 5 notas)\n"))
    if quantidade_notas >= 2 and quantidade_notas <= 5: 
        break
    else: 
        print("\nVocê pode inserir entre 2 e 5 notas!")

# caso seja entre 2 e 5 notas parta inserir ele vai para outra etapa, inseriri suas notas 
#sendo que a maior nota que ele pode inserir é 10 
print("\n=== INSERINDO AS NOTAS ===")
for i in range(quantidade_notas): 
    while True: 
        nota = float(input(f"Digite sua {i+1}° nota:\n"))
        # a nota SÓ é guardada no vetor se for menor que 10 
        if nota >= 0 and nota <= 10: 
            lista_notas.append(nota)
        # soma =+ nota === soma todas as notas
            soma = sum(lista_notas)
        # media 
            media = soma / quantidade_notas

        if nota >= 0 and nota <= 10: 
            break
        else: 
            print("\nA nota max é 10.00!")

# calculando o menor e maior valor
menor_nota = min(lista_notas)
maior_nota = max(lista_notas)

# estrutura para printar as notas válidas 
print("\n=== SUAS NOTAS ===")
for i in range(quantidade_notas):
    print(f"{i+1}° nota : {lista_notas[i]}")
# printando os resultados que foram validados 
print("\n===  MÉDIA ===")
print(f"Menor nota  : {menor_nota}")
print(f"Maior nota foi : {maior_nota}")
print(f"Soma das notas : {soma: .2f}")
print(f"Sua média foi de : {media: .2f} ")

# requisitos de aprovação
print("\n=== RESULTADO FINAL ===")
if media >= 7: 
    print("Parabens! Você foi aprovado")
elif media >= 5: 
    print("Você foi para a recuperação!")
else: 
    print("Infelizmente você está reprovado!")


