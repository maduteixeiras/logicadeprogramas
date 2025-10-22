import os
os.system("cls")

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

nome_user = input("Digite seu nome: ")
idade_user = input("Digite sua idade: ")

pessoa_user = pessoa(nome_user, idade_user)
pessoa_user.apresentar()