lanche= ['lanche','bala','refri']
print(lanche[2])

lanche[2]='pirulito'
print(lanche[2])

lanche.append('cookie') # insere na ultima posição
print(lanche)

lanche.insert(0,'hot dog') # insere na posição desejada
print(lanche)

del lanche[3] # deleta a posição
print(lanche)

lanche.pop(3) # geralmente pra deletar o ultimo, mas serve pra deletar pela posição também 
print(lanche)

lanche.remove('lanche') # remove pelo conteudo
print(lanche)

valores = list(range(4,11))
print(valores)

valores.sort() # ordena a  lista 
valores.sort(reverse=True) # ordena inversamente 

len(valores) # saber tamanho da lista 

num = (2, 5, 9, 1)
print(num)
print(valores)
valor = list()
for cont in range(0,5):
    valor.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encotrei o valor {v}!')
    
a = [2,3,4,7]
b = a[:]
b[2] = 8
print(f'A lista A: {a}')
print(f'A lsita B: {b}')
    