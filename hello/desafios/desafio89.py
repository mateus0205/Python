# crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista 
# composta. no final, mostre um boletim contendo a media de cada aluno
# permita que o usario possa mostrar as notas de cada aluno individualmente. 
boletim = list()
quantidade = 0
while True:
    nome = str(input('Digite seu nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2:'))
    
    media = (nota1+nota2)/2

    boletim.append([nome, [nota1, nota2],media])
    quantidade += 1
    resposta = input('Quer Continuar: [S/N]: ').strip().upper()
    
    if resposta == 'N':
        break
 
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\nNo.       NOME        MEDIA')
print('-'*30)
for i, aluno in enumerate(boletim):
    print(f'{i:<4} {aluno[0]:<10} {aluno[2]:>8.2f}')  # Exibe nome e média dos alunos
print('-' * 30)


while True:  
    print('-'*30)
    escolha = int(input('Escolha o numero do aluno (999 para interromper): '))

    if escolha == 999:
        break

    if escolha <= len(boletim):
        print(f'Notas de {boletim[escolha][0]} são {boletim[escolha][1]}')
    else: 
        print('Aluno nao existe')