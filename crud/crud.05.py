import os 
os.system("cls")

v_clientes = []
v_produtos = []

class Endereco: 
    def __init__(self, rua, numero, cidade):
        self.rua = rua 
        self.numero = numero
        self.cidade = cidade

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}"


class Cliente: 
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome 
        self.email = email 
        self.telefone = telefone 
        self.enderco = endereco

def ListaVazia_Clientes:
