'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

import math

num = int(input("Digite um número para ser calculado seu fatorial: "))
fatorial = 1
count = num

print("Calculando {}! = ".format(num), end="")
while count > 0:
        print("{} ".format(count), end="")
        print("X " if count > 1 else " = ", end="")
        fatorial *= count
        count -= 1
print("{}".format(fatorial))

