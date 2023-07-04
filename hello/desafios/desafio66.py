# Crie um programa que leia vário números inteiros pelo teclado. O programa so vai parar quando o usuário
# O programa so vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
n = s = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram digitados {cont} números e a sua soma será: {s}')
    