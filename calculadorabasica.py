num1 = float(input("Digite o primeiro valor:"))
num2 = float(input("Digite  segundo número:"))

print("Escolha um operador:")
sinal = int(input("1 = soma 2 = subtração 3 = multipiclação 4 = multiplicação"))

if sinal == 1:
    print(num1 + num2)
elif sinal == 2:
    print(num1 - num2)
elif sinal == 3:
    print(num1 * num2)
elif sinal == 4:
    print(num1 / num2)

