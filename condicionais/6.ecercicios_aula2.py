import os
os.system("cls")

valor1 = float(input("insira um numero:"))
valor2 = float(input("insira outro valor:"))

media = (valor1 + valor2) / 2
soma = (valor1 + valor2)
produto = (valor1 * valor2)

print(f"a média desses valores é: {media}")
print(f"a soma desses valores é: {soma}")
print(f"o produto desses valores é: {produto}")

if valor1 > valor2 :
    print(f"o {valor1} é o maior desses valores")
else:
    print(f"o {valor2} é o maior desses valores")