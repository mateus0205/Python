# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
# para salarios a 1.250.00 calcule um aumento de 10%
# para inferirores ou iguais, o aumento é de 15%
salario = int(input('Digite seu salario: '))
if salario > 1250:
    print(f'Seu novo salário será de: {salario*1.10}')
else:
    print(f'Seu novo salário sera de: {salario*1.15}')