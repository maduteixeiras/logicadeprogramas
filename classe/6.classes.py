import os
os.system("cls")

QUANTIDADE_CAD = 2

class Cadastro:
    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco

    def mostrar_dados(self):
        print(f"""
Nome: {self.nome}
E-mail: {self.email}
Endereço: {self.endereco}""")

    def mostra_apenas_nome(self): 
        print(f"Nome: {self.nome}")

cadastros = [] # criando lista para armazenar dados

for i in range(QUANTIDADE_CAD):
    user_nome = input(f"Digite o nome para o cadastro {i+1}: ")
    user_email = input(f"Digite o e-mail para o cadastro {i+1}: ")
    user_endereco = input(f"Digite o endereço para o cadastro {i+1}: ")
    
    # Cria o objeto e adiciona na lista
    pessoa = Cadastro(user_nome, user_email, user_endereco)
    cadastros.append(pessoa)
    
    os.system("cls")

print("=== DADOS CADASTRADOS ===")
for pessoa in cadastros:
    pessoa.mostrar_dados()

print("\n=== NOMES CADASTRADOS ===")
for pessoa in cadastros:
    pessoa.mostra_apenas_nome()
