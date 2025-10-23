import os 
os.system("cls")

class cadastro: 
    def __init__(self, nome, email, telefone, endereco): 
        self.nome = nome 
        self.email = email
        self.telefone = telefone 
        self.endereco = endereco 

    def apresentar(self): 
        print(f"""
     === informações ===
Nome: {self.nome}
E-mail: {self.email}
Telefone: {self.telefone}
Endereço: {self.endereco}
        """)

nome_user = input("Digite seu nome: ")
email_user = input("Digite seu e-mail: ")
telefone_user = input("Digite seu telefone: ")
endereco_user = input("Digite seu endereço: ")

cadastro_user = cadastro(nome_user, email_user, telefone_user, endereco_user)
cadastro_user.apresentar()