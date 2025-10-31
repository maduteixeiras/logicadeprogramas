import os 
os.system("cls")

QUANTIDADE_LIVROS = 3
lista_livros = []

class Livro: 
    def __init__(self, nome, autor, categoria, preco): 
        self.nome = nome
        self.autor = autor 
        self.categoria = categoria
        self.preco = preco

for i in range(QUANTIDADE_LIVROS): 
    print("Solicitando informações: ")
    nome_livro = input("Digite nome do livro: ")
    autor_livro = input("Digite nome do autor: ")
    categoria_livro = input("Digite categoria do livro: ")
    preco_livro = input("Digite valor do livro: ")

    livro = Livro(nome_livro, autor_livro, categoria_livro, preco_livro)
    lista_livros.append(livro)

print("Salvando informações do livro! ")

arquivo = "catalogo_livros.txt"

with open(arquivo, "a") as arquivo_livros: 
    for livro in lista_livros: 
        arquivo_livros.write(f"Nome: {nome_livro}, Autor: {autor_livro}, Categoria: {categoria_livro}, Valor: {preco_livro}\n")
     