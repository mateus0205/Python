# Refaça o DESAFIO 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# equilatero: todos os lados iguais 
# isosceles: dois lados iguais
# escalenos todos os lados diferentes
n1 = int(input('Digite o primeiro lado: '))
n2 = int(input('Digite o segundo  lado: '))
n3 = int(input('Digite o terceiro lado: '))
if (n1+n2) > n3 and (n1+n2) > n2 and (n2+n3) > n1:
    print('Essas medidas forma um tringualo!')
    if n1 == n2 == n3: # python pode fazer a comparação direto
        print('Esse triangulo é: \033[0;034mEquilatero.')
    elif n1 != n2 != n3:
        print('Esse triangulo é: \033[0;034mESCALENO.')
    else:
        print('Esse triangulo é: \033[0;034mISOCELES.')
else:
    print('Essas medidas não formam um triangulo')