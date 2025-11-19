import os
os.system("cls")

QUANT_CAD = 1 
v_usuario = []

class DadosUser: 
    def __init__(self, nome, nascimento, rg, cpf):
        self.nome = nome
        self.nascimento = nascimento
        self.rg = rg 
        self.cpf = cpf 

    def ExibirDados(self): 
        print("Mostrando dados no terminal !")
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.nascimento}")
        print(f"RG: {self.rg}")
        print(f"CPF: {self.cpf}")

# solicitando os dados do usuario 

for i in range(QUANT_CAD): 
    user = DadosUser(
        nome = input("Nome: ") , 
        nascimento= input("Data de nascimento (xx/xx/xx): ") , 
        rg = input("RG: ") , 
        cpf = input("CPF: ")
    )

    v_usuario.append(user)
    print("\nDados salvos!\n")
    
# criando o arquivo para salvar os dados 
nome_arquivo = "dados_user.csv"
with open (nome_arquivo, "a", encoding="utf-8") as arquivo_user: 
    for user in v_usuario: 
        arquivo_user.write(f"{user.nome}, {user.nascimento}, {user.rg}, {user.cpf}")
        user.ExibirDados()
        


    
