## crie um programa que o usuario digite uma expressao
## que use (), analise se a expressao esta com, os ()
## abertos e fechados na ordem correta
expressao = ''
quantidadeTotal = 0
quantidadeAbre = 0
quantidadeFecha = 0 
expressao = (input('Digite uma expressão: '))
valida = True
for char in expressao:
    if char == '(':
        quantidadeAbre +=1
    elif char == ')':
        quantidadeFecha +=1 
        if quantidadeFecha > quantidadeAbre:
            valida = False
            break
if quantidadeAbre == quantidadeFecha and valida:
    print('Expressao valida!')
else:
    print('Expressao invalida!')    
