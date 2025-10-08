import math

def menu():
    print("\nEscolha a operação desejada:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Raiz Quadrada")
    print("5 - Ao Quadrado")
    print("6 - Porcentagem")

def calcular(opcao, numeros):
    match opcao:
        case 1:  # Adição
            soma = 0
            for n in numeros:
                soma += n
            print("\nResultado da adição:", soma)

        case 2:  # Subtração
            resultado = numeros[0]
            for n in numeros[1:]:
                resultado -= n
            print("\nResultado da subtração:", resultado)

        case 3:  # Multiplicação
            resultado = 1
            for n in numeros:
                resultado *= n
            print("\nResultado da multiplicação:", resultado)

        case 4:  # Raiz quadrada de todos
            print("\nRaiz quadrada de cada número:")
            for n in numeros:
                if n >= 0:
                    print(f"{n} → {math.sqrt(n)}")
                else:
                    print(f"{n} → não existe raiz real")

        case 5:  # Ao quadrado de todos
            print("\nQuadrado de cada número:")
            for n in numeros:
                print(f"{n} → {n ** 2}")

        case 6:  # Porcentagem (considerando % de 100)
            print("\nPorcentagem (em relação a 100):")
            for n in numeros:
                print(f"{n}% de 100 = {(n * 100) / 100}")

        case _:
            print("\nOpção inválida!")


continuar = "s"
while continuar == "s":
    qtd = int(input("\nQuantos números deseja informar? "))
    numeros = []
    for i in range(qtd):
        n = float(input(f"Digite o {i+1}º número: "))
        numeros.append(n)

    menu()
    opcao = int(input("\nDigite a opção desejada: "))

    calcular(opcao, numeros)

    continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()

print("Encerrando a calculadora...")