import os 
os.system("cls || clear")
from datetime import datetime
import time

alunos_cadastrados = []

class Endereco:
    def __init__(self,lougadouro, numero, cidade, estado):
        self.lougadouro = lougadouro
        self.numero = numero 
        self.cidade = cidade 
        self.estado = estado 

    def __str__(self): #organização do endereço para ser exibido em apenas uma linha
        return (f"{self.lougadouro}, {self.numero} | {self.cidade} - {self.estado}")

class Aluno: 
    # Atributo de CLASSE: o próximo RA a ser atribuído.
    proximo_ra = 1000 # Inicia o RA com um valor, ex: 1000
    def __init__(self, nome, nascimento, curso, endereco, cpf):
        self.nome = nome 
        self.nascimento = nascimento 
        self.curso = curso 
        self.endereco = endereco 
        self.cpf = cpf

        # Atribui o RA e incrementa o contador para o próximo aluno
        self.ra = Aluno.proximo_ra 
        Aluno.proximo_ra += 1 # Prepara o valor para o próximo aluno

    def ExibirDados(self): 
        print("-- Dados dos Alunos --")
        print(f"Nome: {self.nome}")
        print(f"Nascimento: {self.nascimento}")
        print(f"R.A: {self.ra}")
        print(f"Curso: {self.curso}")
        print(f"Endereço: {self.endereco}")
        print(f"")
        print("-------------------------")

#verificação da lista, Caso Vazio 
def ListaVazia(alunos_cadastrados): 
    if not alunos_cadastrados: 
        print("Não há alunos  cadastrados! ❌")
        return True
    return False 


#buscando aluno pelo cpf
def buscar_aluno_por_cpf(lista_alunos):
    # Verifica se a lista está vazia
    if ListaVazia(lista_alunos):
        return

    cpf_busca = input("➡️ Digite o CPF do aluno (somente números ou com pontuação): ").strip().replace('.', '').replace('-', '')
    aluno_encontrado = None
    for aluno in lista_alunos:
        cpf_aluno_formatado = aluno.cpf.strip().replace('.', '').replace('-', '')
        if cpf_aluno_formatado == cpf_busca:
            aluno_encontrado = aluno
            break 
    os.system("cls || clear")
    if aluno_encontrado:
        print(f"\n✅ Aluno encontrado para o CPF {cpf_busca}!")
        aluno_encontrado.ExibirDados()
    else:
        print(f"\n❌ Aluno com CPF {cpf_busca} não encontrado.")

# Exibir 
def ExibirDados(alunos_cadastrados): 
    if ListaVazia(alunos_cadastrados):
        return 
    
    print("\n==================================")
    print("📋 TODOS ALUNOS CADASTRADOS")
    print("==================================")
    for aluno in alunos_cadastrados: 
        alunos_cadastrados.ExibirDados() 
        time.sleep(0.5) 

# Atualizar
def AtualizarFuncionario(os_funcionarios_cadastrados): 
    if ListaVazia(os_funcionarios_cadastrados): 
        return
    
    ExibirDados(alunos_cadastrados)
    print("\n-- ATUALIZAR ALUNO --")

  