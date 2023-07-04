# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher sera a base de conversão
# 1 para binario
# 2 para octal
# 3 para hexadecimal
num = int(input('Digite um numero: '))
conv = int(input('Digite 1 para conversão em binário, 2 para octal ou 3 para hexadecimal: '))
if conv == 1:
    print(f'O número {num} convertido para binário é: {(bin(num)[2:])}')
elif conv == 2:
    print(f'O número {num} convertido em octal é: {oct(num)[2:]}')
elif conv == 3:
    print(f'O número {num} convertido para hexadecimal é: {hex(num)[2:]}')
else:
    print('Opção Inválida!')