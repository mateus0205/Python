# faça um programa que mostre na tela uma contagem regressiva para o estouro de fotos de artificio, indo de 10 ate 0, com uma pausa de 1 segundo
import time
for contador in range(10,-1,-1):
    print(contador)
    time.sleep(1)
print('BUUM')