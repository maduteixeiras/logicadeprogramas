# usado para importar e usar funções matematicas 
import math
# usado para importar e usar sistemas operacionais 
import os 
# ("cls") é usado para limpar o terminar, pode ser usado também entre linhas de codigo para deixar mais limpo 
os.system("cls")
import time


valor = int(input("Digite o valor \n"))
# atribruindo uma variavel a uma função para poder invocala e usar durante execução. 
# como são calculos matematicos uso a biblioteca math e uso math.(funçao existente da biblioteca)
raiz_q = math.sqrt(valor)
seno = math.sin(valor)

print(f"Raiz quadrada de {valor} = {raiz_q}")
print(f"O seno de {valor} = {seno}")

if valor: 
    os.system("cls")
    time.sleep(9)