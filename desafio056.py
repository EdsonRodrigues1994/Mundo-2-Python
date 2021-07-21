#Faça um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

somaIdade = 0
maioridadehomem = 0
count = 0
maior = 0
menor = 0
nomevelho = ""

for pessoas in range(1,5):
    print("Informe os seguintes dados da {}ª pessoa: ".format(pessoas))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo ( M / F): ").upper())
    somaIdade = somaIdade + idade
    media = somaIdade / pessoas
    if pessoas == 1 and sexo == "M":
        maioridadehomem = idade
        nomevelho = nome
    if sexo == "M"and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and sexo == "F":
        count = count + 1
print("A média de idade do grupo é {} anos, o homem mais velho se chama {} e tem {} anos de idade. Temos {} mulher(es) com menos de 20 anos.".format(media,nomevelho, maioridadehomem, count))


