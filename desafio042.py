#Que tipo de triângulo será formado:
#EQUILATERO: Todos os lados sao iguais
#ISOSCELES: Dois lados iguais
#ESCALENO: Todos os lados são diferentes

n1 = float(input("Digite a primeira reta:"))
n2 = float(input("Digite a segunda reta: "))
n3 = float(input("Digite a terceira reta: "))
soma = n1 + n2

if soma > n3 and n1 == n2 and n1 == n3 and n2 == n3:
    print("Será formado um Equilátero!")
elif soma > n3 and n1 == n2 or n1 == n3 or n2 == n3:
    print("Será formado um Isósceles")
else:
    print("Será formado um Escaleno")
