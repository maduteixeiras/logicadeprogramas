import os 
os.system("cls")

lista_cad = [] # lista para salvar os cadastros

# criando uma classe para agrupar os informações do endereço
class Endereco: 
    def __init__(self, cidade, lougadouro, numero):
        self.cidade = cidade
        self.lougadouro = lougadouro
        self.numero = numero 
        
    def __str__(self): # organizando o endereço para exibir em apenasuma linha
        return (f"{self.cidade} - {self.lougadouro}, {self.numero}")
    
class Informacoes: # agrupando todas as informaçoes peiddas do usuario 
    def __init__(self, nome, email, Endereco):
        self.nome = nome 
        self.email = email 
        self.endereco = Endereco

    def mostrar_info(self): # função para exibir todas as informações coletadas
        print(f"\n✅ Exibindo informações de {self.nome}")
        print(f"Nome: {self.nome} ")
        print(f"E-mail: {self.email} ")
        print(f"Endereço: {self.endereco} ")

quantidade_cad = int(input("Quantos cadastros deseja salvar? ")) # pede quantos cadastros deseja fazer 
os.system("cls")

for i in range(quantidade_cad) : # apartir de quantos cadastros desejar salvar faz as seguintes perguntas * quantidade escolhida 
    print(f"Realizando {i+1}° cadastro 💻\n")
    cidade_user = input("Digite sua cidade: ")
    lougadouro_user = input("Digite seu lougadouro: ")
    numerocasa_user = input("Digite número do lougadouro: ")
    endereco_user = Endereco(cidade_user, lougadouro_user, numerocasa_user) #  apos coletar as info necessarios para o endereço agrupa eles e joda na classe

    user_nome = input("Digite seu nome: ")
    email_user = input("Digite seu e-mail: ")
    todas_info = Informacoes(user_nome, email_user, endereco_user) # agripada todas as informações necessarias e joga na classe das informaçoes
    lista_cad.append(todas_info) #coloca todas as Informacoes na lista 
    os.system("cls")

for todas_info in lista_cad: 
    todas_info.mostrar_info() # para cada cadastro presente na lista exibi as infrmaçoes de cada um 
