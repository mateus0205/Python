n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print(f'A sua média foi: {media:.1f}')

if media >= 6.0:
    print('Sua media foi boa! PARABENS!')
else:
    print('Sua media foi ruim, estude mais!')