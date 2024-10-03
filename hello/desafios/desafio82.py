## crie um programa que vai ler varios numeros e colocar em uma lista
## crie duas listas extas que vao conter apenas os valores pares e os valores impares
## imprimir as 3 listas 
lista = [] 
listapar = [] 
listaimpar = [] 
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    resposta = input('Quer continuar? [S/N]: ').strip().upper() # strip remove espaços brancos
    
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
    
    if resposta == 'N':
        break

print('lista completa: ',(lista)) # lista completa 
print('lista de pares: ', (listapar)) # lista de pares
print('lista de impares: ',(listaimpar)) # lista de impares 
