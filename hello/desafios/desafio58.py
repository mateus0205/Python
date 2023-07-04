# Melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10, so que o jogador vai tentar adivinhar ate acertar, mostrando quantos palpites foram 
# necessários para vencer
import random
tentativas = 0
numero = int(input('Digite um número entre 0 e 10: '))
lista = (0,1,2,3,4,5,6,7,8,9,10)
sorteado = random.choice(lista)
while sorteado != numero:
    numero = int(input('Você errou, Digite um número entre 0 e 10: '))
    tentativas += 1
print(f'Parabéns, você acertou em {tentativas+1} tentativas! ')