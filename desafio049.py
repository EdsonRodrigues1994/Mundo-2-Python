#Refaça i desafio 009, mostrandoa tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
import time

print("=-=" * 15)
numero = int(input("  Insira um número a ser multiplicado:"))
print("=-=" * 15)
print("Você solicitou a tabuada do {}.".format(numero))
print("=-=" * 15)


print("Processando ...")
time.sleep(3)
print("=-=" * 15)
print("")
print("")

print("=-=" * 7)
for i in range(1, 11):
    total = numero * i
    print("   {} X {} = {}".format(numero, i, total))
print("=-=" * 7)