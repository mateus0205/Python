## leia nome e peso de varias pessoas e guarde na lista
## quantas pessoas foram cadastradas 
## uma listagem com as pessoas mais pesadas 
## uma listagem com as pessoas mais leves
pessoas = []  # Lista principal onde cada pessoa será uma sublista [nome, peso]
pesados = []  # Lista para pessoas com o maior peso
leves = []    # Lista para pessoas com o menor peso

while True:
    nome = str(input('Digite seu nome: '))
    peso = float(input('Digite seu peso: '))
    
    # Adiciona nome e peso como uma sublista à lista principal
    pessoas.append([nome, peso])
    
    resposta = input('Quer continuar? [S/N]: ').strip().upper()
    if resposta == 'N':
        break

# Determinar o maior e o menor peso
maior = max(pessoa[1] for pessoa in pessoas)  # O maior peso entre as pessoas
menor = min(pessoa[1] for pessoa in pessoas)  # O menor peso entre as pessoas

# Classificar pessoas como pesadas ou leves
for pessoa in pessoas:
    if pessoa[1] == maior:
        pesados.append(pessoa[0])
    if pessoa[1] == menor:
        leves.append(pessoa[0])

# Quantidade total de pessoas
qtde = len(pessoas)

# Exibir resultados
print(f'\nA quantidade de pessoas cadastradas foi: {qtde}')
print(f'O maior peso foi {maior:.2f}Kg. Peso de {pesados}')
print(f'O menor peso foi {menor:.2f}Kg. Peso de {leves}')
