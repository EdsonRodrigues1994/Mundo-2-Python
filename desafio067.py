'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
usuário. O programa será interrompido quando o número solicitado for negativo.'''


while True:
    num = int(input("Quer ver a tabuada de qual valor: "))
    if num < 1:
        print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
        break
    for i in range(1, 11):
        total = num * i
        print(f"{num} X {i} = {total}")


