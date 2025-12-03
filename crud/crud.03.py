import os 
from datetime import datetime
import time 

# Lista global para armazenar os objetos Funcionário
os_funcionarios_cadastrados = []

# Limpando terminal em windows e linux
os.system("cls || clear") 

# --- CLASSE ---
class Funcionario: 
    def __init__(self, nome, nascimento, cpf, funcao):
        self.nome = nome 
        self.nascimento = nascimento # Mantido como string DD/MM/AAAA
        self.cpf = cpf 
        self.funcao = funcao 

    def ExibirDados(self):
        print("--- DADOS DO FUNCIONÁRIO ---")
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.nascimento}")
        print(f"CPF: {self.cpf}")
        print(f"Função: {self.funcao}")
        print("----------------------------")


# --- FUNÇÕES AUXILIARES ---
def ListaVazia(os_funcionarios_cadastrados):
    """Verifica se a lista de funcionários está vazia."""
    if not os_funcionarios_cadastrados:
        print("\n🚫 Não há funcionários cadastrados!")
        return True
    return False

def BuscarCPF (os_funcionarios_cadastrados, cpf_buscar): 
    """Busca um funcionário pelo CPF."""
    # Garante que a busca é case-insensitive (embora CPF seja numérico, é bom praticar)
    cpf_buscar_lower = cpf_buscar.lower() 
    for funcionario in os_funcionarios_cadastrados: 
        # CORREÇÃO: Usar .lower() com parênteses
        if funcionario.cpf.lower() == cpf_buscar_lower:
            return funcionario
    return None

# --- FUNÇÕES PRINCIPAIS ---

# 1. Inserir
def InserirFuncionario(os_funcionarios_cadastrados): 
        
    nome = input("Nome: ")

    # Validação da Data (Como sugerido anteriormente)
    while True:
        nascimento_str = input("Digite seu aniversário (No formato DD/MM/AAAA): ")
        
        try:
            # Tenta converter para verificar o formato e validade
            datetime.strptime(nascimento_str, '%d/%m/%Y') 
            nascimento = nascimento_str
            print("✅ Data validada com sucesso.")
            break 
            
        except ValueError:
            print("\n❌ Formato de data inválido. Por favor, use o formato DD/MM/AAAA. Tente novamente.\n")
            
    cpf = input("Digite seu CPF: ")
    funcao = input("Digite cargo: ")

    novo_funcionario = Funcionario(nome=nome, nascimento=nascimento, cpf=cpf, funcao=funcao)
    os_funcionarios_cadastrados.append(novo_funcionario)
    print(f"\n✨ Funcionário {nome} cadastrado com sucesso!")


# 2. Exibir
def ExibirTodosFuncionarios(os_funcionarios_cadastrados): 
    if ListaVazia(os_funcionarios_cadastrados):
        return 
    
    print("\n==================================")
    print("📋 TODOS FUNCIONÁRIOS CADASTRADOS")
    print("==================================")
    for funcionario in os_funcionarios_cadastrados: 
        # CORREÇÃO: Chamar o método sem chaves {}
        funcionario.ExibirDados() 
        time.sleep(0.5) # Pausa para melhor visualização


# 3. Atualizar
def AtualizarFuncionario(os_funcionarios_cadastrados): 
    if ListaVazia(os_funcionarios_cadastrados): 
        return 
    
    ExibirTodosFuncionarios(os_funcionarios_cadastrados)
    print("\n -- ✏️ ATUALIZAR FUNCIONÁRIO --")
    cpf_buscar = input("\nDigite o CPF do funcionário que deseja atualizar: ")
    funcionario_para_atualizar = BuscarCPF(os_funcionarios_cadastrados, cpf_buscar)

    if funcionario_para_atualizar: 
        print(f"\nFuncionario {funcionario_para_atualizar.nome} encontrado!")
        print("Digite novos dados para atualizar ou **deixe em branco** para manter o valor atual.")

        # Nome
        print(f"\nNome atual: {funcionario_para_atualizar.nome}")
        novo_nome = input("Digite novo nome: ")

        # Data de Nascimento
        # CORREÇÃO: Corrigido o erro de digitação de 'nascimnento' para 'nascimento'
        print(f"Data de Nascimento atual: {funcionario_para_atualizar.nascimento}")
        
        novo_nascimento = input("Digite nova data de nascimento no formato (DD/MM/AAAA): ")
        
        # CPF
        print(f"CPF atual: {funcionario_para_atualizar.cpf}")
        novo_cpf = input("Digite novo CPF: ")

        # Função
        print(f"Função atual: {funcionario_para_atualizar.funcao}")
        novo_funcao = input("Digite nova função: ")

        # Aplica as atualizações se o campo não estiver vazio
        if novo_nome: 
            funcionario_para_atualizar.nome = novo_nome
        
        if novo_nascimento: 
            # (Opcional) Adicionar validação de data aqui também seria ideal, mas por enquanto aceitamos a string
            funcionario_para_atualizar.nascimento = novo_nascimento

        if novo_cpf: 
            funcionario_para_atualizar.cpf = novo_cpf 

        if novo_funcao: 
            funcionario_para_atualizar.funcao = novo_funcao

        print("\n⭐ Dados atualizados com sucesso!")
    else:
        print("\nFuncionário não encontrado com o CPF informado.")


# 4. Excluir
def ExcluirFuncionario(os_funcionarios_cadastrados): 
    # CORREÇÃO: Removido o argumento 'cpf_buscar' da definição
    if ListaVazia(os_funcionarios_cadastrados):
        return 

    ExibirTodosFuncionarios(os_funcionarios_cadastrados)
    print("\n -- 🗑️ EXCLUIR FUNCIONÁRIO --")
    
    cpf_buscar = input("\nDigite o CPF do funcionário que deseja excluir: ")
    funcionario_para_excluir = BuscarCPF(os_funcionarios_cadastrados, cpf_buscar)

    if funcionario_para_excluir: 
        os_funcionarios_cadastrados.remove(funcionario_para_excluir)
        print(f"\n✅ Funcionário {funcionario_para_excluir.nome} excluído com sucesso!")
    else: 
        print("\nFuncionário não encontrado!")


# --- MENU PRINCIPAL ---
def menu():
    while True:
        print("\n------ ⚙️ OPÇÕES ------")
        print("1 - Adicionar Funcionário")
        print("2 - Listar Funcionários")
        print("3 - Atualizar Funcionário")
        print("4 - Remover Funcionário")
        print("5 - Sair")
        print("--------------------------")

        opcao = input("Escolha uma opção: ")
        
        # Mapeamento das opções (usando 'match' que é Python 3.10+)
        match opcao:
            case "1":
                InserirFuncionario(os_funcionarios_cadastrados)

            case "2":
                ExibirTodosFuncionarios(os_funcionarios_cadastrados)
            
            case "3": 
                AtualizarFuncionario(os_funcionarios_cadastrados)

            case "4": 
                # CORREÇÃO: Chamando a função ExcluirFuncionario corretamente
                ExcluirFuncionario(os_funcionarios_cadastrados) 

            case "5": 
                print("\nSaindo do sistema...")
                time.sleep(1.5)
                os.system("cls || clear") # Limpa o terminal na saída
                break # Sai do loop while
                
            case _:
                print("\n⚠️ Opção inválida. Escolha um número entre 1 e 5.")

        time.sleep(1) # Pequena pausa para melhor leitura antes do próximo menu
        
# Chama o menu para iniciar o programa
menu()