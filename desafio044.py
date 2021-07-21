4000#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro ou cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print("=-=" * 50)
produto = float(input("                       Inisira o valor do produto: "))
qntd = int(input("                       Insira a quantidade de peças: "))
pagamento = int(input("Insira a forma de pagamento: \n"
                      "[1] - Dinheiro/Cheque \n"
                      "[2] - Cartão \n"
                      "[3] - Cartão em até 2x \n"
                      "[4] - Cartão em 3x ou mais "))
print("=-=" * 50)
DinChe = 1
cartao = 2
cartaoduas = 3
cartaopar = 4

if pagamento == 1:
    desconto = produto * qntd - (produto * qntd * 10 / 100)
    print("Forma de Pagamento: Dinheiro / Cheque.")
    print("Valor do produto R${:.2f}. Total a pagar com 10% de desconto R${:.2f}".format(produto * qntd, desconto))
elif pagamento == 2:
    desconto = produto * qntd - (produto * qntd * 5 / 100)
    print("Forma de Pagamento: Cartão à Vista.")
    print("Valor do produto R${:.2f}. Total a pagar com 5% de desconto R${:.2f}".format(produto * qntd ,desconto))
elif pagamento == 3:
    print("Forma de Pagamento: Cartão em 2x. Total a pagar R${:.2f}.".format(produto * qntd))
    print("O valor da parcela ficará em R${:.2f}".format(produto * qntd / 2))
elif pagamento == 4:
    juros = produto * qntd + (produto * qntd * 20 / 100)
    print("Forma de Pagamento: Cartão 3x ou mais.")
    print("do produto R${:.2f}. Total a pagar com 20% de juros R${:.2f}".format(produto * qntd, juros))
else:
    print("Opção selecionada inválida, tente novamente")

print("=-=" * 50)
