# faça um programa que leia o peso de cinco pessoas, no final, mostre qual foi o maior e menor peso
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite o seu peso: '))
    if c == 1:
        maior = c
        menor = c
        print(descarta)
    else:     
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso  
print(f'O maior peso é: {maior}')
print(f'O menor peso é: {menor}')
