'''Crie um programa que leia varios numeros inteiros pelo teclado.
O prograsma só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles.'''

soma = 0
count = 0

while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    soma += num
    count += + 1
print(f"Você digitou {count} número(s) e a soma entre eles é {soma}.")