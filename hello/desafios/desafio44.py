# Elabore um program que calcule o valor a ser ago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em ate 2x no cartão: preço normal 
# 3x ou mais no cartão: 20% de juros
valor = float(input('Qual o valor que você tem que pagar? '))
opção = int(input('''formas de pagamento 
[1]dinheiro 
[2]cheque 
[3]cartao a vista
[4]cartao em 2 vezes
[5]cartao em 3 ou mais vezes
Qual a sua opção de pagamento: '''))       
if opção == 1:
    print(f'Com a forma de pagamento em dinheiro, você pagará: {valor*0.90} reais, ja com o desconto de 10%')
elif opção == 2:
    print(f'Com a forma de pagamento cheque, você pagará: {valor*0.90} reais, ja com o desconto de 10%')
elif opção == 3:
    print(f'Com a forma de pagamento cartão a vista, voce pagará: {valor} reias')
elif opção == 4:
    print(f'Com a forma de pagamento parcelado em 2 vezes no cartão, você pagará {(valor/2)} em cada parcela')
elif opção == 5:
    parcela = int(input('Quantas parcelas você necessita(3 ou mais): '))
    print(f'Com a forma de pagamento parcelado em 3 vezes ou mais, você pagara em {parcela} parcelas {valor*1.20}, sendo cada parcela {(valor*1.20)/parcela} reais ')
        