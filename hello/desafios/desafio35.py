#  Desenvolva que leia o comprimento de tres retas e diga ao usuario se eleas podem ou não formar triangulo
n1 = float(input('Digite o comprimento da primeira reta: '))
n2 = float(input('Digite o comprimento da segunda reta: '))
n3 = float(input('Digite o comprimento da terceria reta: '))
if (n1 + n2) > n3 and (n1 +n3) > n2 and (n2 + n3) > n1:
    print('Essas medidas formam um triangulo!')
else:
    print('Essas mediadas não formam um triangulo!')
