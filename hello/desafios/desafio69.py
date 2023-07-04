# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pesssoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. no final mostre:
# quantos pessoas tem mais de 18 anos
# quantos homens foram cadastrados
# quantas mulheres tem menos de 20 anos 
maior = 0
homens = 0
mulheres20 = 0
while True:
    idade = int(input('\nDiga sua idade: '))
    sexo = str(input('Diga seu sexo, [f/m]: '))
    if sexo == 'm':
        homens += 1
        if idade > 18:
            maior += 1
    elif sexo == 'f':
        if idade < 20:
            mulheres20 += 1
    escolha = str(input('\nDiga se quer continuar, [s/n]: '))
    if escolha == 'N':
        break
print(f'Quantidade de homens com mais de 18 anos: {maior}')
print(f'Quantidade de homens cadastrados: {homens}')
print(f'Quantidade de mulheres que tem menos de 20 anos: {mulheres20}')
        