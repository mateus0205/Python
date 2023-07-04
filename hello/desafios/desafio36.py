# Escreva um programa para aprovar emprestimo bancario para a compra de uma casa
# o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# calcule o valor da prestanção mensal sabendo que ela não pode exceder 30% do salario ou então o emprestimo sera negado. 
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salario? '))
anos = int(input('Em quantos anos vc pretende pagar? '))
parcela = (valor/anos *12)
print(f'Para pagar a casa de {valor} reais em {anos} anos a prestação sera de {parcela} reais.')
if parcela > (salario * 0.30):
    print('Seu emprestimo foi negado!')
else:
    print('Emprestimo aprovado!')
