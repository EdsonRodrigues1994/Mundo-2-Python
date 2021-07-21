#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não
#atingiram a maioridade  equantas já são maiores.

from datetime import date


maior = 0
menor = 0

for pessoas in range(1,8):
    ano = int(input("Em que ano a {}ª pessoa nasceu? ".format(pessoas)))
    atual = date.today().year - ano
    if atual >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print("Dentre as 7 pessoas descritas {} pessoa(s) possuem mais de 18 anos e {} são menor(es) de idade.".format(maior, menor))

