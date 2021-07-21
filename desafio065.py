'''Crie um programa que leia vários numeros inteiros pelo teclaod.
No final da execucao, mostre a media entre todos os valores e qual foi o maior  eo menor dos valores lidos.
O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.'''
num = 0
count = 0
soma = 0
media = 0.0

num = int(input("Digite um número: "))
opcao = str(input("Deseja digitar outro número? [S] / [N]")).upper()[0]
count += + 1
soma += num
maior = num
menor = num
while opcao not in "Nn":
    if opcao not in "SsNn":
        print("Informação inválida!")
        opcao = str(input("Deseja digitar outro número? [S] / [N]")).upper()[0]
        if opcao == "S":
            num = int(input("Digite outro número: "))
            opcao = str(input("Deseja digitar outro número? [S] / [N]")).upper()[0]
            soma += + num
            count += + 1
            media = soma / count
            if num > maior:
                maior = num
            if num < menor:
                menor = num
    else:
        num = int(input("Digite outro número: "))
        opcao = str(input("Deseja digitar outro número? [S] / [N]")).upper()[0]
        soma += num
        count += + 1
        media = soma / count
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print("A média entre os {} número(s) digitados é: {:.2f}, o maior número é {} e o menor número é {}.".format(count, media, maior, menor))
print("Saindo ...")


