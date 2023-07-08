# Desenvolva um programa que leia quatros valores pelo teclado e guadre-os em uma tupla no final
# quantas vezes apareceu o valor 9
# em que posição foi digitado o primeiro valor 3 (falta ele)
# quais foram os numeros pares 
valores = []
nove = 0
pares = []
numero = 3
posicao = -1

for _ in range(4):
    valor = int(input("Digite um valor: "))
    valores.append(valor)
tupla = tuple(valores)

print("Valores inseridos na tupla:", tupla)
for valor in tupla:
    if valor == 9:
        nove = nove + 1      
print(f'Quantiadade de 9 que apaeceu na tupla: {nove}')

for i, valor in enumerate(tupla):
    if valor == numero:
        posicao = i
        break 
print(f'o número {numero} foi inserido na posição {posicao+1}')

for num in tupla:
    if num % 2 == 0:
        pares.append(num)
print(f'os números pares que foram obtidos: {(pares)}')
