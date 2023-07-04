# refaça o desafio 009, mostrando a tabuada de um numero que o usuário escolher, so que agora utilizando um laço for
n = int(input('Digite um valor: '))
for c in range(1,11):
    multi = n * c
    print(f'{n} x {c} = {multi} ')
    