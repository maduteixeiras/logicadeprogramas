import os 
os.system("cls")

#Fazer um programa que solicita o preço de um produto e
#inflaciona esse preço em 10% 
# se ele for menor que 100 e
#em 20% se ele for maior ou igual a 100. 
#Utilize uma função com retorno para obter o resultado solicitado.

valor_produto = float(input("Valor do produto = "))

def inflacao(valor_produto): 
    if valor_produto < 100: 
        inflacionando = valor_produto + (valor_produto * 0.1) 
        porcentagem = 10
    else: 
        inflacionando = valor_produto + (valor_produto * 0.2)
        porcentagem = 20
    return inflacionando, porcentagem  

valor_inflacionado, porcentagem = inflacao(valor_produto)

# Exibe o resultado
print(f"""
Valor após inflação = R$ {valor_inflacionado:.2f}
Valor % da inflação adicionada = {porcentagem}%
""")

