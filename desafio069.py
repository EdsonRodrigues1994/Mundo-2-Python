'''Crie um programa que leia a idade e o sexo de varias pessoas.
Acada pessoa cadastrada, o programa deverá perguntarse o usuário quer ou nao continuar, no final mostre:
A) QUANTAS PESSOAS TEM MAIS DE 18 ANOO
B) QUANTOS HOMENS FORAM CADASTRADOS.
C) QUANTAS MULHERES TEM MENOS DE 20 ANOS.'''

countIdade = 0
countHomem = 0
countMulher = 0


while True:
    idade = int(input("Qual a sua idade? "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Qual seu sexo? [M / F]")).upper()[0]
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? [S / N]: ")).upper()[0]
    if idade >= 18:
        countIdade += + 1
    if sexo == "M":
        countHomem += + 1
    if sexo == "F" and idade < 20:
        countMulher += + 1
    if continuar == "N":
        print(f" {countIdade} Pessoa(s) tem mais de 18 anos. \n {countHomem} Homem(ns) foram cadastrados. \n {countMulher} Mulher(es) tem menos de 20 anos.")
        break

