#  Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 1
termos = 0
mais = 10
while mais != 0:
    termos = termos + mais
    while contador <= termos:
        print(primeiro)
        primeiro += razao
        contador += 1
    mais = int(input('Digite quantos termos você quer a mais? '))
print('FIM')
