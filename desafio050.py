#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.
count = 0
soma = 0

for i in range(0,6):
    num = int(input("Insira seis números: "))
    if num % 2 == 0:
        count = count + 1
        soma = soma + num
print("Foram contabilizados {} número(s) par(es), e a soma dele(s) é {}.".format(count, soma))
