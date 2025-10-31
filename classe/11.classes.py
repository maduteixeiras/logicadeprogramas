import os 
os.system("cls")

class Endereco: 
    def __init__(self,lougadouro, numero): 
        self.lougadouro = lougadouro
        self.numero = numero

    def __str__(self): # organizando o endereço para exibir em apenasuma linha
        return (f"{self.lougadouro}, {self.numero}")


class Pessoa: 
    def __init__(self,nome, idade,endereco):
        self.nome = nome   
        self.idade = idade 
        self.endereco = endereco

    def ExibirInfo(self):
        print(f"Nome = {self.nome}\nIdade = {self.idade}\nEndereço = {self.endereco}")

lougadouro_user = input("Digite seu lougadouro: ")
numerocasa_user = input("Digite número do lougadouro: ")
user_endereco = Endereco(lougadouro_user, numerocasa_user)

nome_user = input("Digite seu nome: ")
idade_user = input("Digite sua idade: ")

InfoUser = Pessoa(nome_user, idade_user, user_endereco)
InfoUser.ExibirInfo()


