'''Crie um progrma que leia dois valores e mostre um menu na tela
[1] Somar
[2] Multiplicar
[3] Maior
[4]Sair'''

from time import sleep

num1 = 0
num2 = 0
total = 0
print(" [1] Somar\n [2] Multiplicar \n [3] Maior \n [4] Sair")
opcao = int(input("Selecione uma opção: "))

while opcao < 1 or opcao > 5:
    print("Opção inválida, selecione uma opção de 1 à 4:")
    opcao = int(input("Selecione uma opção: "))
    print("Opção selecionada: {}".format(opcao))
if opcao == 1:
    print("Opção selecionada: 1 - Somar")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    total = num1 + num2
    print("Processando ...")
    sleep(2)
    print("RESULTADO: {} + {} = {}".format(num1, num2, total))
    print(" [4] - Nova consulta \n [5] - Sair")
    opcao = int(input("Selecione uma opção: "))
    while opcao == 4:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        total = num1 + num2
        print("Processando ...")
        sleep(2)
        print("RESULTADO: {} + {} = {}".format(num1, num2, total))
        print(" [4] - Nova consulta \n [5] - Sair")
        opcao = int(input("Selecione uma opção: "))
        while opcao != 4 and opcao != 5:
            print("Opção inválida!")
            print(" [4] - Nova consulta \n [5] - Sair")
            opcao = int(input("Selecione uma opção: "))
            if opcao == 5:
                print("Saindo ...")
    if opcao == 5:
        print("Processando ...")
        sleep(2)
        print("Saindo ...")
elif opcao == 2:
    print("Opção selecionada: 2 - Multiplicação")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    total = num1 * num2
    print("Processando ...")
    sleep(2)
    print("RESULTADO: {} X {} = {}".format(num1, num2, total))
    print(" [4] - Nova consulta \n [5] - Sair")
    opcao = int(input("Selecione uma opção: "))
    while opcao == 4:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        total = num1 * num2
        print("Processando ...")
        sleep(2)
        print("RESULTADO: {} + {} = {}".format(num1, num2, total))
        print(" [4] - Nova consulta \n [5] - Sair")
        opcao = int(input("Selecione uma opção: "))
        while opcao != 4 and opcao != 5:
            print("Opção inválida!")
            print(" [4] - Nova consulta \n [5] - Sair")
            opcao = int(input("Selecione uma opção: "))
            if opcao == 5:
                print("Saindo ...")
    if opcao == 5:
        print("Processando ...")
        sleep(2)
        print("Saindo ...")
elif opcao == 3:
    print("Opção selecionada: 3 - Maior")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num1 > num2:
        maior = num1
    else:
        maior = num2
        print("Processando ...")
        sleep(2)
    print(("RESULTADO: O maior número é {}.").format(maior))
    print(" [4] - Nova consulta \n [5] - Sair")
    opcao = int(input("Selecione uma opção: "))
    while opcao == 4:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        if num1 > num2:
            maior = num1
        else:
            maior = num2
            print("Processando ...")
            sleep(2)
        print(("RESULTADO: O maior número é {}.").format(maior))
        print(" [4] - Nova consulta \n [5] - Sair")
        opcao = int(input("Selecione uma opção: "))
        while opcao != 4 and opcao != 5:
            print("Opção inválida!")
            print(" [4] - Nova consulta \n [5] - Sair")
            opcao = int(input("Selecione uma opção: "))
        if opcao == 5:
            print("Saindo ...")
    if opcao == 5:
        print("Processando ...")
        sleep(2)
        print("Saindo ...")
elif opcao == 4:
    print("Opção selecionada: 4 - Sair")
    print("Processando ...")
    sleep(2)
    print("Saindo ...")
