lanche = 'Hambúrguer', 'suco', 'pizza', 'pudim'
for comida in lanche:
    print(f'Eu vou comer: {comida}')
print('Comi pra caramba')
print()

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print()

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print()
    
print(sorted(lanche))
print(lanche)

a = 2,5,4
b = '5','8','1','2'
c = a + b
print(c)
print(len(c))
print(c.count(4))
print(c.index(2))

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa)
