# Crie um programa que leia o nome de uma ciadade e diga se ela começa ou não com o nome "SANTO"
nome = str(input('Digite um nome de uma cidade: ')).upper()
print(f'A cidade começa com santo: {nome.find("SANTO")}')
if nome : 
    print('sim, começa com santo')

print(nome[:5] == 'SANTO')