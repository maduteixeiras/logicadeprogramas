import os
import time

# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(3) # Espera 3 segundos.
    os.system("cls")

# Função com parâmetros e com retorno.
def somar(n1, n2):
    return n1 + n2

# Função com parâmetros e sem retorno.
def mostrar_resultado(soma):
    print(f"Resultado: {soma}")

# Código principal.
# Função sem parâmetros e sem retorno.
limpa_tela() # Chamando a função.

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

# Função com parâmetros e com retorno.
soma = somar(primeiro_numero, segundo_numero)

# Função com parâmetros e sem retorno.
mostrar_resultado(soma) # Chamando a função.

