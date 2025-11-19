import os 
os.system("cls")

QUANT_PAC = 2
vetor_pacientes = []

class Paciente: 
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade


for i in range(QUANT_PAC): 
    paciente = Paciente( 
        nome= input("Nome do paciente: ") ,
        idade= int(input("Idade do paciente: "))
    )

    vetor_pacientes.append(paciente)
    print()

nome_do_arquivo = "dados_paciente.csv"
with open(nome_do_arquivo, "w") as arquivo_pacientes: 
    for paciente in vetor_pacientes: 
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}")
        print("Salvando os dados!")