import os 
os.system("cls")

@dataclass
class pessoa: 
    nome : str 
    idade : int 
    cpf : str 

@dataclass
class pet:
    nome : str 
    idade : int 
    peso: float

pessoa1 = pessoa("Maria" , 16, '123456789011')
pet1 = pet("Toffe", 1, 2.1)


