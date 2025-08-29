import os 
os.system("cls")

valor1 = float(input("Digite o primeiro número: \n"))
valor2 = float(input("Digite o segundo número: \n"))



operador = input("Escolha um dos operadores: + x - % \n" )

soma = (valor1 + valor2) 
sub = (valor1 - valor2)
multi = (valor1 * valor2)
div = (valor1 / valor2)

match operador:
    case "+":
        print(f"RESULTADO: {soma}")
    case "-":
        print(f"RESULTADO: {sub}")
    case "x":
        print(f"RESULTADO: {multi}")
    case "%":
        print(f"RESULTADO: {div}")
    case _:
        print("operador inválido :(")