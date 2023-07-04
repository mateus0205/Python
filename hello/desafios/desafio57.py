# faça um programa que leia o sexo de uma pessoa, mas so aceite o valores 'M' OU 'F', caso esteja errado, peça a digitação novamente ate um valor correto
letra = str(input('Digite seu sexo: '))
while letra not in 'MmFf':
    letra = str(input('Digite novamente: '))
print(f'Você digitou a letra correta! que foi {letra}')