import os 
os.system("cls")

valor = float(input("Qual valor do produto? \n"))
desconto = valor *  0.1
valor_com_desconto = valor - desconto

print("""
===== FORMAS DE PAGAMENTO ====
    1 - Pagamento à vista (10% de desconto)
    2 - Pagamento à prazo (até 6x sem juros )
""")

while True: 
    formadepagamento = int(input("Qual forma de pagamento? \n"))

    if formadepagamento >= 1 and formadepagamento <= 2:
        break 


match formadepagamento:
    case 1: 
        print(f"""
==== INFORMAÇÕES DA COMPRA ====
    Valor: {valor}
    Forma de pagamento: à vista
    Desconto: {desconto}
    Valor total a pagar: {valor_com_desconto}
""")
    case 2: 
        while True: 
            parcelas = int(input("Parcelamos em até 6x sem juros! Deseja quantas parcelas?\n"))
            if parcelas >= 1 and parcelas <= 6:
                break
           

        print(f"""
    ==== INFORMAÇÕES DA COMPRA ====
    Valor: {valor}
    Forma de pagamento: á prazo
    Quantidade de parcelas: {parcelas}
    Desconto: 00,00
    Valor total a pagar: {valor / parcelas}

""")

