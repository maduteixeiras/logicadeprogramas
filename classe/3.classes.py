import os 
os.system("cls")

class pessoa: 
    def __init__(self,nome,idade,peso,altura): 
        self.nome = nome 
        self.idade = idade 
        self.peso = peso 
        self.altura = altura
    
    def apresentar(self): 
        print("\nInformações")
        print(f"Nome: {self.nome}\nIdade: {self.idade} anos\nPeso: {self.peso}kg\nAltura: {self.altura}m")


nome_user = input("Digite seu nome: ")
idade_user = input("Digite sua idade: ")
peso_user = input("Digite seu peso: ")
altura_user = input("Digite sua altura: ")

pessoa_user = pessoa(nome_user, idade_user, peso_user, altura_user)
pessoa_user.apresentar()









