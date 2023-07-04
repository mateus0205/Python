# o mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos.
# faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
al1 = str(input('Digite o nome do aluno 1: '))
al2 = str(input('Digite o nome do aluno 2: '))
al3 = str(input('Digite o nome do aluno 3: '))
al4 = str(input('Digite o nome do aluno 4: '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print(f'A ordem do sorteio ficou: {lista}')