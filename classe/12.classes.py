import os 
os.system("cls")

class Autor: 
    def __init__(self,nome, biografia): 
        self. nome = nome 
        self.biografia = biografia

    def __str__(self): # organizando o endereço para exibir em apenasuma linha
        return (f" {self.nome} - {self.biografia}")

class Livro: 
    def __init__(self,titulo, ano, autor): 
        self.titulo = titulo
        self.ano = ano 
        self.autor = autor 

    def ExibirDetalhes(self): 
        os.system("cls")
        print("Exibindo informações do Livro:\n")
        print(f"Nome do Autor: {self.autor}")
        print(f"Nome do Livro: {self.titulo}")
        print(f"Ano do livro: {self.ano}")

user_nomeautor = input("Digite nome do Autor: ")
user_biografiaautor = input("Digite biografia do Autor: ")
nome_e_bio_autor = Autor(user_nomeautor,user_biografiaautor)

user_titulolivro = input("Digite Título do LIvro: ")
user_anolivro = input("Digite Ano do Livro: ")

todas_info_livro = Livro(user_titulolivro,user_anolivro, nome_e_bio_autor)

todas_info_livro.ExibirDetalhes()