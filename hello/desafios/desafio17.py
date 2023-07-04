# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, 
# calcule e mostre o comprimento da hipotenusa
from math import sqrt
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
print(f'A hipotenusa sera {(sqrt((oposto*oposto)+(adjacente*adjacente)))}')