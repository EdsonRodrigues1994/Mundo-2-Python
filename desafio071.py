'''Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro)
e o programa vau informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$1, R$10, R$20 e R$50'''


valor = int(input("Qual valor será sacado? "))
total = valor
cedula = 50
totCed = 0

while True:
    if total >= cedula:
        total -= cedula
        totCed += 1
    else:
        if totCed > 0:
            print(f"Total de {totCed} cédulas de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totCed = 0
        if total == 0:
            break
