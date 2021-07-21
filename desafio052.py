#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um número: "))
total = 0

for i in range(1, num +1):
    if num % i == 0:
        total = total + 1
print("O número {} foi divisível {} vezes.".format(num, total))