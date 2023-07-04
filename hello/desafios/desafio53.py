# crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconderando os espaços 
# apos a sopa
# a sacada da casa
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona 
frase = str(input('Digite uma frase: ')).strip()
invertida = ""

for letra in reversed(frase):
    invertida += letra
print(invertida)

if frase == frase[::1]:
    print(f'A frase {frase} é um palindromo de {invertida}')
else:
    print('Não é um palindromo')