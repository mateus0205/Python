# crie um programa o usuario possa digitar cinco valores numericos e cadastre-os em uma lista
# ja na posição correta de inserção (sem usar o sort())
# no final, mostre a lista ordenada na tela 
lista = []
for cont in range(0,5):
    valor = int(input('Digite um valor: '))
    if cont == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionando ao final da lista...')
    else:
        for j in range(len(lista)):
            if valor <= lista[j]:
                lista.insert(j,valor)
                print(f'adicionado na posição {j} da lista')
                j+= 1
                break
print(f'lista ordenada {lista}')            
    