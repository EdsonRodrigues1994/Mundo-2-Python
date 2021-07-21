#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
#de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#Wntre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print("O seu IMC é: {:.2f} - Abaixo do peso".format(imc))
elif imc >= 18.5 and imc < 25:
    print("O seu IMC é: {:.2f} - Peso ideal".format(imc))
elif imc >= 25 and imc < 30:
    print("O seu IMC é: {:.2f} - Sobrepeso".format(imc))
elif imc >= 30 and imc < 40:
    print("O seu IMC é: {:.2f} - Obesidade".format(imc))
else:
    print("O seu IMC é: {:.2f} - Obesidade mórbida".format(imc))