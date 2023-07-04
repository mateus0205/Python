#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
import time
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
opc = 0
while opc != 5:
    print('''         [ 1 ] somar
         [ 2 ] multiplicar
         [ 3 ] maior 
         [ 4 ] novos números 
         [ 5 ] sair do programa''')
    opc = int(input('>>>>>>> Digite sua opção: '))
    if opc == 1:
        print(f'A soma dos dois valores digitados é: {num1 + num2}')
    elif opc == 2: 
        print(f'A multiplicação dos dois valores digitados é: {num1 * num2}')
    elif opc == 3:
        if num1 > num2:
            print(f'O maior entre {num1} e {num2} será: {num1}')
        elif num2 > num1:
            print(f'O maior entre {num1} e {num2} será: {num2}')
        else:
            print(f'Os números {num1} e {num2} são iguais!')
    elif opc == 4:
        print('Digite os número novamente:')
        num3 = int(input('Digite um valor: '))
        num4 = int(input('Digite outro valor: '))
    elif opc == 5:
        print('Finalizando...')
        time.sleep(5)
    else:
        print('Opção errada. Digite novamente.')
print('Fim')