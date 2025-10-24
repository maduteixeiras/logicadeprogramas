import os 
import time as sleep
os.system("cls")


class cadastro: 
    def __init__(self, nome, email, endereco): 
        self.nome = nome 
        self.email = email 
        self.endereco = endereco

    def dados_entrega(self): 
        print(f"""
= Dados de Entrega = 
Nome: {self.nome}
Endereço: {self.endereco}""")

    def dados_email_marketing(self): 
        print(f"""
= Dados para o Marketing -    
Nome: {self.nome}
E-mail: {self.email} """)



nome_user = input("Digite nome: ")
email_user = input("Digite seu e-mail: ")
endereco_user = input("Digite seu endereço: ")

os.system("cls")


dados_cadastro_user = cadastro(nome_user, email_user, endereco_user)
dados_cadastro_user.dados_entrega()
dados_cadastro_user.dados_email_marketing()





