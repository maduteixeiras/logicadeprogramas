import os 
os.system("cls")

print("Ola. Iremos calcular sei IMC!")
h = float(input("Qual sua altura? \n"))
kg = float(input("Qual seu peso? \n"))

imc = kg / (h * h)

print(f"Seu Índice de Massa Corporal é {imc} \n")

if imc <= 18.5:
    print("Abaixo do peso!")
elif imc <= 24.9: 
    print("Peso ideal. Parabéns!")
elif imc <= 29.9:
    print("Levemente acima do peso!")
elif imc <= 34.9:
    print("Obesidade gra 1")
elif imc <= 39.9:
    print("Obesidade grau 2")
else: 
    print("Obesidade grau 3")