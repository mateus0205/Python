# crie um programa onde o usuário possa digitar vários valores numericos e cadastre-os em uma lista
# caso o numero ja exista la dentro, ele não será adicionado.
# no final, serão exibidos os
# valores unicos digitados em ordem crescente.
lista = list()
for cont in range(0,5):
    valor = int(input('Digite um valor: '))
    
    if valor not in lista:
        lista.append(valor) 

lista.sort()
print(lista)