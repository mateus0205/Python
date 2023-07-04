# Escreva um programa que faça o computador "pensar" em um número inteiro de 0 e 5 e peça para o usuário 
# tentar descobrir qual foi o numero escolhido pelo computador. O programa deverá escrever na tela se o usuário 
# venceu ou perdeu.
import random
n = int(input('Digite um numero entre 0 e 5: '))
lista = (0,1,2,3,4,5)
sorteado = random.choice(lista)
if sorteado == n:
    print('Parabens, você ACERTOU!')
else:
    print('Infelizmente, você ERROU!')

