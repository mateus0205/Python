# crie um programa onde o usuario digite sete valores numericos
# cadastre-os em uma lista unica que mantenha separados os valores
# pares e impares. mostre os valores pares e impares em ordem crescente
listaSete = list()
listapar = list()
listaimpar = list()
for c in range(0,7):
    valor = int(input('Digite 7 valores: '))
    listaSete.append(valor) 
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
listaSete.sort()
listaimpar.sort()
listapar.sort()
print(listaSete)
print(f'lista de pares:', listapar)
print(f'lista de impares: ',listaimpar)
