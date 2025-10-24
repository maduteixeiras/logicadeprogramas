import os 
os.system("cls")
QUANT_CAD = 3 
cadastros = []

class Pessoas:
    def __init__(self, nome, cpf, tel):
        self.nome = nome 
        self.cpf = cpf 
        self.tel = tel 

    def mostrar_dados(self): 
        print(f"""Nome = {self.nome}
CPF = {self.cpf}
Telefone = {self.tel}
""")

    def dados_sms_marketing(self): 
        print(f"Telefone: {self.tel}")

for i in range(QUANT_CAD): 
    print (f"REALIZANDO O {i+1}° CADASTRO: ")
    nome_user = str(input("Digite nome: "))
    cpf_user = str(input("Digite seu CPF: "))
    tel_user = int(input("Digite seu telefone: "))

    pessoa = Pessoas(nome_user, cpf_user, tel_user)
    cadastros.append(pessoa)
    os.system("cls")

print("=== CADASTROS ===")
for pessoa in cadastros: 
    pessoa.mostrar_dados()

print("=== SMS PARA MARKETING ===")
for pessoa in cadastros: 
    pessoa.dados_sms_marketing()





