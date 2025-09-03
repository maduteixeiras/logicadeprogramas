import os 
os.system("cls")

numero = int(input("Digite um número: "))

match numero:
    case 1: 
        print("Corresponde a domingo")
    case 2: 
        print("Corresponde a segunda-feira")
    case 3: 
        print("Corresponde a terça-feira")
    case 4: 
        print("Corresponde a quarta-feira")
    case 5: 
        print("Corresponde a quinta-feira")
    case 6: 
        print("Corresponde a sexta-feira")
    case 7: 
        print("Corresponde a sábado")
    case _ : 
        print("Não corresponde a nenhuma dia")

  
    