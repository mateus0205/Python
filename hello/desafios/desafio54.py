# crie um programa que leia o ano de nascimento de sete pessoas, no final, mostre quantas pessoas ainda não atingiram a maioridade e quantos ja são maiores
from datetime import date
maior = 0
menor = 0
print(f'ano é: {date.today().year}')
for c in range(0,7):
    nascimento = int(input('Digite o ano do seu nascimento: '))
    if  date.today().year - nascimento >= 18:
        maior += 1
    else:
        menor += 1
print(f'O número de maiores é: {maior}')
print(f'O número de menores é: {menor}')