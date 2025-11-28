import os 
import time
os.system("cls || clear") #limpando terminal em windows e linux

lista_clientes = []

class Cliente: 
    def __init__(self, nome, email, telefone): 
        self.nome = nome 
        self.email = email 
        self.telefone = telefone

    def MostrarDados(self): 
        print(f"Nome: {self.nome}\nE-mail: {self.email}\nTelefone: {self.telefone}")


def lista_esta_vazia(lista_clientes): 
    if not lista_clientes: 
        print("\nNão existem clientes cadastrados")
        return True
    return False

def adicionar_clientes(lista_clientes): 
    print("\n -- Adicionando novo cliente --")
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f"Cliente {nome} adicionado com sucesso!")


#função para encontrar um cliente na lista 
def encontrar_cliente_por_nome(lista_clientes, nome_buscar): 
    nome_buscar_lower = nome_buscar.lower()
    for cliente in lista_clientes: 
        if cliente.nome.lower() == nome_buscar_lower:
            return cliente
    return None #none significa retornar vazio , sem conteúdo 
    
# função para  mostrar todos os clientes: 
def mostrar_todos_clientes(lista_clientes): 
    if lista_esta_vazia(lista_clientes):
        return
    
    print("n\ -- Lista de clientes --")
    for cliente in lista_clientes: 
        {cliente.MostrarDados()}

# função para atualizar cliente 
def atualizar_clientes(lista_clientes): 
    if lista_esta_vazia(lista_clientes): 
        return 
    
    #mostrar lista para ajudar a atualização do cliente
    mostrar_todos_clientes(lista_clientes)
    print("\n -- Atualizar cliente --")
    nome_buscar = input("\nDigite o nome do cliente: ")
    cliente_para_atualizar = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_atualizar: 
        print("\nPessoa encontrada!")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nE-mail atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo e-mail: ")

        print(f"\nTelefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone = input("Novo telefone: ")

        if novo_nome: 
            cliente_para_atualizar.nome = novo_nome

        if novo_email: 
            cliente_para_atualizar.email = novo_email

        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone

        print(f"\nDados do cliente: {nome_buscar} atualizados com sucesso!")
    else: 
        print(f"\nCliente com nome: {nome_buscar} não emcontrado!")

#função para excluir um cliente
def excluir_cliente(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)
    
    nome_buscar = input("\nDigite cliente que deseja excluir: ")
    cliente_para_remover = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_remover: 
        lista_clientes.remove(cliente_para_remover)
        print(f"\nCliente {cliente_para_remover} removido com sucesso!")
    else: 
        print(f"\nCliente com nome {nome_buscar} não encontrado :(")


def menu():
    while True:
        print("\n------ OPÇÕES ------")
        print("1 - Adicionar Cliente")
        print("2 - Listar Clientes")
        print("3 - Atualizar Cliente")
        print("4 - Remover Cliente")
        print("5 - Sair")
        print("--------------------------")

        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                adicionar_clientes(lista_clientes)

            case "2":
                mostrar_todos_clientes(lista_clientes)
            
            case "3": 
                atualizar_clientes(lista_clientes)

            case "4": 
                excluir_cliente(lista_clientes)

            case "5": 
                print("Saindo no sistema...")
                time.sleep(3.0)
                os.system("cls") 


            

menu()

