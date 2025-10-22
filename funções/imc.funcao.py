import os 
os.system("cls")

# O índice de massa corpórea (IMC) de um indivíduo é obtido dividindo-se o seu peso
#  (em Kg) por sua altura (em metros) ao quadrado. 
#Assim, por exemplo, 
# uma pessoa de 1,67m e pesando 55kg tem IMC igual a 20,14, já que

#Escreva um programa que solicite ao utilizador o fornecimento do seu peso em kg e de sua altura em m 
# a partir deles calcule o índice de massa corpórea do utilizado

h = float(input("Informe sua altura (em metros): "))
kg = float(input("Informe seu peso (em kg): "))

def imc(kg, h): 
    return kg / (h * h)

def recomendacao(imc): 
    if imc < 18.5: 
        return "Abaixo do peso. Consulte um nutricionista para orientação"
    elif 18.5 <= imc <= 24.9: 
        return "Peso normal. Mantenha hábitos saudáveis"
    elif 25 <= imc <= 29.9: 
        return "Sobrepeso. Considere uma dieta balanceada e atividade física"
    elif 30 <= imc <= 34.9: 
        return "Obesidade grau 1. Procure orientação de um profissional de saúde"
    elif 35 <= imc <= 39.9: 
        return "Obesidade grau 2. Consulte um médico para avaliação e orientação"
    else:  # imc >= 40
        return "Obesidade grau 3. Busque assistência médica imediatamente"

print("\nResultado: " )
print(f"Seu IMC é: {imc(kg,h):.2f}")
print(recomendacao(imc(kg,h)))
