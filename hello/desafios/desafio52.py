# Faça um programa que leia um numero inteiro e diga se ele é ou não número primo
num = int(input('Digite um número inteiro: '))
total = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[034m', end=' ')
        total += 1
    else:
        print('\033[m', end=' ')
    print(f'{c}', end=' ')
print(f'\nO número {num} foi divisivel {total} vezes')
if total == 2:
    print('É numero primo')
else:
    print('Ele não é numero primo')