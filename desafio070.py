'''Crie um programa que leia o nome e o preço de varios produtos.
O programa deverá  perguntar se o usuário vai continuar.
No final, mostre:
A) QUAL É O TOTAL GASTO NA COMPRA\
B) QUANTOS PRODUTOS CUSTAM MAIS DE 1000\
C) QUAL É O NOME DO PRODUTO MAIS BARATO.'''

count = 0
countMil = 0
soma = 0
maisMil = 0
barato = " "

while True:
    produto = str(input("Insira o nome de um produto: "))
    preco = float(input("Insira o valor do produto: "))
    soma += + preco
    count += + 1
    if preco > 1000:
        countMil += + 1
    if count == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? [S / N]: ").upper()[0])
    if continuar == "N":
        break
print(f" O total gasto foi  R${soma:.2f}.\n "
    f"{countMil} Produto(s) custam mais de R$ 1000,00. \n "
      f"O produto mais barato é {barato} que custa custa R${menor:.2f}.")
