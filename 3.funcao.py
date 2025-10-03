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
            return sum(numeros)
        case 2:  # Subtração
            resultado = numeros[0]
            for n in numeros[1:]:
                resultado -= n
            return resultado
        case 3:  # Multiplicação
            resultado = 1
            for n in numeros:
                resultado *= n
            return resultado
        case 4:  # Raiz quadrada (primeiro número apenas)
            return math.sqrt(numeros[0])
        case 5:  # Ao quadrado (primeiro número apenas)
            return numeros[0] ** 2
        case 6:  # Porcentagem (primeiro número é o valor, segundo é a %)
            if len(numeros) < 2:
                return "Para porcentagem informe pelo menos 2 números (valor e %)."
            return (numeros[0] * numeros[1]) / 100
        case _:
            return "Opção inválida!"

# Programa principal (sem main)
while True:
    try:
        qtd = int(input("\nQuantos números deseja informar? "))
        numeros = []
        for i in range(qtd):
            n = float(input(f"Digite o {i+1}º número: "))
            numeros.append(n)

        menu()
        opcao = int(input("Digite a opção desejada: "))

        resultado = calcular(opcao, numeros)
        print("Resultado:", resultado)

        continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if continuar != "s":
            print("Encerrando a calculadora...")
            break
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
