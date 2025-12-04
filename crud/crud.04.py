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


#adiconando aluno 

def AdicionarAluno(alunos_cadastrados): 
    print("-- Adicionando Alunos --")
    nome = input("Digite nome: ")
    nascimento = input("Digite nascimento: ")
    curso = input("Digite curso: ")
    lougadouro = input("Digite lougradouro: ") 
    numero = input("Digite n° da casa: ")
    cidade = input("Digite cidade: ")
    estado = input("Digite estado: ")
    cpf = input("Digite CPF: ").strip().replace('.', '').replace('-', '')

    endereco_aluno = Endereco(lougadouro=lougadouro, numero=numero, cidade=cidade, estado=estado)
    novo_aluno = Aluno(nome=nome, nascimento=nascimento, curso=curso, endereco=endereco_aluno, cpf= cpf)
    alunos_cadastrados.append(novo_aluno)


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
def ExibirTodos(alunos_cadastrados): 
    if ListaVazia(alunos_cadastrados):
        return 
    
    print("\n==================================")
    print("📋 TODOS ALUNOS CADASTRADOS")
    print("==================================")
    for aluno in alunos_cadastrados: 
        alunos_cadastrados.ExibirDados() 
        time.sleep(0.5) 

# Atualizar
def AtualizarAluno(alunos_cadastrados): 
    if ListaVazia(alunos_cadastrados): 
        return
    
    ExibirTodos(alunos_cadastrados)
    print("\n-- ATUALIZAR ALUNO --")

    cpf_busca = input("Informe CPF do funcionario que deseja buscar: ")
    aluno_para_buscar = buscar_aluno_por_cpf(alunos_cadastrados, cpf_busca)

    if aluno_para_buscar: 
        print(f"Aluno {aluno_para_buscar.nome} encontrado!")
        print("Informe novas informaçõs ou *mantenha em branco* para manter!")

        print(f"\nNome atual: {aluno_para_buscar.nome}")
        novo_nome = input("Digite novo nome: ")

        print(f"Data denascimento atual: {aluno_para_buscar.nascimento}")
        novo_nascimento = input("Digite novo nascimento: ")

        print(f"Curso atual: {aluno_para_buscar.curso}")
        novo_curso = input("Digite novo curso: ")

        print(f"Endereço atual: {aluno_para_buscar.endereco}")
        novo_endereco = input("Digite noco endereço: ")

    if novo_nome: 
        aluno_para_buscar.nome = novo_nome

    if novo_nascimento: 
        aluno_para_buscar.nascimento = novo_nascimento

    if novo_curso: 
        aluno_para_buscar.curso = novo_curso

    if novo_endereco: 
        aluno_para_buscar.endereco = novo_endereco

        print("Dados Atualizados com sucesso! 👍")
    else: 
        print("Aluno não encontrado através do CPF 🫥")
  
def EXcluiraluno(alunos_cadastrados):
    if not ListaVazia(alunos_cadastrados):
        return

    ExibirTodos(alunos_cadastrados)
    print("\n Informe CPF do aluno que deseja excluir:")

    cpf_busca = input("CPF: ")
    aluno_para_excluir = buscar_aluno_por_cpf(alunos_cadastrados, cpf_busca)

    if aluno_para_excluir:
        alunos_cadastrados.remove(aluno_para_excluir)
        print("Aluno ❌ com sucesso!")
    else: 
        print("Erro ao deletar aluno!")




def menu(): 

    while True: 
        print("--- MENU PRINCIPAL ---")
        print("1 - Adicionar Aluno ")
        print("2 - Exibir todos os alunos ")
        print("3 - Atualizar aluno ")
        print("4 - Excluir aluno ")

        opcao = input("\nOpção = ")

        match opcao: 
            case "1": 
                AdicionarAluno(alunos_cadastrados)
            case "2":
                ExibirTodos(alunos_cadastrados)
            case "3":
                AtualizarAluno(alunos_cadastrados)
            case  "4":
                EXcluiraluno(alunos_cadastrados)
            case "5":
                print("Saindo do sistema 💢 ")
                time(3)
                os.system("cls")
            case _: 
                print("Insera uma opção válida!")
            

menu()