# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
termos = 0
soma = 0
numero = 0
while numero != 999:
    numero = int(input('Digite o numero desejado [999 termina]: '))
    termos += 1
    soma =  soma + numero 
print(f'Quantidade de termos: {termos-1}')
print(f'A soma desses números será: {soma-999}')