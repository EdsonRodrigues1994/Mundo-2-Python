# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint

itens = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)
player = int(input("Digite um número de 1 à 3, sendo 1 - Pedra , 2 - Papel, 3 - Tesoura: "))

if pc == 0:
    if player == 0:
        print("Jogador escolheu {}, PC escolheu {}, EMPATE!".format(itens[player], itens[pc]))
    elif player == 1:
        print("Jogador escolheu {}, PC escolheu {}, VENCEU!".format(itens[player], itens[pc]))
    elif player == 2:
        print("Jogador escolheu {}, PC escolheu {}, PERDEU!".format(itens[player], itens[pc]))
elif pc == 1:
    if player == 0:
        print("Jogador escolheu {}, PC escolheu {}, PERDEU!".format(itens[player], itens[pc]))
    elif player == 1:
        print("Jogador escolheu {}, PC escolheu {}, EMPATE!".format(itens[player], itens[pc]))
    elif player == 2:
        print("Jogador escolheu {}, PC escolheu {}, VENCEU!".format(itens[player], itens[pc]))
elif pc == 2:
    if player == 0:
        print("Jogador escolheu {}, PC escolheu {}, VENCEU!".format(itens[player], itens[pc]))
    elif player == 1:
        print("Jogador escolheu {}, PC escolheu {}, PERDEU!".format(itens[player], itens[pc]))
    elif player == 2:
        print("Jogador escolheu {}, PC escolheu {}, EMPATE!".format(itens[player], itens[pc]))


