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
            soma = sum(numeros)
            print("Resultado da adição:", soma)

        case 2:  # Subtração
            resultado = numeros[0]
            for n in numeros[1:]:
                resultado -= n
            print("Resultado da subtração:", resultado)

        case 3:  # Multiplicação
            resultado = 1
            for n in numeros:
                resultado *= n
            print("Resultado da multiplicação:", resultado)

        case 4:  # Raiz quadrada de todos
            print("Raiz quadrada de cada número:")
            for n in numeros:
                if n >= 0:
                    print(f"{n} → {math.sqrt(n)}")
                else:
                    print(f"{n} → Não existe raiz real")

        case 5:  # Ao quadrado de todos
            print("Quadrado de cada número:")
            for n in numeros:
                print(f"{n} → {n ** 2}")

        case 6:  # Porcentagem de todos
            print("Porcentagem (valor → resultado):")
            for n in numeros:
                print(f"{n}% de 100 = {(100 * n) / 100}")
                # aqui fiz a conta em cima de 100, mas dá pra adaptar
        case _:
            print("Opção inválida!")

# Programa principal
while True:
    try:
        qtd = int(input("\nQuantos números deseja informar? "))
        numeros = []
        for i in range(qtd):
            n = float(input(f"Digite o {i+1}º número: "))
            numeros.append(n)

        menu()
        opcao = int(input("Digite a opção desejada: "))

        calcular(opcao, numeros)

        continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if continuar != "s":
            print("Encerrando a calculadora...")
            break
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
