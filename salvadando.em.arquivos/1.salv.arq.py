import os 
os.system("cls")

#texto que deseja salvar 
texto = input("Digite o que deseja salvar: ")

# definindo o nome de um arquivo para salvar o texto 
nome_arquivo = "salvar.txt"

#comandos para salvar 
#
with open(nome_arquivo, "a") as meu_arquivo: 
    meu_arquivo.write(f"{texto} \n")
    print("Salvo som sucesso")
