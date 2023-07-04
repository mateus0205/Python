# faça um programa que leia largura e altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria 
# para pintar, sabendo que cada litro de tinta pinta uma area de 2metros quadrados
n1 = float(input('Digite a largura em metros: '))
n2 = float(input('Digite a altura em metros: '))
print(f'A área será de {n1*n2} metros ao quadrado, será necessário {(n1*n2)/2:.4f} latas de tinta para pintar a parede')