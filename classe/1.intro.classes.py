
""""

class carro: 
    def __init__(self): 
        self.marca = 'honda'
        self.modelo = 'civic'
        self.ano = '2023'
        self.cor = 'preto'
    pass

carro1 = carro()
print(carro1.marca, carro1.modelo, carro1.ano, carro1.cor

""" 

class carro: # classe
    # o __init__ é um construtor, que permite criar uma funcionalidade inicial da classe
    # instanciar precisa criar uma variável (objeto)
    # de forma parametrizada
    def __init__(self, marca, modelo, ano, cor): # atritubos 
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_info(self):
        print(self.marca, self.modelo, self.ano, self.cor)

    def acelerar(self): # metodos 
        print("acelerando")

    def frear(self): # metodos 
        print("freando")

carro1 = carro('honda', 'civic', '2023', 'preto')
carro1.exibir_info()
carro1.acelerar()
carro1.frear()
