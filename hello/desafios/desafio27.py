#Faça um programa que leia o nome completo de uma pessoa, 
#mostrando em seguida o primeiro e o último nome separadamente
# ex: Ana maria de souza -> primeiro: Ana, ultimo: souza
nome = str(input('Digite o seu nome completo: ')).strip()
divisao = nome.split()
print(divisao[0], divisao[-1]) # usei o -1 para pegar o ultimo nome, visto que foi divido no split