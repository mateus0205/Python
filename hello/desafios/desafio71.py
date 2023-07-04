# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuário qual será o valor a ser sacado 
# (número inteiro) e o programa vai informar quantas cedulas serão entregues. 
# caixa possui cedulas de 50,20,10 e 1
saque = int(input('Digite o valor a ser sacado: '))
total = saque
cinquenta = 0
vinte = 0 
dez = 0 
um = 0 
while saque > 0:
    if saque >= 50:
        saque = saque - 50
        cinquenta += 1
    elif saque >= 20:
        saque -= 20
        vinte += 1
    elif saque >= 10:
        saque -= 10
        dez += 1
    elif saque >= 1:
        saque -= 1
        um += 1
print(f'''Para o valor de {total} reais, a quantidade de notas entregues será de:
{cinquenta} de notas de 50
{vinte} de notas de 20
{dez} de notas de 10
{um} de notas de 1
      
      ''')