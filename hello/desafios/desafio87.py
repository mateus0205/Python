# aprimore o desafio anterior
# a soma de todos os valores pares digitados 
# a soma dos valores da terceira coluna 
# o maior valor da segunda linha
somapares = 0
somacoluna3 = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int((input(f'Digite um valor para {linha}, {coluna}: ')))

for linha in range(0,3):
    for coluna in range(0,3):
       print(f'[{matriz[linha][coluna]: ^5}]',end='') 
    print()
# a soma de todos os valores pares digitados 
pares = [num for linha in matriz for num in linha if num % 2 == 0]
somapares = sum(pares)
print(f'\nA soma dos valores pares da matriz é: ', somapares)

# a soma dos valores da terceira coluna 
coluna = [linha[2] for linha in matriz]
somacoluna3 = sum(coluna)
print('\nA soma da terceira coluna é: ',somacoluna3)

# o maior valor da segunda linha
linha2 = max(matriz[1])
print(f'\no maior valor da segunda linha é: ', linha2)
