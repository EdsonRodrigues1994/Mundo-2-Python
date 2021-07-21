#Crie um programa que leia uma frase qualquer e diga se ela é palíndroma, desconsiderando os espaços.

frase = str(input("Digite uma frase")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

for letras in range(len(junto) - 1, - 1, - 1):
    inverso = inverso + junto[letras]
if inverso == junto:
    print("Temos um palíndromo")
else:
    print("A frase digitada não é um palíndromo")