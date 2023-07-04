# Um professsor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome delas e escrevendo o nome do escolhido
import random
alu1 = str(input('Digite o nome do primeiro aluno: '))
alu2 = str(input('Digite o nome do segundo aluno: '))
alu3 = str(input('Digite o nome do terceiro aluno: '))
alu4 = str(input('Digite o nome do quarto aluno: '))
lista = (alu1, alu2, alu3, alu4)
print(f'O aluno sorteado foi: {random.choice(lista)}')