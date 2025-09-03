import os
os.system("cls")

print("""
Código \t Prato \t\t Valor
1 \t Picanha \t 25,00
2 \t Lasanha \t 20,00
3 \t Strogonoff \t 18,00
4 \t Bife Acebolado  15,00
5 \t Pão com ovo \t 5,00

""")

while True:
    codigo = int(input("Digite o código do prato desejado: \n"))

    if codigo <= 5 and codigo >= 1:
        break 

    match codigo:
        case _:
            print("Prato Inválido. Escolha um prato disponível! ")
match codigo:
        case 1:
            print("PICANHA : 25,00")
        case 2:
            print("LASANHA : 20,00")
        case 3:
            print("STROGONOFF: 18,00")
        case 4: 
            print("BIFE ACEBOLADO: 15,00")
        case 5: 
            print("PÃO COM OVO: 5,00")