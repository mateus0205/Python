# crie um programa onde o usuário possa digitar vários valores numericos e cadastre-os em uma lista
# caso o numero ja exista la dentro, ele não será adicionado.
# no final, serão exibidos os
# valores unicos digitados em ordem crescente.
lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    resposta = input('Quer Continuar? [S/N] ').strip().upper()
    if resposta == 'N':
        break
lista.sort()
print(sorted(lista))  # Ordena e imprime a lista de valores únicos
