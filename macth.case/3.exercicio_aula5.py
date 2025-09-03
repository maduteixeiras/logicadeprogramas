import os 
os.system("cls")

nome = str(input("Primeiro nome: \n"))
h = float(input(f"Qual sua altura atual, {nome}? \n"))


print("""
    M = masculino 
    F = feminino
""")
genero = str(input("Qual seu sexo biológico? \n"))
calculo_masculino = (72.7 * h ) - 58
calculo_feminino = (62.1 * h) - 44.7

match genero:
    case "M" | "m":
        print(f"""
  === Peso ideal ===
{calculo_masculino:.2f}""")
        
    case "F" | "f":
        print(f"""
  === Peso ideal === 
{calculo_feminino:.2f}""")
    case _:
        print("Essa letra não corresponde a nenhuma das opções. Tente Novamente")

