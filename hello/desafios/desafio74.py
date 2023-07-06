# crie um programa que vai gerar cinco números aleatorios e colocar em uma tupla.
# depois disso, mostre a listagem de numeros gerados e tamabem indique o menor e o maior valor que estão na tupla

from random import randint
tupla = ()
for c in range(5):
    numero = randint(0,100)
    tupla = tupla + (numero,)
print(tupla)
print(f'qual é o menor número da tupla {min(tupla)}')
print(f'qual é o maior número da tupla {max(tupla)}')