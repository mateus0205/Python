# faça um programa que jogue jokenpo com vc
from random import randint
import time
vitorias = 0
empates = 0
derrotas = 0
while True: 

    jogada = str(input('''\nVamos jogar Jokenpo?
    Pedra
    Tesoura
    Papel
Qual é a sua jogada? ''')).capitalize()
    itens = ('Pedra', 'Tesoura', 'Papel')
    computador = randint(0,2)
    print('-='*30)
    print('JO')
    time.sleep(0.8)
    print('KEN')
    time.sleep(0.8)
    print('PO')
    print('-='*30)
    
    if computador == 0:
        if jogada == 'Pedra':
            print(f'\nVocê jogou {jogada} e o computador jogou {itens[computador]}') 
            print('EMPATOU!! \n')
            empates +=1
            
        elif jogada == 'Tesoura':
            print(f'\nVocê jogou {jogada} e o computador jogou {itens[computador]}')
            print('Perdeu (KKKK), Tente melhorar sua jogada!\n')
            derrotas +=1
            
        elif jogada == 'Papel':
            print(f'\nVocê jogou {jogada} e o computador jogou {itens[computador]}')
            print('Finalmente Ganhou uma!\n')
            vitorias +=1
        else:
            print('JOGADA INVALIDA, (JOGADAS SOMENTE "pedra, tesoura e papel"\n')
    elif computador == 1:
        if jogada == 'Pedra':
            print(f'\nVocê jogou {jogada} e o computador jogou {itens[computador]}')
            print('Finalmente Ganhou uma!\n')
            vitorias +=1
            
        elif jogada == 'Tesoura':
            print(f'\nVocê jogou {jogada} e o computador jogou {itens[computador]}')
            print('EMPATOU!!\n')
            empates +=1
        elif jogada == 'Papel':
            print(f'\nVocê jogou {jogada} e o computador jogou {itens[computador]}')
            print('Perdeu (KKKK), Tente melhorar sua jogada!\n')
            derrotas +=1
            
        else:
            print('\nJOGADA INVALIDA, (JOGADAS SOMENTE "pedra, tesoura e papel")\n')
            
    elif computador == 2:
        if jogada == 'Pedra':
            print(f'\nVocê jogou {jogada} e o computador jogou {itens[computador]}')
            print('PERDEU (KKKK), Tente melhorar sua jogada!\n')
            derrotas +=1
            
        elif jogada == 'Tesoura':
            print(f'\nVocê jogou {jogada} e o computador jogou {itens[computador]}')
            print('Finalmente Ganhou uma!\n')
            vitorias +=1
            
        elif jogada == 'Papel':
            print(f'\nVocê jogou {jogada} e o computador jogou {itens[computador]}')
            print('EMPATOU!!\n')
            empates +=1
            
        else:
            print('\nJOGADA INVALIDA, (JOGADAS SOMENTE "pedra, tesoura e papel")\n')
            
    print(f"Vitorias: {vitorias}")
    print(f'Empates: {empates}')
    print(f'Derrotas: {derrotas}\n')
    
    jogar = str(input('Deseja jogar novamente? (s/n): ')).lower()
    if jogar == 'n':
        break
