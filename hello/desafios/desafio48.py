# faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500
soma = 0
cont = 0
for contador in range(0,500):
    if contador % 2 == 1:
        if contador % 3 == 0:
            cont = cont + 1
            soma = soma + contador
             
print(f'A soma dos {cont} numeros é:  {soma}')
            
           
        
