# Escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80km/h mostre a mensagem dizendo que ele foi multado
# a multa vai custar 7 reais por cada km acima do limite.
velocidade = float(input('Digite em km/h a velocidade do carro: '))
if velocidade > 80:
    print(f'Você foi multado em {(velocidade - 80)*7:.2f} reais')
else:
    print('Velocidade dentro da lei! ')