#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se ja passou do tempo de se alistar
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

nascimento = int(input("Digite o ano do seu nascimento: "))
anos = date.today().year - nascimento

if anos < 18:

    print("Faltam {} ano(s) para o seu alistamento militar.".format(18 - anos))
elif anos == 18:
    print("É hora de se alistar")
else:
    print("Já se passaram {} ano(s) do seu alistamento militar.".format(anos - 18))