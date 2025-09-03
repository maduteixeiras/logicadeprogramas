import os 
os.system("cls")

senhacerta = "3010"
logincerto = "mariateixeira2@gmail.com"

login = input("Digite seu login: \n")
senha = input("Digite sua senha: \n")

if login == logincerto and senha == senhacerta:
    print("Bem-Vindo")
else:
    print("Login ou senha inválidos. Tente Novamente")