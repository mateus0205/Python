# crie um programa onde o usuário possa digitar vários valores numericos e cadastre-os em uma lista
# caso o numero ja exista la dentro, ele não será adicionado.
# no final, serão exibidos os
# valores unicos digitados em ordem crescente.
lista = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print()
    resposta = str(input('Quer Continuar? [S/N] '))
    if resposta in 'Nn':
        break

lista.sort()
print(lista)