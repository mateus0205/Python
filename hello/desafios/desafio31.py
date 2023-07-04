# Desenvolva um program que pergunte a distancia de uma viagem em km.
# Calcule o preço da passagem, cobrando 0.50 por km para viagens de ate 200km
# e 0.45 para viagens mais longas.
dis = float(input('Digite a distancia da viagem em km: '))
if dis <= 200:
    print(f'O preço da sua viagem é: {dis*0.50} reais')
else:
    print(f'O preço da sua viagem é: {dis*0.45} reais')
 