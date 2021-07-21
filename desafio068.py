'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só séra interrompido quiando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

import random
from time import sleep

jogador = 0
maquina = random.randint(0, 10)
count = 0


while True:
    jogador = int(input("Você é PAR, insira seu número:  "))
    resultado = jogador + maquina
    if resultado % 2 != 0:
        vencedor = maquina
        print("Processando ...")
        sleep(2)
        print(f"A máquina escolheu {maquina}, você perdeu! O seu número de vitórias consecutivas foi {count} vez(es).")
        break
    else:
        print("Processando ...")
        sleep(2)
        print(f"A máquina escolheu {maquina}, você venceu!")
        maquina = random.randint(0, 10)
        vencedor = jogador
        count += + 1




