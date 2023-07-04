# Crie um programa que leia o nome completo de uma pessoa e mostre
# 1- O nome com todas as letras maiúculas
# 2- O nome com todas as letras minúsculas
# 3- Quantas letras ao todo (sem considerar espaços)
# 4- Quantas letras tem o primeiro nome
nome = str(input('Digite um nome completo: '))
dividido = nome.split()
print(f'Nome em maiusculo: {nome.upper()}')
print(f'Nome em minusculo: {nome.lower()}')
print(f'Quantidade de letras do nome: {len(nome.replace(" ",""))}') # len conta, replace troca o " ", por vazio, ou seja, tira o espaço assim podendo contabilizar 
print(f'Quantidade do primeiro nome: {len(dividido[0])}')