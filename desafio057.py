''' Faça um programa que leia o seco de uma pessoa, mas só aceite os valores "M" ou "F" ,
caso ele esteja errado, peça digitação novamente até ter um valor correto:'''

from time import sleep

sexo = str(input("Infome seu sexo [M] / [F]: ")).strip().upper()[0]


while sexo not in "MMfF":
    print("Sexo inválido, insira seu sexo novamente.")
    sexo = str(input("Infome seu sexo [M] / [F]: ")).upper()
print("Processando ...")
sleep(2)
print("O sexo mencionado é: {}".format(sexo))