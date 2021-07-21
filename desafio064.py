'''Crie um programa que leia varios números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, qe é a condicao de parada. No final
mostre quantos números foram digitados e qual foi a soma entre eles.'''

num = 0
count = 0
soma = 0

while num != 999:
    num = int(input("Digite números, para sair digite '999': "))
    if num != 999:
        count += + 1
        soma += + num
else:
    print("Você digitou {} números e a soma entre eles é {}.".format(count, soma))