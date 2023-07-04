# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte
# seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezessis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 0 and num < 20:
        break
    print('Tente novamente. ')
print(f'Você digitou o número {numeros[num]} ')