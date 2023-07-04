# faça um programa que jogue par ou impar com o computador. o jogo sera interrompido quando o jogador Perder mostrando o total
# de vitorias consecutivas que ele conquistou no fim do jogo
import random
print('------------------')
print('Par ou impar')
print('------------------')
vitoria = 0
derrota = 0
while True:
    jogada = int(input('\nDiga um valor: '))
    escolha = str(input('Par ou impar? [P/I] '))
    x = random.randint(0, 10)
    resultado = 'par' if (jogada + x)  % 2 == 0 else 'ímpar'
    print(f'A soma das jogadas deu {jogada + x}')
    if escolha == 'p' and resultado == 'par' or escolha == 'i' and resultado == 'ímpar':
        print('\nVocê ganhou! ')
        vitoria += 1
    else:
        print('\nVocê perdeu!')
        break
print(f'vitorias: {vitoria}')