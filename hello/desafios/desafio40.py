# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final de acordo com a media atingida
# Média abaixo de 5.0: Reprovado
# Media entre 5.0 e 6.9: Recuperação
# Media 7.0 ou superior: Aprovado
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = ((n1+n2)/2) 
if media< 5:
    print(f'Sua média foi {media} e está abaixo de 5.0: \033[0;34mREPROVADO')
elif media >= 5 and media <=6.9:
    print(f'Sua média foi de {media} e está entre 5 e 6.9: \033[0;34mRECUPERAÇÃO')
else:
    print(f'Sua média foi de {media} e está entre 7.0 ou superior: \033[0;034mAPROVADO')