# Faça um programa que leia uma frase pelo teclado e mostre:
# 1- Quantas vezes aparece a letra 'A'.
# 2- Em que posição ela aparece a primeira vez.
# 3- Em que posição ela aparece a ultima vez.
frase = str(input('Digite uma frase: ')).upper()
contador = frase.count('a')
b = 'a'
print(f'A letra "a" aparece {contador} vezes')
print(f'A primeira letra "a" aparece na posição {frase.find(b)+1}')
print(f'A ultima letra "a" aparece na posição {frase.rfind(b)+1}')



