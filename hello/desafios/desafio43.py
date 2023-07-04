# desenvolva logica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo
# abaixo de 18.5: Abaixo do peso
# entre 18.5 e 25: Peso ideal
# 25 ate 30: Sobrepeso
# 30 ate 40: Obesidade
# acima de 40: Obesidade mórbida
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura*altura)
if imc < 18.5:
    print(f'Seu IMC está em {imc:.2f}: Abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu IMC está em {imc:.2f}: Peso ideal.')
elif imc > 25 and imc <= 30:
    print(f'Seu IMC está em {imc:.2f}: Sobrepeso.')
elif imc > 30 and imc <= 40:
    print(f'Seu IMC está em {imc:.2f}: Obesidade.')
else:
    print(f'Seu imc está em {imc:.2f}: Obsesidade mórbida.')