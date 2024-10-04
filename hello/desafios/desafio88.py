# faça um programa que ajude na mega sena.
# o programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros
# para cada jogo, cadastre tudo em uma lista composta 
import random 

print('-'*30)
print('      JOGA NA MEGA SENA   ')
print('-'*30)

numero_jogos = int(input('Quantos jogos voce quer que seja sorteados? '))
print(f'-=-=-= SORTEANDO {numero_jogos} jogos -=-=-=')
for jogos in range(1,numero_jogos+1):
    sorteados = sorted(random.sample(range(1,61),6))
    print(f'Jogo {jogos}: {sorteados}')

