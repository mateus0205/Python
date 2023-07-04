# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
from math import cos, sin, tan
angulo = int(input('Digite um angulo: '))
print(f'Com o angulo {angulo} teremos os valores de seno: {sin(angulo)}\ncosseno: {cos(angulo)}\ntangente: {tan(angulo)}')