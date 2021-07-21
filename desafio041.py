#A confederação nacional de natação precisa deum programa que leia o ano de nascimento
#de um atleta e motre a sua categoria, de acordo com a idade:

from datetime import date

nascimento = int(input("Informe o seu ano de nascimento: "))
ano = date.today().year - nascimento

if ano <= 9:
    print("Categoria: MIRIM")
elif ano <= 14:
    print("Categoria: INFANTIL")
elif ano <= 19:
    print("Categoria: JUNIOR")
elif ano == 20:
    print("Categoria: SENIOR")
else:
    print("Categoria: MASTER")