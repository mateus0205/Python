# faça um programa que leia 5 valores numeros e guarde os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
lista = list()
for cont in range(0,5):
    lista.append(int(input('Digite os valores para adicionar na lista: ')))
    
maior_valor = max(lista)
menor_valor = min(lista)

posicao_maior = lista.index(maior_valor)
posicao_menor = lista.index(menor_valor)

print(f'O maior valor da lista é: {max(lista)} e está na posição da lista {(posicao_maior+1)}')
print(f'o menor valor da lista é: {min(lista)} e está na posição da lista {(posicao_menor+1)}')