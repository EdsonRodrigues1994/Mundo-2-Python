#Escreve um programa que leia um número inteiro qualquer e peça para o usuário escolhar qual será a base de conversão:
print("=-=" * 35)
print("                                           CONVERSOR")
print("=-=" * 35)

num = int(input("Digite um número: "))
conversao = int(input("Digite 1 para converter o decimal para binário, 2 para octal e 3 para hexadecimal: "))

binario = 1
octal = 2
hexadecimal = 3



if  conversao < 1 or conversao > 3:
    print("Opção invalida, digite um número de 1 à 3: ")
elif conversao == 1:
    print("Opção selecionada: 1 - CONVERSÃO DE DECIMAL PARA BINÁRIO")

    print("Aconversão do número {} para binário é {} !".format(num, bin(num)[2:]))
elif conversao == 2:
    print("Opção selecionada: 2 - CONVERSÃO DE DECIMAL PARA OCTAL")
    print("")
    print("A conversão do número {} para octal é {} !".format(num, oct(num)[2:]))
elif conversao == 3:
    print("Opção selecionada: 1 - CONVERSÃO DE DECIMAL PARA HEXADECIMAL")
    print("")
    print("A conversão do número {} para hexadecimal é {} !".format(num, hex(num).upper()[2:]))
print("=-=" * 35)


