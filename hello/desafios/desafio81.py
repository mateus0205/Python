## crie um programa que vai ler varios numeros e colocar em uma lista
## a) quantos numeros foram digitados
## b) a lista de valores ordenada de forma decrescente 
## c) se o valor 5 foi digitado esta ou não na lista 
lista = [] 
cont = 1
cinco = ''
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    resposta = input('Quer Continuar? [S/N]:  ').strip().upper()
    if resposta == 'N': 
        break
    if valor >= 0:
        cont += 1
    if valor == 5:
        cinco = '5'
    else:
        cinco = 'nao'
lista.sort()
print(f'A quantidade de numeros digitados foram {cont} digitos')
print(sorted(lista,reverse= True))
print(f'o valor {cinco} foi digitado')