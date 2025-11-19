import os 
os.system("cls")

v_pacientes = []
QUANT_PAC = 5

class Paciente: 
    def __init__(self, nome, idade, peso, h, cpf):
        self.nome = nome 
        self.idade = idade 
        self.peso = peso 
        self.h = h 
        self.cpf = cpf 

    def ExibirDados(self): 
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.h}")
        print(f"CPF: {self.cpf}")

for i in range(QUANT_PAC): 
    paciente = Paciente(
        nome=input("Nome do paciente: "),
        idade=int(input("Idade do paciente: ")),
        peso=float(input("Peso do paciente: ")),
        h=float(input("Altura do paciente: ")),
        cpf=input("CPF do paciente: ")
    )
       
    v_pacientes.append(paciente)
    print("Salvando dados!")
    
nome_arquivo = "dados_pacientes.csv"
with open(nome_arquivo, "a") as arquivo_pacientes: 
    for paciente in v_pacientes: 
        arquivo_pacientes.write(f"{paciente.nome},{paciente.idade}, {paciente.peso}, {paciente.h}, {paciente.cpf}\n")

    #for paciente in v_pacientes: 
    # print("\nExibindo dados no terminal!")
    #   paciente.ExibirDados()

# print("\nExibindo no terminal")
# try: 
#     with open(nome_arquivo, "r") as arquivo: # r = read == leitura
#         # Recebe todos os dados dos arquivos de uma so vez 
#         linhas = arquivo.readlines()
#         for linha in linhas: 
#             print(f"- {linha.strip()}")
# except FileNotFoundError:
#     print("Arquivo não encontrado")

print("\nExibindo no terminal")
lista = []
try: 
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()  
        
        for linha in linhas:
            nome, idade, peso, h, cpf = linha.strip().split(",")
            dados_paciente = Paciente(
                nome=nome,
                idade=int(idade),
                peso=float(peso),
                h=float(h),
                cpf=cpf
            )
            lista.append(dados_paciente)

    for paciente in lista: 
        paciente.ExibirDados()

except FileNotFoundError:
    print("Arquivo não encontrado")


