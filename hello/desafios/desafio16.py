# Crie um programa que leia um número real qualquer pelo teclado
# e mostre na tela a sua posição inteira. EX: 6.127 e saia 6
from math import trunc 
n = float(input('Digite um número com virgula: '))
print(f'A parte interira do {n} é {trunc(n)}')