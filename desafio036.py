#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Clcule o valor da prestação mensa, sabendo que ela não pode exceder 30% dp salário ou então empréstimo será negado.

print("=-=" * 30)
print("                                 EMPRÉSTIMO BANCÁRIO                     ")
print("=-=" * 30)

valCasa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o salário: "))
qntPag =  int(input("Informe em quantos anos será pago: "))
meses = qntPag * 12
prestacao = valCasa / meses
desconto = salario * 30 / 100

if prestacao < desconto:
    print("Empréstimo aprovado!")
    print("O valor da sua parcela consiste em R${:.3f}, que deverão ser pagas em {} meses.".format(prestacao, meses))
else:
    print("Empréstimo negado! O valor da sua parcela seria R${:.2f}, e representa mais que 30% do seu salário.".format(prestacao))

