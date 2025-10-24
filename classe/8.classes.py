import os
os.system("cls")

QUANT_CAD = 1
lista_cadastros = []

class Endereco:
    def __init__(self, lougadouro, numero_casa): 
        self.lougadouro = lougadouro
        self.numero_casa = numero_casa

    def __str__(self):
        return f"{self.lougadouro}, {self.numero_casa}"

class Pessoa: 
    def __init__(self, nome, idade, endereco): 
        self.nome = nome 
        self.idade = idade 
        self.endereco = endereco

    def mostrar_dados(self): 
        print("Exibindo os dados do cliente:\n")
        print(f"Nome = {self.nome}")
        print(f"Idade = {self.idade}")
        print(f"Endereço = {self.endereco}\n")

for i in range(QUANT_CAD): 
    lougadouro_user = input("Digite Lougadouro: ")
    numero_casa_user = input("Digite Número do Lougadouro: ")
    endereco_user = Endereco(lougadouro_user, numero_casa_user)

    nome_user = input("Digite nome: ")
    idade_user = input("Digite idade: ")

    dados_pessoa = Pessoa(nome_user, idade_user, endereco_user)
    lista_cadastros.append(dados_pessoa)

    os.system("cls")

for dados_pessoa in lista_cadastros: 
    dados_pessoa.mostrar_dados()


