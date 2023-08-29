#Crie um algoritimo que leia um número e mostre seu dobro, triplo e raiz quadrada.
import math

n1 = int(input('Informe um número inteiro: '))
soma = n1 + n1
tri = n1 * 3
raiz = math.sqrt(n1)
print('O dobro de {} é: {} \n O triplo de {} é {} \n A raiz quadrada de {} é {:.2f}'.format(n1, soma, n1, tri, n1, raiz))
