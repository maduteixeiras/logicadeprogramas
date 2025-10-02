import os 
os.system("cls")

#Faça um algoritmo que mostre um menu com
#opções de um cardápio de restaurante para
#uma pessoa. A pessoa vai escolher o prato desejado.

#Após escolher o prato, o algoritmo deve
#perguntar ao usuário se ele deseja escolher
#outro prato.

#Quando o usuário não quiser mais realizar
#pedidos, mostre o nome e o valor dos pratos
#escolhidos e calcule o valor  total da conta.

lista_códigos = [1,2,3,4,5]
lista_pratos = ["Picanha", "Lasanha", "Strogonoff", "Bife Acebolado" , "Pão com ovo"]
lista_valores = [25.00, 20.00, 18,00, 15,00, 5.00]
lista_escolhas = []


print("""
Código \t Prato \t\t Valor

1 \t Picanha \t 25,00
2 \t Lasanha \t 20,00
3 \t Strogonoff \t 18,00
4 \t Bife Acebolado  15,00
5 \t Pão com ovo \t 5,00

""")

# Criar um loop principal que:
#Pergunte o código do prato.
#Verifique se é válido.
#Se válido, adicione na lista de escolhas.
#Pergunte se quer escolher outro prato.
#Se não quiser, saia do loop.
#Depois do loop, faça a soma dos valores e mostre o pedido.

while True: 
    escolha_codigo = int(input("Digite pelo código (1 a 5) qual prato deseja:\n"))
    
    if escolha_codigo in lista_códigos:
        lista_escolhas.append(escolha_codigo)
        
        outra_opcao = str(input("Deseja escolher outro prato? (S ou N)\n")).upper()
        if outra_opcao == "N":
            break
    else:
        print("Código inválido! Digite um número de 1 a 5.")

# Mostrar resumo do pedido
print("\n===== Seu Pedido =====")
total = 0
for codigo in lista_escolhas:
    prato = lista_pratos[codigo - 1]
    valor = lista_valores[codigo - 1]
    print(f"{prato} - R$ {valor: .2f}")
    total += valor

print(f"\nValor total da conta: R$ {total: .2f}")
        
            
        


    


    

        
