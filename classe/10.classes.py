import os 
os.system("cls")

QUNAT_CAD = 4
array_dados = []
class DadosNecessarios: 
    def __init__(self, nome, idade, peso, h):
        self.nome = nome 
        self.idade = idade 
        self.peso= peso 
        self.h = h 

    def ExibirDados(self): 
        print(f"\nExibindo dados de {self.nome} ✅")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"peso: {self.peso}")
        print(f"Altura: {self.h}")

for i in range(QUNAT_CAD): 
    print(f"Solicitando dados do {i+1}° cadastro 💻")
    user_nome = str(input("Digite nome: "))
    user_idade = int(input("Digite idade: "))
    user_peso = float(input("Digite peso: "))
    user_h = float(input("Digite altura: "))

    TodoOsdados = DadosNecessarios(user_nome, user_idade, user_peso, user_h)
    array_dados.append(TodoOsdados)
    os.system("cls")

for TodosOsDados in array_dados: 
    TodosOsDados.ExibirDados()