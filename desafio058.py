'''Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

import random
from time import sleep


sorteio = random.randint(0, 10)
tentativa = 1
chute = int(input("Digite um número de 0 a 10: "))

while chute < 0 or chute > 10:
    print("Número inválido , insira um chute novamente:")
    chute = int(input("Digite um número de 0 a 10:"))
while chute != sorteio:
    sorteio = random.randint(0,10)
    tentativa += + 1
    print("Você errou! Tente novamente.")
    chute = int(input("Digite um número de 0 a 10: "))
else:
    print("Processando ...")
    sleep(2)
    print("Parabéns você acertou! E seu número de tentativas foram {} vez(es).".format(tentativa))

