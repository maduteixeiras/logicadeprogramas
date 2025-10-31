import os
os.system("cls")  # Limpa a tela (Windows)

QUAN_CAD = 2
lista_cadastros_alunos = []

class Aluno:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Solicitação de dados
for i in range(QUAN_CAD):
    print(f"\nSolicitando informações do aluno {i+1}:")
    nome_aluno = input("Digite o nome: ")
    idade_aluno = input("Digite a idade: ")
    email_aluno = input("Digite o e-mail: ")
    telefone_aluno = input("Digite o telefone: ")

    aluno = Aluno(nome_aluno, idade_aluno, email_aluno, telefone_aluno)
    lista_cadastros_alunos.append(aluno)

# Salvando dados no arquivo
arquivo = "dados_aluno.txt"

with open(arquivo, "a") as arquivo_alunos:
    for aluno in lista_cadastros_alunos:
        arquivo_alunos.write(f"Nome: {aluno.nome}, Idade: {aluno.idade}, "
                             f"E-mail: {aluno.email}, Telefone: {aluno.telefone}\n")

print("\nDados salvos com sucesso!")

