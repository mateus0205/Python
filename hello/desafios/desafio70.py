# crie um programa que leia o nome e o preço de varios produtos. O produto devera perguntar se o usuário vai continuar no final. Mostre:
# qual é o total gasto na compra
# quantos produtos custam mais de 1000 
# nome do produto mais barato 
total = 0
produtos1000 = 0
barato = 5000
nome = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o valor do seu produto: '))
    total += preco
    if preco > 1000:
        produtos1000 += 1
    if preco < barato:
        nome = produto
        barato = preco   
    escolha = str(input('Gostaria de continuar, [s/n]: '))
    if escolha == 'n':
        break
print(f'O total gasto {total}')
print(f'Quantos produtos custam mais que 1000: {produtos1000}')
print(f'O nome do mais barato: {nome}')