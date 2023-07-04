#  Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
limite = int(input('Informe o limite da serie de fibonacci: '))
contador = 0
penultimo = 0
ultimo = 1
proximo = 1
print('0-1-', end = '')
while proximo <= limite:
    print(proximo, end = '-')
    penultimo = ultimo
    ultimo = proximo
    proximo = ultimo + penultimo
