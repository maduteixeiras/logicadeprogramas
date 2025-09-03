num1 = float(input("Digite o primeiro valor:"))

print("Escolha um operador:")
print("soma = 1")
print("subtração = 2")
print("multiplicação = 3")
print("divisão = 4")
sinal = int(input("escolha um operador:"))

num2 = float(input("Digite  segundo número:"))

if sinal == 1:
    print(num1 + num2)
elif sinal == 2:
    print(num1 - num2)
elif sinal == 3:
    print(num1 * num2)
elif sinal == 4:
    print(num1 / num2)
