# desenvolva um program que leia o nome, idade, e sexo de 4 pessoas, no final do programa:
# a media de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos 
num = 0 
maior = 0
m20 = 0
soma = 0
num = int(input('Digite o numero de pessoas: '))
for c in range(0,num):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: '))
    if (sexo == 'm' or sexo == 'M') and idade > maior:
        velho = nome
    else:
        if idade < 20:
            m20 += idade
    soma += idade
print(f'\nQuantidade de mulheres que tem menos de 20 anos é: {m20}')
print(f'O nome do homem mais velho: {velho}')
print(f'A média de idade do grupo será: {soma/num}')
# fazer soma da idade pra atualizar a varivel