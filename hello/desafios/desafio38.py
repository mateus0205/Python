# Escreva um programa que leai dois números interios e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
n1= int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print(f'O primeiro valor {n1} é o maior!')
elif n2 > n1:
    print(f'O segundo valor {n2} é o maior!')
else:
    print(f'Não existe valor maior, os valores {n1} e {n2} são iguais')