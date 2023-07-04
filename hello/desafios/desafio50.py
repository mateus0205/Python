# Desenvolva um programa que leis seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar desncosidere
soma = 0
for c in range(0,6):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        soma = soma + num
print(f'A soma dos valores será: {soma}')